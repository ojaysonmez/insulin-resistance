# Update plan: keeping the IR project current (draft, not running)

> Paths: this file lives in `update-watch/`. The deliverables (`merged-conclusion.md`, `usecases-verified.md`) are in the project root; reviews are in `reviews/`; reports in `analysis/` and `usecases/`. Other files named here without a folder are in `update-watch/`.

Status: DRAFT written 2026-10-19. Nothing here is scheduled or running. It describes how to keep `merged-conclusion.md` and `usecases-verified.md` current as new evidence appears, without re-running the whole system. Coverage and reimbursement are out of scope.

## Principles
1. **Incremental, not full re-runs.** Weekly runs look only for what changed since the last run. Full re-analysis happens only when a trigger in `WATCHLIST.md` fires.
2. **Nothing changes the deliverables automatically.** Weekly and monthly runs write to `PENDING.md`. `merged-conclusion.md` and `usecases-verified.md` change only after triage and a skeptic review, and every change gets a `CHANGELOG.md` entry.
3. **Unattended means no questions.** Scheduled runs never stop to ask. They record assumptions and failures in the run log and continue.
4. **Short searches.** The project's own lesson: long conjunctive strings returned zero hits and broke. Use the short strings in `WATCHLIST.md`, date-limited, and read the full result set when it is under about 60 records (at least the top 25 otherwise), and say so.
5. **Identifiers.** Record both PMID and DOI for every paper (role-file identifier rule).
6. **Do not run the same role in both modes** (see `CONVENTIONS.md`): all update runs are subagents.

## Cadence
| Run | When | What | Agent | Output | Budget (tokens) |
|---|---|---|---|---|---|
| Weekly watch | Mondays, early morning local time | Retraction/correction check on every PMID and DOI in the two deliverables; registry status check for tracked trials; document/label version check; the date-limited PubMed queries in `WATCHLIST.md` | One `ir-evidence-searcher` subagent | Appends a dated run log and new items to `PENDING.md` | 300,000 per run; stop and log if exceeded |
| Monthly triage | First Monday of each month | Read the month's `PENDING.md` items, classify impact, escalate | `ir-evidence-searcher` or main session | Triage section in `PENDING.md` | 500,000 |
| Trigger review | Only when an item is classed "review" or "urgent" | Read the item in full text; check the affected claims; skeptic review of any proposed change | `ir-biostatistician` or `ir-specialty-reviewer` for the topic, then `ir-skeptic` | Proposed edit, skeptic review file, CHANGELOG entry | Case by case; ask the user before a trigger review that needs more than 1,000,000 tokens |
| Quarterly sanity check | Every three months | Re-run the baseline checks (all PMIDs, all registry IDs, guideline versions) and review `PENDING.md` backlog | Subagents as above | Summary in `CHANGELOG.md` | 1,000,000 |

Timings are suggestions. They depend on usage limits (one skeptic run already hit a limit) and on whether scheduled tasks can run these agents unattended (see "Before relying on it").

## What a weekly run does, step by step
1. Read `WATCHLIST.md` and the last run date from `PENDING.md`.
2. Run the citation check on all PMIDs and DOIs in `merged-conclusion.md` and `usecases-verified.md` (title match against PubMed, Crossref `updated-by`). Any retraction, correction or expression of concern is class **urgent**.
3. Check each tracked registry ID for a status change, posted results or changed enrolment. Result posted = class **review**.
4. Check each tracked document or label for a new version or erratum (ADA Standards living updates, AACE, EASL, AASLD, the teplizumab label, PCOS guideline, Endocrine Society, ISPAD, KDIGO, ESC, AHA). New text touching IR measurement = class **review**.
5. Run the watchlist PubMed queries limited to the last 8 days (one-day overlap). Screen titles and abstracts; keep only items that match a trigger. Everything else is logged as "screened, no trigger" with counts.
6. For each kept item, write a `PENDING.md` entry (format below). Do not edit any deliverable.
7. Append a run log: queries run with counts, what failed (tool errors, blocked pages), tokens used, items kept.

## PENDING.md entry format
```
### P-YYYYMMDD-NN
- Found: date, run (weekly / monthly / manual)
- Source: title; PMID and DOI (https://doi.org/..., PubMed link if no DOI); or registry ID with link; or document URL, issuing body, date
- Type: paper / trial result / registry change / guideline or label update / retraction / correction
- Read level: full text / abstract / title only
- What it says: two sentences, numbers only if read
- Affects: claim or section in merged-conclusion.md or row in usecases-verified.md (until a claim ledger exists, name the section; with a ledger, the claim ID)
- Proposed impact: none / minor (add a citation or caveat) / review (may change a claim or status) / urgent (retraction or contradicts a stated fact)
- Status: new / triaged / in review / applied / rejected, with date and reviewer
- Notes: why, and the CHANGELOG entry if applied
```

## Impact classes and what happens
| Class | Meaning | Action |
|---|---|---|
| none | Screened, no effect | Logged; no further action |
| minor | Adds a citation or caveat to an existing claim | Batched into the monthly triage; applied with a skeptic spot-check |
| review | May change a claim, confidence figure or use-case status | Trigger review: full-text read, specialty or biostatistician check, then skeptic review before any edit |
| urgent | Retraction or correction of a cited paper, or a fact in the deliverables shown to be wrong | Same week: flag to the user, check which statements depend on it, propose the correction |

## Gate before any edit to a deliverable
- The proposed change is written as a diff-style note in `PENDING.md`.
- A skeptic subagent reviews it against primary sources.
- The main session applies it and adds a `CHANGELOG.md` entry with the PENDING ID.
- The confidence figures in `merged-conclusion.md` change only through a trigger review, never in a weekly run.

## Before relying on it (prerequisites)
1. **Skeptic pass on the round 2 corrections** now in `merged-conclusion.md` (they have not been reviewed), so the baseline is stable.
2. **Claim ledger**, so "affects" can name a claim ID and the watch can compare a new paper with specific claims. Without it, entries name sections and the comparison is weaker.
3. **Citation-check script**, so the weekly retraction and identity check is cheap and consistent (Scholar Sidekick has failed on every skeptic run).
4. **Full-text reader helper**, so a trigger review reads documents end to end.
5. **Version history** for the project folder (git repo) so changes can be diffed and undone.
6. **A dry run.** One manual weekly-watch subagent over a one-week window, to check: the queries return usable results, tool failures are logged and do not stop the run, the output is correct and fits the budget, and the PENDING entries are in the right format.
7. **A scheduling test.** *Done 2026-10-19:* two one-time tasks ran unattended in Auto mode; the second made a PubMed search and started a subagent (see `CHANGELOG.md`); not shown: a heavy screening run. Results were checked with a session timer (see `CONVENTIONS.md`, "Checking a scheduled or background run"). Original wording: Confirm that a scheduled task can start the subagent unattended: working directory, permissions for reading and writing the project folder, MCP tools available (PubMed, Crossref, registries), and that role files load as agent types. If scheduled sessions cannot spawn subagents, run the weekly watch as a single scheduled session and record that in the README.

## Expected yield and cost
- Most weekly runs should find nothing that changes a claim. The conclusion has been stable across every review round. The value is in catching rare triggers: a retraction, a trial result, a guideline change.
- Per weekly run: about 150,000 to 300,000 tokens. Four to five runs a month plus a triage: roughly 1 to 2 million tokens a month, before any trigger reviews.
- Review these figures after the dry run and after the first month, and cut queries that produce only "no trigger".

## Design after the dry run (2026-10-19, decision D-29)
The dry run (`dry-run-2026-10-19.md`) let one agent search and read everything and used 231,550 tokens against a 150,000 cap, partly because single tool results were about 80,000 characters long. The watch is therefore split:
- **Retrieval by script, no model:** `tools/watch_fetch.py` runs the queries in `queries.json` over the entry-date window (2 days in the daily pilot, 8 in a weekly run), drops PMIDs already listed in `seen-pmids.txt`, fetches compact records (title, first author, journal, date, DOI), checks the tracked NCT numbers against `registry-baseline.json` (status, results flag, enrolment, last update, and the stale-record rule), and writes `runs/<date>-candidates.md`. `tools/check_citations.py --refresh` does the retraction and correction check. Tested on the dry run window: 12.7 seconds, 51 new records, the same hit counts and the same registry values as the agent found.
- **Judgement by a model, small input:** an `ir-evidence-searcher` subagent reads only the candidates file, applies the log-only rule (`WATCHLIST.md` section 6), fetches abstracts for at most about 10 records, and writes entries for `PENDING.md`. The budget is bounded by construction (a short list and a cap on abstracts), and the real token count is read from the completion notice and logged in each run.
- **Limits for any tool step by an agent:** at most about 4 PubMed searches in parallel (rate limit) and about 10 records per metadata call (output limit); if a query returns more than about 60 hits, rewrite the string.
- The "Affects" field is filled from the deliverable headings and row titles that the script prints at the end of the candidates file.

## Decisions (settled 2026-10-19, user accepted the defaults; recorded as D-28 in `DECISIONS.md`)
1. ~~Cadence~~ **Changed by the user the same day: the watch runs once a day during a tuning pilot (about two weeks; two-day PubMed window; log tokens per run), then weekly. Triage (the first-pass judgement and impact classing by the lean agent) runs daily during the pilot as well, at the user's request; see `DAILY-PILOT-PLAN.md`.** Urgent items are flagged the day they are found.
2. ~~Notification~~ **`PENDING.md` only.** The session-start brief prints the pending count, so the user sees it at the start of any chat. No push messages.
3. ~~Budget~~ **Caps as drafted, but the first weekly runs start with the PubMed screening at about 150,000 tokens**; the retraction check and registry check are scripts (no model cost) where possible.
4. ~~Scope~~ **Both** the IR conclusion and the use-case list (rows 1-47).
5. ~~Start date~~ **Dry run first**, after a scheduling test. Order: scheduling test, dry run, then schedule the weekly run.

## Pilot monitoring (added 2026-10-19)
During the daily tuning pilot, each run appends to its run log: the queries run with counts, tokens used, items kept and failures. The user sees the state through the pending count in the session-start brief. To check a run right after a change to the watch, use the timer pattern in `CONVENTIONS.md`; the timer is a developer aid and is not part of the schedule.
