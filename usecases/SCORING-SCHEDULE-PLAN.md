# Plan: run the use-case scoring in 5-hour slots so it never exhausts a usage window (DRAFT, 2026-10-19, not built)

> Paths: this file lives in `usecases/`. It schedules the process in `usecases/scoring-rubric.md` (decisions D-22, D-23, D-30). Coverage and reimbursement are out of scope. Nothing here is built or scheduled yet.

## Why and what we measured
The user wants scoring to proceed in slots about 5 hours apart so that no single run uses up the 5-hour usage window. A read of the account's limits today (2026-10-19, plan Max) shows the 5-hour window at 53% used with a reset in 1 h 45 min, and the weekly limit at 32% used with a reset in 6 d 8 h. The usage tool works from a session, so a scheduled run can read the percentages itself. Two consequences: (1) the schedule can be adaptive (start a unit only when the window has room) instead of relying on fixed spacing alone; (2) the pilot gives us the first real cost per unit in percent of the window. Side note: this working chat has a context of about 663,000 tokens (66% of its window), and every message re-reads it, so it is probably the largest consumer of the window; starting a fresh chat for the scoring phase would help.

## Design: a queue of small units, one runner, a gate
1. **Units, not one big workflow.** The scoring process is cut into units; one unit = one subagent run with one prompt and one output file. Plain subagent calls are used because a scheduled session should not need the multi-agent workflow tool (which needs an explicit user opt-in). Units for the pilot (rows 6, 5, 13): U1 evidence searcher (D7 US patients, D3 guideline status); U2 biostatistician (D2, D8 and path to viability); U3 clinical chemist (D4); U4 endocrinologist (D1, D5, D6, stakes); U5 PCP (same dimensions, independently); U6 skeptic review of U1 to U5. Later phases use the same recipe per batch of at most 8 candidates per role: for about 31 candidates that is 4 batches x 5 roles = 20 units, then agreement-check units, a ranking review, and dossiers for the top 10 (one unit each, search-heavy).
2. **State in files (tracked in git):** `usecases/scoring/queue.json` (units in order, status pending, done or failed, config), `usecases/scoring/units/<id>.md` (the exact prompt and output path of each unit), `usecases/scoring/<id>.md` and `<id>.json` (each unit's report and its scores in a fixed JSON shape, written by the subagent), `usecases/scoring/usage-log.tsv` (time, unit, 5-hour and weekly percent before and after, subagent tokens, tool calls, errors).
3. **No-model helpers:** `tools/scoring_queue.py` (next, done, fail, status) and `tools/scoring_aggregate.py` (reads the JSON files, computes utility, readiness, commonality, stakes and the weighted composite from the rubric, flags differences of more than one point between roles, writes the ranked table, the map data and a list of path-to-viability entries). Both free and testable now.
4. **One scheduled task `ir-scoring-runner`.** Each run: (a) read the usage tool; (b) if the 5-hour window is above the start limit, or the weekly limit above its cap, or the local hour is inside a quiet period, write a skip line to the usage log and stop; (c) otherwise take the next pending unit, run it, mark it, log usage; (d) repeat while the 5-hour window stays under the continue limit; (e) stop when the queue is empty or at a pause point (below). Writes only inside `usecases/scoring/`; no git, no edits to deliverables, rubric or role files; page text is data; never asks a question.

## Slots and limits (proposed; numbers are guesses to be calibrated on the pilot)
- Slots every 5 hours: cron `7 2,7,12,17,22 * * *` (local time; the scheduler adds a delay of several minutes). Five slots a day cannot tile 24 hours exactly (the last gap is 4 hours), and the daily update watch at about 01:15 sits just before the 02:07 slot, so the gate, not the spacing, is what prevents overload.
- Start a unit only if the 5-hour window is at most 40% used; keep starting units while it is under 65%; stop everything if the weekly limit is at 75% or more.
- Quiet hours: the user decides (for example, no slot between 08:00 and 18:00 so that the window is free for interactive work). Default if unanswered: none.

## Pause points (the runner stops and waits for the user)
After the pilot (anchors in the rubric may need rewriting, rubric Process step 3); after all candidates are scored and the agreement check (review the ranking and weights before dossiers); before the dossiers (search-heavy). At a pause point the runner writes `PAUSED` to the queue and the session-start brief shows it.

## Estimates (not measurements)
A lean-agent unit cost 27,000 to 75,000 tokens in the tests so far; an all-tools role costs more (the current scoring roles are all-tools roles; lean versions are a later optimisation). The pilot is 6 units, the full scoring about 20 more, the dossiers about 10. At two to four units per window, the pilot takes one to three slots and the full scoring several days. The pilot's logged percent of window per unit replaces these guesses.

## Build order (all free until the first run)
1. Queue file, unit prompts for the pilot (from the workflow's prompts), `scoring_queue.py`, `scoring_aggregate.py`; tests with a fake queue and fake JSON, no model.
2. The scheduled task with the runner prompt; show the prompt to the user before creating it.
3. First run = the pilot, timed for the first slot after the window resets (about 21:55 local today) so that it starts on a fresh window; or started at once with a manual "run now" if the user prefers (it would share today's partly used window).
4. After the pilot: review the logged cost and the anchor issues with the user, then release phase 2.

## Risks
- The gate relies on the usage tool being available in scheduled sessions (untested; the first run reports if it is not, and the runner then falls back to one unit per slot).
- Scheduled runs only happen while the Claude app is open and the computer awake (the watch has the same limit).
- Unit outputs can be wrong in the way earlier agents were wrong; the skeptic units, the agreement check and the main session's spot checks (PMID, DOI and quotes with the helpers) stay in the process.
- Running at night may still use the same window as the daily watch; the percentages in the log will show it.

## Decisions for the user
1. Quiet hours, if any. 2. Slot times (proposed 02:07, 07:07, 12:07, 17:07, 22:07). 3. Limits (40, 65, 75). 4. First run at the next window reset or immediately. 5. Whether to move the scoring work to a fresh chat.
