#!/usr/bin/env python3
"""Store open full texts of corpus articles locally (no model, standard library plus openpyxl).

For each corpus row that has a PubMed Central copy and no local text yet, fetches the text with
the same reader as tools/pmc_text.py (XML, or the PubMed Central page when the publisher does not
allow XML) and writes corpus/fulltext/<ID>.txt: a short header (ID, PMID, DOI, PMCID, source,
date) and the article text with section headings. The folder is git-ignored and the pre-commit
check blocks it, because full texts are copyrighted (open access does not always mean free reuse).
PDFs you download yourself can be placed next to them as corpus/fulltext/<ID>.pdf.
Run tools/corpus_build.py afterwards to update the 'Full text local' column.

Usage (project root):  python tools/corpus_fulltext.py [--max N] [--delay SECONDS]
"""
import argparse
import datetime
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pmc_text  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "corpus" / "fulltext"


def blocks_for(pmcid):
    """Blocks (section path, text) for one article: XML first, then the web page."""
    import urllib.parse
    import xml.etree.ElementTree as ET
    from check_citations import http_get
    num = re.sub(r"\D", "", pmcid)
    blocks, source = [], "XML"
    try:
        status, body = http_get(pmc_text.EFETCH + "?" + urllib.parse.urlencode({"db": "pmc", "id": num, "retmode": "xml"}))
        art = ET.fromstring(body).find(".//article")
        bodyel = art.find("body") if art is not None else None
        if bodyel is not None:
            pmc_text.walk(bodyel, [], blocks)
    except Exception:
        blocks = []
    if not blocks:
        _, blocks = pmc_text.page_blocks(num)
        source = "PubMed Central page"
    return blocks, source


def main():
    ap = argparse.ArgumentParser(description="Store open full texts of corpus articles locally.")
    ap.add_argument("--max", type=int, default=0, help="stop after this many new texts (0 = all)")
    ap.add_argument("--delay", type=float, default=1.5)
    a = ap.parse_args()
    import openpyxl
    ws = openpyxl.load_workbook(ROOT / "corpus" / "corpus.xlsx").active
    rows = list(ws.iter_rows(values_only=True))
    hdr = list(rows[0])
    recs = [dict(zip(hdr, r)) for r in rows[1:]]
    OUT.mkdir(parents=True, exist_ok=True)
    todo = [r for r in recs if r.get("PMCID") and not (OUT / f"{r['ID']}.txt").exists()]
    print(f"{len(todo)} article(s) with a PubMed Central copy and no local text")
    done = failed = 0
    for r in todo:
        if a.max and done >= a.max:
            break
        try:
            blocks, source = blocks_for(str(r["PMCID"]))
            if not blocks:
                raise RuntimeError("no article body")
            lines = [f"ID: {r['ID']}", f"PMID: {r['PMID']}", f"DOI: {r['DOI']}", f"PMCID: {r['PMCID']}", f"Title: {r['Title']}",
                     f"Source: {source}; fetched {datetime.date.today().isoformat()}; local copy only, not for the repository", ""]
            last = None
            for path, txt in blocks:
                if path != last:
                    lines += ["", f"## {path}"]
                    last = path
                lines.append(txt)
            (OUT / f"{r['ID']}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
            done += 1
        except Exception as e:
            failed += 1
            print(f"  {r['ID']} {r['PMCID']}: failed ({e})")
        time.sleep(a.delay)
    print(f"stored {done}, failed {failed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
