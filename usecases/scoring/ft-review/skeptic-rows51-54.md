# Skeptic check of rows 51 to 54 (usecases-verified.md section 1; claims UC-51 to UC-54)

Method: keyword reads of local texts in corpus/fulltext (C073, C079, C038, C051, C145, C148, C152, C170, C165, C153, C157, C162); PMID and DOI compared with corpus/corpus.csv. Not run: tools/check_citations.py (corpus.csv integrity column used instead). Quotes under 20 words.

## Identifiers (all four rows)
All PMIDs and DOIs in rows 51-54 match corpus/corpus.csv (C073, C079, C038, C051, C145, C148, C152, C170, C165). Integrity column is Clean for all except C165 (Hopkins 2018): "Correction or erratum", correction DOI 10.1038/s41586-018-0506-3. Row 54 must note this (mouse paper, not a decision source, but the flag should be shown).

## Row 51 (PLIS, C073) - ACCEPT WITH EDIT
Verified: n=1105; stratified by "insulin secretion, insulin sensitivity and liver fat content"; high-risk randomised conventional vs intensified; low-risk conventional vs control. CI [-0.544;-0.036], p=0.025 confirmed. Local text is a preprint-style full text (abstract and main text read).
Corrections:
- The CI/p refers to the PRIMARY endpoint: change in post-challenge glucose (frequently sampled OGTT), difference -0.290 mmol/l. It is not a hard outcome. The row says the outcome was not identified; it can now be stated. Liver fat difference -1.34 points (CI -2.17;-0.50, p=0.002) and cardiovascular risk score difference also favoured intensified.
- 1105 is the number included/stratified, not randomised to each comparison; 908 (82%) completed 12 months. Row says "about 1105 people (scout figure)"; replace with verified wording.
- Low-risk: text says "No difference was found for the primary endpoint" versus control (line ~523); row's "conventional was not superior to control" is consistent.
- Status Research-only: accepted (one RCT, no guideline). Measure type "post-load, multi-sample OGTT" is correct; note that the stratifying phenotype is a composite plus MR liver fat, so it is not an insulin test alone.
- Overlap: rows 17 and 45 not re-read; claim that they lack a stratified-treatment decision was not checked by me (unverified).
OLD: "the outcome variable was not identified in the skeptic's grep." 
NEW: "the outcome is the primary endpoint, change in post-challenge glucose (difference -0.290 mmol/l); it is a glucose surrogate, not incident diabetes."
OLD: "About 1105 people (scout figure, not re-checked)."
NEW: "1105 people were included and stratified; 908 (82%) completed 12 months (local text)."
Also change the Read level in the sources cell and claims UC-51 accordingly ("abstract and main text read by keyword search").

## Row 52 (TRIO-BD C079; Lin C038) - ACCEPT WITH EDIT (material correction)
Verified: Calkin n=45 randomised, metformin n=20, placebo n=25; 11 "converters" (n=10 metformin, n=1 placebo; P=.0009). All patients had IR at entry (HOMA-IR cutoff 1.8 per methods line ~92).
Correction needed: the primary outcome compared MADRS change "between those who no longer met IR criteria (converters) and those who still did". The "Cohen d > 1" large effect sizes are converters vs non-converters (a post-randomisation, non-randomised grouping), not metformin vs placebo. Between randomised arms the 30% response rates were not significant in the non-converter analysis shown (metformin 4/10 vs placebo 7/24 among non-converters); the whole-arm result was not read by me. The row's wording "large effect sizes on MADRS" in a "randomised placebo-controlled trial" overstates. Also the study enrolled only IR patients, so it does not test whether IR selects responders. IR was defined by HOMA-IR (fasting-based) in Calkin; the composite (fasting glucose, 2-h OGTT, FPI, HOMA-IR above 3.8) is Lin only.
Lin: RCT (12-week, pioglitazone 30 mg vs placebo), 42 enrolled, 37 completed; text says pioglitazone improved mood "only when IR was present". The IR-subgroup finding is a subgroup analysis in an RCT; "post hoc" was not found by grep, so I could not confirm that label. Composite includes 2-h OGTT glucose (not insulin), so partly a non-insulin surrogate; the insulin items are fasting insulin and HOMA-IR.
Status Research-only: accepted. Overlap with row 13 not re-read (unverified).
OLD: "Calkin: randomised placebo-controlled trial in bipolar depression, n=45 (metformin n=20), with large effect sizes on MADRS reported in the text."
NEW: "Calkin: randomised placebo-controlled trial in bipolar depression with insulin resistance (HOMA-IR cutoff 1.8) at entry, n=45 (metformin n=20, placebo n=25); the primary comparison was between patients who no longer met IR criteria (converters, 10 of 11 on metformin) and those who did, with large effect sizes (Cohen d above 1) for that comparison, not for metformin against placebo."
OLD: "Lin: post hoc analysis in which"
NEW: "Lin: 12-week randomised trial (42 enrolled, 37 completed) in which a subgroup finding showed that"
Add "(fasting insulin, HOMA-IR; Lin's composite also uses 2-h OGTT glucose)" to the test cell only if wanted; the "mixed surrogate" label is acceptable for Lin only.

## Row 53 (DIETFITS C051) - ACCEPT
Verified: 609 adults without diabetes randomised; "no significant diet-genotype pattern interaction (P = .20) or diet-insulin secretion (INS-30) interaction (P = .47)". Weight change -5.3 kg (low-fat) vs -6.0 kg (low-carbohydrate). INS-30 = insulin 30 min after glucose load; post-load label correct (75 g dose not checked by me; delete "75 g" if not confirmed elsewhere, or confirm). The "Unsupported" status for a negative randomised interaction test is appropriate. Optional edit: add the P value.
OLD: "no significant diet by INS-30 interaction (skeptic, local text)."
NEW: "no significant diet by INS-30 interaction (P=.47); 12-month weight change -5.3 kg low-fat vs -6.0 kg low-carbohydrate (local text)."
Caveat: one trial, 12-month weight outcome only; it does not exclude other outcomes.

## Row 54 (breast cancer; C145 C148 C152 C170 C165; C153 C157 C162) - ACCEPT WITH EDIT
Verified (abstracts and text read by keyword search):
- C145 Goodwin 2002: 512 women, no diabetes, fasting insulin; adjusted HR upper vs lower quartile 2.1 (1.2 to 3.6) distant recurrence and 3.3 (1.5 to 7.0) death. Insulin and BMI r=0.59; after BMI adjustment HR for overall survival 3.2 (1.4 to 7.1), for distant DFS 1.7 (0.9 to 3.1), so attenuation applies to DDFS only.
- C148 Duggan 2011: 527 women (HEAL); HOMA per increase HR 1.12 (1.05 to 1.20) breast cancer mortality, 1.09 all-cause; adverse direction. Fasting insulin/HOMA. Text also reports C-peptide from an earlier report (negative association with survival).
- C152 Goodwin 2012: 535 nondiabetic women; fasting insulin, HOMA, C-peptide, glucose; adverse associations "significant only during the first 5 years" (insulin Q4 vs 1 HR 2.32, 1.39 to 3.86 for DDFS). Obesity variables were constant over time. The row's "attenuated by BMI" holds for C145 only; for C152 the time-limited pattern is the statement.
- C170 MA.32 (the result the scout did not see): 3649 women randomised; metabolic analysis in 1412 metformin and 1503 placebo with baseline and 6-month fasting blood. Metformin lowered insulin (relative change -11% vs +6%) and HOMA. "There was little evidence of a significant interaction ... with baseline BMI or insulin"; isolated interactions: baseline insulin with hsCRP p=0.04. This interaction analysis is for metabolic markers, not cancer outcomes; no insulin-by-metformin test for recurrence was found in this paper. Primary cancer-outcome paper not in local texts (not read).
- C165 Hopkins 2018: mouse work; hyperinsulinaemia after PI3K inhibitors limits efficacy; has an erratum (see above). Human trial evidence was not read.
- Window studies: C153 (Niraula 2012) reports 48 patients signed consent and were enrolled, metformin 500 mg tid, HOMA decreased; C157 endometrial cancer, 11 patients (not breast). C162 (NHANES, 10,033 adults, fasting insulin, cancer death) is not breast. I did not read C153/C157/C162 beyond these lines.
Status Research-only: accepted (cohort associations; no insulin-guided decision). The row lists measure type fasting-based, C-peptide in C152 only (and cited earlier by C148); fine.
Overlap with rows 17 and 40 not re-read (unverified).
OLD: "Read level: scout reports from digest excerpts and local texts, not re-verified in depth by the skeptic"
NEW: "Read level: full texts or abstracts of C145, C148, C152, C170 and C165 read by keyword search by a second skeptic; C153, C157, C162 only skimmed"
OLD: "Scout-reported, not re-verified: prospective cohorts of 512, 527 and 535 women link higher fasting insulin or HOMA to worse recurrence or mortality, attenuated by BMI and limited to the first years; window-of-opportunity metformin studies were small; the MA.32 trial result for insulin-by-metformin interaction was not seen; the PI3K-inhibitor finding is from mice."
NEW: "Prospective cohorts of 512 (fasting insulin, adjusted HR 2.1 distant recurrence, 3.3 death), 527 (HOMA, HR 1.12 breast cancer mortality) and 535 women (adverse insulin associations significant only in the first 5 years) link higher fasting insulin or HOMA to worse outcome; in the 512 cohort the distant recurrence association weakened after BMI adjustment (HR 1.7, 0.9 to 3.1). The window-of-opportunity metformin study (48 enrolled) was small. In the MA.32 randomised trial (3649 women) metformin lowered insulin and HOMA, with little evidence that this change depended on baseline insulin; that analysis covers metabolic markers, not recurrence. The PI3K-inhibitor finding is from mice, and that paper carries an erratum (10.1038/s41586-018-0506-3)."
Also fix the "Hopkins 2018 (mouse)" source entry by adding "(erratum issued)". Also update the matching claims.csv UC-54 text identically. The "PI3K-pathway inhibitor treatment" in the patient type is supported only by the mouse paper; consider dropping it from the title (suggestion, not required).

## Summary
| Row | Verdict |
|---|---|
| 51 | ACCEPT WITH EDIT (name the primary outcome as post-challenge glucose; fix 1105 wording) |
| 52 | ACCEPT WITH EDIT (large effect sizes are converters vs non-converters, not drug vs placebo; Lin n and design) |
| 53 | ACCEPT (optional P and weights) |
| 54 | ACCEPT WITH EDIT (replace scout wording; add MA.32 result; erratum on C165) |

Not traced or not read: rows 17, 13, 40, 45 text; Calkin whole-arm metformin vs placebo MADRS result; "75 g" in DIETFITS; "post hoc" label for Lin; full text of C153, C157, C162; C073 is a preprint version, so numbers may differ from the published Diabetes paper.
Tool calls used: 9 (including this write).
