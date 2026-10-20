#!/usr/bin/env python3
"""Turn the watch's structured signals into rescore requests (no model, standard library only).

The daily triage agent writes update-watch/runs/<date>-signals.json:
  {"date": "2026-10-21",
   "signals": [{"type": "S2", "rows": [13], "dimensions": ["D2", "D8"], "pmid": "12345678",
                "doi": "10.x/y", "read_level": "abstract", "note": "why it matters"}],
   "new_candidates": [{"pmid": "...", "doi": "...", "title": "...", "why": "..."}]}
This script validates it, appends every new signal to update-watch/signals.tsv (a signal already
listed for the same PMID, row and type is skipped), and for S1, S2 and S3 signals that name rows
it adds a pending rescore unit (R1, R2, ...) to the scoring queue. A rescore unit PROPOSES a
score change in usecases/scoring/R*.json; the aggregator does not read R files, so a score changes
only when the main session applies a proposal after review (rubric: originals are kept). S4 new
candidates and S5 integrity signals are only logged (S5 as urgent). It never edits a score.

Usage (project root):  python tools/watch_to_queue.py update-watch/runs/2026-10-21-signals.json [--root DIR] [--dry-run]
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scoring_queue as sq  # noqa: E402

DEFAULT_ROOT = Path(__file__).resolve().parent.parent
TYPES = {"S1", "S2", "S3", "S4", "S5"}
RESCORE_TYPES = {"S1", "S2", "S3"}
DIMS = {"D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "S"}
HEADER = ["date", "type", "rows", "dimensions", "pmid", "doi", "status", "queued_unit", "note"]


def known_rows(root):
    rows = set()
    f = Path(root) / "usecases-verified.md"
    if f.exists():
        for ln in f.read_text(encoding="utf-8", errors="ignore").splitlines():
            m = re.match(r"^\|\s*(\d+)\s*\|", ln)
            if m:
                rows.add(int(m.group(1)))
    return rows


def load_log(root):
    f = Path(root) / "update-watch" / "signals.tsv"
    seen = set()
    if f.exists():
        for ln in f.read_text(encoding="utf-8").splitlines()[1:]:
            c = ln.split("\t")
            if len(c) >= 6:
                seen.add((c[4], c[1], c[2]))   # (pmid, type, rows)
    return seen


def append_log(root, rows):
    f = Path(root) / "update-watch" / "signals.tsv"
    f.parent.mkdir(parents=True, exist_ok=True)
    if not f.exists():
        f.write_text("\t".join(HEADER) + "\n", encoding="utf-8")
    with f.open("a", encoding="utf-8") as fh:
        for r in rows:
            fh.write("\t".join(str(x).replace("\t", " ").replace("\n", " ") for x in r) + "\n")


def next_rescore_id(root):
    d = sq.load(root)
    n = [int(u["id"][1:]) for u in d["units"] if re.fullmatch(r"R\d+", u["id"])]
    return f"R{(max(n) + 1) if n else 1}"


def add_rescore(root, uid, sig):
    class A:
        pass
    a = A()
    a.id, a.agent, a.phase, a.template = uid, "ir-usecase-scout", "rescore", "rescore"
    a.dims = ", ".join(sig["dimensions"]) if sig.get("dimensions") else "the dimensions the paper bears on"
    a.rows = ",".join(str(r) for r in sig["rows"])
    a.needs, a.inputs, a.pause_after = "", "", False
    a.extra = (f"Signal type {sig['type']} found by the watch on {sig.get('date', '')}. Paper: PMID {sig['pmid']}"
               + (f", DOI {sig['doi']}" if sig.get("doi") else "")
               + f" (read level when flagged: {sig.get('read_level', 'unknown')}). Why the watch flagged it: {sig.get('note', '')}")
    sq.cmd_add(a, root)


def main():
    ap = argparse.ArgumentParser(description="Turn watch signals into rescore requests (no model).")
    ap.add_argument("signals")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    root = Path(a.root)
    try:
        data = json.loads(Path(a.signals).read_text(encoding="utf-8"))
    except Exception as e:
        print("cannot read signals file:", e, file=sys.stderr)
        return 2
    date = data.get("date") or datetime.date.today().isoformat()
    rows_ok = known_rows(root)
    seen = load_log(root)
    log_rows, queued, skipped, errors = [], [], [], []
    for s in data.get("signals", []) or []:
        t, pmid = s.get("type"), str(s.get("pmid", "")).strip()
        rows = s.get("rows") or []
        if t not in TYPES or not pmid.isdigit():
            errors.append(f"bad signal (type {t!r}, pmid {pmid!r})")
            continue
        if any((not isinstance(r, int)) or (rows_ok and r not in rows_ok) for r in rows):
            errors.append(f"signal {pmid}: unknown row in {rows}")
            continue
        dims = [d for d in (s.get("dimensions") or []) if d in DIMS]
        key = (pmid, t, ",".join(map(str, rows)))
        if key in seen:
            skipped.append(key)
            continue
        seen.add(key)
        unit, status = "", "logged"
        if t == "S5":
            status = "URGENT"
        elif t in RESCORE_TYPES and rows:
            s = dict(s, date=date, dimensions=dims)
            if not a.dry_run:
                unit = next_rescore_id(root)
                add_rescore(root, unit, s)
            else:
                unit = "(dry run)"
            queued.append((unit, pmid, rows))
            status = "rescore queued"
        elif t == "S4":
            status = "new candidate"
        log_rows.append([date, t, ",".join(map(str, rows)), ",".join(dims), pmid, s.get("doi", ""), status, unit, s.get("note", "")[:240]])
    for c in data.get("new_candidates", []) or []:
        pmid = str(c.get("pmid", "")).strip()
        key = (pmid, "S4", "")
        if not pmid.isdigit() or key in seen:
            continue
        seen.add(key)
        log_rows.append([date, "S4", "", "", pmid, c.get("doi", ""), "new candidate", "", (c.get("title", "") + " | " + c.get("why", ""))[:240]])
    if log_rows and not a.dry_run:
        append_log(root, log_rows)
    print(f"{len(log_rows)} signal(s) logged, {len(queued)} rescore unit(s) queued, {len(skipped)} duplicate(s) skipped, {len(errors)} error(s)")
    for u, p, r in queued:
        print(f"  {u}: PMID {p}, rows {r}")
    for e in errors:
        print("  error:", e, file=sys.stderr)
    return 1 if errors and not log_rows else 0


if __name__ == "__main__":
    sys.exit(main())
