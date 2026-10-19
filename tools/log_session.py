#!/usr/bin/env python3
"""Session-start hook: record the ID of each session that starts in this project.

Claude Code passes a small JSON block on standard input to SessionStart hooks. This script
reads it, appends one line (time, source, session ID, transcript file name, input keys) to
.claude/sessions.log, and prints one line so the new session can tell the user its own ID.

The log is git-ignored: it stays on this machine and is not published. The input keys are
logged on purpose, to show what the hook receives on this platform. Whether this ID matches
the "local_..." IDs used by the transcript search tools is not yet verified.
Standard library only. Never fails the session: any error is swallowed.
"""
import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOG = ROOT / ".claude" / "sessions.log"


def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except Exception:
        data = {}
    if not isinstance(data, dict):
        data = {}
    sid = str(data.get("session_id", "unknown"))
    source = str(data.get("source", "unknown"))
    transcript = pathlib.PurePath(str(data.get("transcript_path", ""))).name or "-"
    keys = ",".join(sorted(data.keys())) or "-"
    event = str(data.get("hook_event_name", "unknown"))
    reason = str(data.get("reason", "-"))
    title = " ".join(str(data.get("session_title", "-")).split())[:80] or "-"
    stamp = datetime.datetime.now().isoformat(timespec="seconds")
    try:
        LOG.parent.mkdir(exist_ok=True)
        with LOG.open("a", encoding="utf-8") as f:
            f.write(f"{stamp}\tevent={event}\tsource={source}\treason={reason}\tsession_id={sid}\ttitle={title}\ttranscript={transcript}\tkeys={keys}\n")
    except Exception:
        pass
    if event == "SessionEnd":
        return
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(f"Session ID (from the start hook; logged in .claude/sessions.log): {sid} (source: {source})")


if __name__ == "__main__":
    main()
