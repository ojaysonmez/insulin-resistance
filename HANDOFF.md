# Handoff

Updated: 2026-10-27 (full-text waves, corpus extension, discovery pass and rows 51 to 54 added; stale cloud-watch and corpus bullets replaced)

The current state and the next step, written by hand at the end of a working session. It is overwritten each time (history lives in `CHANGELOG.md` and git). `tools/session_start_context.py` prints this note's main sections at the start of each session. Update it at the end of every working session. Local and cloud sessions cannot see each other's chats (D-36), so anything a later session needs goes here, in `DECISIONS.md`, `CHANGELOG.md` or `memory/`.

## Where we are
- **Goal (D-30):** find and score the most viable uses of insulin, C-peptide and insulin-resistance measurement, and what would make the weaker ones viable. Clinical utility (`merged-conclusion.md`) is the constraint.
- **Scoring is finished for rows 1 to 50 (D-32 to D-43):** `usecases/scoring/ranking.md` ranks 32 rows in tiers A to D; tier A is rows 6, 1 and 31 (rows 6 and 31 are one pathway), then row 10, 47, 24 and 32 in tier B; row 7 is conditional. Read the tier, not the rank. Wave 1 of the full-text review changed nine one-point scores (original scores kept with notes); no tier changed. Stage 3 dossiers are in `usecases/scoring/dossiers/`.
- **Documents:** `usecases-verified.md` now has 54 rows. Rows 51 to 54 (prediabetes lifestyle intensity by OGTT insulin indices, insulin sensitiser in mood disorders, INS-30 diet choice as a negative entry, baseline insulin in early breast cancer) were added on 2026-10-27 from the discovery scans, tier D first pass, **not scored and not in the ranking**. The claim ledger (`claims/claims.csv`, UC-51 to UC-54 added) checks at 0 errors and 0 warnings. Edits go ledger first.
- **Corpus (D-34):** 334 articles in `corpus/corpus.csv`; 309 have a local text in the git-ignored `corpus/fulltext/` (108 PDFs plus texts), 25 are marked inaccessible and are to be requested through a colleague (`corpus/oa-check.csv`, `corpus/download-list.md`, section D). Reading columns are filled for the papers reviewed so far.
- **Full-text review so far:** units FT1 to FT17 cover 124 papers (`usecases/scoring/ft-review/`, impact in `impact.md`). Full texts rarely change scores (about 3% of cells, one point each) but improve wording accuracy; the 50 claim-only papers support `merged-conclusion.md`, not any row.
- **Discovery pass done (2026-10-27):** scans D1 to D3 plus a skeptic (`ft-review/D1.md` to `D3.md`, `skeptic-D1-3.md`) found no candidate above tier D; merges and refinements were applied to ten rows. Two optional `merged-conclusion.md` edits (skeptic A9), the SOS note and the infant PEG wording are still not applied.
- **Running in both places (D-36):** Claude Code locally and Claude cloud sessions on `main`; hooks and permissions in `.claude/settings.json`; send "status" as the first message. The session-ID feature was removed. The cloud scheduler was removed by the user; work is done locally.
- **Daily update watch (D-48):** the local task `ir-update-watch-daily` runs at 01:15, commits and pushes only the allow-listed files (`tools/watch_commit.py`), applies one-point rescores (`tools/apply_rescore.py`, log in `usecases/scoring/rescore-log.tsv`) and flags `update-watch/URGENT.md`.

## Next step
Run these from a fresh chat (this one is long and expensive), after the 5-hour usage window allows it. Each batch costs about 60,000 to 110,000 tokens; ask the user before starting.
1. **Wave 1b (10 papers):** C190 C194 C196 C197 C235 C259 C268 C276 C282 C325, the texts now available behind rows 1, 2, 6, 7, 10, 24, 31, 32 and 47. Reader agents (ir-usecase-scout, local texts only), then a skeptic (ir-row-skeptic); proposals only (FT*.json), applied by the main session.
2. **Wave 2a (about 57 papers):** papers with a local text, not yet reviewed, that are tied to a use-case row. Includes the 66 PDFs saved on 2026-10-25 to 26. About 7 batches. Build the batch list with the check used on 2026-10-27: texts in `corpus/fulltext/` minus the IDs found in `usecases/scoring/ft-review/FT*.json`.
3. **Wave 2b (about 128 papers):** the remaining papers with a text (mostly support the conclusion, not a row). Do last, or skip those with title-only digests.
4. **Score rows 51 to 54** on the rubric (search-heavy; ask first), then add them to the ranking.
5. Optional: short extractions may be partial (C022 C036 C043 C137 C192 C196 C200 C207 C235 C276 under 3,000 words); check before relying on them. Unread items from the skeptic: C318, C333, C166, C207, C220, C164, C309.
6. Open from earlier handoffs: search-string logs for 5 ledger absence rows; an ID-consistency script; retrieval of the ISPAD monogenic chapter (PMID 36537518); Gavigan numbers in `usecases/scoring/dossiers/row-31.md`; PRINCESS (NCT05760339) stale and four non-NCT registry IDs to check by hand; the summary editor pass on `summary.md`; row 7 D4 versus row 33 D4 inconsistency (clarification 25); row 24 status "Established" (only Rec 1.1 names a test).
7. Decide whether to start harmonisation or accuracy-study planning for pathway 1 (rows 6 and 31).
8. Author contacts (D-35): `corpus/local/contacts.xlsx` (git-ignored, personal, never commit; local machine only) for the investor letters of intent; open: the investor's three questions and deduplication against the Drive files (read-only, needs the user's go-ahead). The assistant sends no email.

## Waiting on the user
- **Scoring runner (D-48):** the task `ir-scoring-runner-2` is disabled with its old prompt. The user will enable it and paste the prompt from `usecases/scoring/RUNNER-PROMPT.md` (steps 6b `python tools/apply_rescore.py --pending` and 6c `python tools/watch_commit.py --message ... --push`). The R2 rescore proposal (row 11) is pending.
- Review the first automatic watch commit and push and the first rescore-log entries.
- Request the 25 inaccessible articles through the colleague (`corpus/download-list.md`, section D).
- Permission for search-heavy agent runs (the user is watching a usage limit).

## Watch out for
- Do not launch search-heavy agents without asking. Commit and push only when the user asks, and show the diff first (`memory/feedback_review_before_commit.md`).
- Create files where they belong, not as drafts in another folder. Use project-root-relative paths.
- Make a tool or schedule work and show it before asking to commit (`memory/feedback_verify_before_commit.md`).
- Read `DECISIONS.md` before changing a settled decision. Confidence figures (about 40%, about 30%, 80-85%, 45-50%) are judgements and stay unchanged.
- Constraints from the user: coverage and reimbursement are out of scope; the repository is public (no personal data, no PDFs or full texts, a colleague is referred to only as "a colleague"); hard stop for agents at 95% of the 5-hour usage window; deliverables (`merged-conclusion.md`, `usecases-verified.md`, `claims/claims.csv`) change only in the main session after a skeptic check. JSON score files have mixed formatting, so edit them line by line and keep the format.
- In the Bash tool, heredocs and backslash escapes can corrupt Python; write scripts with the Write tool.
