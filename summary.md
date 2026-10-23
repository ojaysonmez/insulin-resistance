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

## Scorecard (generated 2026-10-23; preliminary, it improves as more scoring runs finish)

Index = mean of the screening scores (decision change, evidence, guideline status, patients per year, stakes) rescaled to 0-1. Composite = the rubric's weighted score, shown only for rows with every dimension scored. Patients per year are screening estimates, mostly low confidence. Details: `usecases/scoring/screen-summary.md`, `usecases/scoring/ranking.md`.

| Tier | Row | Use | Status in list | Index | Composite | Dimensions scored | Patients per year | Missing piece (type, effort) | Watch signal |
|---|---|---|---|---|---|---|---|---|---|
| viable now | 6 | Diabetes classification: T1D, T2D, LADA | Established | 0.75 | 0.71 | 9/9 | 100k-1M | One agreed C-peptide cut-off set and conditions of use (time since diagnosis, renal function, concurrent glucose) in a single US guideline, with... (guideline, medium) | - |
| viable now | 1 | Adult with hypoglycaemia: insulinoma vs other causes | Established | 0.74 | 0.65 | 9/9 | 10k-100k | A prospective accuracy study with a standard assay-specific cutoff set (current insulin and C-peptide immunoassays) in consecutive patients with... (evidence, medium) | - |
| viable now | 2 | Suspected factitious or exogenous insulin hypoglycaemia | Established | 0.63 | 0.57 | 9/9 | 1k-10k | Report analogue cross-reactivity per assay with a validated cutoff pattern, and a cohort accuracy study of insulin plus C-peptide against drug screen... (assay, medium) | - |
| viable now | 10 | Islet or pancreas transplant graft function | Established | 0.59 | 0.56 | 9/9 | 1k-10k | A published Igls 2.0-type document with explicit C-peptide thresholds by assay, and adjustment for kidney function. (guideline, small) | - |
| viable now | 24 | Child older than 2 years with new hyperinsulinaemic hypoglycaemia; MEN1... | Established | 0.57 | 0.55 | 9/9 | 100-1k | A paediatric series of insulin and C-peptide at hypoglycaemia in children over 2 years with confirmed insulinoma or MEN1, with age-specific cutoffs. (evidence, medium) | - |
| viable now | 29 | Children/adolescents, recently diagnosed Stage 3 T1D: selecting for teplizumab | Established | 0.69 | 0.53 | 9/9 | 1k-10k | Clinical-outcome follow-up of PROTECT (HbA1c, insulin dose, hypoglycaemia) and a subgroup analysis by baseline C-peptide showing selection adds to... (evidence, large) | - |
| viable now | 4 | Infant or child with persistent hypoglycaemia | Established | 0.66 | 0.53 | 9/9 | 1k-10k | A guideline-adopted high-sensitivity insulin assay with a defined detection limit and a standard critical-sample set across US hospitals. (assay, small) | - |
| close | 31 | Adults clinically T1D >=3 years, or anyone on insulin with doubtful type... | Established | 0.67 | 0.58 | 9/9 | 100k-1M | Prospective validation of a C-peptide threshold (with glucose, duration and antibody status) for safe insulin withdrawal in doubtful-type adult... (evidence, medium) | - |
| close | 7 | Choosing who gets genetic testing for MODY | Established | 0.57 | 0.58 | 9/9 | 10k-100k | External validation of a UCPCR or C-peptide pathway with better positive predictive value (20% quoted) and a US-available assay and collection... (assay, medium) | - |
| close | 47 | Slowly progressive type 1 diabetes | Limited | 0.49 | 0.54 | 9/9 | 10k-100k | Adoption or validation of the fasting C-peptide threshold by a US or international body in non-Japanese cohorts. (guideline, medium) | - |
| close | 32 | Adults with DKA but not classic T1D: ketosis-prone diabetes | Limited | 0.53 | 0.54 | 9/9 | 10k-100k | A multi-centre prospective cohort in a US population testing C-peptide-guided insulin withdrawal and relapse. (evidence, medium) | - |
| close | 5 | Hypoglycaemia after bariatric surgery | Limited | 0.55 | 0.53 | 9/9 | 10k-100k | An accepted insulin or C-peptide threshold during a standardised mixed-meal test, validated against symptoms and CGM (evidence, medium) | - |
| close | 3 | Sulfonylurea or meglitinide hypoglycaemia | Established | 0.58 | 0.49 | 9/9 | 1k-10k | Accuracy data and an up-to-date drug screen covering newer agents, with a stated insulin and C-peptide threshold during hypoglycaemia. (assay, small) | - |
| close | 13 | Stroke or TIA with prediabetes/IR: pioglitazone selection | Limited | 0.54 | 0.49 | 9/9 | 100k-1M | Analysis or trial showing whether pioglitazone benefit differs by baseline HOMA-IR, with a standardised insulin assay (evidence, small) | - |
| close | 33 | Children/adolescents, diabetes >~2 years, suspected non-T1D | Limited | 0.47 | 0.47 | 9/9 | 1k-10k | A multi-centre validation of a single UCPCR cutoff against genetic and autoantibody-defined type, with a comparison to autoantibody testing alone. (evidence, medium) | - |
| close | 22 | Insulinoma with negative imaging; MEN1; suspected adult nesidioblastosis | Established | 0.52 | 0.46 | 9/9 | 100-1k | A head-to-head cohort of calcium-stimulated venous sampling against exendin PET/CT in negative-imaging patients, with surgical cure as the outcome. (evidence, medium) | - |
| close | 23 | Insulinoma presenting with postprandial symptoms only | Limited | 0.43 | 0.44 | 9/9 | 1k-10k | A prospective study of OGTT or mixed-meal insulin and C-peptide ratios in patients with postprandial symptoms and a negative fast, with an external... (evidence, medium) | - |
| close | 49 | Autoantibody-positive relatives: individual progression risk | Limited | 0.38 | 0.40 | 9/9 | 1k-10k | External validation of simplified C-peptide scores in a large antibody-positive cohort, plus a trial showing C-peptide-guided monitoring changes... (evidence, large) | - |
| far | 20 | Adult with hyperinsulinaemic hypoglycaemia and insulin autoantibodies: insulin... | Limited | 0.49 | 0.53 | 9/9 | 100-1k | A guideline or consensus text that states which insulin, antibody and PEG results define insulin autoimmune syndrome, with a harmonised... (guideline, medium) | - |
| far | 21 | Non-islet-cell tumour hypoglycaemia | Limited | 0.49 | 0.52 | 9/9 | 1k-10k | Guideline or review text stating the insulin and C-peptide pattern as the first step before IGF-II testing. (guideline, small) | - |
| far | 12 | Severe or syndromic IR: genetic IR syndromes, type B IR | Limited | 0.48 | 0.51 | 9/9 | 1k-10k | Diagnostic accuracy study of fasting insulin thresholds in severe IR and type B IR with standardised assay and US adoption. (evidence, medium) | - |
| far | 35 | Pregnancy/GDM | Not evaluated | 0.43 | 0.49 | 9/9 | >1M | Prospective study showing first-trimester HOMA-IR adds to risk-factor screening for GDM, then a trial of early intervention guided by it. (evidence, large) | - |
| far | 14 | Suspected MASLD without T2D | Limited | 0.45 | 0.47 | 9/9 | >1M | Trial or cohort showing HOMA-IR or OGTT-derived estimates change management beyond FIB-4 and elastography, with an agreed assay cut-off. (evidence, large) | - |
| far | 28 | C-peptide interpretation in kidney disease | Research-only | 0.44 | 0.44 | 9/9 | 100k-1M | Validated eGFR-adjusted C-peptide or UCPCR thresholds in a US CKD cohort, and a guideline note. (evidence, medium) | - |
| far | 46 | Fulminant type 1 diabetes: ketoacidosis soon after hyperglycaemic symptoms... | Limited | 0.40 | 0.43 | 9/9 | 1k-10k | Accuracy study of the C-peptide cut-offs in a non-Japanese population and a Western guideline recognising fulminant T1D. (evidence, medium) | - |
| far | 25 | Infant with spuriously high insulin from maternal insulin antibodies or... | Limited | 0.40 | 0.42 | 9/9 | <100 | Validation of an interpretation algorithm with PEG precipitation in infant hypoglycaemia on a larger cohort, and a routine PEG assay. (assay, medium) | - |
| far | 11 | Bariatric surgery: predicting diabetes remission | Limited | 0.40 | 0.41 | 9/9 | 10k-100k | Analysis of whether C-peptide adds to diabetes duration, BMI and age in remission prediction, with external validation of a cutoff on a standard... (evidence, small) | S2 2026-10-22 (rescore queued) |
| far | 45 | Prior gestational diabetes | Not evaluated | 0.35 | 0.40 | 9/9 | 100k-1M | A cohort showing postpartum fasting insulin or HOMA-IR adds to OGTT, A1C and BMI for predicting type 2 diabetes after gestational diabetes, and a... (evidence, large) | - |
| far | 8 | Residual beta-cell function in T1D: trial endpoints | Research-only | 0.34 | 0.37 | 9/9 | 1k-10k | Regulatory-accepted use of stimulated C-peptide to select or monitor an individual patient, plus a shorter validated meal-test protocol. (workflow, medium) | - |
| far | 9 | Pancreatogenic diabetes, post-pancreatitis or pancreatectomy | Limited | 0.43 | 0.36 | 9/9 | 1k-10k | Published C-peptide cut-offs for type 3c and for TPIAT outcome prediction, validated prospectively. (evidence, medium) | - |
| far | 27 | Post-pancreatectomy/TPIAT: beta-cell reserve before and graft function after... | Limited | 0.30 | 0.30 | 9/9 | 100-1k | A prospective TPIAT cohort testing whether preoperative MMTT C-peptide predicts insulin independence beyond islet yield and glucose measures. (evidence, medium) | - |
| far | 48 | Non-diabetic adult with suspected reactive hypoglycaemia, no gastric surgery | Research-only | 0.26 | - | 8/9 | - | Agreed diagnostic criteria for non-surgical postprandial hypoglycaemia and a study showing insulin or C-peptide changes management beyond documented... (guideline, medium) | - |

<!-- SCORECARD:END -->
