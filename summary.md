# Which uses of insulin and C-peptide measurement are viable?

One-page brief, written 2026-10-19. Preliminary: it uses the status of each use case, not scores (scoring is the next step). Detail and sources: `summary-detailed.md`, `merged-conclusion.md`, `usecases-verified.md`. Not medical advice.

**Goal.** Find the uses of insulin, C-peptide and insulin-resistance measurement that are most viable, and what would make the less viable ones viable. We already know routine insulin-resistance screening is not supported (below); that is the constraint, not the finding to repeat.

## 1. Viable now: 11 uses with established support
All are about insulin secretion or classification, not insulin-resistance screening [usecases-verified: Summary by kind].
- **Hypoglycaemia work-up** in adults and children: insulin and C-peptide at the time of low glucose, with other markers (rows 1-4, 22, 24).
- **Diabetes classification** in insulin-treated people: a random C-peptide with a glucose, and urinary C-peptide for MODY triage (rows 6, 7, 31).
- **Islet or pancreas graft function:** C-peptide within the Igls criteria (row 10).
- **Teplizumab eligibility:** peak stimulated C-peptide of at least 0.2 pmol/mL in ages 8-17 (row 29).

## 2. Closest to viable (from the stage 1 screen)
Eleven uses are "close": limited or partly established support plus one specific missing piece (full table in the scorecard below). The cheapest next steps are the small-effort ones:
- **Pioglitazone after stroke** (row 13): re-analyse the IRIS trial by HOMA-IR stratum and agree an assay standard.
- **Slowly progressive type 1 diabetes** (row 47): validate the 0.6 ng/mL C-peptide cutoff outside Japan.
- **Sulfonylurea hypoglycaemia** (row 3): show what insulin and C-peptide add to the drug screen alone.
Medium-effort steps: a validated insulin cutoff for post-bariatric hypoglycaemia (row 5), a prospective cohort for C-peptide-guided de-escalation of insulin (row 31), validation of the MODY triage pathway (row 7), a guideline statement on post-DKA C-peptide (row 32), accuracy series for postprandial-only insulinoma (row 23) and for urinary C-peptide in US children (row 33), and external validation of the Index60 score for type 1 risk staging (row 49).
Screened "far": fatty liver (row 14, a very large patient pool but weak evidence), type 3c diabetes (row 9) and severe or genetic insulin resistance (row 12).

## 3. What would unlock more (research targets, not conclusions)
- A pre-specified study of whether HOMA-IR or TyG adds to risk scores (PCE, SCORE2) with calibration [merged-conclusion: Open gaps 2].
- A trial of measurement-guided care against usual care; none was found [merged-conclusion: Trials and interaction].
- Treatment-interaction tests stated per measure, in adequately sized trials [merged-conclusion: Open gaps 3].
- Assay-harmonised cutoffs: one fasting insulin varies about 25-30% within a person, and assays disagree [merged-conclusion: Open gaps 4; Added by chemist runs].
- Post-meal and stimulated tests: only research-level uses beyond rows 10 and 29 so far (rows 48 and 49 are new, research-only and limited).

## 4. Not worth pursuing now
Routine fasting insulin, HOMA-IR or TyG screening in primary care, prediabetes, type 2 diabetes, PCOS, fatty liver or obesity: no established utility, about 80-85% likely to stay so (a judgement); the PCOS and paediatric obesity guidelines advise against routine insulin testing [merged-conclusion: Bottom line 1; usecases-verified: rows 15, 16].

## Next step
Score the candidates (decision impact, evidence, readiness, patients affected, stakes, and path to viability) to pick 2-3 pathways to focus on [usecases/scoring-rubric.md]. The pilot on rows 6, 5 and 13 waits for a go-ahead.

*Limits:* percentages are judgements; specialty reviews are not done; about 20-30 key papers were read at abstract level only.

<!-- SCORECARD:START -->

## Scorecard (generated 2026-10-20; preliminary, it improves as more scoring runs finish)

Index = mean of the screening scores (decision change, evidence, guideline status, patients per year, stakes) rescaled to 0-1. Composite = the rubric's weighted score, shown only for rows with every dimension scored. Patients per year are screening estimates, mostly low confidence. Details: `usecases/scoring/screen-summary.md`, `usecases/scoring/ranking.md`.

| Tier | Row | Use | Status in list | Index | Composite | Dimensions scored | Patients per year | Missing piece (type, effort) |
|---|---|---|---|---|---|---|---|---|
| viable now | 1 | Adult with hypoglycaemia: insulinoma vs other causes | Established | 0.77 | - | 5/9 | 10k-100k | Prospective accuracy data for the thresholds with current assays (evidence, medium) |
| viable now | 6 | Diabetes classification: T1D, T2D, LADA | Established | 0.75 | 0.75 | 9/9 | 100k-1M | One agreed C-peptide cut-off set and conditions of use (time since diagnosis, renal function, concurrent glucose) in a single US guideline, with... (guideline, medium) |
| viable now | 4 | Infant or child with persistent hypoglycaemia | Established | 0.73 | - | 5/9 | 1k-10k | Sensitive paediatric insulin assay standardisation and cutoffs (assay, medium) |
| viable now | 29 | Children/adolescents, recently diagnosed Stage 3 T1D: selecting for teplizumab | Established | 0.73 | - | 5/9 | 1k-10k | Clinical-outcome confirmation of benefit and guideline endorsement of Stage 3 use (evidence, large) |
| viable now | 2 | Suspected factitious or exogenous insulin hypoglycaemia | Established | 0.63 | - | 5/9 | 1k-10k | Accuracy data and analogue-detecting assay performance for the high insulin/low C-peptide pattern (evidence, small) |
| viable now | 24 | Child older than 2 years with new hyperinsulinaemic hypoglycaemia; MEN1... | Established | 0.54 | - | 5/9 | 100-1k | Registry data on diagnostic yield in children over 2 years (evidence, medium) |
| viable now | 10 | Islet or pancreas transplant graft function | Established | 0.53 | - | 5/9 | 1k-10k | Igls 2.0 with agreed numeric C-peptide thresholds (guideline, small) |
| close | 31 | Adults clinically T1D >=3 years, or anyone on insulin with doubtful type... | Established | 0.71 | - | 5/9 | 100k-1M | Prospective cohort showing C-peptide thresholds predict safe insulin de-escalation in T2D (evidence, medium) |
| close | 7 | Choosing who gets genetic testing for MODY | Established | 0.62 | - | 5/9 | 10k-100k | Prospective validation of the combined triage pathway PPV in US-relevant populations (evidence, medium) |
| close | 3 | Sulfonylurea or meglitinide hypoglycaemia | Established | 0.58 | - | 5/9 | 1k-10k | Evidence on added value of insulin/C-peptide over drug screen alone, and screen coverage of newer agents (evidence, small) |
| close | 32 | Adults with DKA but not classic T1D: ketosis-prone diabetes | Limited | 0.57 | - | 5/9 | 10k-100k | Consensus or guideline statement endorsing post-DKA C-peptide (with timing) for deciding insulin withdrawal, with a US multi-ethnic cohort validation (guideline, medium) |
| close | 13 | Stroke or TIA with prediabetes/IR: pioglitazone selection | Limited | 0.59 | 0.57 | 9/9 | 100k-1M | Analysis or trial showing whether pioglitazone benefit differs by baseline HOMA-IR, with a standardised insulin assay (evidence, small) |
| close | 22 | Insulinoma with negative imaging; MEN1; suspected adult nesidioblastosis | Established | 0.54 | - | 5/9 | 100-1k | Multicentre series with concordance to surgical findings, compared with modern imaging (evidence, medium) |
| close | 5 | Hypoglycaemia after bariatric surgery | Limited | 0.55 | 0.53 | 9/9 | 10k-100k | An accepted insulin or C-peptide threshold during a standardised mixed-meal test, validated against symptoms and CGM (evidence, medium) |
| close | 23 | Insulinoma presenting with postprandial symptoms only | Limited | 0.49 | - | 5/9 | 100-1k | Diagnostic accuracy series of OGTT or mixed-meal insulin/glucose in surgically confirmed insulinoma with postprandial-only presentation (evidence, medium) |
| close | 33 | Children/adolescents, diabetes >~2 years, suspected non-T1D | Limited | 0.48 | - | 5/9 | 1k-10k | Multi-centre validation of UCPCR/post-meal C-peptide cut-offs in a US paediatric population, then inclusion in a paediatric guideline (evidence, medium) |
| close | 47 | Slowly progressive type 1 diabetes | Limited | 0.47 | - | 5/9 | 10k-100k | External validation of the 0.6 ng/mL cut-off against insulin requirement in a non-Japanese cohort (existing LADA cohorts) (evidence, small) |
| close | 49 | Autoantibody-positive relatives: individual progression risk | Limited | 0.43 | - | 5/9 | 1k-10k | External validation of Index60 or C-peptide thresholds in independent cohorts and a guideline line on monitoring (evidence, medium) |
| far | 14 | Suspected MASLD without T2D | Limited | 0.50 | - | 5/9 | >1M | Evidence that insulin-based testing changes MASLD management, and standardised assays (evidence, medium) |
| far | 9 | Pancreatogenic diabetes, post-pancreatitis or pancreatectomy | Limited | 0.47 | - | 5/9 | 10k-100k | A C-peptide cutoff that separates type 3c from T2D, validated, and a consensus statement that adopts it (evidence, medium) |
| far | 28 | C-peptide interpretation in kidney disease | Research-only | 0.46 | - | 5/9 | 100k-1M | Validated eGFR-adjusted C-peptide or UCPCR cutoffs in CKD (evidence, medium) |
| far | 12 | Severe or syndromic IR: genetic IR syndromes, type B IR | Limited | 0.44 | - | 5/9 | 100-1k | A US-validated insulin threshold with an assay-specific cutoff for severe-IR work-up (evidence, medium) |
| far | 21 | Non-islet-cell tumour hypoglycaemia | Limited | 0.44 | - | 5/9 | 100-1k | A guideline or review statement that places insulin and C-peptide suppression plus IGF-II in a defined NICTH work-up (guideline, small) |
| far | 46 | Fulminant type 1 diabetes: ketoacidosis soon after hyperglycaemic symptoms... | Limited | 0.44 | - | 5/9 | 100-1k | Accuracy and outcome data for the C-peptide criterion outside Japan, and a Western consensus adoption (evidence, medium) |
| far | 35 | Pregnancy/GDM | Research-only for | 0.44 | - | 4/9 | >1M | Prospective study showing first-trimester HOMA-IR adds to clinical risk factors and changes management (evidence, medium) |
| far | 20 | Adult with hyperinsulinaemic hypoglycaemia and insulin autoantibodies: insulin... | Limited | 0.40 | - | 5/9 | <100 | Guideline or consensus text naming insulin plus antibody/PEG testing in the hypoglycaemia work-up, or a diagnostic case series with defined cut-offs (guideline, medium) |
| far | 45 | Prior gestational diabetes | Research-only | 0.39 | - | 4/9 | 100k-1M | Study showing postpartum insulin or HOMA-IR adds to OGTT/A1C in choosing prevention (evidence, medium) |
| far | 11 | Bariatric surgery: predicting diabetes remission | Limited | 0.37 | - | 5/9 | 10k-100k | A study showing C-peptide adds to duration and BMI in remission prediction (evidence, small) |
| far | 8 | Residual beta-cell function in T1D: trial endpoints | Research-only | 0.33 | - | 5/9 | 1k-10k | Regulatory or consensus statement that an MMTT C-peptide change is an accepted surrogate for clinical benefit, plus a care-use rule (guideline, medium) |
| far | 25 | Infant with spuriously high insulin from maternal insulin antibodies or... | Limited | 0.30 | - | 5/9 | <100 | Case series quantifying how often infant insulin immunoassay results are antibody-affected and the effect on management (evidence, medium) |
| far | 27 | Post-pancreatectomy/TPIAT: beta-cell reserve before and graft function after... | Limited | 0.29 | - | 5/9 | 100-1k | A pre-operative C-peptide threshold predicting insulin independence after TPIAT (evidence, medium) |
| far | 48 | Non-diabetic adult with suspected reactive hypoglycaemia, no gastric surgery | Research-only | 0.25 | - | 4/9 | - | Agreed glucose and insulin criteria for reactive hypoglycaemia, validated in a multi-centre cohort (evidence, medium) |

<!-- SCORECARD:END -->
