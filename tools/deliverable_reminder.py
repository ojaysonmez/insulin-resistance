#!/usr/bin/env python3
"""PostToolUse hook: remind the session when a deliverable file was edited.

Claude Code passes a JSON block on standard input after each Edit, Write or MultiEdit.
If the edited file is one of the deliverables named in CLAUDE.md, this script prints a
short reminder that goes back to the session as extra context. It never blocks anything
and never fails the tool call: any error is swallowed and nothing is printed.

Limit: edits made through shell commands (for example sed or a Python script run from
Bash) do not pass through Edit or Write, so they are not caught.
Standard library only.
"""
import json
import pathlib
import subprocess
import sys

DELIVERABLES = {
    "merged-conclusion.md",
    "usecases-verified.md",
    "claims/claims.csv",
}

REMINDER = (
    "Deliverable edited: {name}. Per CLAUDE.md: (1) only the main session edits deliverables, "
    "not subagents; (2) a substantive change needs a skeptic review before it is committed; "
    "(3) log the change in CHANGELOG.md; (4) keep the measure-type scope wording and the "
    "PMID + DOI + read-level rule. If this edit was wording-only, say so in the changelog entry."
)


def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
        tool_input = data.get("tool_input") or {}
        raw = str(tool_input.get("file_path") or tool_input.get("path") or "")
        if not raw:
            return
        path = pathlib.PurePath(raw.replace("\\", "/"))
        parts = path.as_posix().split("/")
        name = None
        for key in DELIVERABLES:
            n = len(key.split("/"))
            if parts[-n:] == key.split("/"):
                name = key
                break
        if not name:
            return
        text = REMINDER.format(name=name)
        if name in ("merged-conclusion.md", "usecases-verified.md"):  # citations may have changed: is the corpus behind?
            try:
                root = pathlib.Path(__file__).resolve().parent.parent
                r = subprocess.run([sys.executable, str(root / "tools" / "corpus_build.py"), "--check"], capture_output=True,
                                   text=True, timeout=20, cwd=str(root))
                if r.stdout.strip():
                    text += " Corpus: " + r.stdout.strip()
            except Exception:
                pass
        out = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": text,
            }
        }
        sys.stdout.reconfigure(encoding="utf-8")
        print(json.dumps(out))
    except Exception:
        return


if __name__ == "__main__":
    main()
