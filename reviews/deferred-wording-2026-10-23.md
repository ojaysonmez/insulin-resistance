# Deferred wording items: relabel proposal for rows 17, 35, 45 and the WBISI check (2026-10-23)

Status: PROPOSAL, not applied. `usecases-verified.md` is a deliverable; a substantive change goes in only after a skeptic review (CLAUDE.md). Written by the main session, file-only, no searches except two PubMed reads for item 2.

## 1. Relabel rows 17, 35 and 45 (scope audit U1, U5; skeptic-scope findings)

Problem: the three rows carry "not determinable from the files" qualifiers but are counted in a default status. The scope-audit skeptic asked for a relabel or an explicit note, and for row 35 to be treated like row 45 (same title-level evidence).

Proposed changes (final status column, plus the counts table and the two notes that mention them):

| Row | Now | Proposed |
|---|---|---|
| 17 | Unsupported (with "monitoring not determinable" qualifier) | Prediction and screening with routine fasting HOMA-IR or TyG: Unsupported. Monitoring: Not evaluated (variability argument only; no monitoring study read). Measure types: fasting-based (HOMA-IR) and non-insulin surrogate (TyG). |
| 35 | Research-only (b) | (b) first-trimester HOMA-IR (fasting-based): Not evaluated (cohorts read at title level only). (a) GCK trigger: unchanged, glucose-based, not an insulin or C-peptide use. |
| 45 | Research-only (insulin/HOMA) | Not evaluated (postpartum cohorts read at title level; the ADA 2026 text read only in part). No insulin test found in the guideline text read. |

Effect on the counts table (section 2, Insulin resistance row): research-only 6 becomes 4 (35 and 45 move out); unsupported 8 stays 8 if row 17 keeps its prediction/screening label; a new column or footnote "Not evaluated: 2 or 3 rows (17 monitoring part, 35, 45)". Totals: research-only 11 becomes 9. The notes "Rows 17, 35 and 45 carry ... but are counted in their default status" and the counts in README and `merged-conclusion.md` Bottom line 3 would need the same change, so the edit touches several deliverable sentences.

Not proposed: splitting row 17 into three rows (scope-audit U1). It would renumber the 49-row list that the scoring files, `queue.json` and the ranking use. If the user wants the split, do it as rows 17a to 17c.

Scoring effect: none. Rows 35 and 45 are already scored on the insulin part only, at low confidence, and the rubric treats "not evaluated" as D2 of 0 or 1 (weak evidence flag already shown for row 45).

Next step if the user agrees: run the cheap `ir-row-skeptic` on these three rows plus the counts text, then apply.

## 2. Is WBISI the Matsuda index?

Answer: yes by definition, with one gap.

- Matsuda and DeFronzo 1999 (PMID 10480510, DOI 10.2337/diacare.22.9.1462, abstract read now) name their OGTT-derived measure "an index of whole-body insulin sensitivity" and give the formula 10,000 / square root of [(fasting glucose x fasting insulin) x (mean glucose x mean insulin during the OGTT)]. That formula is what the literature calls the Matsuda index and also WBISI (whole-body insulin sensitivity index).
- Hani 2024 (PMID 39726936, DOI 10.1155/2024/2136173, PMC full text read now): the introduction lists "the Matsuda index, QUICKI and HOMA-IR" as the sensitivity indices; the outcome list names HOMA-IR, WBISI, QUICKI, 1/fasting insulin and FGIR; Matsuda is not named again. The formulas were stripped from the text retrieved, so the paper's own WBISI formula was not seen. It is very likely the same index, but that rests on the naming convention, not on a formula check.
- Where it matters: `merged-conclusion.md` line 54 says "Matsuda-specific variation" is not covered, and line 56 and `reviews/subagent-runs/skeptic-scope.md` cite Hani for WBISI. If WBISI is the Matsuda index, the "not covered" sentence is wrong for children (Hani, 257 children, OGTT-derived WBISI more reproducible than fasting indices; ICC values were in a table not retrieved) and still right for adults.
- Proposed wording change in `merged-conclusion.md` (substantive, skeptic review needed): "Not covered: TyG repeatability (none found) and Matsuda reproducibility in adults. In children WBISI (the Matsuda formula, by naming convention) was more reproducible than fasting indices (PMID 39726936, DOI 10.1155/2024/2136173, full text, 257 children without diabetes, ICC table not read)."
- Read level for the note: Matsuda abstract and Hani full text, both read 2026-10-23.
