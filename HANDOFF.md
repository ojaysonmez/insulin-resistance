# Handoff

Updated: 2026-10-26 (rewritten from the cloud and local work of 2026-10-23 to 25; older bullets that described the pilot, tonight's runs and a paused queue were removed)

The current state and the next step, written by hand at the end of a working session. It is overwritten each time (history lives in `CHANGELOG.md` and git). `tools/session_start_context.py` prints this note's main sections at the start of each session. Update it at the end of every working session. Local and cloud sessions cannot see each other's chats (D-36), so anything a later session needs goes here, in `DECISIONS.md`, `CHANGELOG.md` or `memory/`.

## Where we are
- **Goal (D-30):** find and score the most viable uses of insulin, C-peptide and insulin-resistance measurement, and what would make the weaker ones viable. Clinical utility (`merged-conclusion.md`) is the constraint. Coverage and reimbursement are out of scope.
- **Scoring is finished (D-32 to D-43):** the queue is DONE (36 units, none failed). `usecases/scoring/ranking.md` ranks 32 rows in tiers A to D; tier A is rows 6, 1 and 31 (rows 6 and 31 are one pathway), row 7 is conditional. Row 48 is unranked and rows 35, 36, 43, 44, 45 are Not evaluated. Scores stay preliminary judgements; read the tier, not the rank. Stage 3 dossiers (rows 6, 1, 7, 31) are in `usecases/scoring/dossiers/`. `usecases/scoring/usage-log.tsv` has no lines after V6 (later units were not logged).
- **Documents:** `summary.md` (rewritten after scoring; section 1b lists the pathways), `merged-conclusion.md` and `usecases-verified.md` (50 rows) are updated by all six specialty reviews (D-44, D-45). The claim ledger v1 is built (`claims/claims.csv`, 386 rows, D-46); edits now go ledger first.
- **Pathway 1 work (rows 6 and 31), 2026-10-24/25:** `usecases/scoring/pathways/` holds the plan (`pathway-1-plan.md`, `.docx`), a registry search and a partner scouting file; also `usecases/scoring/metsulin-fit.md`, `home-cpeptide-precedents.md`, `t1d-preservation-trials.md`, `stem-cell-islet-trials.md` and a 50-row review sheet (XLSX). These were produced in cloud sessions; read the CHANGELOG entries before relying on them.
- **Running in both places (2026-10-23, D-36):** the project runs in Claude Code locally and in Claude cloud sessions on `main` (rule in `CLAUDE.md`). Hooks and permissions live in `.claude/settings.json`. The session-start hook prints a screen message and a brief that includes a short environment check (`tools/cloud_check.py --brief`). Send "status" as the first message for a summary. `CLOUD-SETUP.md` has the setup notes; the cloud push, branch and ask-rule questions for unattended runs are still open there. The session-ID feature was removed. Desktop scheduled tasks are paused.
- **Daily update watch in the cloud (D-47):** a scheduled cloud task runs at 01:43 America/Los_Angeles and pushes only `update-watch/` files and the citation report to `main`. On 2026-10-26 the latest watch run in the repository is 2026-10-24; check whether the runs of 10-25 and 10-26 happened (trigger history on claude.ai, and whether the push was refused or skipped).

## Next step
- Check the daily cloud watch gap above first.
- Open from the 10-24 handoff: search-string logs for 5 ledger absence rows; an ID-consistency script; retrieval of the ISPAD monogenic chapter (PMID 36537518); Gavigan numbers in `usecases/scoring/dossiers/row-31.md`; PRINCESS (NCT05760339) stale and four non-NCT registry IDs to check by hand; the summary editor pass on `summary.md`.
- Decide whether to start harmonisation or accuracy-study planning for pathway 1, and whether to score more of the rows that only have a stage 1 screen (search-heavy; ask about the usage limit first).
- Author contacts (D-35): `corpus/local/contacts.xlsx` (git-ignored, personal, never commit; local machine only): 190 rows from 138 articles, 33 articles with a US contact that has an email, for the investor letters of intent. Open: the investor's three questions (to rank contacts), dedupe against the Drive files `Investigators.xlsx` and the Outreach Tracker (read-only, needs the user's go-ahead). The assistant sends no email.
- Corpus (D-34): rebuilt 2026-10-26 to 189 articles; the reading columns (role, design, key numbers, claims) are still empty (extraction not run). The brief and the deliverable reminder warn when cited PMIDs are missing; rebuild with `python tools/corpus_build.py` on the local machine (full texts and the eLFA path exist only there). `corpus/pdf-wanted.md` lists articles without an open copy; `python tools/corpus_fulltext.py` fetches new open texts.

## Waiting on the user
- **Scoring runner (D-48):** the task `ir-scoring-runner-2` is still disabled with its old prompt. Updating and enabling it was denied by the auto-mode classifier. Enable it (or allow `mcp__scheduled-tasks__update_scheduled_task`) so R2 runs overnight and small rescores are applied; the new steps are 6b (`python tools/apply_rescore.py --pending`) and 6c (`python tools/watch_commit.py --message ... --push`) after the aggregate and scorecard step.
- Review the first automatic watch commit and push (the next 01:15 run) and the first rescore-log entries.
- Whether to supply PDFs for the load-bearing papers that were read only at abstract level (user said not yet).
- Permission for search-heavy agent runs (the user is watching a usage limit).
- How cloud runs should push: allow `main` for state files only, or a `claude/` branch first (see `CLOUD-SETUP.md`).

## Watch out for
- Do not launch search-heavy agents or push to the public repo without being asked; push only when the user asks.
- Create files where they belong, not as drafts in another folder. Use project-root-relative paths.
- Make a tool or schedule work and show it before asking to commit (`memory/feedback_verify_before_commit.md`).
- Read `DECISIONS.md` before changing a settled decision. Confidence figures were not re-derived after the measure-type rescoping.
- Constraints from the user: coverage and reimbursement are out of scope; the repository is public (no personal data, no PDFs or full texts); hard stop for agents at 95% of the 5-hour usage window; new agent roles become usable only after the turn that creates them.
