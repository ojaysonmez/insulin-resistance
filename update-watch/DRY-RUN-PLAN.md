# Dry run of the weekly watch (DRAFT plan, 2026-10-19, not run)

> Paths: this file lives in `update-watch/`. Other files named without a folder are in `update-watch/`; the deliverables are in the project root.

Purpose: run the watch once by hand over a one-week window, to check the prerequisite in `UPDATE-PLAN.md` item 6 before anything is scheduled: queries return usable results; tool failures are logged and do not stop the run; the output is correct and fits the budget; entries are in the `PENDING.md` format. Decisions behind it: D-18 (gate before any edit) and D-28 (parameters). Coverage and reimbursement are out of scope.

## What runs

| Part | Who | Cost |
|---|---|---|
| A. Retraction and correction check on every PMID and DOI in the two deliverables | Main session runs `tools/check_citations.py` (script, no model) | Network only; cache makes it fast |
| B. The 13 PubMed queries in `WATCHLIST.md` section 4, limited to the window | One background `ir-evidence-searcher` subagent | Budget cap 150,000 tokens |
| C. Registry status of the 7 tracked NCT numbers (`WATCHLIST.md` section 2) | The same subagent, ClinicalTrials.gov tool | Inside the same cap |
| Not in this dry run | Section 3 (documents and labels: web-heavy and costly; test separately), the 4 non-NCT registry IDs (CTRI, IRCT, ISRCTN x2), new-trial searches | |

## Window
Entry date 2026-10-11 to 2026-10-19 (an 8-day window with one day of overlap). Use the PubMed entry-date field, so records new to PubMed in the window are found whatever their publication date, for example `("2026/10/11"[EDAT] : "2026/10/19"[EDAT])` added to each query. Log the exact strings used.

## Rules for the subagent (it never asks questions)
- Short strings as written in `WATCHLIST.md`. If a query returns zero hits, rerun a shorter variant and log both strings; word negatives as "not found in the screened records".
- Read the whole result set when it is under about 60 records; otherwise screen at least the top 25 by title and abstract and say so.
- Keep only items that match a trigger in `WATCHLIST.md` section 5. Everything else is logged as "screened, no trigger" with counts.
- Each kept item: PMID and DOI, read level, two sentences on what it says (numbers only if read), "Affects" (a section of `merged-conclusion.md` or a row of `usecases-verified.md`), proposed impact class (none, minor, review, urgent). Use the entry format in `UPDATE-PLAN.md`.
- Registry check: for each of the 7 NCT numbers, record status, whether results are posted, enrolment, and the last-update date, and say what changed only if an earlier value is known (none is recorded yet, so this run sets the baseline).
- Stop and log if the work reaches the 150,000-token cap. Record every tool error and continue.
- Write only `update-watch/dry-run-2026-10-19.md` (a run log plus candidate entries). Do not edit `PENDING.md`, the deliverables or any other file. Do not commit.

## How I would start it
1. Run part A myself (script), read the report, note any new retraction or correction.
2. Start the subagent in the background with the rules above (role file supplies the identifier rule and retrieval method).
3. Set a one-shot timer after its expected finish (see `CONVENTIONS.md`). The agent's completion notice also reports its token use.
4. Read its output file and spot-check three kept items and one "no trigger" screen against PubMed.

## How we judge it (pass if all hold)
- Queries: at most 3 of 13 return zero after the shorter variant; the rest give a reviewable list.
- Failures: every tool error is logged and the run still finishes.
- Cost: within 150,000 tokens; record the real figure and the wall time.
- Format: kept items follow the entry format and carry PMID and DOI.
- Accuracy: the three spot-checked items match their PubMed records; no invented identifiers.
- Yield: note which queries produced only "no trigger", as candidates to cut.

## What the user decides after the run
Move the kept items into `PENDING.md`? Adjust queries or the cap? Then the daily tuning pilot as a saved scheduled task (D-28).

## Risks
- A heavy run could hit the user's usage limit; the 150,000 cap and the single agent limit this.
- Registry and PubMed tools may be refused or rate-limited in a background run; this is part of what the dry run tests.
- The dry run searches the public web and PubMed; it sends no project data, only the query strings in `WATCHLIST.md`.
