# Plan: add use cases that rely on post-meal, post-load or stimulated insulin or C-peptide (DRAFT, 2026-10-19, not run)

> Paths: this file lives in `usecases/`. The deliverable `usecases-verified.md` is in the project root and is changed only by the main session after a skeptic review (CLAUDE.md). Coverage and reimbursement are out of scope.

## Why
The conclusion points to secretion (hypoglycaemia work-up, diabetes classification, graft function), yet the 47 rows have only 10 that rely on a post-meal, post-load or stimulated test, 7 of them C-peptide in diabetes or pancreas settings, only 2 established (rows 10 and 29). The user asked for at least 5 to 10 more, with the postprandial insulin uses best represented. Count of the existing 10: rows 5, 8, 9, 10, 19, 23, 27, 29, 32, 38 (judged from the measurement and decision columns).

## Candidate topics (from memory, to be verified; each becomes a row only if a source supports it)
| Id | Topic | Short PubMed string (run without a date window, relevance order, 20 per topic) |
|---|---|---|
| T1 | Mixed-meal test for suspected reactive (postprandial) hypoglycaemia | `"postprandial hypoglycemia" AND ("mixed meal" OR "mixed-meal") AND insulin` |
| T2 | Late dumping syndrome after gastric surgery | `("late dumping" OR "dumping syndrome") AND (insulin OR "mixed meal")` |
| T3 | Non-insulinoma pancreatogenous hypoglycaemia | `("noninsulinoma pancreatogenous hypoglycemia" OR nesidioblastosis) AND (insulin OR "calcium stimulation")` |
| T4 | OGTT C-peptide to stage type 1 diabetes risk (Index60-type scores) | `"C-peptide" AND "oral glucose tolerance" AND "type 1 diabetes" AND (progression OR "risk score")` |
| T5 | Stimulated C-peptide in LADA to guide treatment | `LADA AND "C-peptide" AND (stimulated OR "mixed meal") AND (treatment OR insulin)` |
| T6 | Glucagon stimulation versus meal test in type 1 diabetes | `"glucagon stimulation" AND "mixed meal" AND "C-peptide"` |
| T7 | Protein or leucine challenge in congenital hyperinsulinism | `hyperinsulinism AND (leucine OR protein) AND (challenge OR provocation) AND insulin` |
| T8 | Predicting diabetes after pancreatic surgery from a pre-operative OGTT or meal test | `pancreatectomy AND ("oral glucose tolerance" OR "mixed meal") AND ("C-peptide" OR insulin) AND (diabetes OR "beta-cell")` |
| T9 | Meal-test beta-cell function to predict diabetes remission after bariatric surgery | `bariatric AND "mixed meal" AND "C-peptide" AND remission` |
| T10 | Insulinogenic index or OGTT insulin to predict progression in prediabetes | `"insulinogenic index" AND (prediabetes OR "diabetes risk")` |
Topics already covered by existing rows (5, 19, 23, 38 and others) are not repeated; a topic that adds only a citation to an existing row is reported as such, not as a new row.

## Steps
1. **Retrieval by script, no model:** a small `tools/usecase_search.py` (same pattern as `tools/watch_fetch.py`) runs the 10 strings and writes `usecases/postprandial-candidates.md` (PMID, DOI, first author, year, journal, title, publication types, grouped by topic; reviews, guidelines and consensus statements listed first). Free and fast.
2. **Verification by a lean agent:** a new role `ir-usecase-scout` with `tools: Read, Write, Bash, WebFetch` reads only the candidates file, fetches abstracts with `python tools/watch_fetch.py --abstracts ...` (at most 12 per call), and may fetch at most 4 guideline or consensus pages. For each topic it writes a draft row in the format of `usecases-verified.md` (patient type, measurement, decision it informs, measure type, status, sources with PMID and DOI and read level, notes). Status rules as in the existing file: nothing is "established" without guideline, consensus or regulatory text it has read; abstract-only rows are marked as such; a topic with no usable source is reported as "no use found in the sources read". At most 20 tool calls. Output: `usecases/postprandial-additions-draft.md`.
3. **Skeptic review** of the draft rows against their sources, then the main session merges accepted rows into `usecases-verified.md` (rows 48 onward), updates the counts and logs the change in `CHANGELOG.md`. The merged rows also join the scoring candidates.

## Pass criteria for the agent step
- At least 5 draft rows with a source for every row; both PMID and DOI recorded.
- No row marked established on abstract-level evidence.
- Measure type named for every row (post-meal, post-load, stimulated, or C-peptide or insulin).
- At most 80,000 tokens (the lean triage agent used 27,576); the figure is read from the completion notice.
- Only the one draft file written; no change to any deliverable.

## Cost and risks
- Steps 1 is free; step 2 is one agent run estimated at 40,000 to 80,000 tokens (an estimate, not a measurement); step 3 is a skeptic run, estimated at 100,000 tokens or more with the current all-tools skeptic.
- The topic list comes from memory and may miss uses or include ones with no source; the scout reports those honestly. Relevance-ordered PubMed results favour reviews, which is intended, but small important studies can be missed; the result is "found in the screened records", not a complete search.
- A new role file is usable only after the app announces the new agent type, as with `ir-watch-triage`.
