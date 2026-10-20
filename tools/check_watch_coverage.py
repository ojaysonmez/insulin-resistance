#!/usr/bin/env python3
"""Which scored use cases have at least one watch query tagged to them (no model).

Reads update-watch/queries.json (the "rows" field of each query) and the rows scored in
usecases/scoring/[SUV]*.json, and prints the rows with no query. Exit code 1 if any scored row
is uncovered, so it can be run as a check.  Usage (project root):  python tools/check_watch_coverage.py
"""
import glob
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def coverage(root=ROOT):
    q = json.loads((Path(root) / "update-watch" / "queries.json").read_text(encoding="utf-8"))["queries"]
    tagged = {}
    for x in q:
        for r in x.get("rows", []) or []:
            tagged.setdefault(r, []).append(x["id"])
    scored = set()
    for f in glob.glob(str(Path(root) / "usecases" / "scoring" / "[SUV]*.json")):
        try:
            for s in json.loads(Path(f).read_text(encoding="utf-8")).get("scores", []):
                scored.add(s["row"])
        except Exception:
            pass
    return tagged, scored


def main():
    tagged, scored = coverage()
    miss = sorted(scored - set(tagged))
    print(f"{len(scored)} scored rows; {len(scored) - len(miss)} have a row-tagged query; uncovered: {miss or 'none'}")
    for r in sorted(scored & set(tagged)):
        print(f"  row {r}: {', '.join(tagged[r])}")
    return 1 if miss else 0


if __name__ == "__main__":
    sys.exit(main())
