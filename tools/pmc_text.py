#!/usr/bin/env python3
"""Verbatim text from PubMed Central full-text XML (no model, standard library only).

Prints the article text as paragraphs labelled with their section path, or only the windows
around a regular expression, so a reader (or a lean agent) can quote passages exactly. It does
not summarise. Works only for articles with an open PubMed Central copy.

Usage (from the project root):
  python tools/pmc_text.py PMC12690183 --sections                     list section headings
  python tools/pmc_text.py PMC12690183 --grep "C-peptide|stage 2"      windows around matches
  python tools/pmc_text.py PMC12690183 --grep "OGTT" --window 400 --max 8
  python tools/pmc_text.py PMC12690183 --all --max-chars 15000         whole text (cut off at a limit)
Environment: NCBI_API_KEY (optional). Exit code: 0 ok, 2 could not fetch or parse.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_citations import http_get  # noqa: E402

EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
BLOCK_TAGS = {"p", "table-wrap", "list", "boxed-text", "disp-quote"}


def local(tag):
    return tag.rsplit("}", 1)[-1] if isinstance(tag, str) else ""


def flat(el):
    return " ".join("".join(el.itertext()).split())


def walk(el, path, out):
    for child in el:
        t = local(child.tag)
        if t == "sec":
            title = flat(child.find("title")) if child.find("title") is not None else ""
            walk(child, path + ([title] if title else []), out)
        elif t in BLOCK_TAGS:
            txt = flat(child)
            if txt:
                label = "Table" if t == "table-wrap" else None
                out.append((" > ".join(path) or "(front)", ("[Table] " if label else "") + txt))
        else:
            walk(child, path, out)


class PageParser(HTMLParser):
    """Blocks (section path, text) from the main article body of a PubMed Central web page."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks, self.title = [], ""
        self.depth = 0          # section depth inside the main article body (0 = outside)
        self.heads = {}
        self.buf = None         # list of text pieces for the block being built
        self.kind = None
        self.head_lvl = None
        self.head_buf = []
        self.row = None
        self.in_title = False
        self.done = False
        self.skip = 0

    def path(self):
        return " > ".join(self.heads[k] for k in sorted(self.heads)) or "(front)"

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "title":
            self.in_title = True
        if tag == "section":
            if self.depth == 0 and "main-article-body" in (a.get("class") or ""):
                self.depth = 1
            elif self.depth:
                self.depth += 1
        if not self.depth or self.done:
            return
        if tag in ("h2", "h3", "h4"):
            self.head_lvl, self.head_buf = int(tag[1]), []
        elif tag in ("p", "li") and self.buf is None and self.row is None:
            self.buf, self.kind = [], tag
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.buf, self.kind = [], "cell"

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
        if tag == "title":
            self.in_title = False
        if tag == "section" and self.depth:
            self.depth -= 1
        if not self.depth or self.done:
            return
        if tag in ("h2", "h3", "h4") and self.head_lvl is not None:
            text = " ".join("".join(self.head_buf).split())
            if self.head_lvl == 2 and text.lower() in ("references", "bibliography"):
                self.done = True
            lvl = self.head_lvl
            self.heads = {k: v for k, v in self.heads.items() if k < lvl}
            if text:
                self.heads[lvl] = text
            self.head_lvl = None
        elif tag == self.kind and tag in ("p", "li") and self.buf is not None:
            text = " ".join("".join(self.buf).split())
            if text:
                self.blocks.append((self.path(), text))
            self.buf, self.kind = None, None
        elif tag in ("td", "th") and self.kind == "cell" and self.buf is not None:
            self.row.append(" ".join("".join(self.buf).split()))
            self.buf, self.kind = None, None
        elif tag == "tr" and self.row is not None:
            if any(self.row):
                self.blocks.append((self.path(), "[Table] " + " | ".join(self.row)))
            self.row = None

    def handle_data(self, data):
        if self.skip:
            return
        if self.in_title and not self.title:
            self.title = " ".join(data.split())
        if self.head_lvl is not None:
            self.head_buf.append(data)
        elif self.buf is not None:
            self.buf.append(data)


CACHE = Path(__file__).resolve().parent.parent / "scratch" / "pmc-cache"


def page_blocks(num):
    """Blocks from the PubMed Central web page, cached in scratch/ (git-ignored). The site
    sometimes answers fast repeat requests with a page that lacks the article, so retry."""
    cache_file = CACHE / f"{num}.json"
    if cache_file.exists():
        try:
            d = json.loads(cache_file.read_text(encoding="utf-8"))
            return d["title"], [tuple(b) for b in d["blocks"]]
        except Exception:
            pass
    last = "no article body in the page"
    for attempt in range(4):
        if attempt:
            time.sleep(5 * attempt)
        try:
            req = urllib.request.Request(f"https://pmc.ncbi.nlm.nih.gov/articles/PMC{num}/",
                                         headers={"User-Agent": "Mozilla/5.0 (ir-project text helper)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                html = r.read().decode("utf-8", errors="replace")
            p = PageParser()
            p.feed(html)
            if p.blocks:
                CACHE.mkdir(parents=True, exist_ok=True)
                cache_file.write_text(json.dumps({"title": p.title, "blocks": p.blocks}), encoding="utf-8")
                return p.title, p.blocks
            last = "the page had no article body (a bot check or rate limit?)"
        except Exception as e:
            last = str(e)
    raise RuntimeError(last)


def main():
    ap = argparse.ArgumentParser(description="Verbatim text from PubMed Central full-text XML.")
    ap.add_argument("pmcid", help="for example PMC12690183")
    ap.add_argument("--grep", default="", help="regular expression (case-insensitive); print windows around matches")
    ap.add_argument("--window", type=int, default=300, help="characters either side of a match")
    ap.add_argument("--max", type=int, default=12, help="maximum number of windows")
    ap.add_argument("--sections", action="store_true", help="list section headings only")
    ap.add_argument("--all", action="store_true", help="print the whole text")
    ap.add_argument("--max-chars", type=int, default=20000, help="cut-off for --all")
    args = ap.parse_args()

    num = re.sub(r"\D", "", args.pmcid)
    params = {"db": "pmc", "id": num, "retmode": "xml"}
    if os.environ.get("NCBI_API_KEY"):
        params["api_key"] = os.environ["NCBI_API_KEY"]
    source = "XML"
    blocks, title = [], ""
    try:
        status, body = http_get(EFETCH + "?" + urllib.parse.urlencode(params))
        root = ET.fromstring(body)
        art = root.find(".//article")
        bodyel = art.find("body") if art is not None else None
        if bodyel is not None:
            title = flat(art.find(".//article-title")) if art.find(".//article-title") is not None else ""
            walk(bodyel, [], blocks)
    except Exception as e:
        print("XML fetch or parse failed:", e, file=sys.stderr)
    if not blocks:
        # some publishers do not allow full text in XML; use the PubMed Central web page instead
        try:
            title, blocks = page_blocks(num)
            source = "web page (the publisher does not allow full text in XML)"
        except Exception as e:
            print("web page fetch failed:", e, file=sys.stderr)
            return 2
    if not blocks:
        print("no article body found (no open full text?)", file=sys.stderr)
        return 2
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(f"PMC{num} | {title} | source: {source}")
    print(f"{len(blocks)} blocks, {sum(len(b[1]) for b in blocks)} characters")
    print()
    if args.sections:
        seen = []
        for path, _ in blocks:
            if path not in seen:
                seen.append(path)
        for p in seen:
            print("-", p)
        return 0
    if args.grep:
        rx = re.compile(args.grep, re.I)
        n = 0
        total = sum(len(rx.findall(t)) for _, t in blocks)
        for path, txt in blocks:
            for m in rx.finditer(txt):
                if n >= args.max:
                    break
                s = max(0, m.start() - args.window)
                e = min(len(txt), m.end() + args.window)
                print(f"[{n + 1}] section: {path}")
                print(("..." if s else "") + txt[s:e] + ("..." if e < len(txt) else ""))
                print()
                n += 1
        print(f"{total} match(es) in the text; {n} shown (pattern: {args.grep})")
        return 0
    used = 0
    for path, txt in blocks:
        if used > args.max_chars:
            print(f"[cut off at {args.max_chars} characters]")
            break
        print(f"## {path}")
        print(txt)
        print()
        used += len(txt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
