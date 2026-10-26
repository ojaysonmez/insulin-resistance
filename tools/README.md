# Tools

Scripts and hook setup for the project. Nothing here changes the findings; the scripts read files and write only their own report or cache files.

## session_start_context.py (session-start hook, installed 2026-10-19)
Prints a short, read-only context brief for the start of each session: the hand-written handoff note (`HANDOFF.md`), a one-line index of the decisions in `DECISIONS.md`, the project memory index (`memory/MEMORY.md`), the last five commits, the branch and uncommitted changes (with a warning when local commits are not pushed), the pending update items, the open items from `CHANGELOG.md`, and the conventions in two lines. Read-only and standard-library only; it does not call the network. Output is capped at 70 lines.

How it is wired: the hook entry is in `.claude/settings.local.json` (tracked in git since 2026-10-19, so a clone of the public repo gets the hooks; they run the scripts in `tools/` at session start, so read them before trusting a clone). The same block would also work in `.claude/settings.json`:

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

## deliverable_reminder.py (PostToolUse hook, added 2026-10-19)

After each Edit, Write or MultiEdit, checks whether the edited file is `merged-conclusion.md`, `usecases-verified.md` or `claims/claims.csv`. If so, it returns a short reminder to the session as extra context: only the main session edits deliverables, a substantive change needs a skeptic review, log it in `CHANGELOG.md`, keep the scope wording and the identifier rule. It never blocks an edit and never fails the tool call. Limit: edits made through shell commands (sed, a Python script run from Bash) are not caught. Registered under `PostToolUse` in `.claude/settings.local.json`; takes effect in the next new session.

## precommit_check.py and tools/githooks/pre-commit (added 2026-10-19)

A git pre-commit check for the public repository. It examines only what a commit would add and blocks the commit on: PDF, EPUB or Word files; a `local_...` session ID; an absolute Windows or Unix user path (except in the documentation files that discuss history: `CHANGELOG.md`, `CONVENTIONS.md`, `DECISIONS.md`, `HANDOFF.md`, `CLAUDE.md`, this README and `memory/`); and strings that look like API keys, tokens or private keys. It only warns about email addresses and files over 1 MB. Dry run on history: `python tools/precommit_check.py --range A..B`. Enable the hook once per clone with `git config core.hooksPath tools/githooks` (done on this machine 2026-10-19). Skipping it with `--no-verify` is against the project rules. Tested on the staged test file (all four kinds blocked) and on the commit that once carried a session ID (blocked); the last eleven normal commits pass.

## Permission rules (added 2026-10-19)

`.claude/settings.local.json` also holds permission rules: read-only git commands and the two local check scripts are allowed without a prompt; `git push`, `git remote add/set-url` and `gh repo ...` ask each time; force pushes, `git reset --hard` and commits that skip hooks are denied. The rule syntax and the effect inside this app were not tested in a live session; if a rule does nothing or blocks something it should not, edit the file.

## watch_fetch.py (update watch retrieval step, added 2026-10-19)

No model, standard library only. Runs the PubMed queries in `update-watch/queries.json` over an entry-date window (`--days`, default 2; `--date-to`, default today), skips PMIDs already in `update-watch/seen-pmids.txt`, fetches compact records for the new ones, compares the tracked NCT numbers with `update-watch/registry-baseline.json` (first run sets the baseline; flags status, results, enrolment or last-update changes and registrations whose completion date passed more than 183 days ago while still active), and writes `update-watch/runs/<date>-candidates.md` with the deliverables' headings and row titles for the Affects field. `--no-update` writes only the report, for tests. Imports the HTTP helper from `check_citations.py`. Tested 2026-10-19 on the dry run window: 13 queries, 51 new records, 0 errors, same hit counts and registry values as the dry run agent, 12.7 seconds. Use `check_citations.py --refresh` (not the cached default) for the retraction check in the watch.

## apply_rescore.py, watch_commit.py and URGENT.md (added 2026-10-26, D-48)

`apply_rescore.py --pending` applies small rescore proposals from the R units (one point, medium or high confidence, a quote, exactly one matching score entry; original score kept; log in `usecases/scoring/rescore-log.tsv`; regenerates the ranking and the scorecard). `watch_commit.py --message TEXT [--push] [--dry-run]` commits and pushes only allow-listed files on main (summary.md only inside the scorecard block). `update-watch/URGENT.md` is written by the daily watch on an urgent flag and shown by the session-start brief. Tests: `python tools/test_autonomy.py`.
