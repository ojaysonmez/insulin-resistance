#!/usr/bin/env python3
"""Small PubMed search for agents and humans (no model, standard library only).

Prints one compact line per record (PMID, DOI, year, journal, publication types, title), most
relevant first, so an agent can search without a search tool. Use --abstracts on
tools/watch_fetch.py to read abstracts of the PMIDs it returns.

Usage (project root):
  python tools/pubmed_search.py "QUERY" [--max 15] [--since YEAR]
Examples:
  python tools/pubmed_search.py "post-bariatric hypoglycemia prevalence United States" --max 10
  python tools/pubmed_search.py "insulin autoimmune syndrome incidence" --since 2015
Environment: NCBI_API_KEY (optional). Exit code 0 ok, 2 failure.
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_citations import http_get  # noqa: E402
from watch_fetch import ESEARCH, fetch_records, pubmed_params  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="Compact PubMed search (no model).")
    ap.add_argument("query")
    ap.add_argument("--max", type=int, default=15)
    ap.add_argument("--since", type=int, default=0, help="only records published from this year on")
    a = ap.parse_args()
    delay = 0.12 if os.environ.get("NCBI_API_KEY") else 0.4
    p = {"db": "pubmed", "term": a.query, "retmax": min(a.max, 50), "retmode": "json"}
    if a.since:
        p.update({"datetype": "pdat", "mindate": str(a.since), "maxdate": "3000"})
    try:
        status, body = http_get(ESEARCH + "?" + pubmed_params(p))
        time.sleep(delay)
        res = json.loads(body).get("esearchresult", {})
        ids = res.get("idlist", [])
        recs, errs = fetch_records(ids, delay)
    except Exception as e:
        print("search failed:", e, file=sys.stderr)
        return 2
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(f"PubMed hits: {res.get('count', len(ids))}; listed: {len(ids)}; query: {a.query}" + (f"; since {a.since}" if a.since else ""))
    for pid in ids:
        r = recs.get(pid)
        if not r:
            print(f"PMID {pid}; (no summary)")
            continue
        yr = (r["date"] or "")[:4]
        print(f"PMID {pid}; DOI {r['doi'] or 'none'}; {yr}; {r['journal']}; {', '.join(r['pubtype'][:2])}; {r['title']}")
    for e in errs:
        print("warning:", e, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
