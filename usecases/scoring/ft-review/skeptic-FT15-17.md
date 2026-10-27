# Skeptic review of FT15, FT16 and FT17

Reviewer: skeptic. Method: every quote and number re-checked by script and grep against `corpus/fulltext/<ID>.txt` (whitespace, hyphen and dash normalised); rubric and score files re-read. No web, no git. Nothing here is applied; each score proposal is a recommendation for the user.

Limits stated up front:
- `corpus/fulltext/C098.txt` (hyperinsulinism guideline) has no tables and no figures. The text has zero hits for "peptide" (any spelling) and for "less definitive", so Table 1 thresholds, C-peptide use and the "less definitive" criteria could not be checked. Rec 1.1 and Rec 1.4 are present as section headings with their text; their grade circles are in the headings.
- `C004` and `C008` are PDF extractions (two columns, Greek letters lost, no ID header). Identifier matching for them rests on the JSON (the journal strings in the extract are consistent). Their numbers were checked only where lines read cleanly.
- `tools/check_citations.py` was not run (tool budget). Retraction and correction status is therefore unchecked for all 21 papers. PMID and DOI in the `corpus/fulltext` headers match the JSON for 19 of 21 (C004 and C008 have no header).

## 1. Quote table

All 21 paper quotes found except one, which is an extraction artefact.

| Paper | Result | Note |
|---|---|---|
| C052, C068, C111, C224, C253, C271, C302 | exact | |
| C098 | exact | Rec 1.4 body sentence ("possibility of an insulinoma should be considered"), not a numbered recommendation sentence |
| C204, C321, C029, C226, C278, C011 | exact | |
| C004 | exact | |
| C008 | extraction artefact | "has the highest accuracy and predictive value in classifying KPD patients" is present but split by the two-column layout ("...classi-" / "fying KPD patients..."), line 35 |
| C230, C246, C063, C104, C285, C306 | exact | |

Proposal quotes (where the proposal quote differs from the paper quote): row 24 D3 and D8 (C098) exact; row 32 D8 (C011) exact; row 47 D3 (C063, "C-peptide measurement should drive the decision-making process for the choice of LADA treatment.") exact. Other `proposals` entries in FT15 and FT17 (no change proposed) list several quotes under a `papers` list that only occur in one of the listed papers; the quote is from the first matching paper and is exact there.

## 2. Score-proposal verdicts

Current values: every cell below is scored by exactly one entry in the U*/V* files. A search of all `U*.json` and `V*.json` for these row and dimension cells found no second role, no `original_score` and no `correction` on them. V13 (skeptic) and V6 (skeptic) already asked for the row 24 D8 and row 32 D8 downgrades; neither was applied.

| Row, dim | Current (entry) | Proposed | Verdict | Evidence |
|---|---|---|---|---|
| 24 D3 | 3 (V8 only) | 2 | ACCEPT 2 | Rec 1.4 text read: "In children older than 2 years of age with acquired HI, the possibility of an insulinoma should be considered"; it names the condition but no test (clarification 5: condition named, not the test, is 2). Rec 1.1 is the measurement recommendation (insulin, "should be measured using a high-sensitivity assay", at spontaneous or fasting-induced hypoglycaemia) but it is written for HI diagnosis generally, with neonatal worked examples, so under clarification 14 it is a broader population and scores 2. Not checked: Table 1 and any C-peptide statement (not in the stored text); V8's own reason already says C-peptide is not named. |
| 24 D8 | 3 (V9 only; reads the abstract only) | 2 | ACCEPT 2 | The Rec 1.1 text says: "the focus should be on the markers of insulin action, not the insulin level itself" when insulin and ketone/glucagon markers disagree, so the guideline text does not make insulin the decisive step. No reclassification data are cited by V9 ("No reclassification data"); clarification 19 caps mechanism at 2. |
| 32 D8 | 3 (V2 only) | 2 | ACCEPT 2 | C008 comparator AUCs read: 0.972 versus 0.707, 0.703, 0.766, so the accuracy gap is real; but the outcome (peak glucagon C-peptide at least 1.5 ng/mL at 12 months, C008 lines 28 and 85-89) is the same test that sets the scheme's function axis, and C011 (same group) says "although the cutoffs noted above do not independently predict the potential for successful and safe withdrawal of insulin" (line 163). Clarification 19 needs data that the measurement changes the answer for the named decision (insulin withdrawal); not shown. V6 reached the same conclusion on the abstract. Confidence low is right (PDF text, C004 group table garbled). |
| 47 D3 | 1 (V1 only) | 3 | ACCEPT 3 (confidence low, fallback 2) | C063 lines 77-79 read: "The panel recommends measurement of serum (plasma) C-peptide levels ... in islet-cell related autoantibody-positive patients", "in case of treatment failure, C-peptide measurement should be repeated to identify progression to insulin deficiency and the need for insulin treatment", and tiers <0.3, 0.3-0.7, >0.7 nmol/L. This is an international expert panel consensus (title: "A Consensus Statement From an International Expert Panel") that covers the use-case population (autoantibody-positive slowly progressive diabetes) and the progression decision, so clarifications 6, 13 and 14 give 3; V1 scored only the Japanese criteria and ADA 2026. Limits: the paper says there are no LADA guidelines; its tiers (0.3 nmol/L) and sample conditions (fasting, random or postprandial, glucose 80-180 mg/dL) are not the 0.6 ng/mL fasting criterion of the row; the LADA definition (no insulin for at least 6 months) only overlaps the Japanese definition. Consequence the user should decide: the row 47 status is "Limited"; a quoted consensus recommending the test for the decision would allow "established" under the status rule, but the row's threshold is not what the panel recommends, so keeping "Limited" with the added source is defensible. |

## 3. Claim-issue verdicts

Score-file reasons (V*/U* JSON text) are corrections of the reason text, not of the score. Rows marked "reason text" below do not touch `usecases-verified.md` or `merged-conclusion.md`.

| Unit, issue | Target | Verdict | Check and reason |
|---|---|---|---|
| FT15 #1, row 24 Rec 1.4 names insulin and C-peptide | usecases-verified.md line 41 (tests and sources columns) | REWORD | Confirmed: Rec 1.4 text names no test; Rec 1.1 is the insulin measurement; "peptide" has 0 hits in C098. Proposed text lacks the DOI and says Rec 1.1 covers "children generally" (the text says "HI" and uses neonatal examples). Corrected wording in Apply 1 and 2. The row 24 status "Established (guideline recommendation, low-quality evidence)" is not edited here; the user should decide whether it still stands, since the only recommendation that names a test (Rec 1.1) is the general HI one. |
| FT15 #2, row 4 Table 1 thresholds | usecases-verified.md line 21 | REWORD | Confirmed that C-peptide, "less definitive", 1.25 uU/mL and 0.5 ng/mL are absent from the stored text (cannot be checked, not shown wrong). The proposed claim that they are "recorded from the published table" cannot be verified here, so use an uncertainty label only (Apply 3). |
| FT15 #3, row 10 Igls 2.0 | usecases-verified.md line 27 | REWORD | C068 line 86 and Table 2: composite where "Clinical outcome would encompass glycemic control and hypoglycemia and be sufficient for defining treatment success"; good function = ">0.5 (0.17) stimulated, >=0.2 (0.07) fasting" ng/mL (nmol/L); "the herewith-proposed Igls 2.0 criteria are only preliminary ... reconvene for another workshop". "It is not adopted" is not in the paper; use "no adopted version found". Added PMID and DOI (Apply 4). |
| FT15 #4, row 10 cites the 10-patient TPIAT series | usecases-verified.md line 27 (sources) | REWORD | C111 text has 0 hits for "Igls" and for any pre-operative C-peptide; row 27 (line 44) already cites PMID 38895780, so no new row 27 entry is needed. C253 line 70 supports the replacement: "using fasting C-peptide in the absence of a stimulated value may risk over-estimating islet graft failure"; "In 248 patients ... 57 (23%) had fasting C-peptide <=0.5 ng/mL but stimulated C-peptide >0.5 ng/mL". Proposed wording lacked DOIs and its "over-call" phrase should follow the paper's "may risk over-estimating" (Apply 5). Measure type: MMTT-stimulated versus fasting C-peptide, in total pancreatectomy with islet autotransplant (autologous), not allotransplant. |
| FT15 #5, C224 reference measurement system | reason text of V3 row 31 D4 (and row 32 D4 source list); not in usecases-verified.md or merged-conclusion.md (grepped for reference measurement, recalibration, harmonisation, JCTLM: no hit) | REWORD (reason text only) | C224 confirmed: serum-based secondary calibrators greatly reduced variability; two listed ID-LC/MS procedures with a discrepancy under investigation (line 56); recalibration asked of manufacturers (line 21). "disagree most at higher concentrations" has no hit in C224, but V3 cites five other sources for that sentence (PMID 18420730, 37141618, 38549041, 35177563, 40587435) that were not read here, so the phrase is not shown wrong, only not traceable to C224. Reword the sentence "A reference measurement system exists, but ..." to: "A reference measurement system for C-peptide was being implemented in 2017 (PMID 28646033, DOI 10.1373/clinchem.2016.269274, full text: two listed ID-LC/MS procedures, no listed serum certified reference material, recalibration to serum-based calibrators reduced between-method variability; whether manufacturers completed it is not stated); the claim that methods disagree most at higher concentrations is not in this paper." Score unchanged. |
| FT16 #1, row 32 "not within ~2 weeks" has no support | usecases-verified.md line 49 | REWORD (not reject, but not as proposed) | The issue is wrong that the full texts do not support a 2-week delay: the row's caveat comes from Holt 2021 (C074) and ADA Standards 2026 (C127), both of which say "Do not test C-peptide within 2 weeks of a hyperglycaemic emergency" (verified verbatim). What is true: C008 line 131 gives the Houston glucagon test "within 2 weeks of resolution of the index DKA episode" and C011 line 162 advises "generally 1-3 wk after resolution of ketoacidosis", so the cohort practice differs from the ADA rule and the clock starts at a different event. FT16's proposed "within about 1 to 2 weeks" would contradict ADA. Corrected wording in Apply 8. The V3 row 32 D4 reason phrase "weeks to months after the DKA episode" is a reason-text point: "months" is not in any of these sources; replace by "about 2 weeks or more after the episode (ADA 2026, Holt 2021) or 1-3 weeks after resolution (review)". Score unchanged. |
| FT16 #2, row 32 cohort shows function, not safe withdrawal | usecases-verified.md line 49 (evidence cell and caveat) | REWORD | Confirmed: outcome is C-peptide-defined (C008 lines 28, 85-89); C011 line 163 quote verified; fasting C-peptide to glucose ratio >11 predicts withdrawal among beta-positive patients (C011 lines 163 and 180, citing ref 23, not read). "31% withdrawn from insulin" in C008 line 216 is a partial hit ("31% of our cohort who presented ..."), not fully read. The sources cell still says "abstract" for three papers now read in full; Apply 6 and 7 update read levels and add DOIs. |
| FT16 #3, row 31 "Likelihood ratios ~2" understates Funakoshi | usecases-verified.md line 48 | REWORD | C029 table line 31 reads likelihood ratios 2.0, 2.1, 1.6, 2.3, 2.8 for five fasting or glucagon-stimulated indices; AUC 0.69-0.75 per FT16 (AUC not re-read). But the "~2" in the row 31 caveat follows the Jones 2013 sentence and is not shown to be about Funakoshi, so do not replace it; instead add the Funakoshi numbers and measure type to the Funakoshi evidence text (Apply 9). |
| FT16 #4, V8 row 24 D7 "country not stated" | reason text of V8 row 24 D7 | CONFIRMED (reason text only) | C321 lines 16-17: Children's Hospital of Philadelphia Congenital Hyperinsulinism Center, 2006-2024; line 30: ages 2-26, mean and median 13; 23 patients (line 41). 23 over 18 years is about 1.3 per year. Wording to use in the reason, with identifiers: "One US academic hyperinsulinism centre (Philadelphia) treated 23 patients aged 2 to 26 with insulinoma between 2006 and 2024 (about 1 per year; PMID 42149805, DOI 10.1159/000552145, full text); the share of US cases it sees is not stated." Score unchanged (low confidence stays). |
| FT16 #5, V1 row 31 D7 "40% of adults with new type 1 diabetes" cited to C278 | reason text of V1 row 31 D7 | REJECT | V1 attributes the figure to ADA Standards 2026, and the stored ADA text (C127 line 88) says: "misdiagnosis can occur in up to 40% of adults with new type 1 diabetes". The V1 wording is therefore accurate for its cited source. C278 differs ("adults older than 30 years with type 1 diabetes", prevalent), which is a note for anyone who cites C278, not a correction of V1. |
| FT17 #1, V1 row 47 D7 "2-12% of adult-onset diabetes" | reason text of V1 row 47 D7 | REWORD (reason text only) | C063 line 10: "account for 2-12% of all patients with diabetes", lower in primary care than secondary care; 7-14% in Northern Europe and China versus African American and Hispanic individuals. Confirmed. The V1 chain applies this share to new adult diagnoses, which is an assumption to state. Wording: "LADA accounts for 2-12% of all patients with diabetes (international expert panel consensus, PMID 32847960, DOI 10.2337/dbi20-0017, full text), lower in primary care and in African American and Hispanic individuals than in Northern Europe and China; applying the share to new adult diagnoses is an assumption." Score unchanged. |
| FT17 #2, row 47 should cite C063 | usecases-verified.md line 64 | CONFIRMED with edits | Content verified (see 2, row 47 D3). Needs measure type, panel's own "no guidelines" statement, and the Japanese criterion DOI (10.1111/jdi.14121, matches C104). Row 6 (line 23) already cites Buzzetti 2020, PMID 32847960. Status is not changed (Apply 10). No statement in merged-conclusion.md about row 47 or LADA international sources was found. |
| FT17 #3, V2 row 47 D2 "9.1 percent" | reason text of V2 row 47 D2 | CONFIRMED (reason text only) | C306 line 31: undetectable C-peptide at 5 years 9.1% (n = 7) and at 10 years 16.4% (n = 10) in slowly progressive; line 33: "At 5 years after onset, 41.3% of participants with SP T1D had developed insulin dependency, increasing to 57.9% at 10 years" with insulin dependency defined by F-CPR <0.6 ng/mL (quote verified). C285 line 10 states it is part of TIDE-J, same registry as C306, so not independent. Wording: "In TIDE-J (PMID 40509916, DOI 10.2337/dc25-0579, full text; 105 slowly progressive cases), fasting C-peptide <0.6 ng/mL (insulin dependency) was reached by 41.3% at 5 years and 57.9% at 10 years; undetectable C-peptide (<0.03 ng/mL) by 9.1% and 16.4%. The 60-patient study (PMID 38451108, DOI 10.1111/jdi.14178) is drawn from the same registry." Score unchanged. |
| FT17 #4, V2 row 47 D8 "56-72 to 77-84 percent" | reason text of V2 row 47 D8 | CONFIRMED (reason text only) | C285 line 38: RIA-GADA 56.3% to 70.0% (high titre) and 81.0% with fasting C-peptide, 76.9% with age, 84.2% with BMI; ELISA 73.1% high titre and 79.0% with fasting C-peptide, 81.8% age, 82.4% BMI. The table (line 39) shows IA-2A combinations at 75.0 and 73.3, below the "77" lower bound, so V2's range is not exact for IA-2A. NPV 55.6% (RIA, F-CPR) and 42.9% (ELISA, F-CPR) support "NPV 43-56%". Wording: "Adding fasting C-peptide <1.41 ng/mL to high-titre GADA raised PPV from 70.0 to 81.0% (RIA) and from 73.1 to 79.0% (ELISA), about the same as age or BMI; NPV 43-56%; n=60 (PMID 38451108, DOI 10.1111/jdi.14178, full text)." Score unchanged. |

Not traced: the ADA 2026 and Holt 2021 texts were read only for the quoted sentences; ENETS 2016, Jones and Hattersley 2013 and the five V3 row 31 D4 sources were not read; C011 reference 23 (fasting C-peptide to glucose ratio >11) was not read.

## Apply

Only changes to `usecases-verified.md` are listed (no confirmed or reworded issue touches `merged-conclusion.md`; it was grepped for the affected terms and for C098, C008, 17130187, 14602731 and found no occurrence). Each OLD string occurs once in the named file, on the line stated (checked with fixed-string grep). Strings 3, 4, 5, 6, 7, 8 and 9 are in different cells or non-overlapping parts of the same cell. No confidence figure or score is changed.

### Apply 1: usecases-verified.md line 41 (row 24, tests column)

OLD:
```
Insulin and C-peptide at hypoglycaemia as in row 4, then insulinoma/MEN1 work-up
```
NEW:
```
Insulin (high-sensitivity assay) at spontaneous or fasting-induced hypoglycaemia with BOHB, FFA and glucagon response (Rec 1.1, general HI diagnosis); C-peptide as in row 4 (not named in the stored guideline text, which lacks tables); then insulinoma/MEN1 work-up (Rec 1.4 names no test)
```

### Apply 2: usecases-verified.md line 41 (row 24, sources column)

OLD:
```
HI guideline Rec 1.4, PMID 37454648, full text (Grade 1, low-quality evidence; skeptic). ENETS 2016 for MEN1 clue
```
NEW:
```
HI guideline, PMID 37454648, DOI 10.1159/000531766, full text (PMC11124746; stored copy lacks tables). Rec 1.4 (Grade 1, low-quality evidence) recommends screening children whose hyperinsulinism begins after age 2 years for insulinoma and directing genetic work-up for MEN1; it names no biochemical test. Measurement of insulin (high-sensitivity assay) at hypoglycaemia comes from Rec 1.1 (Grade 1, moderate-quality evidence), which covers hyperinsulinism diagnosis generally (worked examples are neonatal); full-text check in FT15. ENETS 2016 for MEN1 clue
```

### Apply 3: usecases-verified.md line 21 (row 4, caveats column)

OLD:
```
C-peptide >0.5 ng/mL (>0.17 nmol/L); Rec 1.1 is Grade 1, moderate.
```
NEW:
```
C-peptide >0.5 ng/mL (>0.17 nmol/L) (Table 1 values and the phrase "less definitive" are not in the stored text copy, which lacks tables, and could not be re-checked in FT15; C-peptide is not mentioned anywhere in the stored text); Rec 1.1 is Grade 1, moderate.
```

### Apply 4: usecases-verified.md line 27 (row 10, caveats column)

OLD:
```
Igls 2.0 document not found
```
NEW:
```
No adopted Igls 2.0 document found; a preliminary Igls 2.0 is proposed in the 2021 IPITA symposium report (PMID 34061967, DOI 10.1210/clinem/dgab386, full text read in FT15): treatment success would rest on glucose regulation and hypoglycaemia alone (HbA1c or CGM metrics, severe hypoglycaemia), and C-peptide (absolute thresholds, good function: stimulated >0.5 ng/mL or fasting >=0.2 ng/mL) would only grade graft function; the authors call the criteria preliminary and propose reconvening a workshop.
```

### Apply 5: usecases-verified.md line 27 (row 10, sources column)

OLD:
```
Igls report 2021, PMID 34061967, abstract. TPIAT series, PMID 38895780, abstract
```
NEW:
```
Igls report 2021, PMID 34061967, DOI 10.1210/clinem/dgab386, full text (FT15). TPIAT graft grading (Auto-Igls, autologous islets, MMTT-stimulated versus fasting C-peptide): PMID 33020957, DOI 10.1111/tri.13762, full text (FT15; in 248 patients with both measures, 57 (23%) had fasting C-peptide <=0.5 ng/mL but stimulated >0.5 ng/mL, so fasting alone may over-estimate graft failure). The 10-patient paediatric TPIAT series (PMID 38895780, DOI 10.1111/petr.14813) reports post-operative MMTT C-peptide only, has no Igls grading, and is cited under row 27, not here
```

### Apply 6: usecases-verified.md line 49 (row 32, sources column)

OLD:
```
Balasubramanyam 2006, PMID 17130187, abstract. PMID 18292467, abstract. PMID 14602731 title only
```
NEW:
```
Balasubramanyam 2006, PMID 17130187, DOI 10.2337/dc06-0749, full text (FT16; PDF extraction, comparator AUCs read). PMID 18292467, DOI 10.1210/er.2007-0026, full text (FT16; narrative review by the same group). PMID 14602731, DOI 10.1210/jc.2003-030180, full text (FT16; PDF extraction, group table not read)
```

### Apply 7: usecases-verified.md line 49 (row 32, caveats column, evidence part)

OLD:
```
One prospective cohort (n=294); mostly single-centre cohorts in specific populations
```
NEW:
```
One prospective cohort (n=294) shows that autoantibodies plus fasting or glucagon-stimulated C-peptide predict beta-cell function at 12 months (AUC 0.972 against 0.70 to 0.77 for three other schemes); the outcome is itself defined by glucagon-stimulated C-peptide (peak at least 1.5 ng/mL), so this is not a test of C-peptide-guided withdrawal. A review by the same group says the fasting and glucagon C-peptide cut-offs "do not independently predict the potential for successful and safe withdrawal of insulin"; mostly single-centre cohorts in specific populations
```

### Apply 8: usecases-verified.md line 49 (row 32, caveats column, timing part)

OLD:
```
not within ~2 weeks of the acute episode
```
NEW:
```
not within ~2 weeks of the acute episode (ADA Standards 2026 and Holt 2021: "Do not test C-peptide within 2 weeks of a hyperglycaemic emergency"; the Houston cohorts tested within about 2 weeks of resolution of the DKA episode, and a review by the same group advises generally 1 to 3 weeks after resolution of ketoacidosis, so the sources differ in both interval and starting point)
```

### Apply 9: usecases-verified.md line 48 (row 31, sources column)

OLD:
```
Funakoshi 2011, PMID 24843502, abstract (201 Japanese T2D patients: who needs insulin to reach target, not safe withdrawal; a weak match for "predicting success of stopping insulin")
```
NEW:
```
Funakoshi 2011, PMID 24843502, DOI 10.1111/j.2040-1124.2010.00096.x, full text (FT16; 201 Japanese T2D inpatients: who needs insulin to reach target, not safe withdrawal; fasting and glucagon-stimulated C-peptide indices, AUC 0.69 to 0.75, likelihood ratios 1.6 to 2.8, best index (C-peptide index) 2.8; not random C-peptide; a weak match for "predicting success of stopping insulin")
```

### Apply 10: usecases-verified.md line 64 (row 47, sources column)

OLD:
```
PMID 38184802 (PMC10804889), full text read by skeptic; Diabetol Int copy PMID 38264233 not read
```
NEW:
```
PMID 38184802, DOI 10.1111/jdi.14121 (PMC10804889), full text read by skeptic; Diabetol Int copy PMID 38264233 not read. International LADA expert panel consensus (Buzzetti 2020, PMID 32847960, DOI 10.2337/dbi20-0017, full text; the paper states there are no guidelines for LADA management) recommends C-peptide measurement (fasting, random or postprandial, with concurrent glucose 80-180 mg/dL) in islet autoantibody-positive patients and repeat measurement at treatment failure to identify progression to insulin deficiency, with tiers <0.3, 0.3-0.7 and >0.7 nmol/L; these differ from the Japanese fasting 0.6 ng/mL criterion (FT17)
```

Tool calls used: 29 (including this write).
