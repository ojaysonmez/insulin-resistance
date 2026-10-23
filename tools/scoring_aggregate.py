#!/usr/bin/env python3
"""Aggregate the use-case scores (no model, standard library only).

Reads usecases/scoring/U*.json and V*.json (the score files written by the scoring units; a unit may list earlier units in "supersedes" to replace their scores for given dimensions), averages the
roles that scored the same dimension, flags differences of more than one point, computes the
rubric's scores (utility UQ = mean of D1, D2, D8; readiness R = mean of D3 to D6; commonality
C = D7; stakes S) rescaled to 0-1 and the weighted composite, labels weak evidence (D2 of 0 or
1), checks the ranking under other weights, and writes usecases/scoring/ranking.md and
ranking.json. A row with a missing dimension is listed as incomplete, not ranked.

Usage (project root):  python tools/scoring_aggregate.py [--root DIR]
Weights (rubric decision D-23): UQ 0.40, commonality 0.25, stakes 0.20, readiness 0.15.
"""
import argparse
import json
import math
import sys
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent
WEIGHTS = {"default": {"UQ": 0.40, "C": 0.25, "S": 0.20, "R": 0.15},
           "equal": {"UQ": 0.25, "C": 0.25, "S": 0.25, "R": 0.25},
           "utility-heavy": {"UQ": 0.60, "C": 0.10, "S": 0.10, "R": 0.20},
           "need-heavy": {"UQ": 0.20, "C": 0.40, "S": 0.30, "R": 0.10}}
SCALE = {"D1": 4, "D2": 4, "D3": 4, "D4": 4, "D5": 4, "D6": 4, "D7": 5, "D8": 4, "S": 4}


def load_scores(root):
    d = Path(root) / "usecases" / "scoring"
    by = {}      # (row, dim) -> list of (unit, score)
    pv, settings, issues, notes = {}, {}, [], []
    files = sorted(list(d.glob("U*.json")) + list(d.glob("V*.json")))
    superseded = set()   # (unit, dimension) pairs replaced by a later unit
    for f in files:
        try:
            for sp in json.loads(f.read_text(encoding="utf-8")).get("supersedes", []) or []:
                for dm in sp.get("dimensions", []):
                    superseded.add((sp.get("unit"), dm))
        except Exception:
            pass
    for f in files:
        try:
            j = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            notes.append(f"{f.name}: not valid JSON ({e})")
            continue
        for s in j.get("scores", []) or []:
            dim, row, val = s.get("dimension"), s.get("row"), s.get("score")
            if (j.get("unit", f.stem), dim) in superseded:
                continue
            if dim in SCALE and isinstance(row, int):
                if val is None:
                    by.setdefault((row, dim), [])
                    notes.append(f"{f.name}: row {row} {dim} not determinable")
                    continue
                if not isinstance(val, (int, float)) or val < 0 or val > SCALE[dim]:
                    notes.append(f"{f.name}: row {row} {dim} score {val!r} outside 0-{SCALE[dim]}")
                    continue
                by.setdefault((row, dim), []).append((j.get("unit", f.stem), val))
        for p in j.get("path_to_viability", []) or []:
            if isinstance(p.get("row"), int):
                pv.setdefault(p["row"], []).append(p)
        for s in j.get("settings", []) or []:
            if isinstance(s.get("row"), int):
                settings.setdefault(s["row"], set()).add(s.get("setting", ""))
        issues += [f"{f.name}: {x}" for x in j.get("anchor_issues", []) or []]
    return by, pv, settings, issues, notes


def load_alternatives(root):
    """Optional usecases/scoring/d7-alternatives.json (rule 24, D-37): {"row": [alternative D7 bins]}."""
    f = Path(root) / "usecases" / "scoring" / "d7-alternatives.json"
    if not f.exists():
        return {}
    try:
        j = json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {int(r): [a for a in v.get("alt_scores", []) if isinstance(a, int) and 0 <= a <= SCALE["D7"]]
            for r, v in j.get("rows", {}).items()}


def alt_ranks(out, alts):
    """Default-weight rank of a row if its D7 takes each alternative bin, other rows unchanged."""
    res = {}
    for r, bins in alts.items():
        v = out.get(r)
        if not v or "composite" not in v or "D7" not in v["dims"]:
            continue
        for b in bins:
            c = b / SCALE["D7"]
            alt = sum(w * (c if x == "C" else v[x]) for x, w in WEIGHTS["default"].items())
            others = [o["composite"]["default"] for q, o in out.items() if q != r and "composite" in o]
            res[(r, b)] = (alt, 1 + sum(1 for o in others if o > alt))
    return res


def mean(xs):
    return sum(xs) / len(xs) if xs else None


def compute(by):
    rows = sorted({r for r, _ in by})
    out = {}
    for r in rows:
        dims, flags = {}, []
        for d in SCALE:
            vals = [v for _, v in by.get((r, d), [])]
            if vals:
                dims[d] = mean(vals)
                if max(vals) - min(vals) > 1:
                    flags.append(f"{d}: roles differ by more than one point ({', '.join(f'{u}={v}' for u, v in by[(r, d)])})")
        def part(keys, scale_each=True):
            if not all(k in dims for k in keys):
                return None
            return mean([dims[k] / SCALE[k] for k in keys])
        uq, rd, c, s = part(["D1", "D2", "D8"]), part(["D3", "D4", "D5", "D6"]), part(["D7"]), part(["S"])
        missing = [k for k, v in (("UQ", uq), ("R", rd), ("C", c), ("S", s)) if v is None]
        rec = {"row": r, "dims": dims, "UQ": uq, "R": rd, "C": c, "S": s, "flags": flags, "missing": missing}
        if "D2" in dims and dims["D2"] <= 1:
            rec["flags"].append("weak evidence (D2 of 0 or 1)")
        if not missing:
            rec["composite"] = {k: sum(w[x] * rec[x] for x in w) for k, w in WEIGHTS.items()}
        out[r] = rec
    return out


def ranks(out, key):
    done = [(r, v["composite"][key]) for r, v in out.items() if "composite" in v]
    done.sort(key=lambda x: (-x[1], x[0]))
    return {r: i + 1 for i, (r, _) in enumerate(done)}


def write(root, out, pv, settings, issues, notes, alts=None):
    d = Path(root) / "usecases" / "scoring"
    rk = {k: ranks(out, k) for k in WEIGHTS}
    ranked = sorted([r for r, v in out.items() if "composite" in v], key=lambda r: rk["default"][r])
    top_n = max(1, math.ceil(len(ranked) / 4)) if ranked else 0
    stable = {r for r in ranked if all(rk[k][r] <= top_n for k in WEIGHTS)}
    fmt = lambda x: "-" if x is None else f"{x:.2f}"
    L = ["# Use-case ranking (generated by tools/scoring_aggregate.py; do not edit by hand)", "",
         "Scores are rescaled to 0-1. Composite = 0.40 UQ + 0.25 C + 0.20 S + 0.15 R (decision D-23). Weak evidence labels apply whatever the composite. Preliminary: it is only as good as the unit outputs and the skeptic reviews.", "",
         "| Rank | Row | Setting | UQ | R | C | S | Composite | Top group under all weightings | Flags | Path to viability |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in ranked:
        v = out[r]
        pvs = "; ".join(f"{p.get('missing_piece', '')} ({p.get('type', '')}, {p.get('effort', '')})" for p in pv.get(r, [])) or "-"
        L.append(f"| {rk['default'][r]} | {r} | {', '.join(sorted(settings.get(r, []))) or '-'} | {fmt(v['UQ'])} | {fmt(v['R'])} | {fmt(v['C'])} | {fmt(v['S'])} | {v['composite']['default']:.3f} | {'yes' if r in stable else 'no'} | {'; '.join(v['flags']) or '-'} | {pvs} |")
    inc = [r for r, v in out.items() if "composite" not in v]
    if inc:
        L += ["", "## Incomplete rows (not ranked)", ""]
        for r in sorted(inc):
            L.append(f"- Row {r}: missing {', '.join(out[r]['missing'])}" + (f"; flags: {'; '.join(out[r]['flags'])}" if out[r]["flags"] else ""))
    L += ["", f"## Sensitivity (top group = best {top_n} of {len(ranked)})", "", "| Row | " + " | ".join(WEIGHTS) + " |", "|---|" + "---|" * len(WEIGHTS)]
    for r in ranked:
        L.append(f"| {r} | " + " | ".join(str(rk[k][r]) for k in WEIGHTS) + " |")
    ar = alt_ranks(out, alts or {})
    if ar:
        L += ["", "## Sensitivity to an unsourced D7 share (rule 24, D-37)", "",
              "Rows whose D7 rests on an assumed share: the default-weight rank if D7 took the alternative bin named in the unit's reason (other rows unchanged). Alternatives are listed in `usecases/scoring/d7-alternatives.json`.", "",
              "| Row | Default rank | D7 now | Alternative D7 | Composite then | Rank then |", "|---|---|---|---|---|---|"]
        for (r, b), (comp, rank) in sorted(ar.items()):
            L.append(f"| {r} | {rk['default'][r]} | {out[r]['dims']['D7']:g} | {b} | {comp:.3f} | {rank} |")
    if issues:
        L += ["", "## Anchor issues reported by the units", ""] + [f"- {x}" for x in issues]
    if notes:
        L += ["", "## Notes", ""] + [f"- {x}" for x in notes]
    (d / "ranking.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    (d / "ranking.json").write_text(json.dumps({"weights": WEIGHTS, "rows": {str(r): v for r, v in out.items()}, "ranks": {k: {str(r): x for r, x in v.items()} for k, v in rk.items()}}, indent=1), encoding="utf-8")
    return ranked, inc


def main():
    ap = argparse.ArgumentParser(description="Aggregate the use-case scores (no model).")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    a = ap.parse_args()
    by, pv, settings, issues, notes = load_scores(a.root)
    if not by:
        print("no score files found in usecases/scoring/ (U*.json)", file=sys.stderr)
        return 2
    out = compute(by)
    ranked, inc = write(a.root, out, pv, settings, issues, notes, load_alternatives(a.root))
    print(f"ranked {len(ranked)} row(s), incomplete {len(inc)}; wrote usecases/scoring/ranking.md and ranking.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
