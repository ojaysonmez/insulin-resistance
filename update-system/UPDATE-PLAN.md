# Update plan: keeping the IR project current (draft, not running)

> Paths: this file lives in `update-system/`. The deliverables (`merged-conclusion.md`, `usecases-verified.md`) are in the project root; reviews are in `reviews/`; reports in `analysis/` and `usecases/`. Other files named here without a folder are in `update-system/`.

Status: DRAFT written 2026-10-19. Nothing here is scheduled or running. It describes how to keep `merged-conclusion.md` and `usecases-verified.md` current as new evidence appears, without re-running the whole system. Coverage and reimbursement are out of scope.

## Principles
1. **Incremental, not full re-runs.** Weekly runs look only for what changed since the last run. Full re-analysis happens only when a trigger in `WATCHLIST.md` fires.
2. **Nothing changes the deliverables automatically.** Weekly and monthly runs write to `PENDING.md`. `merged-conclusion.md` and `usecases-verified.md` change only after triage and a skeptic review, and every change gets a `CHANGELOG.md` entry.
3. **Unattended means no questions.** Scheduled runs never stop to ask. They record assumptions and failures in the run log and continue.
4. **Short searches.** The project's own lesson: long conjunctive strings returned zero hits and broke. Use the short strings in `WATCHLIST.md`, date-limited, and read the full result set when it is under about 60 records (at least the top 25 otherwise), and say so.
5. **Identifiers.** Record both PMID and DOI for every paper (role-file identifier rule).
6. **Do not run the same role in both modes** (README running convention): all update runs are subagents.

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
7. **A scheduling test.** Confirm that a scheduled task can start the subagent unattended: working directory, permissions for reading and writing the project folder, MCP tools available (PubMed, Crossref, registries), and that role files load as agent types. If scheduled sessions cannot spawn subagents, run the weekly watch as a single scheduled session and record that in the README.

## Expected yield and cost
- Most weekly runs should find nothing that changes a claim. The conclusion has been stable across every review round. The value is in catching rare triggers: a retraction, a trial result, a guideline change.
- Per weekly run: about 150,000 to 300,000 tokens. Four to five runs a month plus a triage: roughly 1 to 2 million tokens a month, before any trigger reviews.
- Review these figures after the dry run and after the first month, and cut queries that produce only "no trigger".

## Open decisions for the user
1. Cadence: weekly watch with monthly triage as drafted, or monthly only?
2. Notification: how and when should urgent items reach you (message in the app, or only in `PENDING.md`)?
3. Budget: are the token budgets above acceptable?
4. Scope: should the watch also cover the use-case list (rows 1-47) or only the IR conclusion? As drafted it covers both.
5. Start date: after the prerequisites above, or run the dry run first?
