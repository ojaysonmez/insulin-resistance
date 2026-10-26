#!/usr/bin/env python3
"""Download open-access PDFs listed in corpus/oa-check.csv into the git-ignored corpus/fulltext/ folder. No model.

Takes rows whose action is 'open' or 'to-download' and that have a best_url (then the other_locations), requests the URL
politely with a browser-like user agent, and keeps the response only if it is a real PDF (starts with %PDF). The file is
saved as corpus/fulltext/<ID>.pdf; the row's action becomes 'downloaded', 'refused' (HTTP error, e.g. 403) or
'landing-page' (an HTML page, not a PDF) with the reason in notes. A refusal is never worked around. Nothing is committed:
corpus/fulltext/ is git-ignored and the pre-commit check blocks it.

Usage (project root):  python tools/corpus_oa_fetch.py [--max N] [--delay SECONDS]
Then: python tools/corpus_build.py --no-network   (updates the 'Full text local' column)
"""
import argparse
import csv
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus_oa_check import COLS, OUT, read_csv  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FT = ROOT / "corpus" / "fulltext"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/pdf,*/*;q=0.5"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read(40_000_000)
            return data, ""
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except Exception as e:
        return None, str(e)[:80]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=0)
    ap.add_argument("--delay", type=float, default=2.0)
    a = ap.parse_args()
    rows = read_csv(OUT)
    FT.mkdir(parents=True, exist_ok=True)
    todo = [r for r in rows if r["action"] in ("open", "to-download") and (r["best_url"] or r["other_locations"])]
    if a.max:
        todo = todo[: a.max]
    done = refused = landing = 0
    for r in todo:
        urls = [r["best_url"]] + [u.strip() for u in r["other_locations"].split("|") if u.strip()]
        why = []
        for u in [x for x in urls if x]:
            data, err = fetch(u)
            if data is None:
                why.append(f"{err} at {u[:60]}")
            elif data[:5] == b"%PDF-":
                (FT / f"{r['ID']}.pdf").write_bytes(data)
                r["action"], r["notes"] = "downloaded", f"PDF from {u[:90]} ({len(data) // 1024} KB)"
                done += 1
                break
            else:
                why.append(f"HTML, not a PDF at {u[:60]}")
            time.sleep(a.delay)
        else:
            html_only = why and all(w.startswith("HTML") for w in why)
            r["action"] = "landing-page" if html_only else "refused"
            r["notes"] = "; ".join(why)[:250]
            if html_only:
                landing += 1
            else:
                refused += 1
        time.sleep(a.delay)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, lineterminator="\n")
        w.writeheader()
        w.writerows({c: r.get(c, "") for c in COLS} for r in rows)
    print(f"tried {len(todo)}: downloaded {done}, refused {refused}, landing page only {landing}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
