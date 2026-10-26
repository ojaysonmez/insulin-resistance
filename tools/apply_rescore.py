#!/usr/bin/env python3
"""Apply small rescore proposals from the watch's rescore units (R*.json). No model, standard library only.

A rescore unit (R1, R2, ...) writes usecases/scoring/R<n>.json with `proposals` (row, dimension, current, proposed,
reason, quote, confidence). This script applies a proposal on its own only when ALL of these hold (D-48):
  - proposed is a whole number, differs from current by exactly 1 point and lies on the dimension's scale;
  - confidence is medium or high and a quote is given;
  - exactly one existing score entry in U*.json / V*.json covers that row and dimension, and its score equals `current`.
The entry is changed in place (score = proposed, original_score kept, a `correction` note added), the decision is
logged in usecases/scoring/rescore-log.tsv, and the ranking and the scorecard in summary.md are regenerated.
Everything else is logged as 'needs review' (kept for the main session) or 'no change'. It never edits the deliverables.

Usage (project root):
  python tools/apply_rescore.py --pending       every R*.json not yet in the log
  python tools/apply_rescore.py R2.json ...     named files (paths under usecases/scoring/ or full)
  --dry-run   show what would happen, change nothing
"""
import argparse
import datetime
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from scoring_aggregate import SCALE, tier  # noqa: E402

LOG_HEADER = ["date", "unit", "row", "dimension", "current", "proposed", "action", "note"]


def log_path(root):
    return Path(root) / "usecases" / "scoring" / "rescore-log.tsv"


def logged_units(root):
    p = log_path(root)
    if not p.exists():
        return set()
    return {l.split("\t")[1] for l in p.read_text(encoding="utf-8").splitlines()[1:] if l.count("\t") >= 6}


def append_log(root, rows):
    p = log_path(root)
    new = not p.exists()
    with p.open("a", encoding="utf-8", newline="\n") as f:
        if new:
            f.write("\t".join(LOG_HEADER) + "\n")
        for r in rows:
            f.write("\t".join(str(x).replace("\t", " ").replace("\n", " ") for x in r) + "\n")


def find_entries(root, row, dim):
    """Every score entry for (row, dim) in U*.json and V*.json: list of (file, data, entry)."""
    d = Path(root) / "usecases" / "scoring"
    out = []
    for f in sorted(list(d.glob("U*.json")) + list(d.glob("V*.json"))):
        try:
            j = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for e in j.get("scores", []) or []:
            if e.get("row") == row and e.get("dimension") == dim and e.get("score") is not None:
                out.append((f, j, e))
    return out


def decide(root, pr):
    """Return (action, note, entry_tuple or None) for one proposal."""
    row, dim, cur, new = pr.get("row"), pr.get("dimension"), pr.get("current"), pr.get("proposed")
    if new is None:
        return "no change", "proposed is null", None
    if not (isinstance(row, int) and dim in SCALE and all(isinstance(x, int) and not isinstance(x, bool) for x in (cur, new))):
        return "needs review", "row, dimension or scores are not whole numbers on a known dimension", None
    if abs(new - cur) != 1:
        return "needs review", f"change of {new - cur:+d} points is not exactly one point", None
    if not 0 <= new <= SCALE[dim]:
        return "needs review", f"proposed {new} is outside 0-{SCALE[dim]}", None
    if str(pr.get("confidence", "")).lower() not in ("medium", "high"):
        return "needs review", f"confidence is {pr.get('confidence')!r}", None
    if not str(pr.get("quote", "")).strip():
        return "needs review", "no quote given", None
    ents = find_entries(root, row, dim)
    if len(ents) != 1:
        return "needs review", f"{len(ents)} score entries exist for row {row} {dim} (exactly one is needed)", None
    if ents[0][2].get("score") != cur:
        return "needs review", f"stored score {ents[0][2].get('score')} differs from current {cur}", None
    return "apply", "", ents[0]


def tiers(root):
    try:
        j = json.loads((Path(root) / "usecases" / "scoring" / "ranking.json").read_text(encoding="utf-8"))
        return {r: tier(v["composite"]["default"]) for r, v in j["rows"].items()}
    except Exception:
        return {}


def regenerate(root):
    for script in ("scoring_aggregate.py", "update_scorecard.py"):
        subprocess.run([sys.executable, str(HERE / script)], cwd=str(root), capture_output=True, text=True, timeout=120)


def main():
    ap = argparse.ArgumentParser(description="Apply small rescore proposals (D-48).")
    ap.add_argument("files", nargs="*")
    ap.add_argument("--pending", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-regenerate", action="store_true", help="tests only: do not rebuild the ranking and scorecard")
    ap.add_argument("--root", default=str(HERE.parent))
    a = ap.parse_args()
    root = Path(a.root)
    d = root / "usecases" / "scoring"
    files = [Path(f) if Path(f).exists() else d / f for f in a.files]
    if a.pending:
        done = logged_units(root)
        files += [f for f in sorted(d.glob("R[0-9]*.json")) if f.stem not in done and f not in files]
    if not files:
        print("nothing to apply")
        return 0
    before = tiers(root)
    today = datetime.date.today().isoformat()
    applied = 0
    for f in files:
        try:
            j = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"{f.name}: not valid JSON ({e}); skipped (not logged, so it is retried)")
            continue
        unit = j.get("unit", f.stem)
        pmid = (j.get("paper") or {}).get("pmid", "")
        rows, touched = [], {}
        for pr in j.get("proposals", []) or []:
            action, note, ent = decide(root, pr)
            if action == "apply" and not a.dry_run:
                action = "applied"
                fpath, data, e = ent
                e.setdefault("original_score", e["score"])
                e["score"] = pr["proposed"]
                e["correction"] = (f"Rescore {unit} ({today}, applied automatically under D-48; watch paper PMID {pmid}): "
                                   f"{pr['dimension']} {pr['current']} to {pr['proposed']}. {str(pr.get('reason', ''))[:300]}")
                touched[fpath] = data
                applied += 1
            if action == "apply" and a.dry_run:
                action = "would apply"
            rows.append([today, unit, pr.get("row", ""), pr.get("dimension", ""), pr.get("current", ""), pr.get("proposed", ""),
                         action, note or str(pr.get("reason", ""))[:200]])
        if not rows:
            rows.append([today, unit, "", "", "", "", "no proposals", ""])
        for fpath, data in touched.items():
            with fpath.open("w", encoding="utf-8", newline="\n") as fh:
                json.dump(data, fh, indent=2, ensure_ascii=False)
                fh.write("\n")
        for r in rows:
            print("\t".join(str(x) for x in r))
        if not a.dry_run:
            append_log(root, rows)
    if applied and not a.dry_run and not a.no_regenerate:
        regenerate(root)
        after = tiers(root)
        moved = [f"row {r}: tier {before[r]} to {after[r]}" for r in after if r in before and before[r] != after[r]]
        if moved:
            append_log(root, [[today, "", "", "", "", "", "TIER CHANGE", "; ".join(moved)]])
            print("TIER CHANGE: " + "; ".join(moved))
    print(f"applied {applied} proposal(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
