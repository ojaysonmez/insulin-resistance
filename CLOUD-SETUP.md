# Cloud setup (Claude's own cloud sessions and routines)

Status: draft written 2026-10-23 from the official Claude Code docs; nothing here has been tested in a cloud session yet. Mark each item below when it is checked.

## What the docs say (and what they leave open)
- A cloud session clones the repository fresh each time. Only what is committed and pushed survives; treat uncommitted files as lost.
- It reads the committed `.claude/settings.json` (hooks, permission rules). It does **not** read `.claude/settings.local.json`. Our hooks and permission rules are in the local file today, so they would not apply.
- Packages: a setup script (set per cloud environment at claude.ai/code, runs as root on Ubuntu, result cached) or a SessionStart hook in `settings.json` can run `pip install openpyxl`. The docs list "Python 3.x with pip" but not the minor version, whether `python` exists (our hooks and task prompts call `python`), or whether openpyxl is present.
- Network: the default level (Trusted) allows only a fixed list (GitHub, package registries and similar). PubMed (`eutils.ncbi.nlm.nih.gov`), Crossref, ClinicalTrials.gov, PubMed Central and CDC are not on it. Use a Custom environment and list those hosts. Connector traffic needs no entry.
- Routines (cloud scheduled tasks) belong to the claude.ai account, run with the computer off, start in auto mode, clone the default branch and by default push to a `claude/`-prefixed branch (a prompt can name another branch; GitHub branch protection decides whether `main` is allowed). Minimum interval is one hour. Local desktop scheduled tasks are a separate system.
- Account connectors (for example Google Drive) are included in routines by default.
- Not documented: whether the usage tool and the 5-hour / weekly windows exist inside a cloud session. `tools/scoring_queue.py gate` depends on them, so the gate needs a fallback (see below).

## First checkout: do these in order
1. Create a cloud environment with network access Custom and these allowed hosts: `eutils.ncbi.nlm.nih.gov`, `api.crossref.org`, `clinicaltrials.gov`, `pmc.ncbi.nlm.nih.gov`, `www.cdc.gov`, plus the default package list.
2. Environment setup script: `pip install openpyxl` (and, if `python` is missing, a link from `python3`).
3. Start a session on this repository and run:
   ```
   python3 tools/cloud_check.py
   ```
   It prints PASS, WARN or FAIL per item with the fix. Send me the output.
4. Read the output: the check shows whether `.claude/settings.json` loaded (proof: the session-start brief, headed "IR project status brief", is in the session's first context) and which commands or hosts fail.
5. Run one routine by hand with a test prompt before any schedule goes live; confirm it can commit and push to its branch.

## Done on 2026-10-23 for running in both places
- Hooks and permission rules now live in the committed `.claude/settings.json` (`settings.local.json` is empty). The hook command picks `python` or else `python3`.
- `python tools/scoring_queue.py gate` works without usage figures: omit `--pct5`/`--weekly` and pass `--units-this-run N`; it stops at `cloud_units_per_run` (default 2, set in `usecases/scoring/queue.json` config). A cloud runner prompt must use this form.
- `scoring_queue.py claim --side local|cloud` and `release` record which side holds the queue (`running_on`); the other side is refused unless `--force`. A runner should claim at the start, release at the end, and pull before it pushes.
- `.gitattributes` normalises line endings to LF for new commits (existing files are not rewritten); the queue helper writes LF.

## Open decisions
- Branch for runs: one branch holding code and data (user preference). Two routines pushing the same branch can conflict; keep the watch and the scoring runner on different hours and have each pull before it pushes.
- Cloud runner prompts (watch and scoring) still need to be written and tested; the local ones use usage figures and `python`.
- The eLFA workbook is on the local `I:` drive; in the cloud the DOI list would have to come through the Drive connector, or the DOI column stays blank.
- Contacts (`corpus/local/`) and full texts (`corpus/fulltext/`) stay out of the repository, so they do not exist in the cloud; corpus extraction that needs full texts stays local.
