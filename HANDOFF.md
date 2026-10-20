# Handoff

Updated: 2026-10-19 (night; scoring funnel stage 1 done for 21 candidates, runners scheduled for tonight)

The current state and the next step, written by hand at the end of a working session. It is overwritten each time (history lives in `CHANGELOG.md` and git). `tools/session_start_context.py` prints this note's main sections at the start of each session. Update it at the end of every working session.

## Where we are
- **Goal reframed (2026-10-19, D-30):** the main goal is scoring the viability of use cases and finding what would make the less viable ones viable; clinical utility is the constraint, not the headline. `summary.md` is now a one-page viable-pathways brief; the long version is `summary-detailed.md`. The rubric records a path to viability for every candidate.
- The merged conclusion and the 49-row use-case list are written, skeptic-reviewed and rescoped by measure type; the repository is public with a disclaimer.
- The use-case scoring rubric is settled (US commonality, weights utility 0.40, commonality 0.25, stakes 0.20, readiness 0.15, all candidates ranked with a setting tag); nothing is scored yet.
- Session continuity is set up this session: `CLAUDE.md`, the session-start hook, `DECISIONS.md`, this note and in-repo project memory (`memory/`).
- Check the session brief for unpushed commits and uncommitted changes (it shows the live git state).

## Next step
- **Start here in a fresh chat (written 2026-10-19 night):** the previous working chat grew to about 790,000 tokens of context and was the main consumer of the 5-hour window (the agents are cheap: the three stage 1 screens cost about 146,000 tokens in total). Do not continue it; start a new chat in this folder. Avoid heavy use of any chat between about 21:50 and 01:30 so tonight's runs find a fresh window.
- **Tonight's scheduled runs (check them first in the morning):** the update watch at about 01:15 and the scoring runner `ir-scoring-runner-2` at 01:30 (cron `21 1 * * *`, Auto mode). The runner reads the usage tool, starts a unit only at or below 40% of the 5-hour window, and runs U2 to U5 of the pilot (U6, the skeptic review, then pauses the queue). Look at `usecases/scoring/usage-log.tsv`, `usecases/scoring/` (U2 to U5 reports and JSON) and `update-watch/runs/`. If the log shows a SKIP line, read its reason (usage tool unavailable, window too full, or quiet hours).
- **Scoring funnel (decision D-30; approach agreed 2026-10-19):** stage 1 cheap screen of all candidates (lean agent; D1, D2, D3, D7, stakes, path to viability, tier); stage 2 all roles on the shortlist; stage 3 skeptic review of the ranking. **Stage 1 is done for all 32 candidates** (units S1 to S4; combined table `usecases/scoring/screen-summary.md`, regenerate with `python tools/scoring_screen_summary.py`). Viable now: rows 1, 4, 29, 6, 2, 24, 10. Close: rows 31, 7, 13, 3, 5, 32, 22, 23, 33, 47, 49. Far: rows 14, 9, 28, 12, 21, 46, 35, 20, 45, 11, 8, 25, 27, 48. D7 in S1 came from memory (rows 5 and 12 have the wrong bin) and most D7 values are low confidence; stage 2 must research them for the shortlist. D8 and the readiness details are not scored yet. Hard stop rule from the user: stop all agents at 95% of the 5-hour window (built into `tools/scoring_queue.py gate`).
- **Scorecard:** `summary.md` ends with a generated scorecard block of all screened rows (tier, index, composite when complete, patients per year, missing piece). `python tools/update_scorecard.py` refreshes it; the night runner does it after each run that finishes a unit.
- **Next steps, in order:** (1) read the overnight results (U2 to U5, the watch); (2) pick the stage 2 shortlist, suggested: the close tier with a small or medium effort and a large patient pool or high stakes (rows 13, 5, 31, 7, 32, 47, 49, 23) plus the viable-now rows whose missing piece is an assay or guideline step (rows 4, 10), then run all roles per row (units like U1 to U5 but one row each, with D7 researched); (3) skeptic review of the ranking and weights (`python tools/scoring_aggregate.py`), then the 2 to 3 pathways; (4) rewrite `summary.md` with the scores. Pilot units U2 to U6 are queued for tonight.
- **Working rules learned this session:** make a tool or schedule work and show it before asking to commit (`memory/feedback_verify_before_commit.md`); new agent roles become available only after the turn that creates them; a scheduled task created in a turn started by an automatic event does not keep Auto mode (recreate it in a typed turn); the scheduler adds a fixed delay per task (the scoring runner shows 01:30 for cron minute 21).
- **Review `summary.md` (written 2026-10-19):** skeptic-review it, then correct the outdated 'Crossref retraction checks found none' sentence in `merged-conclusion.md` (Provenance) with a skeptic check; the summary already states the later result (DiaPep277 retraction, 8 corrections).
- **Check the first daily watch run (scheduled 2026-10-20, about 01:15 local; the computer must stay awake with the app open):** the session brief prints a line "Update watch, latest run ..."; open `update-watch/runs/2026-10-20-triage.md` and `update-watch/runs/usage-log.tsv`; confirm the state files `update-watch/seen-pmids.txt` and `update-watch/registry-baseline.json` were created; look at what the scheduled session itself cost (not logged). Pilot ends 2026-11-02; then decide weekly running (D-28, D-29) and delete the task. The state and run files show as uncommitted changes each day; commit them when you choose.
- Run the scoring pilot on rows 6, 5 and 13 (needs searching for US commonality) once the user agrees, then score about 30 candidates by dimension.
- The pilot is drafted as a workflow script, `.claude/workflows/usecase-scoring-pilot.js` (six agents, not run, review first). Running it needs the user's explicit go-ahead for the Workflow tool and room under the usage limit.
- The session-start brief and the in-repo memory rule were both verified in a new session on 2026-10-19; nothing is pending there.
- Then, as the user chooses: specialty reviews (cardiology first), summary editor, claim ledger build, update-watch dry run.

## Waiting on the user
- Whether to move the hook from `.claude/settings.local.json` to the shared `settings.json`. (The local file is now tracked in git, so this matters less.)
- Whether to supply PDFs for the 20-30 load-bearing papers that were read only at abstract level (user said not yet).
- Permission to start search-heavy agent runs (the user is watching a usage limit).

## Watch out for
- Do not launch search-heavy agents or push to the public repo without being asked.
- Create files where they belong, not as drafts in another folder.
- Deferred wording items from the scope review: about ten generic "IR" statements, rows 17, 35 and 45 relabelling, and a check of whether WBISI is the Matsuda index.
- Confidence figures (80-85% and 45-50%) were not re-derived after the measure-type rescoping.
- Read `DECISIONS.md` before changing a settled decision.
- Constraints from the user: coverage and reimbursement are out of scope; nothing is published or pushed without a request; PDFs are "not yet"; the memory folder is tracked in the public repo.
- Compaction check (2026-10-19): the session-start hook fired once after compaction of the working chat, so the brief is not duplicated. That chat's transcript file shrank from about 5.2 MB to about 0.86 MB for an unconfirmed reason, so treat the repository files, not the transcript, as the reliable record.
- Advice given when the working chat reached about 96% context: start a new chat for the next task (the scoring pilot) instead of continuing in a compacted one, because a long context costs more per message against the usage limit.

## Earlier chats
- The long working chat that built all of this can be searched from a new session with the transcript search tool (it searches other sessions' transcripts by text). Its session ID is in the git-ignored local log `.claude/sessions.log` (the `event=Manual` lines); `memory/reference_working_chat.md` explains how to find it.
