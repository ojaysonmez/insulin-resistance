# Skeptic check of discovery reports D1, D2, D3

Reviewer: skeptic (single pass). Checked against local texts in corpus/fulltext (grep passages, not whole papers). Unread: C318, C333 (no local text); C207, C220, C309, C164, C275 not opened. Tool calls used: 9 (3 reads, 6 shell).

## Verdict table (candidates, merged across D1-D3)

| # | Candidate (reports) | Measure type | Verdict | Tier guess | Reason |
|---|---|---|---|---|---|
| 1 | Post-bariatric hypoglycaemia pre-op prediction (D3: C315, C318, C329, C333) | none in C315; MMCT insulin/C-peptide in C329 | DROP as a prediction use; fold diagnosis part into row 5 | - | C315 predictors are sex, education, T2D, diabetes duration, vitamin deficiency (Table 2); no insulin or C-peptide predictor. C329 is a case series using a 5-h mixed-meal test with insulin and C-peptide, which is row 5 (diagnosis). C318, C333 unread. |
| 2 | Risk-stratified lifestyle in prediabetes (D2: C073, PLIS) | post-load OGTT insulin secretion and sensitivity plus liver fat | NEW-ROW | D | Text says phenotype was "based on insulin secretion, insulin sensitivity and liver fat"; intensified vs conventional lifestyle in high-risk group favoured intensified (difference CI -0.544 to -0.036, p=0.025; the outcome variable is not clear in my grep). Low-risk: conventional not superior to control. Preprint (medRxiv version in corpus), single trial. Row 17/45 do not carry a stratified-treatment decision. |
| 3 | Insulin sensitiser in mood disorders by IR (D1: C038, C158; D2: C079) | fasting insulin / HOMA-IR; C038 uses a composite (FPG, 2-h OGTT, FPI, HOMA-IR>3.8) | NEW-ROW (one combined row) | D | C079 (TRIO-BD) is a randomised placebo-controlled trial, n=45 (metformin n=20), "Effect sizes were large" on MADRS, so D2's "result not seen" is resolved: positive, small. C038 post hoc: pioglitazone helped only the IR subgroup. D1's C038 flag is confirmed; the IR definition is a mixed surrogate, not insulin alone. C158 not checked. Nearest row 13. |
| 4 | Pre-transplant C-peptide for SPK selection (D2: C171, C166) | C-peptide, type not stated | NEW-ROW weak, or DROP | D | C171 asks "Do pretransplant C-peptide levels predict outcomes" and says outcomes are equivalent when detectable; no decision rule. Retrospective, direction mixed. I lean DROP unless C166 gives a threshold (unread). Distinct from row 10 (post-transplant). |
| 5 | OGTT insulin/C-peptide ratios for insulinoma instead of 72-h fast (D2: C249) | post-load insulin and C-peptide ratios | MERGE into row 23 | D | Verified: 37 insulinoma vs 42 controls, AUC 0.97 at ratio threshold >0.351, sensitivity 86.5%. Row 23 already records the single-institution OGTT pattern and Cryer's caution. Add the numbers; D3's C323 (glucose curves beat insulin) is the counterweight, so net unproven. |
| 6 | NAFLD/NASH/fibrosis: IR index, hepatic insulin clearance (D1: C161, C144, C147; D2: C243, C075, C254) | fasting HOMA-IR; post-load insulin/C-peptide for clearance; OGIS | MERGE into row 14 | D | C243 compares HOMA-IR and serum biomarkers for steatosis/fibrosis in morbid obesity; correlational. Row 14 already says Adipo-IR "predicts severity of hepatic fibrosis" (untraced). C161 title only on clearance; no decision. Merge D1 and D2 into one note. |
| 7 | MAFLD definition HOMA-IR (D2: C061) | fasting HOMA-IR | MERGE into row 14 as history, no new row | - | D2 said no HOMA hit; that is wrong. C061 lists "HOMA-insulin resistance score 2.5" among metabolic abnormality criteria for lean MAFLD (consensus definition). Superseded by MASLD terminology, so low value; row 14 already discusses the definition. Correct D2's "unverified". |
| 8 | MODY two-step screening in youth (D1: C201, C218; D2: C256, C241) | fasting C-peptide (C201 >=0.8 ng/mL, C256 >0.6 ng/mL); C218 is post-meal UCPCR >=0.2 nmol/mmol | MERGE into row 7 | - | Row 7 already covers UCPCR. D1 mislabels C218 as fasting C-peptide; it uses a urine sample 2 h after the largest meal. C201 does give the fasting 0.8 ng/mL rule; thresholds differ across studies (0.6 vs 0.8), worth stating. |
| 9 | Antipsychotic weight gain, baseline insulin/HOMA (D1: C217) | fasting insulin, HOMA-IR | MERGE into row 50 | D | Verified n=117, baseline insulin, HOMA-IR and leptin associated with more weight gain; association only. Row 50 is the antipsychotic row. |
| 10 | Breast cancer / oncology fasting insulin, HOMA-IR (D1: C145-C162; D2: C170, C165) | fasting insulin / HOMA | NEW-ROW (single row) or MERGE into row 40 | D | Cohort associations and post hoc trial data; same decision area in D1 and D2, so one row. Not read in depth by me. Research-leaning. |
| 11 | Diet choice by INS-30 (D1: C051) | post-load insulin (30 min) | NEW-ROW as negative entry | D (negative) | Verified: n=609, "no significant diet-insulin interaction". Useful as a negative result. |
| 12 | Data-driven T2D subtypes (D2: C101, C269) | fasting HOMA2-B and HOMA2-IR | MERGE into row 17 | D | Consensus calls it a gap; no decision rule. |
| 13 | IR-stratified cardiorenal drugs, eGDR (D3: C177, C185, C131) | non-insulin surrogate (eGDR) | DROP (or one line in row 13) | - | No insulin or C-peptide measurement; post hoc subgroups. Outside project scope on measure type. |
| 14 | Early-pregnancy TyG (D3: C188, C331) | non-insulin surrogate, fasting | DROP or MERGE into row 35(b) | D | No insulin assay; row 35 covers first-trimester HOMA-IR. |
| 15 | Fasting C-peptide forecasting beta-cell depletion in T1D (D3: C306, C285) | fasting C-peptide | NEW-ROW weak, nearest row 47 | D | C306 is a Japanese prospective cohort of time to undetectable C-peptide; no action attached. Keep only if an action is found; otherwise MERGE into row 47. |
| 16 | eGFR-style youth classification (D2: C252) | non-insulin surrogate | DROP | - | Not insulin or C-peptide. |
| 17 | Assay standardisation (D1 11 papers; D2, D3 several) | all | MERGE into a cross-cutting note, not a row | - | Enabling condition, no clinical decision. Applies to rows 1, 2, 6, 7, 10, 20. |
| 18 | Pancreas transplant candidacy (D3 not-found: C302, C325) | - | DROP | - | Scout found no C-peptide text; agree. |

## Refinements: the 8 most consequential

| Row | Refinement | Verdict | Check |
|---|---|---|---|
| 10 | C271 CITR numeric cut points (D2) | ACCEPT | Verified quote: fasting C-peptide optimal-outcome cut point 0.33 nmol/L (AUC 0.845), MMTT-stimulated C-peptide 0.97 nmol/L, CPGR 0.12 nmol/mmol. Row 10 text has none of these figures. Say that CITR is observational (islet-alone recipients, 677 per D2; count not re-checked). |
| 1 | Assay-specific cut-off (D1: C192, C197) | ACCEPT WITH EDIT | C192: ELISA insulin was <36 pmol/L in four insulinoma patients, three <18 pmol/L. "4 of 11" total not verified; write "four patients". C197 postprandial-only 6% (fasting only 73%) confirmed; row 23 already says up to 18%, so reconcile the two figures. |
| 2 | Analogue cross-reactivity (D1 C155, D2 C272/C175/C276/C264, D3 C181/C292/C291) | ACCEPT as citation-only | Row 2 already states assays miss analogues. The new cases add examples, not a new claim; C175 title only. |
| 6 | Assay harmonisation and pre-analytics (D3: C298, C312, C309, C283) | ACCEPT WITH EDIT | Pre-analytic point (EDTA, 24 h) in C309 not opened by me; mark unverified. Do not carry C283 "AUC 0.95-0.98" forward without reading. Add D2's triage-model papers (C239, C250, C268) as comparators. |
| 7 | Fasting C-peptide screening rule (D2: C256, C241; D1: C201) | ACCEPT | C201: fasting C-peptide >=0.8 ng/mL, antibody-negative. Report thresholds as study-specific. |
| 13 | Glucose-defined route to pioglitazone benefit (D2: C055, C164) | ACCEPT WITH EDIT | C055 is a post hoc IRIS analysis in 2885 participants with prediabetes (glucose-defined); supports saying the measurement is not required. C164 unread. |
| 20 | Free C-peptide after PEG (D1: C207, C220) | REJECT | Row 20 already includes PEG precipitation and cites a case where assays disagreed; C207 and C220 unread and case-level. |
| 29 | PROTECT, C281/C330 (D3) | ACCEPT WITH EDIT | Row 29 already cites PROTECT (328 patients). C330 per-protocol entry peak C-peptide 0.2 nmol/L equals the row's 0.2 pmol/mL (same unit), so no conflict; add only as unit cross-check. C286 not confirmed by scout; do not add. |

## Other notes
- Row 23/48: D3's C323 (glucose curves separate insulinoma from reactive hypoglycaemia better than insulin or C-peptide) is consistent with row 23's Cryer caution; accept as refinement, abstract-level.
- Row 5: D2's C260 (sensitivity 71% vs 47%) is a glucose result; do not describe it as an insulin or C-peptide result.
- Overall: at most 3 or 4 worthwhile new rows (items 2, 3, 11 and perhaps 10), all tier D. Nothing reaches tier C.
- Assumptions: I did not verify PMIDs or DOIs; none are proposed here.
