# Skeptic review of FT13 and FT14

Reviewer: skeptic (independent re-check against corpus/fulltext/<ID>.txt; no web, no git). About 15 tool calls.
Method: every quote was normalised (whitespace, hyphen and dash variants, line-break hyphens, middle dot in "22.2") and searched in the text file. Where the PDF extraction interleaves two columns, the quote was matched by its start and end fragments and the interleaved words were inspected.
Identifiers (PMID, DOI) were taken from the FT13/FT14 JSON files and the existing rows; I did not re-run Crossref/PubMed (check_citations was not run), so identifier matching is unverified by me except where the same PMID/DOI pair already appears in usecases-verified.md.

## 1. Quote table

| Paper | Quote (start) | Status |
|---|---|---|
| C250 | progression to C-peptide deficiency is an appropriate surrogate endpoint | exact |
| C273 | Among the six routine assays, the Beckman and Siemens assay ... | exact |
| C283 | A limitation is the lack of other data sets for external validation. | exact |
| C299 | Diabetes autoantibodies and measures of beta cell function (serum C-peptide) were rarely recorded. | exact |
| C309 | Limitations for this study include the absence of samples with low insulin or C-peptide levels | exact |
| C020 | UCPCR showed excellent discrimination between HNF1A/HNF4A MODY and type 1 diabetes ... | exact |
| C020 | The advantage of using UCPCR is that it has both strong sensitivity (97%) and specificity (96%) | exact |
| C025 | UCPCR testing has limited use in patients with diabetes duration <2 yr | present, two-column interleaving (words from the other column inside the sentence); extraction artefact |
| C025 | UCPCR values close to the 0.7 nmol/mol cutoff should be interpreted with caution | present, interleaved; extraction artefact |
| C025 | suggests that a genetic test might be appropriate | NOT FOUND (checked "genetic test", "appropriate", "might be appropriate"). Paraphrase. The nearest text is "Genetic testing is likely to be the only way of distinguishing MODY from type 2 diabetes". Used only as support for row 33 D1 (verdict there: keep 2; the quote should be replaced by the "Genetic testing is likely..." sentence) |
| C025 | UCPCR has not been validated in patients with renal impairment. | present, interleaved; extraction artefact |
| C025 | 26% of the MODY probands in our study (n = 31) were inappropriately treated with insulin | present, interleaved; extraction artefact |
| C033 | The limitations of our study are its small sample size and the unequal distribution ... | present, interleaved; extraction artefact |
| C033 | a fasting C-peptide level of 0.62 ng/ml demonstrates a sensitivity of 93%, a specificity of 90% | present, interleaved ("evaluate ucpcr values." sits inside it); extraction artefact |
| C033 | Patients collected their urine samples in boric acid preservative 2 h after their lunch meal | exact (the text also says the lunch was a standard lunch in the hospital) |
| C058 | Differentiation between MODY type and T2DM was not performed. | exact |
| C058 | Urine containers with boric acid preservative were used. | present, interleaved; extraction artefact |
| C058 | UCPCR had a sensitivity of 97%, a specificity of 88% at a cutoff point ... | exact (0.28 nmol/nmol) |
| C058 | Fasting C-peptide had a sensitivity of 63%, a specificity of 84% | exact |
| C091 | detectable C-peptide (either in blood or urine) over an extended partial remission phase (at least 5 years after diagnosis) | exact |
| C100 | who are either autoantibody negative and/or have retained C-peptide levels | exact |
| C121 | negative pancreatic autoantibodies and/or a retained serum C-peptide response to hyperglycaemia | exact |
| C186 | MD cases (n=5; 0.5%) had a much higher predicted mean probability | exact |
| C256 | neither facilitated clear discrimination of MODY from non-MODY diabetes, alone or in combination | exact |
| C274 | From 2002 through 2018, SEARCH identified 18,169 youth with T1D among 85 million person-years ... | exact (5,293 T2D among 44 million person-years follows in the same sentence) |
| C274 | 22.2 cases per 100,000 youths per year in 2017-2018, with an annual rate of increase of 2.02% | exact (source uses a middle dot in the numbers) |
| C050 | restoration of clinically significant C-peptide production (>0.5 ng/ml or >0.17 nmol/l) | exact |
| C050 | documentation of an increase over pretransplant measurement of C-peptide | exact (optimal, good and marginal tiers each contain it) |
| C050 | Thus, levels of C-peptide should be measured prior to transplantation in order to determine posttransplant graft function. | exact |

Facts re-checked in the texts: C020 14% post-test probability at 0.7% prevalence, no "20%" anywhere; C025 40.3% from 2.2%, n=177 after 2 y, CV 31%, "2 h after their home evening meal"; C033 0.22 gives 96.3%/85.7%, at 0.68 sensitivity 59.3% and specificity 90.5%, urine "collected 2 h after a standard lunch in the hospital"; C058 0.28 nmol/nmol 97%/88%, fasting 63%/84%, sample "sent to the laboratory same day or refrigerated overnight", home collection only suggested in the discussion; C274 totals are 2002-2018; C186 17.2% / 14.8% / 2.8% / 40.5% / 54.5%; C050 thresholds and "work in progress" wording. Not re-checked by me: C186 AUC figures and the 16-19% positive-test rate, C274 age counts 179/341/445/194 (FT14 says no table in the stored text), C250/C283/C299/C273/C309 numbers beyond the quotes.

## 2. Score-proposal verdicts

Current-value check: I listed the U/V entries by row and dimension in usecases/scoring/*.json.
- Row 10 D1: V4 = 3 (medium) and V5 = 3 (medium) are the only entries; no U, S, R or RS file scores it. Two roles score the cell and both are 3, so `current` 3 is right.
- Row 7 D4: V3 = 2 (medium), the only entry. Row 33 D4: V10 = 1 (low); V13 is a problem report (suggests 2 for serum), not a score. Row 6 D4: U3 = 3 (corrected, low confidence). Row 6 D8: U2 = 3 (corrected, low confidence). U6 holds only problem reports for these cells. RS-D4 does not touch these rows.

| Row | Dim | Current | Proposed | Verdict | Evidence |
|---|---|---|---|---|---|
| 10 | D1 | 3 (V4, V5) | 4 (FT14, from both units) | Accept at 4, low confidence; the user decides. Apply to V4 and V5 together | C050 text: optimal, good and marginal tiers each contain "documentation of an increase over pretransplant measurement of C-peptide", and the conclusion says successful therapies "should require ... restoration of clinically significant C-peptide production (>0.5 ng/ml or >0.17 nmol/l)". Under clarification 15 the named decision is classifying the graft and no other test can substitute for the C-peptide component, which reads as a required result (4) rather than "determines but substitutable" (3). Caveats that keep this low: Igls calls itself "a work in progress [to] be validated", it is an opinion-leader consensus rather than a formal guideline (clarification 15 says "guideline"), and the same text scores D3 at 3 ("should be measured", "is critical"), so D1 4 beside D3 3 needs a one-line justification in the reason. V4's argument "no treatment action named" does not bar 4 because the row's decision is the classification. Clarification 29 does not apply (the Igls grade is used clinically, not only as a research endpoint) |
| 6 | D8 | 3 | none | Agree, no change | C250 and C283 test clinical models against a C-peptide or histology reference (C283 outcome is fasting C-peptide in youth), C299 has no C-peptide evaluation (quote verified). They do not touch the reclassification data behind the 3 (clarification 19). This is a correction candidate for the reason text only (see claim issues 6 and 7) |
| 6 | D4 | 3 | none | Agree, no change | C273 shows +32 to +82% mean bias for four of six routine assays and -6.0 to +1.2% after recalibration (FT13 numbers; the 24.5% CV is not in the paper, I could not check PMID 35177563). Chinese-market lots, so confidence stays at most medium under clarification 20; the existing 3 is already marked low |
| 7 | D4 vs 33 D4 (flag) | 7: 2; 33: 1 | none | Agree, no change from these papers. The inconsistency is real and belongs to a rescoring decision under clarification 25 | V3 scores row 7 at 2 "reflecting the timed protocol", which clarification 25 assigns to D5; V10 scores row 33 at 1 on a zero-hit US-availability search, which V13 already challenged. Under clarification 25 both rows name the same limiting assay (UCPCR), so they should be scored alike (row 7 with the blood C-peptide score in brackets). Nothing in C020, C025, C033 or C058 settles US availability |
| 6 | D4 (flag) | 3 | none | Agree | see above |
| 4, 5, 31 | D4 | 2, 2, 3 | none | Agree | C309 quote verified; 8 healthy adults, one platform, no low-concentration samples. Pre-analytical only |
| 7 | D2, D8, D3, D1, D7 | 3, 3, 3, 2, 3 | none | Agree | Papers do not replace the PMDI/ANZ basis. FT14's note that D3 = 3 is the corrected value of V1 is consistent with the V1 correction field (not re-read by me) |
| 33 | D2, D8, D4, D1, D5, D6, S | 2, 2, 1, 2, 2, 3, 2 | none | Agree | Row 33 D1 supporting quote "suggests that a genetic test might be appropriate" is not in C025 (paraphrase); keep the score, cite "Genetic testing is likely to be the only way of distinguishing MODY from type 2 diabetes" |
| 33 | D3 | 2 | none | Agree | C091 quote exact; ISPAD gives a suspicion feature at least 5 years after diagnosis, no measurement recommendation |
| 29 | D7 | 2 | none | Agree | C274 22.2 per 100,000 in 2017-2018, rise 2.02% a year: exact |

## 3. Claim-issue verdicts

"Score-reason" items are corrections of the reason text in the V*/U* JSON, not of the score or confidence.

| # | Unit | Where | Verdict | Check and reasoning |
|---|---|---|---|---|
| 1 | FT13 | usecases-verified.md line 50, "cut-offs 0.2-0.28" | Reword | Confirmed: 0.7 (C025, children over 2 y), 0.22 (C033, where 0.68 gave sensitivity 59.3% and specificity 90.5%), 0.28 nmol/nmol (C058, read in full text by FT14, so FT13's "abstract, not checked" is now resolved), 0.2 (C020, adults over 5 y). FT13's "0.7 gave 59%" should read 0.68, the value in the C033 text. See Apply 4 |
| 2 | FT13 | line 50 "Home 2-h post-meal UCPCR" and V9 row 33 D2 reason | Reword | Home sample only in C025 ("2 h after their home evening meal"); C033 standard lunch in the hospital, MODY versus type 1 only; C058 collected for the study after lunch (home use only suggested). The "n=264 after 2 years" in the V9 reason is the whole cohort; the over-2-year result is n=177 in C025 (FT13's breakdown 120 type 1 / 57 non-type 1 is from the text I saw partly garbled; I confirm 177 and 120 type 1). See Apply 5. Score-reason part is a correction of V9 text |
| 3 | FT13 | V9 row 33 D8 reason, "Fasting C-peptide did worse than UCPCR in one cohort (sensitivity 63%)" | Reword (FT13's "not supported" is only half right) | The 63% is correct for PMID 32052124 (C058: fasting C-peptide 63%/84% against UCPCR 97%/88%), which V9 lists among its sources. It is contradicted by C033, where fasting C-peptide (0.62 ng/mL) had 93%/90% against UCPCR 96.3%/85.7%. So the sentence is true for one cohort and the cohorts disagree. Corrected reason text: "Cohorts disagree: fasting C-peptide had sensitivity 63% and specificity 84% against UCPCR 97%/88% in 80 Egyptian children with type 1 or type 2 diabetes (PMID 32052124, DOI 10.1007/s00431-020-03606-7, full text), but 93%/90% (AUC 0.967) against UCPCR 96.3%/85.7% (AUC 0.93) in 27 MODY and 42 type 1 children (PMID 25792383, DOI 10.1159/000375410, full text). No study compared UCPCR with antibodies or genetic testing." Score-reason correction only; D8 stays 2 |
| 4 | FT13 | row 7 "20% PPV" remark and V2 row 7 D2 reason | Reword (FT13's "in neither text" is true of C020/C025 but the figure is in PMDI) | The PMDI full text (C100) states "antibody/C-peptide biomarker pathway (PPV 20%)", and its table attributes it to Shields et al 2017: UK, diagnosed up to age 30, screened to antibody negative and urinary C-peptide positive (n = 216), "diagnostic yield was 51/216 (24%)", "positive predictive value of the pathway was 20%, negative predictive value 99.9%". So V2's "antibody-negative UCPCR-positive pathway, PPV 20 percent (project file)" is traceable to PMDI; the 14% (C020, assumed 0.7% prevalence) and 40.3% (C025, assumed 2.2% prevalence) are different, computed figures. This overrides FT14 claim 1's statement that the primary source is "not named" (it is, as Shields 2017; I did not read that primary paper and its PMID is not verified here). See Apply 1. V2 reason correction: replace "(project file)" with "(PMDI 2023, PMID 37794142, DOI 10.1038/s43856-023-00369-8, full text, citing Shields 2017)". Score unchanged |
| 5 | FT13 | U3 row 6 D4 reason, 24.5% / 5.7% attributed to PMID 36843403 | Confirmed (score-reason) | Neither figure is in C273 per FT13; U6 records the 24.5% / 5.7% as from PMID 35177563 ("verified" by U6), which I did not read. Proposed wording is within the paper. It is a correction of the reason text; D4 stays 3 (low) |
| 6 | FT13 | U2 row 6 D8 reason, PMID 39805939 | Confirmed (score-reason) | C299 quote exact; C-peptide recorded in 0.7% of cases (FT13 number, not re-grepped). Proposed wording stays within the paper. Reason text only; D8 stays 3 |
| 7 | FT13 | U2 row 6 D8 reason, AUC 0.95-0.98, PMID 38252849 | Confirmed (score-reason) | The range mixes the clinical-only model (0.95) and biomarker-augmented models (0.972-0.979); outcome is fasting C-peptide in youth. C283 quote exact. Reason text only |
| 8 | FT13 | D4 reasons rows 4, 5, 6, 31, PMID 40587435 | Confirmed (score-reason) | C309 limitation quote exact. FT13 itself says the unit labels look inconsistent and that it could not tell whether that is an error; I did not resolve that. Reason text only; scores stay |
| 9 | FT14 | usecases-verified.md line 24, "20% PPV ... could not be traced" | Reword (the primary source is named) | See claim 4. The figure was found; the nearest verified figure of 16-19% should stay as a separate, different measure (positive-test rate), not as a substitute. See Apply 1 |
| 10 | FT14 | line 24 sources: UCPCR PMIDs list and "ISPAD C-peptide wording unread" | Confirmed | C058 states "Differentiation between MODY type and T2DM was not performed"; the existing row text already quotes the ISPAD wording in the same cell, so "unread" contradicts it. See Apply 2 and 3 |
| 11 | FT14 | V1 row 7 D7 reason, "SEARCH 2017-2018 annual new youth cases 18,169 type 1 and 5,293 type 2" | Confirmed (score-reason) | C274: totals 2002-2018 (85 and 44 million person-years). The line is in usecases/scoring/V1.json line 8, not in usecases-verified.md or merged-conclusion.md (grep). Correction of the reason text; D7 stays 3 per FT14 (low confidence, bin 2 or 3). FT14's national estimate used a US population figure marked [recall]; I did not check it |
| 12 | FT14 | usecases-verified.md row 10 "no numeric threshold" | Confirmed | C050 gives ">0.5 ng/ml [>0.17 nmol/l]" in the functional goal and the conclusion. Note also that the marginal tier requires the documented increase too (the row says only "optimal"). See Apply 6 |
| 13 | FT14 | row 33 "Home 2-h post-meal UCPCR" and cut-offs, from C058 | Reword (merge with FT13 claims 1 and 2) | C058 home collection is only suggested in the discussion; the sample was collected for the study. "ISPAD uses at least 5 years" is verified. Covered by Apply 4 and 5 |
| 14 | FT14 | V8 rows 29 and 33 D7, age counts 179/341/445/194 | Confirmed as "unverified here" | C274 text has no table; I did not check them. Not an error finding; reason text can carry the label "not verified in the stored text". No file change proposed in the deliverables |
| 15 | FT14 | V18 row 35 D5/D6/S sources, V17 row 35 D1 (ANZ 2025) | Confirmed (score-reason) | FT14 reports no HOMA-IR, fasting insulin or C-peptide in the pregnancy text of C121 (keyword search by FT14; I did not repeat it). Reason text only; scores unchanged |

## 4. Apply

Only claim issues that touch usecases-verified.md are listed; merged-conclusion.md contains none of the affected wording (grep for UCPCR, Igls, 18,169, 5,293, 0.28, "numeric threshold" found only unrelated lines). Score-reason corrections (claims 3, 4, 5, 6, 7, 8, 11, 15) go to the JSON reason fields and are not listed here. Line numbers are those of usecases-verified.md today. Each OLD string occurs once on its line; I confirmed that by grep, but the table cells are long, so match on the quoted fragment only.

**Apply 1.** File usecases-verified.md, line 24 (row 7, caveats column).
OLD:
```
The '20% PPV' quoted in an earlier draft could not be traced; the nearest verified figure is a 16-19% positive-test rate at >=5% calculator probability (PMID 41086125, DOI 10.2337/dc25-1029, abstract).
```
NEW:
```
The 20% PPV is in the PMDI 2023 full text (PMID 37794142, DOI 10.1038/s43856-023-00369-8): PPV 20% for the antibody-negative, C-peptide-positive biomarker pathway (its table cites Shields et al 2017, UK, diagnosed up to age 30, urinary C-peptide positive, 51 of 216 tested had monogenic diabetes; the primary paper was not read), against PPV 40% (55% of cases missed) for a calculator probability above 25% and PPV 58% (63% missed) for traditional MODY criteria. Computed post-test probabilities from assumed prevalence are different figures: about 14% for HNF1A/4A MODY at UCPCR >=0.2 nmol/mmol in adults with diabetes >5 years (0.7% prevalence assumed; PMID 21270186, DOI 10.2337/dc10-1293, full text) and 40.3% for non-type 1 diabetes at UCPCR >=0.7 nmol/mmol in UK children with diabetes >2 years (2.2% prevalence assumed; PMID 23289766, DOI 10.1111/pedi.12008, full text). The 16-19% positive-test rate at >=5% calculator probability is a separate figure (PMID 41086125, DOI 10.2337/dc25-1029, abstract).
```

**Apply 2.** File usecases-verified.md, line 24 (row 7, sources column).
OLD:
```
UCPCR studies PMIDs 21270186, 23289766, 25792383, 32052124, abstracts
```
NEW:
```
UCPCR studies PMIDs 21270186, 23289766, 25792383 (MODY triage; full text) and 32052124 (DOI 10.1007/s00431-020-03606-7, full text; type 1 versus type 2 in already-diagnosed children, MODY not studied, so not a MODY-triage source)
```

**Apply 3.** File usecases-verified.md, line 24 (row 7, end of caveats column).
OLD:
```
ISPAD C-peptide wording unread
```
NEW:
```
ISPAD 2022 (PMID 36537518, DOI 10.1111/pedi.13426, full text) lists detectable C-peptide, blood or urine, at least 5 years after diagnosis, as one suspicion feature among several for monogenic diabetes; it gives no assay, threshold or recommendation to measure
```

**Apply 4.** File usecases-verified.md, line 50 (row 33, caveats column).
OLD:
```
cut-offs 0.2-0.28
```
NEW:
```
cut-offs are data-derived and not transferable: 0.7 nmol/mmol in UK children with diabetes >2 years (PMID 23289766, DOI 10.1111/pedi.12008, full text); 0.22 in 27 MODY and 42 type 1 Turkish children, where 0.68 gave 59% sensitivity (PMID 25792383, DOI 10.1159/000375410, full text); 0.28 nmol/nmol in 80 Egyptian children with type 1 or type 2 diabetes, MODY not studied and diagnoses not antibody- or gene-verified (PMID 32052124, DOI 10.1007/s00431-020-03606-7, full text); 0.2 in UK adults with diabetes >5 years (PMID 21270186, DOI 10.2337/dc10-1293)
```

**Apply 5.** File usecases-verified.md, line 50 (row 33, test column).
OLD:
```
Home 2-h post-meal UCPCR
```
NEW:
```
Post-meal (2 h) UCPCR: home sample after the evening meal, mailed to a UK reference laboratory (PMID 23289766, 264 patients, 177 with diabetes >2 years); hospital standard lunch in PMID 25792383 (no type 2 group); collected for the study after lunch in PMID 32052124
```

**Apply 6.** File usecases-verified.md, line 27 (row 10, caveats column).
OLD:
```
it gives no numeric threshold for "clinically significant" C-peptide;
```
NEW:
```
its functional goal and conclusion give a minimum of above 0.5 ng/mL (0.17 nmol/L) as clinically significant C-peptide, while the optimal, good and marginal tier definitions each require a documented rise over the pretransplant value (PMID 29453879, DOI 10.1111/tri.13138, full text); the authors call the classification a work in progress to be validated;
```

No confidence figure changes in any of these edits. I did not run the Apply edits.

## 5. Could not be read or checked
- PMID 35177563 (24.5% / 5.7% survey) and Shields 2017 (primary source of PPV 20%) were not read.
- C274 age counts and appendix numbers: no table in the stored text.
- C025 and C033 are PDF extractions with interleaved columns; no number was called wrong because of garbling. FT13's 120 type 1 / 57 non-type 1 split for the over-2-year group is only partly visible in the garbled text (177 and 120 seen).
- PMID/DOI pairs for papers not already in usecases-verified.md were not re-checked against PubMed or Crossref, and no retraction or correction check was run.
- Conflict-of-interest statements: not found in the extracted text, not shown to be absent.
