#!/usr/bin/env python3
"""List open-access locations for corpus articles that have no local full text. No model, standard library only.

For every corpus row whose 'Full text local' is 'none' (or that is already tracked and still not stored), asks OpenAlex
for the open-access status and the best open location of the DOI, and records the result in corpus/oa-check.csv.
It DOWNLOADS NOTHING: the file is a list of places a copy may be fetched from, for you to approve. It contains
identifiers, statuses and URLs only, no article text. Re-running keeps the 'action' and 'notes' columns you or a session
filled in, and updates the rest.

Columns: ID, PMID, DOI, first_checked, last_checked, oa_status (gold, green, hybrid, bronze, closed, not found),
best_url, host (publisher, repository, ...), version (published, accepted, submitted), license, other_locations,
action (open: not looked at yet; to-download: approved for download; downloaded; refused: server refused; closed: no open copy;
supply-pdf: needs your PDF; inaccessible: tried by hand, not reachable, to be requested through a colleague), notes.

Optional environment variable: OPENALEX_MAILTO (polite pool; never hard-coded).

Usage (project root):  python tools/corpus_oa_check.py [--max N] [--delay SECONDS] [--all]
  --all   also re-check rows already decided (closed, refused, landing-page, supply-pdf, downloaded)
"""
import argparse
import csv
import datetime
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
OUT = CORPUS / "oa-check.csv"
COLS = ["ID", "PMID", "DOI", "first_checked", "last_checked", "oa_status", "best_url", "host", "version", "license",
        "other_locations", "action", "notes"]


def read_csv(path):
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def openalex(doi):
    url = "https://api.openalex.org/works/doi:" + urllib.parse.quote(doi, safe="/")
    mail = os.environ.get("OPENALEX_MAILTO")
    if mail:
        url += "?mailto=" + urllib.parse.quote(mail)
    req = urllib.request.Request(url, headers={"User-Agent": "ir-project corpus check (standard library)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8")), ""
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except Exception as e:
        return None, str(e)[:80]


def summarise(work):
    oa = work.get("open_access") or {}
    best = work.get("best_oa_location") or {}
    others = []
    for loc in work.get("locations") or []:
        u = loc.get("pdf_url") or loc.get("landing_page_url")
        if loc.get("is_oa") and u and u != (best.get("pdf_url") or best.get("landing_page_url")):
            others.append(u)
    src = best.get("source") or {}
    return {
        "oa_status": oa.get("oa_status") or ("closed" if not oa.get("is_oa") else "open"),
        "best_url": best.get("pdf_url") or best.get("landing_page_url") or oa.get("oa_url") or "",
        "host": src.get("type") or ("repository" if best.get("is_oa") and not src else ""),
        "version": best.get("version") or "",
        "license": best.get("license") or "",
        "other_locations": " | ".join(others[:3]),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=0)
    ap.add_argument("--delay", type=float, default=0.3)
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    corpus = read_csv(CORPUS / "corpus.csv")
    old = {r["ID"]: r for r in read_csv(OUT)}
    today = datetime.date.today().isoformat()
    todo = []
    for r in corpus:
        stored = r.get("Full text local", "") not in ("none", "")
        prev = old.get(r["ID"])
        if stored:
            if prev and prev["action"] in ("open", "to-download", "supply-pdf"):
                prev["action"], prev["notes"] = "downloaded", (prev["notes"] + " stored locally").strip()
            continue
        if not r.get("DOI"):
            continue
        if prev and prev["action"] in ("closed", "refused", "landing-page", "supply-pdf", "downloaded", "inaccessible") and not a.all:
            continue  # already decided: do not check again unless --all
        todo.append(r)
    if a.max:
        todo = todo[: a.max]
    n_new = 0
    for r in todo:
        work, err = openalex(r["DOI"])
        prev = old.get(r["ID"], {c: "" for c in COLS})
        row = {c: prev.get(c, "") for c in COLS}
        row.update({"ID": r["ID"], "PMID": r["PMID"], "DOI": r["DOI"], "last_checked": today})
        row["first_checked"] = prev.get("first_checked") or today
        if work is None:
            row["oa_status"] = "not found" if err == "HTTP 404" else f"error: {err}"
            row["best_url"] = row["host"] = row["version"] = row["license"] = row["other_locations"] = ""
        else:
            row.update(summarise(work))
        if not row.get("action"):
            row["action"] = "open" if row["best_url"] else "supply-pdf"
        elif row["action"] in ("open", "supply-pdf", "closed"):
            row["action"] = "open" if row["best_url"] else "supply-pdf"
        old[r["ID"]] = row
        n_new += 1
        time.sleep(a.delay)
    rows = sorted(old.values(), key=lambda x: x["ID"])
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, lineterminator="\n")
        w.writeheader()
        w.writerows({c: r.get(c, "") for c in COLS} for r in rows)
    cnt = {}
    for r in rows:
        cnt[r["action"]] = cnt.get(r["action"], 0) + 1
    with_url = sum(1 for r in rows if r["best_url"] and r["action"] in ("open", "to-download"))
    print(f"checked {n_new} article(s); tracked {len(rows)}; by action {cnt}; with an open location not yet downloaded: {with_url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
