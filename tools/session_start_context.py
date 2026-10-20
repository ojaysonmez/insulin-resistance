#!/usr/bin/env python3
"""Session-start status brief for the IR project (DRAFT, not installed).

Prints a short plain-text brief to stdout. When installed as a Claude Code
SessionStart hook, whatever this prints is added to the start of each session, so
a new or resumed session knows where the project stands.

Read-only: it reads git state, HANDOFF.md, CHANGELOG.md and update-watch/PENDING.md and
writes nothing. Standard library only. Keeps the brief under MAX_LINES lines.
"""
import json
import pathlib
import re
import subprocess
import sys

MAX_LINES = 70
ROOT = pathlib.Path(__file__).resolve().parent.parent


def git(*args):
    try:
        out = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, timeout=15)
        return out.stdout.strip() if out.returncode == 0 else ""
    except Exception:
        return ""


def read(path):
    try:
        return (ROOT / path).read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def section_bullets(text, heading_prefix, limit=8):
    """Bullets under the first heading that starts with heading_prefix (until the next '## ')."""
    lines, out, on = text.splitlines(), [], False
    for ln in lines:
        if ln.startswith("## "):
            if on:
                break
            on = ln.startswith(heading_prefix)
            continue
        if on and ln.lstrip().startswith("- "):
            out.append(ln.strip()[:200])
            if len(out) >= limit:
                break
    return out


def main():
    brief = ["IR project status brief (generated at session start; read-only)"]

    handoff = read("HANDOFF.md")
    if handoff:
        upd = re.search(r"^Updated:\s*(.+)$", handoff, flags=re.M)
        brief.append("Handoff note (HANDOFF.md" + (f", updated {upd.group(1)}" if upd else "") + "):")
        for title in ("## Where we are", "## Next step", "## Waiting on the user", "## Watch out for"):
            for b in section_bullets(handoff, title, limit=5):
                brief.append(f"  [{title[3:]}] {b[2:]}")

    decisions = re.findall(r"^\*\*(D-\d+)\.\s+(.+?)\.?\*\*", read("DECISIONS.md"), flags=re.M)
    if decisions:
        brief.append("Decisions already made (open DECISIONS.md and read the entry before changing one):")
        line = "  "
        for did, title in decisions:
            item = f"{did} {title}; "
            if len(line) + len(item) > 150:
                brief.append(line.rstrip("; "))
                line = "  "
            line += item
        brief.append(line.rstrip("; "))

    notes = [ln.strip() for ln in read("memory/MEMORY.md").splitlines() if ln.startswith("- [")]
    if notes:
        brief.append("Project memory (memory/, one note per file; add new notes there, not in the private Claude folder):")
        brief += [f"  {n[:170]}" for n in notes[:12]]

    log = git("log", "-5", "--format=%h %ad %s", "--date=short")
    if log:
        brief.append("Last commits:")
        brief += [f"  {ln[:150]}" for ln in log.splitlines()]

    status = git("status", "-sb")
    if status:
        lines = status.splitlines()
        branch = lines[0].lstrip("# ").strip()
        changed = [ln.strip() for ln in lines[1:] if ln.strip()]
        brief.append(f"Branch: {branch}")
        if changed:
            brief.append(f"Uncommitted changes ({len(changed)}): " + "; ".join(changed[:8]) + (" ..." if len(changed) > 8 else ""))
        else:
            brief.append("Working tree: clean")
        if re.search(r"ahead \d+", branch):
            brief.append("Note: local commits are not pushed to the public repo. Push only when the user asks.")

    pending = len(re.findall(r"^### P-", read("update-watch/PENDING.md"), flags=re.M))
    brief.append(f"Update watch: {pending} pending item(s) in update-watch/PENDING.md (watch not yet running).")

    latest = None
    runs_dir = ROOT / "update-watch" / "runs"
    if runs_dir.is_dir():
        for f in runs_dir.glob("*-triage.md"):
            m = re.fullmatch(r"(\d{4}-\d{2}-\d{2})-triage\.md", f.name)
            if m and (latest is None or m.group(1) > latest[0]):
                latest = (m.group(1), f)
    if latest:
        summary = ""
        for ln in read(f"update-watch/runs/{latest[1].name}").splitlines()[:5]:
            if ln.startswith("SUMMARY:"):
                summary = ln[len("SUMMARY:"):].strip()
                break
        try:
            import datetime
            age = (datetime.date.today() - datetime.date.fromisoformat(latest[0])).days
        except ValueError:
            age = -1
        note = f" ({age} day(s) ago; the daily pilot expects a run every day)" if age > 2 else ""
        brief.append(f"Update watch, latest run {latest[0]}{note}: {summary or 'no SUMMARY line in the file'}")

    try:
        qd = json.loads(read("usecases/scoring/queue.json") or "{}")
        if qd.get("units"):
            counts = {}
            for u in qd["units"]:
                counts[u["state"]] = counts.get(u["state"], 0) + 1
            note = f" ({qd['pause_reason']})" if qd.get("pause_reason") else ""
            brief.append(f"Scoring queue {qd.get('status', '?')}{note}: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + " (usecases/scoring/queue.json)")
    except Exception:
        pass

    open_items = section_bullets(read("CHANGELOG.md"), "## Not yet run or done")
    if open_items:
        brief.append("Open items (CHANGELOG.md, 'Not yet run or done'):")
        brief += [f"  {b}" for b in open_items]

    brief += [
        "Start here: README.md (index), summary.md (one-page brief of viable uses), CONVENTIONS.md (rules), merged-conclusion.md and usecases-verified.md (final documents),",
        "  usecases/scoring-rubric.md (scoring decisions; pilot on rows 6, 5, 13 not yet run).",
        "Rules in short: relative paths only; record PMID and DOI; unattended runs never stop to ask; agents do not edit",
        "  deliverables; log every change in CHANGELOG.md; commit and push only when the user asks.",
    ]

    if len(brief) > MAX_LINES:
        brief = brief[: MAX_LINES - 1] + ["... (brief truncated)"]
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print("\n".join(brief))


if __name__ == "__main__":
    main()
