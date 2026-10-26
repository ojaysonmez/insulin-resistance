#!/usr/bin/env python3
"""Check that each stored PDF is the article its name says, and convert PDFs to text. No model, standard library only.

For every corpus/fulltext/<ID>.pdf it extracts the text with pdftotext (poppler; must be on PATH), compares the first
pages with the corpus title and DOI, counts the words, and records a verdict in corpus/pdf-check.csv (identifiers and
verdicts only, no article text). Verdicts:
  ok         the DOI appears in the first pages, or at least 60% of the title words do
  mismatch   neither: probably the wrong article (see the 'looks_like' column: the first lines of the text)
  low-text   fewer than 1,500 words: an empty printout, a scan, or only an abstract page
  no-tool    pdftotext is not available
If no corpus/fulltext/<ID>.txt exists yet, the extracted text is written there (git-ignored, local) so that readers can
use it. Re-running keeps verdicts for unchanged files (same size) and only re-checks new or changed ones.

Usage (project root):  python tools/corpus_pdf_check.py [--all]
"""
import argparse
import csv
import datetime
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
FT = CORPUS / "fulltext"
OUT = CORPUS / "pdf-check.csv"
COLS = ["ID", "file_kb", "words", "title_match", "doi_found", "verdict", "looks_like", "checked"]
STOP = set("the and for with from that this are was were into than their after between versus using study".split())


def rd(p):
    if not p.exists():
        return []
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def words(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if len(w) > 3 and w not in STOP]


def pdftext(path, last=None):
    cmd = ["pdftotext", "-layout"] + (["-l", str(last)] if last else []) + [str(path), "-"]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    return p.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    corpus = {r["ID"]: r for r in rd(CORPUS / "corpus.csv")}
    old = {r["ID"]: r for r in rd(OUT)}
    today = datetime.date.today().isoformat()
    have_tool = shutil.which("pdftotext") is not None
    n_new = 0
    for pdf in sorted(FT.glob("C[0-9][0-9][0-9].pdf")):
        cid = pdf.stem
        kb = pdf.stat().st_size // 1024
        if cid in old and old[cid]["file_kb"] == str(kb) and not a.all and old[cid]["verdict"] != "no-tool":
            continue
        row = {"ID": cid, "file_kb": kb, "words": "", "title_match": "", "doi_found": "", "verdict": "no-tool", "looks_like": "", "checked": today}
        if have_tool:
            full = pdftext(pdf)
            head = pdftext(pdf, 3)
            row["words"] = len(full.split())
            c = corpus.get(cid, {})
            tw = set(words(c.get("Title", "")))
            hw = set(words(head))
            row["title_match"] = f"{len(tw & hw) / len(tw):.2f}" if tw else ""
            doi = c.get("DOI", "").lower()
            row["doi_found"] = "yes" if doi and doi in re.sub(r"\s+", "", head.lower()) else "no"
            if row["words"] < 1500:
                row["verdict"] = "low-text"
            elif row["doi_found"] == "yes" or (row["title_match"] and float(row["title_match"]) >= 0.6):
                row["verdict"] = "ok"
            else:
                row["verdict"] = "mismatch"
            row["looks_like"] = " ".join(head.split())[:110].replace('"', "'")
            txt = FT / f"{cid}.txt"
            if not txt.exists() and row["words"] >= 200:
                txt.write_text(f"[text extracted from {cid}.pdf by tools/corpus_pdf_check.py]\n\n" + full, encoding="utf-8")
        old[cid] = row
        n_new += 1
    rows = sorted(old.values(), key=lambda r: r["ID"])
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, lineterminator="\n")
        w.writeheader()
        w.writerows({c: r.get(c, "") for c in COLS} for r in rows)
    cnt = {}
    for r in rows:
        cnt[r["verdict"]] = cnt.get(r["verdict"], 0) + 1
    print(f"checked {n_new} PDF(s); tracked {len(rows)}; verdicts {cnt}")
    for r in rows:
        if r["verdict"] in ("mismatch", "low-text"):
            print(f"  {r['ID']} {r['verdict']} (words {r['words']}, title match {r['title_match']}, DOI {r['doi_found']}): {r['looks_like'][:90]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
