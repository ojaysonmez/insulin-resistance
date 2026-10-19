#!/usr/bin/env python3
"""Session-start status brief for the IR project (DRAFT, not installed).

Prints a short plain-text brief to stdout. When installed as a Claude Code
SessionStart hook, whatever this prints is added to the start of each session, so
a new or resumed session knows where the project stands.

Read-only: it reads git state, HANDOFF.md, CHANGELOG.md and update-system/PENDING.md and
writes nothing. Standard library only. Keeps the brief under MAX_LINES lines.
"""
import pathlib
import re
import subprocess
import sys

MAX_LINES = 60
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

    pending = len(re.findall(r"^### P-", read("update-system/PENDING.md"), flags=re.M))
    brief.append(f"Update watch: {pending} pending item(s) in update-system/PENDING.md (watch not yet running).")

    open_items = section_bullets(read("CHANGELOG.md"), "## Not yet run or done")
    if open_items:
        brief.append("Open items (CHANGELOG.md, 'Not yet run or done'):")
        brief += [f"  {b}" for b in open_items]

    brief += [
        "Start here: README.md (index), CONVENTIONS.md (rules), merged-conclusion.md and usecases-verified.md (final documents),",
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
