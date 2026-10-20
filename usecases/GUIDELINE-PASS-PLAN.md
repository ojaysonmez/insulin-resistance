# Plan: read the guideline and full-text sources behind draft rows D1, D2, D4 and D5 (DRAFT, 2026-10-19, not run)

> Paths: this file lives in `usecases/`. It follows `POSTPRANDIAL-ADDITIONS-PLAN.md` and works on `usecases/postprandial-additions-draft.md`. Coverage and reimbursement are out of scope.

## Why
The scout drafted six rows from abstracts only and fetched no guideline text, so none can be called established. The user asked for the Endocrine Society 2009 hypoglycaemia guideline (for D1, reactive hypoglycaemia) and the ADA Standards 2026 staging text (for D2, type 1 diabetes risk staging) to be read.

## What can and cannot be read (checked 2026-10-19, free lookups)
| Source | For | Open full text? |
|---|---|---|
| Cryer 2009, Endocrine Society hypoglycaemia guideline, PMID 19088155, DOI 10.1210/jc.2008-1410 | D1 | **No.** No PubMed Central copy; a first publisher-page attempt hit the wrong article, and a web search found only summaries. One more attempt on the Endocrine Society site is allowed; if it fails, D1 stays unread at guideline level and the report says so |
| ADA Standards of Care 2026 section 2, PMID 41358893, PMC12690183 | D2 | Yes (already used for row 6) |
| Insel 2015 staging statement of presymptomatic type 1 diabetes, PMID 26404926, PMC5321245 (corrected 2026-10-19: the PMID first written here, 26246049, was wrong and belongs to an unrelated paper) | D2 | Yes |
| Index60 paper, PMID 35998266, PMC9643141; oral minimal model paper, PMID 39992257, PMC12527456 | D2 | Yes |
| Reactive hypoglycaemia studies, PMID 33916952 (PMC8067537), 41829992 (PMC12986748); post-bariatric hypoglycaemia review, PMID 39555226 (PMC11564166) | D1 | Yes |
| Distal pancreatectomy cohorts, PMID 37889837 (PMC10876401), 42146813 (PMC13178281) | D4 | Yes |
| LADA studies, PMID 25572256 (PMC4297398), 41752170 (PMC12940418) | D5 | Yes |
| Hypoglycaemia review, PMID 36464132; relatives study, PMID 42684379 | D1, D2 | No PubMed Central copy; stay at abstract level |

## Steps
1. **A text helper, no model:** `tools/pmc_text.py` fetches the PubMed Central full-text XML for a PMCID and prints plain text, or only the windows around a regular expression (about 300 characters either side, with the section heading). This avoids summarising fetch tools that cannot be quoted verbatim (lessons learned: summarised reads miss things). Tested first on PMC12690183.
2. **A lean agent pass** (the `ir-usecase-scout` role, tools Read, Write, Bash, WebFetch) reads the draft file and, with the helper, the windows around: for D1 "mixed meal", "postprandial", "reactive", "insulin"; for D2 "C-peptide", "OGTT", "Index60", "stage 1", "stage 2"; for D4 "insulinogenic", "predict", "threshold"; for D5 "C-peptide", "cut", "treatment". It writes `usecases/postprandial-fulltext-check.md`: for each of D1, D2, D4, D5 the verbatim passages with section names, whether the text supports, qualifies or contradicts the draft row, and a proposed revised status and wording. One attempt on the Endocrine Society site for Cryer 2009 (at most one fetch). At most 25 tool calls.
3. The main session spot-checks quotes against the helper output, then a skeptic review of the revised rows, then merge into `usecases-verified.md`.

## Rules for the agent step
Quote only text the helper printed; mark anything else [recall]. A status is "established" only if a quoted guideline, consensus or regulatory passage recommends the test for that decision. Negative findings ("the ADA 2026 staging text defines stages by autoantibodies and glucose and does not mention a C-peptide test") must state which passages were searched and with what pattern. Never stop to ask a question.

## Expectations (stated before the run, so they can be checked)
- D2 will most likely stay "limited": staging statements define stages by autoantibodies and glucose, not by C-peptide. A clear negative from the guideline text is itself a useful result.
- D1 will most likely stay "research-only" unless the Cryer 2009 text can be read, which looks unlikely.
- D4 and D5 should be confirmed or corrected from full text; thresholds quoted in the drafts should be checked against the papers.

## Cost
The helper is free. The agent pass is estimated at 50,000 to 80,000 tokens (an estimate; the last scout run used 74,108). A skeptic pass afterwards would be about 100,000 tokens with the current skeptic role.
