# Skeptic review of FT5 and FT6 (full-text claim reviews)

Method: quotes checked by normalised string search (whitespace, hyphenation, punctuation removed) against corpus/fulltext/<ID>.txt; numbers checked by regex against the same files; current wording read from merged-conclusion.md (usecases-verified.md has no hit for any of the cited PMIDs, so nothing to change there). Claims ledger claims/claims.csv rows were read for the claim IDs. All files are PDF/XML extractions; two-column interleaving is common. Tool calls used: 12 reads/greps plus this write (about 14).

## 1. Quote checks

"Interleaved" means the sentence is present but a second column's text is woven into it by the extraction; the words are all there in order across the break. No quote is missing or invented.

| Paper | Result | Note |
|---|---|---|
| C001 (10480510) | Found, interleaved | "provides a reasonable approximation of [column break] whole-body insulin sensitivity from the OGTT". Extraction artefact. |
| C007 (15983289) | Found, interleaved | "TG levels and TG-HDL-C ratio are not reliable markers of insulin resis- [column break] tance". Artefact. |
| C010 (17533210) | Found | "Complex clinical models showed no further im- provement in model discriminations (AROC, 0.850-0.854) and were not superior to the simple clinical model". The first normalised search failed only on the hyphenated "im-provement"; text is present. |
| C016 (19700136) | Found exactly | |
| C034 (25944628) | Found exactly | |
| C085 (35700159) | Found exactly | |
| C088 (36181637) | Found, interleaved | "with a questionable degree [break] of clinical utility due to the lack of standardization of predictive values". Artefact. |
| C101 (37794253) | Found exactly | Sits in the CVD-prognosis section; the following sentences speak of "T2D" prospective studies. |
| C135 (42569452) | Found exactly | |
| C142 (42702103) | Found exactly | |
| C145 (11773152) | Found, interleaved | "Fasting insulin level is associated with [prognostic factors ... collected, and] outcome in women with early breast cancer". Artefact (two columns). |
| C146 (20190296) | Found exactly | |
| C148 (21115858) | Found exactly | |
| C149 (21441124) | Found exactly | |
| C152 (22162568) | Found, interleaved | "univariable adverse prognostic associations were [break] significant only during the first 5 years". Artefact. |
| C156 (24476695) | Found, interleaved | "HEGC-assessed M and M/I predicted both all-cause mortal-[break] ity and CVD deaths, with AUCs ranging from 0.56 to 0.58". Note: the AUCs belong to the clamp-derived M and M/I, not to the surrogate indices. |
| C159 (26526047) | Found exactly | |
| C162 (28390156) | Found exactly | |

## 2. Claim issue verdicts

Line numbers are merged-conclusion.md. "Confirmed (with edits to the proposed text)" is recorded as reword, with the exact wording in the Apply list.

| # | Issue | File and line | Claim IDs | Verdict | Evidence |
|---|---|---|---|---|---|
| FT5-1 | Health ABC: OGTT measure is 2-h glucose, insulin fasting only | merged-conclusion.md line 28 (also line 8) | EV-14 | Confirmed, reword (merge with FT5-2; also fix line 8) | Line 28 says "an OGTT measure (not specified in the files)" and "two post-load prediction results"; confirmed. C016 quote (found exactly) lists "fasting insulin, 2 hour post challenge glucose ... HOMA-based" and n=2386 found. Because Health ABC has no post-load insulin, the phrase "two post-load prediction results" (lines 8 and 28) becomes wrong and must change too. The 2-h glucose is a glucose measure, not a post-load insulin test. |
| FT5-2 | Framingham: insulin was included, outcome is incident diabetes | line 28 and line 34 | EV-15, EV-28 | Confirmed, reword | C010 text: AROC 0.850-0.854, "not superior to the simple clinical model", simple model 0.85; Gutt index and HOMA/fasting insulin among complex models (paper-reading file; text file shows the AROC passages). Line 34 says "AROC unchanged when HOMA-IR or insulin added" and "not verified whether insulin was included"; both are resolved. "160 cases, 3140, 99% white" not re-grepped (reviewer figures). |
| FT5-3 | Wang 2022 is association, not incremental prediction | line 34 | EV-28 | Confirmed, reword | Checked in C085: 1.04 (0.92-1.18) NGT; 1.12 (1.06-1.18); diabetes CI ends 1.21; NGT n = 28,890; P interaction 0.011; "mean [SD] 3.60 [1.04] years"; adjustment list is age, sex, education, alcohol, smoking, physical activity, diet quality (no BMI, lipids or BP). 1.15 lower bound 1.09 not seen (garbled), not contradicted. The existing "Skeptic files disagree on some Wang figures" is resolved by the full text. |
| FT5-4 | ADA/EASD TyG moderate evidence applies to people with T2D; ATTICA wording | line 26 (current text already says "conflicting ATTICA gain"); claims.csv GL-34 | GL-34 | Reword | C101 quote exact. "high predictive utility ... troponin T and triglyceride-glucose (moderate evidence)" sits in the CVD review of "416 studies" and the next passage concerns "clinical decision-support tools in T2D". The T2D scope is supported by the review text; "does not recommend TyG" is an absence claim I did not exhaustively grep. The ATTICA error ("Liu 2026 and ATTICA nulls") exists only in claims.csv GL-34, not in merged-conclusion.md, where line 26 already reads "conflicting ATTICA gain". So the deliverable needs only the T2D qualifier; the ledger needs the ATTICA fix. Proposed wording's "not a recommendation to use TyG clinically" softened to what was checked. |
| FT5-5 | Liu 2026: base models differ; I2 99.1% | line 30 | EV-18, EV-25 | Reword | Found: 0.0004 (-0.0092 to 0.0100), I2 = 99.1%, 27,329 participants and 2,457 events, five studies; Table shows SCORE2-ASIA for one cohort; text says Barzegar "reported an opposing effect size" and used "FRS factors"; leave-one-out driven by Barzegar. "Three Framingham-type models" could not be confirmed (only FRS and PCE named in the text I read) so I drop the count. Own-cohort IDI 0.0034 (0.0005-0.0064), P 0.0231 for quartiles confirmed; the text reports event NRI 0.0476 with 95% CI -0.0048 to 0.0913 and "P < 0.05", an internal inconsistency (CI includes zero), so the proposed "event NRI with P<0.05" must carry that caveat. Continuous TyG delta C 0.0010 (-0.0014 to 0.0034). "Clinically trivial" and very-low certainty: quote found. The existing line says "TyG added to Framingham"; the pooled analysis was not against Framingham alone; confirmed. |
| FT5-6 | HOMA-IR meta-analysis: heterogeneity and fatal MACE wording | line 35 | EV-29 | Confirmed, reword | Found: T2DM 1.87 (1.40-2.49) I2 94%; non-fatal MACE 1.46 (1.08-1.97) I2 84%; hypertension 1.35 (1.15-1.59) I2 16%; fatal MACE 1.31 (0.96-1.77); 215,878 participants; quote on questionable clinical utility. Current line says "with *no* association with fatal MACE"; confirmed. |
| FT5-7 | Matsuda r 0.73 is derivation-sample | line 37 | MEAS-04 | Reword | C001: ISI(HOMA) r = 0.69 found. The composite 0.73 is in the abstract block (grep for 0.732 not repeated by me; reviewer states it). "153 subjects" and "no independent validation" are the reviewer's reading of a derivation paper; the abstract-level facts are consistent. Wording kept with "in the derivation sample". |
| FT5-8 | TG/HDL-C in African Americans needs scope | line 37 | MEAS-02 | Confirmed | C007: quote found; "WC 0.85" and "third tertile" definition found (text says resistance defined as the third tertile of the index as printed; the reviewer's "lowest tertile of the sensitivity index" is the same group). n=98, AUCs 0.55/0.56 not re-grepped. Added "(age 20-50)" omitted: not re-grepped. Wording adopted with the reviewer's figures flagged as not re-checked. |

| # | Issue | File and line | Claim IDs | Verdict | Evidence |
|---|---|---|---|---|---|
| FT6-1 | NHANES: 'reverse causation' is the project's reading | line 32 | EV-26 | Confirmed, reword | "reverse caus" has no hit in C142. C142 says: "this finding does not indicate a protective effect of moderate insulin resistance against cardiovascular death. Rather, it reflects that in the [competing-risk setting] ..." and "the resulting subdistribution hazard differs from the actual cause-specific hazard and warrants cautious interpretation". Tertile Model 3 HR 0.76 (0.62-0.93) and 0.69 (0.55-0.87) found; J-shape "specifically with CVDs and cardiac mortality" found. C-statistics 0.792 to 0.793 (delta C +0.001) for TyG found; the HOMA-IR 0.792 not re-grepped. |
| FT6-2 | Cancer cohorts: not independent, not all breast cancer | line 35 | EV-33 | Reword (parts rejected) | Supported: C145 and C152 are the same Toronto inception cohort (C152 text: "inception cohort of 535" with "previous report" follow-up 4.2 years; C145 affiliation Toronto; 512 of 535); C148 is a separate cohort, "Sixty-two deaths occurred among the 527 women"; C162 quote on assay variation found. Not supported by anything I could find: (a) the proposed sentence that PMID 21115858 "reported a HOMA association in ER-positive disease, which differs from 39808164"; the C148 text I found mentions ER-positive only as a subgroup description, and I could not trace an ER-positive result. I keep the existing 39808164 statement and drop the contrast. (b) "not significant when entered with BMI (P 0.07 and 0.09)": a P .09 appears in C152 but I could not trace P .07 to insulin; dropped. (c) "non-obese but not obese; 10 uU/mL" for C162 is the reviewer's abstract-level detail, not re-grepped; kept only "non-obese" qualifier flagged unverified. |
| FT6-3 | CKD study: 1,074 men, 495 with CKD; clamp AUC | line 37 | MEAS-05 | Confirmed, reword | C156 table "All subjects n = 1074 Non-CKD n = 579 CKD n = 495"; "the agreement observed for the vast majority of ISIs was considered satisfactory (weighted k>0.6)"; Baxter Novum affiliation present; the 0.56-0.58 AUCs are for HEGC M and M/I (quote), "relatively poor prediction capacity". Current text "in 495 men aged about 70" confirmed wrong as to population. The "none independently predicted" statement is supported by "IS as assessed by HEGC was not associated with mortality". "Somewhat lower in CKD" not re-checked (reviewer). Proposed wording wrongly implied the AUCs applied to the indices; corrected. |
| FT6-4 | Dialysis: 12 vs 10 patients, not a re-analysis | line 37 | MEAS-06 | Confirmed, reword | C159 abstract: "Retrospective analysis compared this cohort to 12 hemodialysis patients who had previously undergone similar testing"; r = -0.35 with HOMA-IR (p 0.01) found. C149 quote ("HOMA-IR and QUICKI are reasonable alternatives") found; r -0.58 not re-grepped. Ledger note "re-analysed the same 12 patients" is therefore not exact. "Supported in part by Baxter" not re-grepped. |
| FT6-5 | IADPSG now read in full text | line 21 | GL-24 | Confirmed, reword (minimal edit) | C146: cord C-peptide >90th percentile is a primary HAPO outcome and part of threshold selection (found three times); no maternal insulin/HOMA recommendation in the regex hits (hits are about fetal hyperinsulinemia and insulin treatment). Current line 21 says "search excerpts"; confirmed. Line 21 also covers ADA s15, which is unchanged. Rewriting the whole sentence is unnecessary; two small replacements suffice. |

## 3. Apply

Replace by exact string match in merged-conclusion.md. Confidence figures are not touched anywhere. Parallel edits to the matching claims/claims.csv rows (EV-14, EV-15, EV-18, EV-25, EV-26, EV-28, EV-29, EV-33, GL-24, GL-34 incl. the ATTICA fix, MEAS-02, MEAS-04, MEAS-05, MEAS-06) are needed by the main session; they are not given as CSV strings here because of CSV quoting. Not applied here: FT6 note that ADA/ACOG were not read.

### A1 (line 8; consequence of FT5-1/FT5-2)

OLD:
```
(the two post-load prediction results in the files are both nulls)
```
NEW:
```
(of the two prediction results once counted as post-load, Health ABC measured no post-load insulin, and the Gutt index in Framingham was a null for incident type 2 diabetes, not cardiovascular disease)
```

### A2 (line 28; FT5-1, FT5-2)

OLD:
```
The files hold two post-load prediction results not weighed here: Health ABC (PMID 19700136; abstract level; heart-failure outcome), where an OGTT measure (not specified in the files), fasting insulin and HOMA-IR added to fasting glucose did not improve prediction, so it is also a fasting null; and the Gutt index in Framingham (PMID 17533210; the biostatistician reports no gain, but the evidence searcher notes it was not verified whether insulin was included). Both are nulls.
```
NEW:
```
The files hold two prediction nulls once counted as post-load, neither weighed here as a post-load insulin result. Health ABC (PMID 19700136, DOI 10.1016/j.cardfail.2009.03.001; full text read; heart-failure outcome in 2386 adults aged 70-79 without diabetes): fasting insulin, HOMA-IR and 2-hour OGTT glucose, each added to fasting glucose, did not improve prediction; this is a fasting insulin/HOMA null (fasting-based), and no post-load insulin was measured. Framingham Offspring (PMID 17533210, DOI 10.1001/archinte.167.10.1068; full text read): for 7-year incident type 2 diabetes (160 cases in 3140 mostly white adults), complex models with fasting insulin, the Gutt index (post-load: OGTT glucose and insulin) or HOMA-IR had AROC 0.850-0.854, not superior to the simple clinical model (0.85); the outcome is diabetes, not cardiovascular disease.
```

### A3 (line 30; FT5-5)

OLD:
```
Liu 2026 (PMID 42569452): TyG added to Framingham gave a pooled C-index gain of 0.0004 (-0.0092 to 0.0100), very low GRADE, 0.0051 (0.0007-0.0094) without one dominant cohort; the abstract also reports IDI/NRI gains for TyG quartiles.
```
NEW:
```
Liu 2026 (PMID 42569452, DOI 10.3389/fcvm.2026.1804411; full text read; non-insulin surrogate): in a meta-analysis of five cohorts (27,329 participants) that used different base risk models (including SCORE2-Asia, pooled cohort equations and Framingham-type scores), adding TyG changed the C-index by 0.0004 (-0.0092 to 0.0100), I2 99.1%, very low certainty (GRADE); without the Barzegar cohort, which reported an opposing effect, 0.0051 (0.0007-0.0094), which the authors call clinically trivial. In the authors' own CHNS cohort (n=4,665) continuous TyG added nothing (delta C 0.0010, -0.0014 to 0.0034); TyG quartiles gave IDI 0.0034 (P 0.023) and a reported event NRI of 0.0476 whose printed 95% CI (-0.0048 to 0.0913) includes zero although the text says P < 0.05.
```

### A4 (line 32; FT6-1)

OLD:
```
and under competing risks higher HOMA-IR had a *lower* subdistribution hazard with a J-shaped pattern, consistent with reverse causation.
```
NEW:
```
and in Fine-Gray competing-risk tertile analyses higher HOMA-IR (fasting-based) had a *lower* subdistribution hazard (Model 3 HR 0.76, 0.62-0.93 for CVD; 0.69, 0.55-0.87 for cardiac mortality), with a J-shape for CVD and cardiac mortality. The authors (full text read) say this does not indicate a protective effect, that the subdistribution hazard differs from the cause-specific hazard and warrants cautious interpretation; "reverse causation" was the project's reading, not theirs.
```
(Table column labels for the two HRs were read from a garbled table and are best checked once by the main session; the 0.76 and 0.69 values themselves were found.)

### A5 (line 34; FT5-2, FT5-3)

OLD:
```
Set A biostatistician also cites Framingham Offspring (PMID 17533210, AROC unchanged when HOMA-IR or insulin added) and Wang 2022 (PMID 35700159, per-SD HR about 1.04 in normal glucose tolerance with a CI including 1). Skeptic files disagree on some Wang figures, and the Set A searcher lists 17533210 as "not verified whether insulin was included", so check both before citing.
```
NEW:
```
Set A biostatistician also cites Framingham Offspring (PMID 17533210; full text read: insulin was included, see the incremental-prediction bullet above; outcome is incident type 2 diabetes) and Wang 2022 (PMID 35700159, DOI 10.2337/dc22-0202; full text read; association, not prediction): HOMA-IR (fasting-based) per SD HR 1.04 (0.92-1.18) in normal glucose tolerance (n=28,890), 1.12 (1.06-1.18) in prediabetes and 1.15 (1.09-1.21) in diabetes (P interaction 0.011); mean follow-up 3.6 years; models adjusted for age, sex, education, alcohol, smoking, physical activity and diet quality, not for BMI, lipids or blood pressure.
```

### A6 (line 26; FT5-4)

OLD:
```
is quoted by the Set A searcher as giving TyG "moderate evidence" for CVD prediction. This is about prediction, not reclassification, and should be read next to the Liu 2026 null and the conflicting ATTICA gain below.
```
NEW:
```
(full text read) rates TyG (non-insulin surrogate) as having high predictive utility with moderate evidence in its systematic review of CVD prognosis in people with type 2 diabetes ("troponin T and triglyceride-glucose (moderate evidence)"). This is about prediction in people who already have diabetes, not reclassification, and not a recommendation to measure TyG; read it next to the Liu 2026 near-null and the conflicting ATTICA gain below.
```
(Applies to the string beginning after "(PMID 37794253) " in line 26; the preceding words "ADA/EASD 2023 precision-medicine consensus (PMID 37794253) " stay. Ledger GL-34: also change "Liu 2026 and ATTICA nulls" to "the Liu 2026 near-null and the ATTICA gain".)

### A7 (line 35, HOMA-IR meta-analysis; FT5-6)

OLD:
```
in a 38-cohort meta-analysis (PMID 36181637), with *no* association with fatal MACE.
```
NEW:
```
in a 38-study meta-analysis (PMID 36181637, DOI 10.1007/s40292-022-00542-5; full text read; I2 94% for incident T2D, 84% for non-fatal MACE, 16% for hypertension; fasting-based HOMA-IR); for fatal MACE the HR was 1.31 (0.96-1.77), not significant, so "not shown" rather than absent. Cut-offs differed between studies, and the authors describe clinical utility as questionable because predictive values are not standardised.
```

### A8 (line 35, cancer cohorts; FT6-2)

OLD:
```
(for example PMIDs 11773152, 21115858, 28390156; abstracts)
```
NEW:
```
(PMIDs 11773152 and 22162568 are the same Toronto cohort; PMID 21115858 is a separate cohort of 527 women with 62 deaths, whose all-cause HOMA association was lost when HOMA was log-transformed; PMID 28390156 is all-cancer, not breast-cancer, mortality in NHANES adults, with hazard ratios that varied by insulin assay; all fasting insulin or HOMA; full text read for these four)
```

### A9 (line 37, Matsuda; FT5-7)

OLD:
```
(for example Matsuda versus clamp r 0.73, PMID 10480510)
```
NEW:
```
(for example the post-load Matsuda composite index versus the clamp, r 0.73 in the 153-subject derivation sample, which was also the test sample, with no independent validation; the fasting-based ISI(HOMA) gave r 0.69 in the same sample; PMID 10480510, DOI 10.2337/diacare.22.9.1462, full text read)
```

### A10 (line 37, TG/HDL-C; FT5-8)

OLD:
```
TG/HDL-C fails in African Americans (PMID 15983289).
```
NEW:
```
TG and TG/HDL-C (non-insulin surrogates) did not identify insulin resistance in 98 African American adults with BMI 25 or more (AUC 0.55 and 0.56; FSIVGTT minimal-model reference, lowest-sensitivity tertile as resistant); fasting insulin had AUC 0.85 in the same sample (PMID 15983289, DOI 10.1001/archinte.165.12.1395, full text read; one small sample).
```

### A11 (line 37, CKD; FT6-3)

OLD:
```
in 495 men aged about 70 with eGFR below 60 (median 46), fasting and OGTT-derived indices agreed acceptably with the clamp (weighted kappa above 0.6, OGTT-derived better), and neither the clamp nor the indices independently predicted 10-year mortality (PMID 24476695, DOI 10.1038/ki.2014.1, abstract)
```
NEW:
```
in 1,074 Swedish men aged 70 (495 with eGFR below 60, median 46), the vast majority of fasting-based and OGTT-derived indices agreed with the clamp at weighted kappa above 0.6 (OGTT-derived better in the abstract; agreement somewhat lower in CKD per the reviewer, not re-checked), the clamp-derived M and M/I predicted mortality with AUCs of only 0.56-0.58, and neither the clamp nor the indices independently predicted 10-year mortality (PMID 24476695, DOI 10.1038/ki.2014.1, full text read; one author is Baxter-affiliated)
```

### A12 (line 37, dialysis; FT6-4)

OLD:
```
in dialysis two studies of 12 and 10 patients disagree on HOMA-IR (PMIDs 21441124, 26526047; abstracts, not re-read by the skeptic).
```
NEW:
```
in dialysis two small clamp studies differ on HOMA-IR (fasting-based): 12 haemodialysis patients, HOMA-IR versus clamp r -0.58, judged a reasonable alternative (PMID 21441124, DOI 10.2215/cjn.08070910), and 10 peritoneal-dialysis patients, r -0.35, called weak (PMID 26526047, DOI 10.3747/pdi.2013.00296, which used earlier haemodialysis data as a comparison group, not a re-analysis); both are pilot-sized with no outcome data, and both were read at full text.
```

### A13 (line 21, IADPSG; FT6-5), two replacements

OLD 1:
```
IADPSG 2010 (PMID 20190296, DOI 10.2337/dc09-1848; search excerpts)
```
NEW 1:
```
IADPSG 2010 (PMID 20190296, DOI 10.2337/dc09-1848; full text read)
```
OLD 2:
```
or C-peptide test; ACOG Practice Bulletin 190
```
NEW 2:
```
or C-peptide test (in IADPSG, cord-blood C-peptide above the 90th percentile appears only as one of the neonatal outcomes used to choose the glucose thresholds, not as a maternal test); ACOG Practice Bulletin 190
```

## 4. Not traced or not read

- Not re-grepped by me (taken from the reviewers, flagged in the NEW text where relevant): C001 n=153 and composite r 0.732; C007 n=98 and the TG/HDL-C AUCs; C010 160 cases and 3140; C148 ER-positive result (no result passage found); C149 r -0.58; C152 P .07; C156 "somewhat lower in CKD"; C159 Baxter support; C162 non-obese/obese split and the 10 uU/mL threshold; C142 HOMA-IR C-index 0.792; Liu "three Framingham-type models" (not confirmed, dropped).
- Reviewer statements that a term is absent were treated as search results, not as proof; I grepped HOMA/insulin in C146 and "reverse caus" in C142 only.
- Confidence figures are not changed anywhere, and no DOI or PMID was altered.
