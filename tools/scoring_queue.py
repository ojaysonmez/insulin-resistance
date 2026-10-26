#!/usr/bin/env python3
"""Queue helper for the use-case scoring (no model, standard library only).

The scoring is cut into units (one subagent run each). The queue lives in
usecases/scoring/queue.json. This script adds units, says which unit is next, marks units
done or failed, decides from the usage percentages whether a scheduled run may start or
continue (the percentages come from the session's usage tool and are passed in), and keeps
the usage log. It never calls a model and never reads usage itself.

Commands (run from the project root; add --root DIR to work on another folder, for tests):
  add --id U1 --agent ir-evidence-searcher --dims D7,D3 --rows 6,5,13 [--template score]
      [--needs U2,U3] [--phase pilot] [--pause-after] [--extra TEXT] [--inputs U1,U2]
  next                         print the next eligible unit as JSON, or NONE / PAUSED / BLOCKED
  done ID                      mark a unit done (sets PAUSED when the unit has pause_after)
  fail ID --error TEXT         count a failed attempt; after max_attempts the unit is failed-final
  status                       counts per state and the next unit
  resume                       set the queue back to RUNNING after a pause
  gate --pct5 N --weekly N --hour H [--continue]   print START, CONTINUE or STOP with a reason
  log --unit ID --pct5-before N --pct5-after N --weekly-before N --weekly-after N
      [--tokens N] [--tools N] [--errors TEXT]     append a line to usage-log.tsv
"""
import argparse
import datetime
import json
import sys
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent
CONFIG = {"start_limit_pct5": 40, "continue_limit_pct5": 65, "weekly_cap_pct": 75,
          "quiet_hours": None, "max_attempts": 2, "hard_stop_pct5": 95}
LOG_HEADER = ["time", "unit", "pct5_before", "pct5_after", "weekly_before", "weekly_after", "tokens", "tool_uses", "errors"]


def paths(root):
    d = Path(root) / "usecases" / "scoring"
    return d, d / "queue.json", d / "usage-log.tsv"


def load(root):
    d, q, _ = paths(root)
    if q.exists():
        return json.loads(q.read_text(encoding="utf-8"))
    return {"config": dict(CONFIG), "status": "RUNNING", "pause_reason": "", "units": []}


def save(root, data):
    d, q, _ = paths(root)
    d.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def find(data, uid):
    for u in data["units"]:
        if u["id"] == uid:
            return u
    raise SystemExit(f"unknown unit {uid}")


def render(root, template, unit):
    t = (Path(root) / "usecases" / "scoring" / "templates" / f"{template}.md").read_text(encoding="utf-8")
    rows = ", ".join(str(r) for r in unit["rows"])
    inputs = ", ".join(f"usecases/scoring/{i}.md and usecases/scoring/{i}.json" for i in unit.get("inputs", []))
    for k, v in (("{UNIT}", unit["id"]), ("{ROWS}", rows), ("{DIMS}", unit.get("dims", "")),
                 ("{EXTRA}", unit.get("extra", "")), ("{INPUTS}", inputs)):
        t = t.replace(k, v)
    return t


def cmd_add(a, root):
    data = load(root)
    if any(u["id"] == a.id for u in data["units"]):
        raise SystemExit(f"unit {a.id} exists")
    unit = {"id": a.id, "phase": a.phase, "agent": a.agent, "dims": a.dims, "rows": [int(x) for x in a.rows.split(",") if x],
            "template": a.template, "needs": [x for x in a.needs.split(",") if x], "inputs": [x for x in a.inputs.split(",") if x],
            "extra": a.extra, "pause_after": bool(a.pause_after), "state": "pending", "attempts": 0,
            "prompt": f"usecases/scoring/units/{a.id}.md",
            "outputs": [f"usecases/scoring/{a.id}.md", f"usecases/scoring/{a.id}.json"]}
    d, _, _ = paths(root)
    (d / "units").mkdir(parents=True, exist_ok=True)
    (Path(root) / unit["prompt"]).write_text(render(root, a.template, unit), encoding="utf-8")
    data["units"].append(unit)
    if data["status"] == "DONE":  # a new unit (for example a watch rescore proposal) reopens a finished queue
        data["status"] = "RUNNING"
    save(root, data)
    print(f"added {a.id} ({a.agent}, rows {unit['rows']})")


def eligible(data):
    cfg = data["config"]
    state = {u["id"]: u["state"] for u in data["units"]}
    blocked = False
    for u in data["units"]:
        if u["state"] in ("done", "failed-final"):
            continue
        if any(state.get(n) == "failed-final" for n in u["needs"]):
            blocked = True
            continue
        if all(state.get(n) == "done" for n in u["needs"]) and u["attempts"] < cfg["max_attempts"]:
            return u, False
    return None, blocked


def cmd_next(a, root):
    data = load(root)
    if data["status"] == "PAUSED":
        print("PAUSED: " + data.get("pause_reason", ""))
        return
    if data["status"] == "DONE":
        print("NONE: queue finished")
        return
    u, blocked = eligible(data)
    if u:
        print(json.dumps({k: u[k] for k in ("id", "agent", "prompt", "outputs", "phase", "rows")}))
    elif blocked:
        print("BLOCKED: a unit failed for good and others depend on it")
    else:
        print("NONE: nothing pending")


def cmd_done(a, root):
    data = load(root)
    u = find(data, a.id)
    u["state"] = "done"
    if u.get("pause_after"):
        data["status"] = "PAUSED"
        data["pause_reason"] = f"after unit {u['id']} ({u['phase']}): the user reviews before the queue continues"
    elif all(x["state"] in ("done", "failed-final") for x in data["units"]):
        data["status"] = "DONE"
    save(root, data)
    print(f"{a.id} done; queue {data['status']}")


def cmd_fail(a, root):
    data = load(root)
    u = find(data, a.id)
    u["attempts"] += 1
    u["last_error"] = a.error[:300]
    u["state"] = "failed-final" if u["attempts"] >= data["config"]["max_attempts"] else "pending"
    save(root, data)
    print(f"{a.id} {u['state']} after {u['attempts']} attempt(s)")


def cmd_status(a, root):
    data = load(root)
    counts = {}
    for u in data["units"]:
        counts[u["state"]] = counts.get(u["state"], 0) + 1
    print(f"queue {data['status']}" + (f" ({data['pause_reason']})" if data.get("pause_reason") else "") + f"; units: {counts or 'none'}")
    cmd_next(a, root)


def cmd_resume(a, root):
    data = load(root)
    data["status"] = "RUNNING"
    data["pause_reason"] = ""
    save(root, data)
    print("queue RUNNING")


def in_quiet(quiet, hour):
    if not quiet:
        return False
    s, e = quiet
    return (s <= hour < e) if s <= e else (hour >= s or hour < e)


def cmd_gate(a, root):
    cfg = load(root)["config"]
    if a.pct5 is None or a.weekly is None:
        # No usage tool (cloud session): limit the number of units per run instead.
        cap = cfg.get("cloud_units_per_run", 2)
        n = a.units_this_run
        if n is None:
            print("STOP: no usage figures given and no --units-this-run; pass one of them")
        elif n >= cap:
            print(f"STOP: {n} unit(s) already done this run (cap {cap}, no usage figures)")
        else:
            print(f"{'CONTINUE' if a.cont else 'START'} (no usage figures; {n} of {cap} unit(s) done this run)")
        return
    if a.pct5 >= cfg.get("hard_stop_pct5", 95):
        print(f"STOP: hard stop, 5-hour window at {a.pct5}% (limit {cfg.get('hard_stop_pct5', 95)}%)")
    elif a.weekly >= cfg["weekly_cap_pct"]:
        print(f"STOP: weekly limit at {a.weekly}% (cap {cfg['weekly_cap_pct']}%)")
    elif in_quiet(cfg.get("quiet_hours"), a.hour):
        print(f"STOP: quiet hours {cfg['quiet_hours']}")
    elif a.cont:
        print("CONTINUE" if a.pct5 < cfg["continue_limit_pct5"] else f"STOP: 5-hour window at {a.pct5}% (continue limit {cfg['continue_limit_pct5']}%)")
    else:
        print("START" if a.pct5 <= cfg["start_limit_pct5"] else f"STOP: 5-hour window at {a.pct5}% (start limit {cfg['start_limit_pct5']}%)")


def cmd_claim(a, root):
    """Record which side (local or cloud) is working on the queue; refuse if the other side holds it."""
    data = load(root)
    cur = data.get("running_on", "")
    if cur and cur != a.side and not a.force:
        print(f"REFUSED: queue is held by '{cur}' since {data.get('claimed_at', '?')}; use --force if that run is over")
        return 1
    data["running_on"] = a.side
    data["claimed_at"] = datetime.datetime.now().isoformat(timespec="seconds")
    save(root, data)
    print(f"claimed by {a.side}")
    return 0


def cmd_release(a, root):
    data = load(root)
    data["running_on"] = ""
    data["claimed_at"] = ""
    save(root, data)
    print("released")


def cmd_log(a, root):
    _, _, lg = paths(root)
    lg.parent.mkdir(parents=True, exist_ok=True)
    if not lg.exists():
        lg.write_text("\t".join(LOG_HEADER) + "\n", encoding="utf-8")
    row = [datetime.datetime.now().isoformat(timespec="seconds"), a.unit, a.pct5_before, a.pct5_after, a.weekly_before,
           a.weekly_after, a.tokens, a.tools, a.errors.replace("\t", " ").replace("\n", " ")]
    with lg.open("a", encoding="utf-8") as f:
        f.write("\t".join(str(x) for x in row) + "\n")
    print("logged")


def main():
    ap = argparse.ArgumentParser(description="Queue helper for the use-case scoring (no model).")
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("add")
    p.add_argument("--id", required=True)
    p.add_argument("--agent", required=True)
    p.add_argument("--dims", default="")
    p.add_argument("--rows", required=True)
    p.add_argument("--template", default="score")
    p.add_argument("--needs", default="")
    p.add_argument("--inputs", default="")
    p.add_argument("--phase", default="pilot")
    p.add_argument("--extra", default="")
    p.add_argument("--pause-after", action="store_true")
    for name in ("next", "status", "resume"):
        sub.add_parser(name)
    p = sub.add_parser("done")
    p.add_argument("id")
    p = sub.add_parser("fail")
    p.add_argument("id")
    p.add_argument("--error", default="")
    p = sub.add_parser("gate")
    p.add_argument("--pct5", type=float, default=None)
    p.add_argument("--weekly", type=float, default=None)
    p.add_argument("--hour", type=int, default=0)
    p.add_argument("--units-this-run", type=int, default=None, help="used when no usage figures are available (cloud)")
    p.add_argument("--continue", dest="cont", action="store_true")
    p = sub.add_parser("claim")
    p.add_argument("--side", choices=["local", "cloud"], required=True)
    p.add_argument("--force", action="store_true")
    sub.add_parser("release")
    p = sub.add_parser("log")
    p.add_argument("--unit", required=True)
    for k in ("pct5-before", "pct5-after", "weekly-before", "weekly-after"):
        p.add_argument("--" + k, default="")
    p.add_argument("--tokens", default="")
    p.add_argument("--tools", default="")
    p.add_argument("--errors", default="")
    a = ap.parse_args()
    fn = {"add": cmd_add, "next": cmd_next, "done": cmd_done, "fail": cmd_fail, "status": cmd_status,
          "resume": cmd_resume, "gate": cmd_gate, "log": cmd_log, "claim": cmd_claim, "release": cmd_release}[a.cmd]
    return fn(a, a.root) or 0


if __name__ == "__main__":
    sys.exit(main())
