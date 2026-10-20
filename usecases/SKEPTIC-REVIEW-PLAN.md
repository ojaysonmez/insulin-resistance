# Plan: skeptic review of the revised post-meal and stimulated test rows D1-D6 (DRAFT, 2026-10-19, not run)

> Paths: this file lives in `usecases/`. Follows `POSTPRANDIAL-ADDITIONS-PLAN.md` and `GUIDELINE-PASS-PLAN.md`. `usecases-verified.md` changes only after this review (CLAUDE.md). Coverage and reimbursement are out of scope.

## Step 0: the main session writes the revised rows (before the skeptic runs)
`usecases/postprandial-additions-revised.md` = the scout's six rows with the corrections from the full-text check applied, each change marked:
- **D1** (reactive hypoglycaemia, meal or OGTT test): stays research-only. Add: the 55 mg/dL cut-off is the study authors' own; no insulin threshold in the full texts; Cryer 2009 not readable (unread, not "absent"). The counts 69 and 19 are marked unverified.
- **D2** (OGTT C-peptide, type 1 risk staging): stays limited. Replace "the oral minimal model separated stage 2 from stage 1" with "only phi-total, not AUC C-peptide, was associated with progression". Add the 2015 staging statement (PMID 26404926, PMC5321245) as a descriptive consensus source, and ADA Standards 2026 recs 2.6 and 2.7 as covering autoantibodies only.
- **D4** (OGTT around distal pancreatectomy): the preoperative predictors found are glucose-based (impaired glucose tolerance, glucose AUC); the insulin element is a fall in the insulinogenic index at 1 month. Re-status as research-only for insulin or C-peptide specifically, with a note that it is mainly a glucose-testing use; the skeptic decides whether it belongs in the list at all.
- **D5** (stimulated C-peptide in LADA): research-only for treatment choice; unverified figures removed; "no C-peptide cut-off for treatment selection found in the sources read".
- **D3** (OGTT insulin indices in prediabetes) and **D6** (protein tolerance test in congenital hyperinsulinism): unchanged, flagged abstract-only and not full-text checked.

## Step 1: a lean skeptic role
New role `ir-row-skeptic` with `tools: Read, Write, Bash, WebFetch` (the current `ir-skeptic` role file is short; its cost comes from carrying all tools, as the earlier tests showed). It keeps the skeptic stance: challenge, do not soften, do not raise objections it cannot support. It verifies with the project's no-model helpers instead of memory: `python tools/pmc_text.py PMCID --grep ...` for verbatim passages, `python tools/watch_fetch.py --abstracts PMIDs` for abstracts, `python tools/check_citations.py <file> --refresh` for identifiers and retractions.

## Step 2: the review
The skeptic reads the revised file and the existing rows named there, and checks each row independently (it may read the scout's check file but must re-verify any quote it relies on with the helper). For every row:
1. Does each number and quote match its source? (quote, source, section)
2. Is the status justified by the rule (established only with a quoted recommendation; abstract-only evidence cannot exceed limited)?
3. Does the row rely on a post-meal, post-load or stimulated insulin or C-peptide test, and is the measure type named correctly?
4. Does it duplicate or merely add a citation to an existing row (5, 6, 8, 9, 10, 18, 19, 23, 27, 29, 31, 32, 38)?
5. Identifiers: PMID and DOI both present and matching PubMed; any retraction or correction (the earlier scout run flagged PMID 24408401 as retracted; it must not be used).
Output `usecases/postprandial-skeptic-review.md`: per row a verdict (accept, accept with edits, reject) with the evidence, the required edits, and a list of claims that could not be traced. At most 30 tool calls; never stops to ask.

## Step 3: merge
The main session applies the edits and adds accepted rows to `usecases-verified.md` as rows 48 onward, updates the counts, the summary and the README row count, logs it in `CHANGELOG.md`, and adds the rows to the scoring candidates (`usecases/scoring-rubric.md`). `summary.md` is updated by re-running the summary editor later, not by hand.

## Pass criteria
- Every row has a verdict with checked evidence; at least 10 quotes or figures re-verified by the helper.
- The review finds or clears the points raised by the full-text pass (D2 minimal-model claim, D4 predictors, unverified D5 figures).
- At most 80,000 tokens (the last lean runs used 27,576 to 74,108; read from the completion notice).
- Only the one review file written.

## Cost and risks
Step 0 is main-session work, no new search. Step 2 is one lean agent run, estimated at 50,000 to 80,000 tokens (an estimate). Risk: the skeptic role is new and untested; the first run is itself a test. A skeptic that relies on the same helper output as the scout shares its blind spots (it cannot read paywalled guidelines such as Cryer 2009), so "not readable" stays a limit of the whole addition, not only of one reviewer.
