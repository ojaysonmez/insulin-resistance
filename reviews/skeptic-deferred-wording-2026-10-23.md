# Skeptic review: deferred wording proposals (2026-10-23)

Target: `reviews/deferred-wording-2026-10-23.md` (item 1: relabel rows 17, 35, 45; item 2: WBISI/Matsuda wording).
Checked against: `usecases-verified.md` (rows 17, 35, 45, 36, 42-44, section 2 and notes, section 6), `reviews/subagent-runs/skeptic-scope.md`, `merged-conclusion.md` lines 50-60, `README.md`, `summary.md`, `summary-detailed.md`.
Method: file-only. PubMed fetch used only for PMIDs 10480510 and 39726936 (abstracts, and the PMC full text of 39726936 via PMC11671114). No other searches. No deliverable edited. No retraction signal on either PMID in the records returned (not a dedicated retraction check).
Identifier check: PMID 10480510 = DOI 10.2337/diacare.22.9.1462 (Matsuda and DeFronzo, Diabetes Care 1999); PMID 39726936 = DOI 10.1155/2024/2136173 (Hani et al., Pediatric Diabetes 2024). Both match the files.

## Verdicts

| Item | Verdict |
|---|---|
| 1a. Relabel row 35 (b) as Not evaluated | Apply with changes |
| 1b. Relabel row 45 as Not evaluated | Apply with changes |
| 1c. Row 17 split label (prediction/screening Unsupported; monitoring Not evaluated) | Apply with changes (keep counted as Unsupported; fix the "2 or 3" ambiguity) |
| 1d. Count changes (research-only 11 to 9, unsupported unchanged) | Arithmetic correct for a 2-row move; incomplete as written (see list of sentences) |
| 2. WBISI/Matsuda wording | Apply with changes (two overstatements, one wrong line number, adult data omitted) |

## Question 1

### 1.1 Is "Not evaluated" justified by the read level?

Row 35 (b), first-trimester HOMA-IR (fasting-based): justified. The only evidence on the insulin question is four cohorts read at title level (PMIDs 26754418, 34449903, 36675721, 38017369). ADA, ACOG and IADPSG texts were not retrieved. "Research-only" asserts something the files do not show. Row 35 (a), the GCK trigger, is glucose-based, is not counted in the 11 established, and stays as is.

Row 45, prior GDM: justified, with a caveat. The ADA 2026 s3 text was read for 100k of 159k characters and the guideline text read names no insulin test. The three postpartum cohorts (32184821, 21926287, 19937225) are title only. So what the files support is "no insulin test found in guideline text read" (that is the row 42-44 meaning of Unsupported) plus "research cohorts exist" (title only). They do not support a determinate Research-only.

Row 17: the proposal is acceptable only if the row stays counted once. The monitoring part rests on a variability argument (EuBIVAS 26.7% within-person CV; derived RCV), not on a monitoring study. That is correctly "not evaluated" for monitoring. Prediction/screening "Unsupported" rests on guideline consistency (EASL, PCOS 2023, ES 2017, IRIS, ADA 2026 s3, AACE 2022) and on "underlying prediction-model papers not re-verified". It is the weakest "Unsupported" in the table, and the proposal does not say so. Say it in the row.

### 1.2 Problem: the relabel is applied selectively (severity: moderate-high)

The test the proposal uses is "the evidence read level does not allow a determinate status". Rows that fail it equally or worse, and stay in "Unsupported" or "Research-only":
- Row 43 (antipsychotic monitoring): "original blocked, secondary summaries only; not read at source". Counted Unsupported.
- Row 44 (HIV metabolic): "secondary web snippet only; not read at source". Counted Unsupported.
- Row 36 (children with obesity and prediabetes/T2D): "Unsupported by extension from Rec 1.7 (no source read addresses insulin testing for dysglycaemia in these children)". By its own wording nothing was read on the question.
- Row 42 (metabolic syndrome): abstract of a definition paper; the WHO 1999 IR criterion is [recall].

Rows 42-44 are labelled "no insulin or C-peptide use found in the sources read", which is the same finding as row 45 ("no insulin test found"). Under that convention row 45 is Unsupported, not Not evaluated. Relabelling 35 and 45 but not 36, 43, 44 gives two standards for the same kind of evidence. The scope-audit skeptic's original point (skeptic-scope P6) was inconsistent treatment of identical evidence; this proposal fixes one inconsistency and leaves another.

Fix (choose one, state the choice in `DECISIONS.md`):
- Option A (minimal, recommended for this edit): relabel 35 and 45 only, define "Not evaluated" in the vocabulary line as "the only sources bearing on the insulin or HOMA-IR question were read at title level or not retrieved", and add one note that rows 36, 43 and 44 are counted Unsupported on the weaker "no use found in sources read" meaning and have not been re-labelled. Do not leave this silent.
- Option B (consistent): also relabel 36, 43 and 44 as Not evaluated. Counts then become IR row: 0 / 3 / 4 / 5 unsupported / 5 not evaluated; total Unsupported 8 (5 excluding the 3 negative entries), Not evaluated 5. This contradicts the "unsupported unchanged" line, so it needs the user's decision.

### 1.3 Arithmetic

Current: IR kind 17 rows = 0 established, 3 limited, 6 research-only (35, 37, 38, 39, 41, 45), 8 unsupported (15, 16, 17, 36, 40, 42, 43, 44). Totals 49 = 11 / 16 / 11 / 11.

Proposal, 2-row version (35 and 45 out; 17 stays Unsupported):
- IR kind: 0 / 3 / 4 / 8, plus Not evaluated 2 = 17. Correct.
- Total: 11 + 16 + 9 + 11 + 2 = 49. Correct. Research-only 11 to 9 is correct. Unsupported unchanged at 11 (8 excluding the 3 negative entries) is correct.

Defect: the proposal says "Not evaluated: 2 or 3 rows (17 monitoring part, 35, 45)". That is not a count. If row 17 is counted in the column, it must leave Unsupported (11 to 10; 8 to 7 excluding negatives) and the Prediction/screening part would have no home. If it stays Unsupported, the column holds 2 rows. Use 2 and describe row 17 in a footnote as "partly not evaluated (monitoring), counted as Unsupported". Do not write "2 or 3".

Draft-row line (usecases-verified.md line 87, "19 rows end as 7 established, 6 limited, 3 research-only, 3 unsupported"): unaffected, because 35 and 45 are not draft rows and 17 stays Unsupported. Counts before the skeptic review (line 83, 45 rows: 13 / 11 / 10 / 11): historical, do not touch.

### 1.4 Every sentence that quotes these counts or the status vocabulary

Quoting the 11 research-only count (must change 11 to 9 and add the Not evaluated figure):
1. `README.md` line 16: "lists 49 uses by patient type: 11 established, 16 limited, 11 research-only, 11 unsupported ..."
2. `merged-conclusion.md` line 13 (Bottom line 3): "The use-case review lists 49 uses in total: 11 established, 16 limited, 11 research-only and 11 unsupported ..."
3. `summary-detailed.md` line 34: "The use-case list has 49 rows: 11 established, 16 limited, 11 research-only, 11 unsupported (counts updated 2026-10-19 ...)". The task list omitted this file; it quotes the counts and must change too.
4. `usecases-verified.md` section 2 table: Insulin resistance row (research-only 6 to 4 and the row list), Total row (11 to 9), and a new Not evaluated column or footnote. Header row of the table also changes if a column is added.

Quoting the status vocabulary or the "every IR row" claim (must change even though no number changes):
5. `usecases-verified.md` line 10: "mapped by me to four values (established, limited, research-only, unsupported)". Becomes five, or four plus "Not evaluated (flag, not a status)".
6. `usecases-verified.md` line 86: "Rows 17, 35 and 45 carry 'not determinable from the files' qualifiers but are counted in their default status". Becomes stale; rewrite.
7. `usecases-verified.md` line 85: "row 17 is partly so (monitoring not determinable from the files)". Still true for 17; add that rows 35 and 45 are no longer in the unsupported/research-only cells.
8. `usecases-verified.md` line 180 (section 6 closing): "every IR-kind row is limited, research-only or unsupported". After the change this is false for rows 35 and 45. Add "or not evaluated".
9. `usecases-verified.md` rows 17, 35, 45 (Final status and caveats columns), plus the row 35 and 45 caveat text "not determinable from the files".

Status words that mirror the labels (not counts, but become inconsistent):
10. `summary.md` line 69 (row 35, "Research-only for") and line 71 (row 45, "Research-only") in the scorecard table. `summary.md` line 27 mentions rows 48 and 49 only; no change.
11. `claims/claims.csv` and `queue.json`: not searched here (no count hit in `claims/claims.csv`; the grep found none). Check them when applying, since statuses may be copied there.

Not counts, no change needed: `summary.md` line 7 ("11 uses with established support") is unaffected.

`CHANGELOG.md`: log the change (rule). `DECISIONS.md`: record the Option A or B choice. `HANDOFF.md`: update at session end.

### 1.5 Scoring claim

The proposal says "Scoring effect: none ... the rubric treats 'not evaluated' as D2 of 0 or 1". I did not re-read the rubric (outside the files assigned). Treat as unverified. `summary.md` lines 69 and 71 carry the "Research-only" status next to the scores, so a status/score display mismatch is possible until those cells are updated.

### 1.6 Exact replacement text

`usecases-verified.md` line 10, replace "mapped by me to four values (established, limited, research-only, unsupported) from the reviewers' own wording." with:
"mapped by me to four values (established, limited, research-only, unsupported) from the reviewers' own wording, plus a flag, Not evaluated, for rows where the only sources bearing on the insulin or HOMA-IR question were read at title level or not retrieved. Not evaluated is not a finding of no utility."

Row 17, Final status: "Prediction and screening with routine fasting HOMA-IR or TyG: Unsupported (guideline consistency only; the underlying prediction-model papers were not re-verified). Monitoring: Not evaluated (variability argument only; no monitoring study read). Counted once, as Unsupported. Measure types: fasting-based (HOMA-IR) and non-insulin surrogate (TyG)."

Row 35, Final status: "(b) First-trimester HOMA-IR (fasting-based): Not evaluated (four cohorts read at title level only; ADA, ACOG and IADPSG texts not retrieved). (a) GCK trigger: established but glucose-based, not an insulin or C-peptide use, and not counted among the 11 established."

Row 45, Final status: "Not evaluated for insulin or HOMA-IR (fasting-based and OGTT-based measures not separated in the sources): no insulin test found in the 100k of 159k characters of ADA 2026 s3 read; three postpartum cohorts read at title level only."

Section 2 table, Insulin resistance row: `| Insulin resistance | 17 (12-17, 35-45) | 0 | 3 (12, 13, 14) | 4 (37, 38, 39, 41) | 8 (15, 16, 17, 36, 40, 42, 43, 44) | 2 (35, 45) |` and a sixth column "Not evaluated" with 0 in the other rows. Total row: `| Total | 49 | 11 | 16 | 9 | 11 (8 excluding the 3 negative entries) | 2 |`.

Line 86 replacement: "Rows 35 and 45 are flagged Not evaluated and are counted in neither research-only nor unsupported. Row 17 is counted once, as Unsupported (prediction and screening); its monitoring part is Not evaluated. Rows 36, 43 and 44 are counted Unsupported on the weaker 'no use found in the sources read' meaning (36 by extension, 43 and 44 from secondary summaries or a snippet) and have not been re-labelled."
(If Option B is chosen, replace the last sentence with the relabel and use the Option B counts.)

Line 180: replace "every IR-kind row is limited, research-only or unsupported" with "every IR-kind row is limited, research-only, unsupported or not evaluated".

README line 16 and `merged-conclusion.md` line 13 and `summary-detailed.md` line 34: replace "11 research-only, 11 unsupported" with "9 research-only, 11 unsupported and 2 not evaluated" and keep the existing parenthesis; the total of 49 then adds up (11 + 16 + 9 + 11 + 2).

`summary.md` lines 69 and 71: change the status cell to "Not evaluated".

## Question 2

### 2.1 Is WBISI the Matsuda index?

By formula and convention, yes. Matsuda and DeFronzo (PMID 10480510, abstract read now) give "an index of whole-body insulin sensitivity (10,000/square root of [fasting glucose x fasting insulin] x [mean glucose x mean insulin during OGTT])", r = 0.73 against the euglycemic clamp, n = 153 adults aged 18-71 (62 NGT, 31 IGT, 60 T2D). The abstract does not use the names "Matsuda index" or "WBISI". The naming is the literature's, not the paper's.

Hani 2024 (PMID 39726936, PMC full text read now): the introduction lists "the Matsuda index, QUICKI, and HOMA-IR" as insulin sensitivity indices; the outcome list and results use WBISI, and the formulas were stripped from the retrieved text. So the identity of Hani's WBISI with the Matsuda formula is by naming convention, not seen in the paper's own formulas. The proposal says this correctly. Hani's OGTT sampled at 0, 30, 60, 90 and 120 minutes, which fits a mean-glucose, mean-insulin formula; this supports but does not prove the identity.

### 2.2 Problems with the proposed wording

P1 (moderate). "WBISI was more reproducible than fasting indices" overstates the full text. Comparison was of Spearman correlations. WBISI beat HOMA-IR, QUICKI, FGIR and 1/fasting insulin in the overall and overweight/obese groups. In the normal-weight group (n = 71) WBISI beat HOMA-IR and QUICKI but not FGIR or 1/fasting insulin. Bonferroni threshold P < 0.001 over 50 comparisons. The authors called the finding "surprising" and "we are unsure of why this is the case". Say "more reproducible than HOMA-IR and QUICKI (and than FGIR and 1/fasting insulin except in normal-weight children)".

P2 (moderate). "Children" is too narrow and ignores the setting: 257 children and adolescents aged 8-17 without known diabetes (8% had dysglycaemia on OGTT), most pubertal, one research unit, two OGTTs a median of 14 days apart, one RIA insulin assay (Linco), 1.75 g/kg glucose up to 75 g. ICC values were in a table not retrieved (the abstract and text give the Spearman comparison). Hani's authors themselves state the result may be paediatric-specific.

P3 (moderate-high). "Still right for adults" omits adult data that point the other way. Hani's discussion reports Hudak et al. (89 adults without diabetes, two OGTTs; this is PMID 34679116 in the files, which the files cite only for OGIS CV 6.5%) finding that fasting-based indices had smaller coefficients of variation than OGTT-derived indices, and that QUICKI variants were most reproducible. So in adults the one study Hani cites found the opposite direction to the children's result. I did not read Hudak and do not know whether it included the Matsuda index; check before writing "not covered in adults". The sentence "Matsuda reproducibility in adults" as "not covered" is true only as "not found in the files"; the files already hold an adult comparison of OGTT-derived and fasting indices. Add it.

P4 (low-moderate). Wrong line reference. The proposal says `merged-conclusion.md` line 54 says "Matsuda-specific variation" is not covered. Line 54 is the LC-MS/MS 22.2% inter-laboratory CV sentence. The phrase is in line 56, which also already cites WBISI in children (39726936) in the same bullet. The proposed sentence would duplicate that clause, so edit line 56 once instead of appending.

P5 (low-moderate). Downstream: line 57 says "reproducibility has been measured and is mixed (OGIS and WBISI good ...)". "Good" is not supported for WBISI: the files and Hani give comparative reproducibility (better than HOMA-IR and QUICKI), and the ICC values were not read. Change "good" to "better than fasting indices in children" for WBISI, and note the adult direction (P3).

P6 (low). Scope. Hani's test is OGTT-derived (post-load), not mixed-meal, and not fasting-based. The proposal's scoping (fasting vs post-load) is right, but the replacement text never names the measure type, which the project rule (CLAUDE.md, Scope) requires.

### 2.3 Exact replacement

In `merged-conclusion.md` line 56, replace
"Not covered: TyG repeatability (none found), Matsuda-specific variation, current-platform proinsulin cross-reactivity, variation in obesity, PCOS or children."
with
"Not covered: TyG repeatability (none found), current-platform proinsulin cross-reactivity, and variation in PCOS. Post-load indices (OGTT-derived, not fasting-based): WBISI, which has the Matsuda index formula by naming convention (the paper's own formula was not seen), was more reproducible than HOMA-IR and QUICKI in 257 children and adolescents aged 8-17 without known diabetes (PMID 39726936, DOI 10.1155/2024/2136173, full text; Spearman comparison, ICC table not read; not better than FGIR or 1/fasting insulin in the 71 normal-weight participants). In 89 adults, as reported by that paper's authors, fasting indices had smaller coefficients of variation than OGTT-derived indices (Hudak, PMID 34679116, not read for this point). Matsuda reproducibility in adults was not found in the files."
(The deleted words "variation in obesity ... or children" are now partly covered by Hani, which included overweight/obese and normal-weight youth; keep "obesity in adults" as not covered if the team prefers: "variation in adults with obesity".)

In line 56, change the existing clause "WBISI more reproducible than fasting indices in children (39726936)" to "WBISI better than HOMA-IR and QUICKI in children and adolescents (39726936)". In line 57, change "OGIS and WBISI good" to "OGIS good in adults; WBISI better than fasting indices in children, with adult data pointing the other way".

Read level for the note: Matsuda abstract and Hani full text, both read 2026-10-23 (this review), PubMed record verified.

## Claims that survived

- WBISI and Matsuda share the formula in the literature; Matsuda DOI and PMID, Hani DOI and PMID, n = 257, ages 8-17, "OGTT-derived more reproducible than fasting" as the authors' conclusion.
- The arithmetic of the 2-row move (research-only 11 to 9, unsupported unchanged, total 49 with a 2-row Not evaluated flag).
- "Scoring effect none" for rows 35 and 45 is plausible but unverified here.
- The decision not to split row 17 (renumbering risk; 17a-17c if the user wants it).

## Overall

Apply item 1 as Option A with the sentence list above (nine places plus `summary-detailed.md`), and tell the user about the 36, 43, 44 inconsistency so they can pick Option B. Apply item 2 with the replacement text above. Both are label and scoping changes; neither makes the case for IR measurement stronger or weaker, and the verdict (no established routine utility for fasting insulin, HOMA-IR and TyG) is unchanged. Confidence in the replacement text: about 80%; the remaining risk is the unread Hudak study and the unseen WBISI formula.
