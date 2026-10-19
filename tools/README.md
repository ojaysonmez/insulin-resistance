# Tools

Scripts and hook setup for the project. Nothing here changes the findings; the scripts read files and write only their own report or cache files.

## session_start_context.py (session-start hook, installed 2026-10-19)
Prints a short, read-only context brief for the start of each session: the hand-written handoff note (`HANDOFF.md`), a one-line index of the decisions in `DECISIONS.md`, the project memory index (`memory/MEMORY.md`), the last five commits, the branch and uncommitted changes (with a warning when local commits are not pushed), the pending update items, the open items from `CHANGELOG.md`, and the conventions in two lines. Read-only and standard-library only; it does not call the network. Output is capped at 70 lines.

How it is wired: the hook entry is in `.claude/settings.local.json` (git-ignored, so it stays on this machine and is not shipped to clones of the public repo). To share it, put the same block in `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear|compact",
        "hooks": [
          { "type": "command", "command": "python tools/session_start_context.py" }
        ]
      }
    ]
  }
}
```

The static project rules are in `CLAUDE.md` in the project root, which Claude Code loads automatically; no hook is needed for them.

To remove: delete `.claude/settings.local.json` (or its `hooks` entry).

Checks and limits:
- The brief is only as accurate as `HANDOFF.md`, `CHANGELOG.md` ("Not yet run or done" section) and git state. Update the handoff at the end of each working session.
- Not yet verified in a new session: that the brief appears once at the start, and not twice (for example on `compact`).
- A hook runs a command automatically. Read the script before enabling it.

## check_citations.py (citation checker)
Extracts PMIDs and DOIs from markdown files and checks them against PubMed and Crossref: PMID not found, DOI and PMID pairs on one line that PubMed disagrees with, retractions, corrections and errata, and DOIs PubMed knows that the files do not record. Checks identity and notices only, not that a claim matches its paper. Caches results so repeat runs fetch only what is new.

```
python tools/check_citations.py merged-conclusion.md usecases-verified.md
```

Defaults write `tools/citation-report.md`, `tools/citation-report.json` and `tools/.citation-cache.json` (all git-ignored). Optional environment variables: `NCBI_API_KEY` (higher rate limit) and `CROSSREF_MAILTO` (Crossref's polite pool; never hard-coded). Exit code 1 means an urgent flag (a retracted paper or mismatch), 2 a network failure. Use `--max 10` for a small test run.
