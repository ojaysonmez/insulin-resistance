#!/usr/bin/env python3
"""Build compact digests of the corpus for a use-case discovery pass. No model, standard library only.

For every article in corpus/corpus.csv it writes one block: ID, title, first author and year, the use-case rows the corpus
already ties it to, and (when a local text exists in the git-ignored corpus/fulltext/) about 1,500 characters from the abstract
or the start of the text. Blocks are split into N files under scratch/discovery/ (git-ignored, copyrighted excerpts stay local).
The discovery agents read these files instead of the full texts, which keeps the pass cheap.

Usage (project root):  python tools/discovery_digest.py [--parts 3] [--chars 1500]
"""
import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def excerpt(path, chars):
    t = path.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"^\[text extracted from .*?\]\s*", "", t)
    m = re.search(r"\babstract\b", t[:20000], re.I)
    start = m.end() if m else min(300, len(t) // 4)
    s = re.sub(r"\s+", " ", t[start:start + chars * 2]).strip()
    return s[:chars]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parts", type=int, default=3)
    ap.add_argument("--chars", type=int, default=1500)
    a = ap.parse_args()
    rows = list(csv.DictReader((ROOT / "corpus" / "corpus.csv").open(encoding="utf-8", newline="")))
    blocks = []
    for r in rows:
        p = ROOT / "corpus" / "fulltext" / f"{r['ID']}.txt"
        ex = excerpt(p, a.chars) if p.exists() else "(no local text: title only)"
        blocks.append(f"[{r['ID']}] {r['First author']} {r['Year']}. {r['Title']} (PMID {r['PMID']}; rows already tied: {r['Use-case rows'] or 'none'})\n{ex}\n")
    out = ROOT / "scratch" / "discovery"
    out.mkdir(parents=True, exist_ok=True)
    n = len(blocks)
    size = -(-n // a.parts)
    for k in range(a.parts):
        chunk = blocks[k * size:(k + 1) * size]
        (out / f"digest-{k + 1}.txt").write_text("\n".join(chunk), encoding="utf-8")
        print(f"digest-{k + 1}.txt: {len(chunk)} articles, {sum(len(b) for b in chunk) // 1000} kB")


if __name__ == "__main__":
    main()
