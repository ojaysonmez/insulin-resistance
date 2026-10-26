#!/usr/bin/env python3
"""Set the tracking status of corpus articles in corpus/oa-check.csv by hand. No model, standard library only.

Usage (project root):
  python tools/corpus_oa_mark.py inaccessible C072 C112 C138 --note "tried by hand, not reachable"
  python tools/corpus_oa_mark.py to-download C040

Statuses: open, to-download, downloaded, refused, landing-page, closed, supply-pdf, inaccessible.
'inaccessible' means someone tried by hand and the article cannot be reached (or does not exist online): it is listed
in part D of corpus/download-list.md as '???' (to be requested through a colleague) and is never checked again.
Run python tools/corpus_download_list.py afterwards to refresh the list.
"""
import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus_oa_check import COLS, OUT, read_csv  # noqa: E402

STATUSES = ["open", "to-download", "downloaded", "refused", "landing-page", "closed", "supply-pdf", "inaccessible"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("status", choices=STATUSES)
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--note", default="")
    a = ap.parse_args()
    rows = read_csv(OUT)
    by = {r["ID"]: r for r in rows}
    corpus = {r["ID"]: r for r in read_csv(OUT.parent / "corpus.csv")}
    for i in a.ids:
        if i not in by:
            if i not in corpus:
                print(f"{i}: not in the corpus; skipped")
                continue
            c = corpus[i]
            by[i] = {k: "" for k in COLS}
            by[i].update({"ID": i, "PMID": c["PMID"], "DOI": c["DOI"]})
            rows.append(by[i])
        by[i]["action"] = a.status
        if a.note:
            by[i]["notes"] = a.note
        print(f"{i}: {a.status}")
    rows.sort(key=lambda r: r["ID"])
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, lineterminator="\n")
        w.writeheader()
        w.writerows({c: r.get(c, "") for c in COLS} for r in rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
