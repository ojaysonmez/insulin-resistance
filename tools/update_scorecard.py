#!/usr/bin/env python3
"""Refresh the scorecard block in summary.md from the scoring files (no model, standard library only).

Reads usecases/scoring/S*.json (stage 1 screen) and U*.json (detailed units), and
usecases/scoring/ranking.json if present, plus the use names and statuses in
usecases-verified.md. Replaces the text between the markers
  <!-- SCORECARD:START -->  and  <!-- SCORECARD:END -->
in summary.md (adds the block at the end if the markers are missing). Nothing else in
summary.md is touched. Preliminary data are labelled as such: the index is the mean of the
screening scores, the composite is the rubric's weighted score and exists only for rows
where every dimension has been scored.

Usage (project root):  python tools/update_scorecard.py [--root DIR] [--dry-run]
"""
import argparse
import datetime
import glob
import json
import re
import sys
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- SCORECARD:START -->", "<!-- SCORECARD:END -->"
SCREEN_SCALE = {"D1": 4, "D2": 4, "D3": 4, "D7": 5, "S": 4}
ALL_DIMS = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "S"]
BIN = {0: "<100", 1: "100-1k", 2: "1k-10k", 3: "10k-100k", 4: "100k-1M", 5: ">1M"}
ORDER = {"viable now": 0, "close": 1, "far": 2, None: 3}


def use_names(root):
    names = {}
    f = Path(root) / "usecases-verified.md"
    if f.exists():
        for ln in f.read_text(encoding="utf-8", errors="ignore").splitlines():
            m = re.match(r"^\|\s*(\d+)\s*\|", ln)
            if m:
                c = [x.strip() for x in ln.strip().strip("|").split("|")]
                if len(c) >= 6:
                    name = re.sub(r"\s*\((skeptic|H|C|M)[^)]*\)", "", c[1])
                    names[int(c[0])] = (name[:52], c[5].split(" (")[0].split(",")[0][:22])
    return names


def load(root):
    d = Path(root) / "usecases" / "scoring"
    scores, tier, pv = {}, {}, {}
    for f in sorted(glob.glob(str(d / "[SU]*.json"))):
        try:
            j = json.loads(Path(f).read_text(encoding="utf-8"))
        except Exception:
            continue
        for s in j.get("scores", []) or []:
            if s.get("score") is not None and s.get("dimension") in ALL_DIMS:
                scores.setdefault(s["row"], {}).setdefault(s["dimension"], []).append(s["score"])
        for t in j.get("tiers", []) or []:
            tier[t["row"]] = t["tier"]
        for p in j.get("path_to_viability", []) or []:
            pv[p["row"]] = f'{p["missing_piece"][:70]} ({p["type"]}, {p["effort"]})'
    comp = {}
    rk = d / "ranking.json"
    if rk.exists():
        try:
            j = json.loads(rk.read_text(encoding="utf-8"))
            for r, v in j.get("rows", {}).items():
                if "composite" in v:
                    comp[int(r)] = v["composite"]["default"]
        except Exception:
            pass
    return scores, tier, pv, comp


def index(dims):
    v = []
    for d, sc in SCREEN_SCALE.items():
        if d in dims:
            v.append(sum(dims[d]) / len(dims[d]) / sc)
    return sum(v) / len(v) if v else None


def build(root):
    names = use_names(root)
    scores, tier, pv, comp = load(root)
    rows = sorted(set(scores) | set(tier), key=lambda r: (ORDER.get(tier.get(r)), -(comp.get(r) or index(scores.get(r, {})) or 0), r))
    L = [START, "", f"## Scorecard (generated {datetime.date.today().isoformat()}; preliminary, it improves as more scoring runs finish)", "",
         "Index = mean of the screening scores (decision change, evidence, guideline status, patients per year, stakes) rescaled to 0-1. Composite = the rubric's weighted score, shown only for rows with every dimension scored. Patients per year are screening estimates, mostly low confidence. Details: `usecases/scoring/screen-summary.md`, `usecases/scoring/ranking.md`.", "",
         "| Tier | Row | Use | Status in list | Index | Composite | Dimensions scored | Patients per year | Missing piece (type, effort) |", "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        dims = scores.get(r, {})
        idx = index(dims)
        d7 = dims.get("D7")
        d7s = BIN.get(round(sum(d7) / len(d7))) if d7 else "-"
        name, status = names.get(r, ("", ""))
        L.append(f'| {tier.get(r, "-")} | {r} | {name} | {status} | {"-" if idx is None else f"{idx:.2f}"} | {f"{comp[r]:.2f}" if r in comp else "-"} | {len([d for d in ALL_DIMS if d in dims])}/9 | {d7s} | {pv.get(r, "-")} |')
    L += ["", END]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Refresh the scorecard block in summary.md (no model).")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    block = build(a.root)
    f = Path(a.root) / "summary.md"
    raw = f.read_bytes().decode("utf-8") if f.exists() else ""
    crlf = "\r\n" in raw
    t = raw.replace("\r\n", "\n")
    if START in t and END in t:
        t = t[:t.index(START)] + block + t[t.index(END) + len(END):]
    else:
        t = t.rstrip("\n") + "\n\n" + block + "\n"
    if a.dry_run:
        print(block)
        return 0
    f.write_bytes((t.replace("\n", "\r\n") if crlf else t).encode("utf-8"))
    print(f"scorecard updated in summary.md ({block.count(chr(10)) - 8} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
