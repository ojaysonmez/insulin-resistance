# Session-start brief and project CLAUDE.md (installed 2026-10-19)

Installed on 2026-10-19 at the user's request: `CLAUDE.md` is in the project root, and the hook is in `.claude/settings.local.json`. Both take effect when a new session starts.

## What it does
- `update-system/session_brief.py` prints a short, read-only status brief (last five commits, branch and uncommitted changes, whether local commits are unpushed, pending update items, the open items from `CHANGELOG.md`, and the conventions in one paragraph). As a Claude Code `SessionStart` hook, its output is added to the context of each new or resumed session.
- `CLAUDE.md` in the project root holds the static rules (it began as `update-system/CLAUDE.md.draft`). Claude Code loads a root `CLAUDE.md` automatically, so no hook is needed for static rules.

## How it was installed (kept for reference and re-installation)
1. **Project rules:** `CLAUDE.md` in the project root (moved from `update-system/CLAUDE.md.draft`).
2. **Hook:** placed in `.claude/settings.local.json`, which is git-ignored, so the hook stays on this machine and is not shipped to clones of the public repo. To share it, put the same block in `.claude/settings.json` instead:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear|compact",
        "hooks": [
          { "type": "command", "command": "python update-system/session_brief.py" }
        ]
      }
    ]
  }
}
```

3. Start a new session and check that the brief appears at the top. If the command is not found, use the full path to `python` in the command; if the path fails, check which directory hooks run in (they normally run in the project root).

## To remove
Delete `.claude/settings.local.json` (or its `hooks` entry) and delete or rename `CLAUDE.md`.

## Checks and limits
- The script is read-only and standard-library only. It does not call the network.
- It reads the "Not yet run or done" section of `CHANGELOG.md`, so that section must stay current. The brief is only as accurate as the changelog and git state.
- Keep the brief short (the script caps it at 45 lines); a long brief uses context in every session.
- I have not verified how the harness handles hook output on every platform. Confirm that the brief appears, and that it does not appear twice (for example on `compact`), before relying on it.
- A hook runs a command automatically. Read `session_brief.py` before enabling it.
