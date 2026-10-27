# Skeptic review of full-text score reviews FT11 and FT12

Reviewer: skeptic (written 2026-10-26). Inputs: `usecases/scoring/ft-review/FT11.json`, `FT12.json` and their reports; local texts `corpus/fulltext/<ID>.txt`; `usecases/scoring-rubric.md`; `usecases/scoring/U*.json`, `V*.json` (S*.json are screener files, listed for information only); `usecases-verified.md`; `merged-conclusion.md`. No web, no git.

Method notes and assumptions
- Quotes were matched after collapsing whitespace and line breaks. C014 is a two-column PDF extraction: a sentence that continues from one column to the next is interleaved line by line, so a straight string match fails; I found each C014 quote by grepping its fragments and reading the adjacent lines (line numbers below). Table 3 of C014 is scrambled and I did not use it.
- "Current" score = the score in force under the rule "later files and corrections win". Where several roles score the same cell I list them all; I did not check how `ranking.md` combines roles.
- Where I write "not read" I mean I did not open that source. C080 (partial text, no abstract or tables) and C014 Table 3 could not be read for numbers.
- Score proposals are recommendations for the user; nothing is applied here.

## 1. Quote table

| Paper | Quote (first words) | Result |
|---|---|---|
| C014 | "The diagnosis of an insulinoma requires convincing clinical and biochemical evidence before any attempt to regionalize or localize the tumor" | Found, column-interleaved (lines 536-538). Exact wording. |
| C039 | "a subset of patients with insulinomas may be diagnosed on the basis of an altered insulin secretory pattern during OGTT" | Exact. |
| C107 | "Accuracy was not assessed for insulin measurements, because there is no reference measurement procedure available." | Exact. |
| C227 | "three cases of insulinoma, one case of hyperinsulinism" | Exact. |
| C264 | "Factitious hypoglycaemia was diagnosed in 11 patients corresponding to a prevalence of 16%." | Exact. |
| C035 | "Not all commercially available insulin assays measure the insulin analogues" | Exact. |
| C272 | "The possibility of exogenous administration of insulin should not be ruled out on the basis of undetectable insulin" | Exact. |
| C292 | "Roche Elecsys assay does not exhibit any cross-reactivity with any insulin analogues, but they are picked up with Abbott analyser." | Exact. |
| C026 | "Mechanisms to correct for renal function when measuring C-peptide have been suggested, but are currently poorly validated" | Exact. |
| C074 | "Where a person is treated with insulin, this test should always be performed prior to insulin discontinuation to exclude severe insulin deficiency." | Exact. |
| C080 | "inter-measurement system %CVs ranging from 10.7% to 58.3% for insulin and from 20.1% to 31.6% for C-peptide" | Exact (line 45). |
| C127 | "Where a person is insulin treated, C-peptide must be measured prior to insulin discontinuation to exclude severe insulin deficiency." | Exact (line 91, figure note). |
| C169 | "The cause of diabetes was reclassified in 58 individuals (6.8% of the tested cohort)." | Exact. |
| C216 | "most (n = 57, 66%, Figure 2) were misclassified as having type 1 diabetes and were producing substantial endogenous insulin" | Exact. |
| C231 | "the estimated prevalences of diagnosed type 1 and type 2 diabetes were 0.55% (corresponding to 1.3 million U.S. adults)" | Exact. |
| C239 | "Type 1 diabetes: Insulin treatment within <=3 years ... non-fasting C-peptide <200 pmol/L" | Found (symbol "<=" printed as a single character). |

Proposal quotes (FT11 and FT12): every proposal quote is present in at least one of the papers it cites. Those listed with two or three papers occur in only one of them (for example FT12 row 31 D5 quote is in C074, not in C026); that is harmless but the `papers` lists overstate support. C014 proposal quotes sit at: "requires convincing ..." 536-538; "should undergo a mixed-meal test" 439-440; "standards for the interpretation ... have not been established" 446-447; "An oral glucose tolerance test should never be used" 444-445; "must rely largely on clinical experience" 237-238; "Endogenous insulin secretion is suppressed appropriately in nonislet cell tumor hypoglycemia" 345-346. No quote is missing and none is a paraphrase.

Numbers I checked in the texts and found as stated: C014 thresholds (lines 74-83: glucose <55 mg/dL, insulin >=3 U/ml with the micro sign lost, C-peptide >=0.6 ng/ml, proinsulin >=5.0 pmol/L, BOHB <=2.7, glucagon rise >=25 mg/dL), "1QQQE" attached to Rec 2.1 (lines 46-49), 5-h mixed meal sampled every 30 min to 300 min and insulin/C-peptide/proinsulin sent only when glucose <60 mg/dL (lines 581, 596-599); C039 18%, 90-100%, <5-10%; C107 13.4%/22.2% (84 measurements), 10.8%, bias 5.2%; C227 1082 per 100,000, 3856 events, three insulinoma and one hyperinsulinism, "about one million inhabitants"; C080 inter-lab 13.6-21.8% and 8.4-64.3%, inter-system 20.1-31.6% and 10.7-58.3%, 58.3% to 44.1% after recalibration, intra-system 4.8% and 6.6%; C169 equation and Roche 269 (lines 240, 245); C231 1.3 million, 5.8% and 90.9% (printed); C127 "up to 40%". Not traced to a source I read: C264 "6% insulinoma share" (no such figure in the text; Figure 1 only), C080 "24.5% and 5.7%" (zero hits for "24.5" and "5.7%" in the local text), the Holt "11% reclassified" (not in C169; I did not read the Holt reference list for it), C264 binomial interval (reader's recall, not in the paper).

## 2. Score-proposal verdicts

FT11 (row, dimension, current in force, proposed).

| Row, dim | Current (entries) | Proposed | Verdict | Evidence and rule |
|---|---|---|---|---|
| 1 D1 | 3 (V11 corrected 4 to 3; V12 corrected 4 to 3; S4 screener 3) | 4 | Accept at 4 (confidence medium) | The guideline text says the diagnosis "requires convincing clinical and biochemical evidence before any attempt to regionalize or localize", and the Rec 2.1 bullet makes localisation conditional on "documented fasting or postprandial endogenous hyperinsulinemic hypoglycemia" (lines 77-79). Clarification 15 gives 4 when a guideline requires the result before the decision; the earlier correction (V13) rested on the text being read as only "measure". Caveat: the sentence is in the remarks, and "biochemical evidence" includes glucose, BOHB and glucagon response, but insulin/C-peptide is the evidence that documents hyperinsulinism and proinsulin/BOHB do not substitute for it. |
| 1 D3 | 3 (V8; S4 screener 4) | 4 | Accept at 4 (confidence low to medium) | Clarification 13 asks for a guideline that says the test must be done before the decision named; the same sentence meets that, and D1 and D3 should move together or the file contradicts itself. Weakness the user should weigh: it is remark text, not the numbered "we recommend" (1QQQE), and it says "biochemical evidence" rather than naming insulin. If the user keeps 3 on D3, keep 3 on D1 as well. |
| 5 D3 | 2 (U1; S1 screener 2) | 3 | Reject (keep 2) | The sentence that recommends the mixed-meal test ("The patient with a history suggestive of postprandial hypoglycemia should undergo a mixed-meal test") does not name bypass patients; bypass appears only as a cause (lines 290-292, 390-392) and as a calcium-stimulation candidate. Clarification 14 allows 3 only if the text covers the use-case population explicitly for the measurement, which it does not. |
| 21 D3 | 2 (V14; S2 screener 2) | 3 | Reject (keep 2) | "Endogenous insulin secretion is suppressed appropriately in nonislet cell tumor hypoglycemia" is a description, not a recommendation to measure insulin in this population; the general Rec 2.1 covers adults with unexplained hypoglycaemia (a broader population, clarification 14 gives 2). I could not read Table 3 (scrambled), so the "IGF-mediated column" cannot support a change. |
| 48 D1 | 1 (V24, primary care physician; S3 screener 1). V23 gave 0 but V24 is later | 1 | Reject as a change: the value in force is already 1 | The reader read only V23 (0). The Cryer sentence ("Current clinical usage is to apply the above criteria developed under fasting conditions to the results from a mixed-meal challenge") is a usage statement; V24's reasoning (the named decision is confirmation of low glucose, insulin adds counselling at most) is unaffected. Two roles disagree (0 and 1); the later one governs. |
| 1 D2 | 3 (V9, corrected; S4 3) | none | Accept (no change) | Text: recommendations "must rely largely on clinical experience", moderate quality only against a much less thorough work-up (lines 237-245), but anchor 3 (guideline backed by studies) is still met by the cited case series; 2 is arguable, as the reader says. |
| 23 D3 | 0 (V8 corrected 2 to 0; S2 screener 2) | none | Accept (no change) | "An oral glucose tolerance test should never be used for the evaluation of suspected postprandial hypoglycemia" (lines 444-445) is a recommendation against in the US-setting guideline; ENETS is narrative. Caveat: it concerns suspected postprandial hypoglycaemia in general, not specifically insulinoma after a negative fast. The V8 correction note ("seen in a search excerpt, not full text") is now out of date (reason-text only). |
| 22 D3 | 2 (V8; S4 2) | none | Accept (no change) | C039 line 57: "positive in 90-100% of cases [126;127] and therefore should be considered in a patient where other imaging tests are negative". "Should be considered" is option level. |
| 1 D4 | 2 (V10) | none | Accept (no change) | C107 line 46: no reference measurement procedure for insulin; its figures are LC-MS/MS research imprecision, not immunoassay disagreement (rule 20). |
| 3 D4 | 1 (V3 corrected 2 to 1 via RS-D4) | none | Accept (no change) | The limiting assay is the drug-screen send-out (clarification 25); C107's 22.2% does not change that. |
| 2 D4 | 2 (V10 2) | none | Accept (no change) | C035 states the analogue caveat; C272 and C292 are single cases (C272 confounded by a simultaneous insulin change). |
| 4 D1 | 2 (V4 2, V5 2; S4 screener 3) | none | Accept (no change) | C035 says insulin may be undetectable; two roles agree on 2. |
| 1 D7 | 3 (V8; S4 3) | none | Accept (no change) | No C227 or C264 figure feeds the bin. Note the V8 reason uses "6% of 70" for insulinoma, which is not in the C264 text (assumption; V8 already labels the shares assumptions). |

FT12.

| Row, dim | Current (entries) | Proposed | Verdict | Evidence and rule |
|---|---|---|---|---|
| 31 D4 | 3 (V3 only) | 2 | Accept at 2 (confidence low; cap medium, rule 20, Chinese data) | Anchor 2 is "widely available but unstandardized"; clarification 25 says score standardisation and availability only. C080 line 45: C-peptide inter-measurement-system CV 20.1-31.6% against a desirable 8.3%; Jones 2013: standardisation "has yet to be achieved". Consistency: rows 28 (V16) and 29 (V10) already score C-peptide D4 at 2 for the same reason. The U3 argument that thresholds are wide relative to assay disagreement is a decision argument, and U3 itself withdrew the "far from cutoffs" sentence. |
| 6 D4 | 3 (U3, revised and kept at 3; no other role) | 2 | Accept at 2 (same reasoning; move with row 31) | Same evidence. The "24.5% and 5.7% after recalibration" figures in the U3 reason are not in the local C080 text (0 hits), so the evidence cited in the U3 correction cannot be traced; the text gives 20.1-31.6% and "all inter-measurement system %CVs met the APS" after recalibration (except one insulin sample). |
| 5 D4 | 2 (U3) | none | Accept (no change) | Insulin inter-system CV up to 58.3% and 44.1% after recalibration; no insulin reference procedure (C080 lines 45-47, 50). |
| 6 D3 | 4 (U1 corrected 3 to 4; S4 3) | none | Accept with a caution | Only the "must" before insulin discontinuation (C127 line 91) gives 4; the uncertain-type test is "recommended" (3). Clarification 13 says score the primary decision and note others; whether the primary decision of row 6 is classification (3) or insulin replacement is a judgement the user may revisit. Row 31 carries the insulin-discontinuation decision on its own. |
| 6 D1 | 4 (U4 corrected 3 to 4; U5 corrected 3 to 4; S4 3) | none | Accept (no change) | Same "should always be performed prior to insulin discontinuation"; clarification 15. |
| 6 D2 | 3 (U2 corrected; S4 3) | none | Accept (no change) | C169 is an uncontrolled single-centre cohort; Holt is consensus; C239 uses C-peptide as the outcome. |
| 6 D8 | 3 (U2 corrected) | none | Accept (no change), low confidence | A reclassification rate exists (rule 19 example), but it comes after an antibody, genetic-score and sequencing work-up and no antibody-first comparison is in C169. A 2 is arguable. |
| 6 D7 | 3 (V7, supersedes U1 4 and S4 4) | none | Accept (no change) | C216 and C231 give assumptions, not the bin-deciding share; the 14% is explicitly lower across all diabetes (line 64). |
| 6 D5 | 3 (U4 3; U5 3) | none | Accept (no change) | Single random sample within 5 h of eating; routine order. |
| 6 D6 | 3 (U4 3; U5 3) | none | Accept (no change) | Holt rules (2 weeks after a hyperglycaemic emergency; repeat if <600 pmol/L with glucose <4 mmol/L, line 28) limit false-low results. |
| 28 D3 | 1 (V14; S3 1) | none | Accept (no change) | Neither source gives plasma C-peptide interpretation guidance in CKD; Holt line 39 is about the urinary ratio. |
| 28 D2 | 2 (V15; S3 2) | none | Accept (no change) | Review mechanism only. |
| 28 D4 | 2 (V16) | none | Accept (no change) | Standardisation not achieved. |
| 28 D1 | 1 (V17, V18, S3, RS-D1S proposal 1) | none | Accept (no change) | Clarification 29: an interpretation limit scores 1 at most. |
| 28 D5 | 1 (V17, V18) | none | Accept (no change), low confidence | Judgement; no source states an owner. |
| 28 S | 2 (V17, V18, S3) | none | Accept (no change), low confidence | The reader reports Jones has no secretagogue passage. I grepped C026: its "sulphonylurea" hits are about insulin-withdrawal studies and MODY, not hypoglycaemia in kidney disease. So S rests on judgement. |
| 31 D1 | 4 (V4 corrected 3 to 4; V5 corrected 3 to 4; S4 3) | none | Accept (no change) | "Should always be performed prior to insulin discontinuation" (Holt); "must" (ADA figure note). |
| 31 D2 | 3 (V2; S4 2) | none | Accept (no change) | Jones lists limitations of the withdrawal studies; Holt is consensus. |
| 31 D3 | 4 (V1; S4 3) | none | Accept (no change) | "Must" in the ADA 2026 Figure 2.1 note, "should always" in Holt; the ADA statement is an ungraded figure note, not a numbered recommendation. |
| 31 D5 | 3 (V4, V5) | none | Accept (no change) | As row 6 D5. |
| 31 D6 | 2 (V4, V5) | none | Accept (no change), low confidence | Judgement on false-high consequences. |
| 31 S | 1 (V4 1; V5 corrected 2 to 1; RS-D1S proposal 1; S4 screener 3) | none | Accept (no change), low confidence | Default of continuing insulin makes marginal harm low (clarification 18/26). |
| 31 D8 | 2 (V2) | none | Accept (no change) | C239 uses C-peptide as outcome; it cannot show added value. |
| 32 D1 | 3 (S2, V4, V5) | none | Accept (no change) | One cohort cited in Jones. |
| 32 D2 | 2 (S2, V2) | none | Accept (no change) | Single cohort. |
| 32 D3 | 2 (V1 2; S2 screener 1) | none | Accept at 2, but for a different reason | The cited quote ("Do not test C-peptide within 2 weeks of a hyperglycemic emergency") is a restriction, not a recommendation. The 2 is better supported by clarification 14: Holt/ADA recommend the test before insulin discontinuation in insulin-treated people, a broader population that includes this one. |
| 32 D5 | 2 (V4, V5) | none | Accept (no change), low confidence | Specialist follow-up; judgement. |
| 7 D3 | 3 (V1 corrected 2 to 3; S4 3) | none | Accept (no change), medium | The quote gates genetic testing on non-fasting C-peptide >200 pmol/L (Holt); that names C-peptide in the pathway but is not a stand-alone recommendation to measure it; 3 is acceptable, 2 would be the strict reading of ADA 2.29b alone. |
| 47 D3 | 1 (V1 1; S2 screener 2) | none | Accept (no change) | I grepped C127: its only C-peptide statements are line 91 (figure note), lines 117 and 121 (background); none concerns LADA criteria. |
| 49 D3 | 1 (S1, V1) | none | Accept (no change) | Same grep: no C-peptide statement in the staging recommendations. The quote supplied ("should be referred to a specialized center for metabolic staging") shows the staging wording but does not itself prove the absence; the absence rests on the grep. |

Rules the readers missed
- Row 1 D1 and D3 are two different dimensions but one sentence; accept or reject them together.
- Row 32 D3: use clarification 14, not the 2-week rule.
- Row 48 D1: check the latest role entry (V24 after V23).

## 3. Claim-issue verdicts

| # | Claim issue | Verdict | Checks |
|---|---|---|---|
| FT11-1 | Row 1 source and `usecases-verified.md` line 121 say Cryer 2009 is abstract-only | Confirmed, with reword | Thresholds, Rec 2.1 wording, the grade string "1QQQE" (read as grade 1, moderate; symbols are extracted as letters) and the fast and mixed-meal protocols are in the C014 text. The draft sentence "a fast of up to 72 h or a mixed meal when none is observed" is right (lines 80-83 area). Keep the unit note: the micro sign is lost in the extraction (printed "U/ml"), read as uU/mL. Apply A1, A2. |
| FT11-2 | Row 22 status "Established, specialist, second-line" | Reword (status stays) | The file already quotes "should be considered ... where other imaging tests are negative". Established under the project rule (a quoted consensus passage recommends the test for that decision) is defensible; what is missing is the option-level label. "Small" for the two cited series is not shown in C039; the file already says "small", I left that alone. Apply A3. |
| FT11-3 | Row 23 ENETS narrative OGTT vs Cryer | Reword | Verified lines 444-447. The reader's wording lacks PMID and DOI for ENETS and Cryer; added. Mixed-meal sampling rule "only on samples with glucose <60 mg/dL" verified at lines 596-599. Apply A4. |
| FT11-4 | Row 48 "NOT read", "no insulin threshold found" | Reword | Verified. Also the row's measure cell includes a "5-h 75 g OGTT" arm, which this guideline recommends against; that conflict should be stated. The reader's "functional disorder" remark (line 308) was not verified and is left out. Apply A5. |
| FT11-5 | V2 row 3 D2 and V9 row 1 D2 reason text "evidence graded low to very low" | Confirmed | V2 row 3 D2 still carries it with no correction note; V9 row 1 D2 carries it with a withdrawal note. Proposed wording is supported by lines 240-246 ("upgrades the quality of the evidence to moderate ... much lower quality evidence supports the recommended strategy when compared with strategies with minor modifications or omissions"). A correction of the reason text; the V2 score (2) and V9 score (3) are not touched. |
| FT11-6 | Row 20 (PEG with Cryer) and row 2 caveat | Reject | Row 20 does not attribute PEG precipitation to Cryer (its source cell says "Cryer 2009 abstract" next to unrelated sources, and the measure cell names PEG without attribution); row 2 attributes the analogue caveat to PES 2015. The absence claim is true: C014 has no "PEG", no "polyethylene" and no analogue-assay statement ("analog" occurs only in a reference title, line 1447). Insulin antibodies are in Rec 2.1 (line 74). Nothing in the file needs changing; at most add "Cryer 2009 full text" where rows 2, 3, 20 and 21 say "abstract" (not part of the draft). |
| FT11-7 | V3 row 3 D4 correction and V10 row 29 D4 reason ("inter-lab CV 22.2%", "interlab 10.8-13.4% imprecision") | Confirmed | C107 line 43: "median imprecision across 84 measurements was 13.4% ... and 22.2%", 10.8% for two-day averages; research LC-MS/MS in three laboratories. It did not test immunoassays. Correction of reason text, not of the scores (V3 row 3 D4 = 1, V10 row 29 D4 = 2). I could not tell from my reading whether the 22.2% is spread across laboratories, days or both, so "inter-lab" cannot be confirmed either way. |
| FT11-8 | V8 row 1 D7 (6% insulinoma share; 1,082 per 100,000) | Confirmed | 11 of 70 is stated; the 6% is not in the C264 text. C227 states 1082 (CI 1019-1148) per 100,000 inhabitants per year for about one million inhabitants, while the 7-year total of all episodes was 13,135, which cannot give 10,820 per year; the count-based figure for transported non-diabetic events is about 55 per 100,000 per year. Correction of reason text only; the D7 score (3) is not touched. |
| FT12-1 | Row 6 and U4 D5 reason name renal impairment as an invalid condition for the test | Confirmed, reword | Holt line 39: "The latter may be confounded by impaired renal function" (urinary ratio only). The plasma caveat comes from Jones (line 21). Row 6 line 23 reads "Invalid in first 3 years, within 2 weeks of hyperglycaemic emergency, with renal impairment, glucose <4 mmol/L", placed after a Jones attribution; the glucose rule in Holt is a repeat rule, not invalidity. Apply A6. U4 D5 reason: reason-text correction, not score. |
| FT12-2 | ADA Standards 2026 as a second source for rows 6 and 31 | Confirmed, reword | C127 line 91 shows the C-peptide advice as a numbered footnote to the Figure 2.1 flowchart; the numbered recommendation does not name C-peptide. Apply A7 (row 6) and A7b (row 31). |
| FT12-3 | Row 6 "6.8% reclassified, abstract level" | Confirmed, reword | Verified 859 tested, 114 triggered, 58 reclassified; Edinburgh (10 hits); cut-off "pragmatic" (lines 233, 511); Roche 269 stated at line 245. Do not repeat "Abbott 200 = Roche 269": the equation as printed (Abbott = 0.8755 x Roche - 40.6) gives about 275 for exactly 200, so 269 belongs to the paper's own cut-off wording. Apply A8. |
| FT12-4 | U3 row 6 D4 and V3 row 31 D4 reason text | Confirmed, reword | "24.5%" and "5.7%" have zero hits in the local C080 text; it gives inter-system 20.1-31.6%, and "samples with a low C-peptide concentration had much higher inter-laboratory %CVs" (line 50), which contradicts V3's "the low end is less affected". The pairing "31.6% = lowest-concentration sample" is not in the text (tables absent), so the proposed phrase "worst at the lowest concentration" should use the inter-laboratory wording. Corrected wording for the reason text: "In a survey of 94 Chinese laboratories (PMID 35177563, DOI 10.3343/alm.2022.42.4.428), C-peptide inter-measurement-system CV was 20.1-31.6% against a desirable 8.3%; samples with low C-peptide had much higher inter-laboratory CVs; after recalibration all C-peptide values met 8.3%. The 24.5% and 5.7% figures could not be traced to the local text." This is a correction of the reason text (U3 and V3 JSON), not of the scores. See also A9 (merged-conclusion). |
| FT12-5 | V7 row 6 D7 (14% anchor) | Confirmed | C216 line 64 "the misclassification rate of 14% is likely to be much lower"; 57 (66%) and 30 (34%) as stated. Proposed wording is within the paper. Correction of reason text; V7 D7 stays 3. |
| FT12-6 | U1 row 6 D7 (C231 1.3 million vs 1.8 million) | Reject as framed | U1 gives the 1.8 million figure to a CDC report (2026) and uses PMID 29596402 only for the 5.8/90.9/3.3 split, which is printed in C231 (lines 10, 13). There is no misquote of C231; the two numbers are different sources and years. U1's D7 is also superseded by V7. Optional note only: NHIS 2016 gives 1.3 million adults with type 1 (self-reported plus insulin use). |
| FT12-7 | Row 28 (Jones) | Reject as a change to the file | Row 28 already reports only "about half ... cleared by the kidney; falsely elevated in renal impairment; correction methods poorly validated" for Jones, and the "secretagogue hypoglycaemia risk" is in the decision cell, not attributed to Jones. The only wrong attribution is in the V18 S reason text (I did not open V18's reason; taken from the reader). That is a reason-text correction. |

## 4. Apply

All OLD strings were checked to occur exactly once in the named file. "Line" is the line in the current file.

### A1. `usecases-verified.md` line 18 (row 1), three edits

OLD:
```
Cryer 2009 (Endocrine Society), PMID 19088155, abstract.
```
NEW:
```
Cryer 2009 (Endocrine Society), PMID 19088155, DOI 10.1210/jc.2008-1410, full text (PDF-derived, two-column interleaving; read 2026-10-26, FT11).
```

OLD:
```
are second-hand via ENETS, not from the ES text.
```
NEW:
```
are given in the Endocrine Society text itself (Rec 2.1 bullets; full text read 2026-10-26) and restated by ENETS; the micro sign of the insulin unit is lost in the PDF-derived text (printed "U/ml") and is read as uU/mL.
```

OLD:
```
grade symbol not independently seen, inferred from the text
```
NEW:
```
grade string "1QQQE" seen in the full text of Rec 2.1 (symbols extracted as letters, read as grade 1 with moderate-quality evidence); the text says the quality is moderate compared with a much less thorough work-up and that much lower quality evidence supports the strategy compared with strategies with minor modifications or omissions
```

### A2. `usecases-verified.md` line 121 (section 4, gaps list)

OLD:
```
- Full text of Cryer 2009 (abstract only; thresholds, grades and 72-hour fast rules are second-hand via ENETS).
```
NEW:
```
- Full text of Cryer 2009: read 2026-10-26 (FT11, PDF-derived two-column text; Table 3 values scrambled and not used); thresholds, grade 1QQQE and the fast and 5-h mixed-meal protocols are in the guideline text itself. No longer a gap; the main session may delete this line.
```

### A3. `usecases-verified.md` line 39 (row 22)

OLD:
```
established as a consensus-endorsed second-line specialist test)
```
NEW:
```
established as a consensus-endorsed second-line specialist test; the wording is "should be considered", which is option level (D3 2))
```

### A4. `usecases-verified.md` line 40 (row 23)

OLD:
```
ENETS 2016, full text | Single-centre data quoted in guideline
```
NEW:
```
ENETS 2016, PMID 26742109, DOI 10.1159/000443171, full text. Cryer 2009, PMID 19088155, DOI 10.1210/jc.2008-1410, full text (FT11, 2026-10-26) | ENETS reports that a subset of insulinomas may be diagnosed by an altered insulin secretory pattern during an OGTT (one mono-institutional study, no graded recommendation). Cryer 2009 states that an OGTT "should never be used for the evaluation of suspected postprandial hypoglycemia" and describes a 5-h mixed-meal test with insulin, C-peptide and proinsulin sent only on samples with glucose below 60 mg/dL; standards for interpreting the mixed-meal test "have not been established" and current usage applies the fasting criteria. The OGTT route in this row is therefore recommended against by the Endocrine Society guideline (D3 0)
```

### A5. `usecases-verified.md` line 65 (row 48), two edits

OLD:
```
Cryer 2009 Endocrine Society guideline (PMID 19088155, DOI 10.1210/jc.2008-1410): NOT read, no open full text (unread, not shown to be silent)
```
NEW:
```
Cryer 2009 Endocrine Society guideline (PMID 19088155, DOI 10.1210/jc.2008-1410), full text read 2026-10-26 (FT11, PDF-derived): a 5-h mixed-meal test with insulin, C-peptide and proinsulin sent only on samples with glucose below 60 mg/dL; "standards for the interpretation of the mixed-meal test have not been established"; current usage applies the fasting criteria to it; an OGTT "should never be used" for suspected postprandial hypoglycemia, so the OGTT arm in this row's measure column is recommended against by that guideline
```

OLD:
```
no insulin threshold found
```
NEW:
```
no validated insulin threshold (Cryer 2009: fasting criteria applied in current usage; interpretation standards not established)
```

### A6. `usecases-verified.md` line 23 (row 6)

OLD:
```
Invalid in first 3 years, within 2 weeks of hyperglycaemic emergency, with renal impairment, glucose <4 mmol/L.
```
NEW:
```
Holt 2021 and the ADA 2026 Figure 2.1 note: recommended where type is uncertain beyond 3 years from diagnosis; do not test within 2 weeks of a hyperglycaemic emergency; if the result is <600 pmol/L and the concurrent glucose is <4 mmol/L (or the person may have been fasting), consider repeating. Renal impairment is not a stated condition for the plasma test in Holt or ADA (Holt names it only as a confounder of the urinary C-peptide:creatinine ratio); Jones and Hattersley 2013 says plasma C-peptide can be falsely raised in renal impairment and correction methods are poorly validated.
```

### A7. `usecases-verified.md` line 23 (row 6) and A7b line 48 (row 31)

OLD (line 23):
```
(raw HTML; reproduces the Holt algorithm, a second consensus source, read by skeptic)
```
NEW:
```
(raw HTML; reproduces the Holt C-peptide advice in a note to Figure 2.1, which is ungraded and not a numbered recommendation, so it restates the same consensus rather than adding an independent source; read by skeptic and in FT12)
```

OLD (line 48):
```
ADA Standards 2026 s2, PMC12690183, full text (second consensus source)
```
NEW:
```
ADA Standards 2026 s2, PMID 41358893, DOI 10.2337/dc26-s002, PMC12690183, full text (the C-peptide advice is a note to Figure 2.1 copied from Holt 2021, ungraded; a restatement, not an independent source)
```

### A8. `usecases-verified.md` line 23 (row 6)

OLD:
```
6.8% reclassified in a single-centre uncontrolled UK implementation cohort (Foteinopoulou 2021, PMID 33131101, DOI 10.1111/dme.14449, abstract)
```
NEW:
```
6.8% (58 of 859 tested) reclassified in a single-centre uncontrolled UK implementation cohort of people with clinician-diagnosed T1D of 3 or more years (Foteinopoulou 2021, PMID 33131101, DOI 10.1111/dme.14449, full text read 2026-10-26, FT12); a random C-peptide at or above a pragmatic cut-off of about 200 pmol/L on Abbott (the paper gives 269 pmol/L on Roche) triggered antibody, genetic-risk-score and genetic testing, and the reclassification followed that work-up; 13 (1.5%) stayed off insulin; no severe hypoglycaemia or DKA was reported
```

### A9. `merged-conclusion.md` (skeptic-found, not in the drafts; optional, for the main session to decide)

Line 51. OLD:
```
C-peptide recalibration cut inter-system CV from 24.5% to 5.7% (Zhou)
```
NEW:
```
In a survey of 94 Chinese laboratories (PMID 35177563, DOI 10.3343/alm.2022.42.4.428; local text partial), C-peptide inter-measurement-system CV was 20.1-31.6% against a desirable 8.3% and all C-peptide values met 8.3% after recalibration (the earlier 24.5% and 5.7% figures could not be traced in the local text; author name not checked)
```

Line 57. OLD:
```
a median inter-laboratory insulin CV of 22.2% for an LC-MS/MS protocol (three laboratories, leftover clinical samples, single-point calibration)
```
NEW:
```
a median imprecision (CV) of 22.2% across 84 insulin measurements by an LC-MS/MS research protocol (three laboratories, leftover clinical samples, single-point calibration; not clinical immunoassays)
```

Not applied anywhere above (score-file reason texts, corrections of reason text only, not of scores): V2 row 3 D2 and V9 row 1 D2 ("low to very low"); V3 row 3 D4 and V10 row 29 D4 (22.2% and 10.8-13.4% as "inter-lab"); V8 row 1 D7 (6% share, 1,082 rate); U3 row 6 D4 and V3 row 31 D4 (24.5%/5.7%, "low end less affected"); V7 row 6 D7 (14% anchor); U4 row 6 D5 (renal impairment); V18 row 28 S (Jones cited for S); V8 row 23 D3 correction note ("seen in a search excerpt").

Tool calls used: about 44, including the one write.
