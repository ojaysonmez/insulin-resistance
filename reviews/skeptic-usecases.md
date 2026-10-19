# Skeptic review of usecases-verified.md (partial: usage limit reached)

Date: 2026-10-18. Reviewer: ir-skeptic. usecases-verified.md was not edited.

Method. I read raw publisher or PMC HTML, PMC XML or the FDA PDF (not a summariser) for: ADA Standards 2026 s3, AACE 2022, IRIS, JDS 2022, ES 2017 pediatric obesity, SIEDP 2024, the Delphi MASLD nomenclature paper, EASL-EASD-EASO 2024, AASLD 2023, the PCOS guideline, the lipodystrophy guideline, ENETS 2016, the HI guideline 2023, PES 2015, Igls 2018, Holt 2021, Jones 2013, Buzzetti 2020, PMDI 2023, the FDA Tzield label (rev 06/2026) and the Pituitary Society 2021 update. Where a passage is quoted below, it is from that raw text.

Citation checks. Scholar Sidekick returned "not subscribed", so I used NCBI esummary (identity, title, journal, year, DOI) and Crossref `updated-by` for all 80 PMIDs cited in the file.

Not done: the ISPAD CFRD, ISPAD monogenic and PMDI neonatal-diabetes passages; the abstract-only rows (bariatric cohorts, 3c diabetes, CKD C-peptide numbers); the missing-use search (item 5 of the brief); the 2026 case reports beyond identity. Statuses for those rows are therefore not re-verified.

## 1. Citation identity and retractions

- All 80 PMIDs resolve to papers whose titles and first authors match what the file says about them. No fabricated or mismatched identifiers.
- PMID 24757230 (DiaPep277, Raz, Diabetes Care 2014) is confirmed retracted: PubMed publication type "Retracted Publication" and Crossref `updated-by` retraction notice 10.2337/dc15-rt01. It appears only in row 8, as a "do not cite" note. It is not cited as support anywhere. Fine.
- No other retractions. Corrections or errata exist for: Holt 2021 (PMID 34590174), Palmer 2004 (14693724), AACE 2022 (35963508), EASL Obes Facts copy (38852583), EASL Diabetologia copy (38869512) and the ERAS bariatric guideline (34984504). None changes anything I checked. The file should say the AACE erratum exists.
- Row 31: PMID 24843502 is Funakoshi 2011, "Utility of indices using C-peptide levels for indication of insulin therapy to achieve good glycemic control in Japanese patients with T2D". It is about when insulin is needed, not about stopping it. The file uses it as support for "predicting success of stopping insulin". This is a weak match; flag it.
- Row 11: the title of PMID 22963817 is "Predicting success of metabolic surgery: age, body mass index, C-peptide, and duration score", i.e. the ABCD score (Lee 2013, Surg Obes Relat Dis). The "unclear whether Diabetes Surgery Score and ABCD are the same" question in sections 1 and 5 is therefore answered by the title: 22963817 is the ABCD score derivation paper. The year is 2013 (the file gives no year).

## 2. The open conflicts, resolved against primary text

1. **ADA 2026 Rec 3.13 (row 13). The merge's unresolved reading was wrong; merged-conclusion.md is right.** Raw PMC HTML: "3.13 In people with a history of stroke and evidence of insulin resistance and prediabetes, pioglitazone may be considered to lower the risk of stroke or myocardial infarction. However, this benefit needs to be balanced with the increased risk of weight gain, edema, and fractures. A. Lower doses may mitigate the risk of adverse effects but may be less effective. C." The text then describes IRIS with "insulin resistance (as defined by a HOMA of insulin resistance index of >=3.0)". The reviewer M's read ("tied to prediabetes, no IR wording") was a summariser error. No assay is named in the recommendation itself. I read the PMC HTML (about 85k characters after stripping); I did not confirm it is the full 159k-character article, but the recommendation and the IRIS paragraph are both present. Section 6 item 2 of the file should be deleted.
2. **AACE 2022 R 9.4 (row 13).** Verified verbatim in the full XML (2.3 MB): "In persons with insulin resistance, prediabetes, or T2D and a prior transient ischemic attack or stroke, pioglitazone should be considered to reduce the risk of recurrent stroke. Grade A; BEL 1." It shares R 9.4 with a GLP-1 RA sentence. The evidence text says the meta-analysis population (N=4980) "with insulin resistance, prediabetes, or DM". No test is named. Status "limited" is right, with the point that both guidelines name insulin resistance as a condition without directing a measurement.
3. **IRIS top-quartile (row 13).** M said "no citation in the text read". Wrong: the text reads "The index threshold of 3.0 was chosen because it identifies the highest quartile among populations without diabetes. 19, 20", so refs 19 and 20 are cited. Also: IRIS is a trial entry criterion, and the primary outcome numbers (9.0% vs 11.8%, HR 0.76) match.
4. **JDS 2022 (row 12).** Verified verbatim in PMC HTML. Table 2 (genetic IR syndrome): Major sign "Hyperinsulinemia with no apparent cause of insulin resistance such as obesity or other conditions (fasting serum insulin level of >30 uU/mL, although this value may depend on the course of treatment for diabetes)". Table 3 (type B): Major sign hyperinsulinaemia, fasting insulin >30 uU/mL; "Definite = A and C", where C is insulin-receptor autoantibody. Correction: the table note says the value "may depend on the course of treatment for diabetes". The file's "invalid on exogenous insulin (JDS table note)" overstates this. The text also says 89 Japanese adults with T2D and BMI <25 had none above 30, and that some genetic cases have values below 30. Status "limited" is right (single-nation, expert criteria).
5. **Endocrine Society 2017 Rec 1.7 (row 16).** Verified verbatim in raw PMC HTML: "1.7 We recommend against measuring insulin concentrations when evaluating children or adolescents for obesity. (1|+++o)", i.e. strong recommendation, moderate quality. Rationale text: "Because of these limitations, measuring plasma insulin concentrations remains a research tool with no clinical value for evaluation of obesity. Measuring fasting insulin concentrations to try to diagnose insulin resistance within general practice should be abandoned." It also says fasting insulin is similar in obese youth with normal and impaired glucose tolerance, which supports row 36. Both are now read at primary level. Remaining caveat: it is a single 2017 guideline.
6. **SIEDP 2024 and the Delphi statement (rows 14, 16, 36).** SIEDP (PMC11463079, raw HTML): "Estimates of IR such as HOMA-IR come to be clinically valuable in patients with suspected MASLD who does not still meet any of the 5 diagnostic criteria [76]". Ref 76 is Rinella et al., "A multisociety Delphi consensus statement on new fatty liver disease nomenclature" (PMID 37364790; Hepatology copy 37363821, PMC10653297). I read the Delphi text. It says that when metabolic dysfunction is strongly suspected without cardiometabolic risk factors, "this may be early MASLD and prompt additional testing (eg, HOMA-IR and oral glucose tolerance tests)" and that the term "possible MASLD" may be used "pending additional testing ... although this should be left to the discretion of the clinical team". It also says the criteria exclude fasting insulin and HOMA-IR "because of their complexity, cost, and variability between laboratories", and that "secondary testing for insulin resistance may be useful". So the SIEDP statement traces to a real source, but SIEDP overstates it ("come to be clinically valuable" versus "may prompt", "discretion"). The Delphi paper is adult-and-general nomenclature, not a paediatric recommendation. The conflict in section 5 item 12 is resolved: there is a source, and it is permissive and weak. It is a second weak source for row 14 and does not change the verdict that no management change depends on it. Row 14 should cite the Delphi paper.
7. **EASL-EASD-EASO 2024 (row 14).** Verified verbatim in raw PMC HTML: "Assessment of insulin resistance (e.g., using HOMA-IR or estimates derived from the OGTT) may be considered to clarify metabolic dysfunction in adults with (suspected) MASLD and without an established diagnosis of type 2 diabetes (LoE 3, weak recommendation, consensus)". Table 7 lists "Fasting plasma insulin and/or C-peptide; HOMA-IR". Correct as stated. **AASLD 2023 negative is now complete**: I searched the whole PMC article (about 238k characters); no HOMA, fasting insulin or C-peptide text outside reference titles. The "AASLD negative covers ~20% of text" caveat can be removed.
8. **PCOS guideline (row 15).** Practice points 1.9.12 and 3.1.10 verified verbatim, including the one-phrase difference.
9. **Teplizumab (rows 8, 29, 30). Verified against the FDA label PDF, revision 06/2026, section 2.1.** "Select pediatric patients aged 8 to 17 years recently diagnosed (within the last 8 weeks) with Stage 3 T1D ... based on confirmation of both: at least one positive pancreatic islet cell autoantibody; peak C-peptide >=0.2 pmol/mL on a mixed-meal tolerance test (if a MMTT is not available, an alternative method for measuring peak C-peptide >=0.2 pmol/mL may be appropriate)." Indication is under accelerated approval "based on evidence of reduced C-peptide decline", continued approval contingent on confirmatory trial. Age range, threshold and timing in row 29 are correct. 0.2 pmol/mL = 0.2 nmol/L = 200 pmol/L is a correct conversion. Two additions: (a) the label's Stage 2 indication is "adult and pediatric patients 1 year of age and older", while the file says "EMA Stage 2 only, 8 years and over" (EMA snippet only); the age difference between FDA and EMA should be stated as FDA >=1 year; (b) Stage 2 selection uses autoantibodies and OGTT, and the label requires that the diagnosis "does not suggest insulin resistance due to obesity, T2D...", which is a clinical judgement, not an insulin test. Row 30 "Unsupported" stands. Row 29 "Established as regulatory eligibility criterion" is justified, but it is a surrogate-endpoint-based accelerated approval, which the row already says.
10. **Row 4 neonatal age cutoff.** The sources differ legitimately. PES 2015: "During the first 24-48 hours of life ... plasma glucose concentrations are typically lower". HI guideline 2023 (newer, hyperinsulinism-specific): "Newborn infants, tested before 72 h of life during the time of transitional hypoglycemia, should be retested after 72 h if hypoglycemia is still present to confirm the diagnosis." Use 48 h for transitional physiology (PES) and 72 h for diagnostic confirmation of hyperinsulinism (HI guideline). H's wording is closer to the newer source.
11. **Igls C-peptide threshold (row 10).** The Igls 2018 text (Transpl Int, PMC5867272) gives **no numeric threshold** for "clinically significant" C-peptide. It defines failed graft as "absence of any evidence for clinically significant C-peptide production" and says that, with sensitive assays, low levels "of questionable clinical significance are often detected (eg <0.3 ng/ml [<0.1 nmol/l] fasting or <0.6 ng/ml [<0.2 nmol/l] postprandial) despite clinical beta-cell failure". So 0.3 ng/mL fasting and 0.6 ng/mL postprandial are the levels below which the document questions significance. The row's "0.3 ng/mL [recall]" should be replaced by this text, and "unverified" removed. Optimal graft requires "an increase over pretransplant measurement of C-peptide"; good requires restoration of clinically significant C-peptide. Status "established (consensus)" is fine.
12. **Cryer 2009.** Full text still unavailable (publisher 403, no PMC). The thresholds are read in ENETS 2016 (PMC4849884): "glucose <55 mg/dl, insulin >=3.0 uU/ml, C-peptide >=0.6 ng/ml, proinsulin >=5.0 pmol/liter ... BOHB <=2.7 mmol/liter ... glucose >=25 mg/dl after iv glucagon", plus the 9% missed at insulin 5. They are quoted second-hand but accurately.

## 3. Other findings on the 13 "established" rows and on new rows

Established rows: 1, 2, 3, 4, 6 (Established in the file is for 6, 7, 31 in the Classification count), 10, 20, 21, 22, 24, 29.

- **Row 4 numbers.** The file gives BOHB <1.5 mmol/L, FFA <1.0-1.5 and glucagon >30 mg/dL (PES 2015). The HI guideline Table 1 (the newer source the row also cites) says: BOHB <1.8 mmol/L, FFA <1.7 mmol/L, glucagon response >=30 mg/dL, and, as "less definitive" evidence of excessive insulin secretion, **plasma insulin >1.25 uU/mL (8.7 pmol/L) and C-peptide >0.5 ng/mL (>0.17 nmol/L)** at glucose <50 mg/dL. The file omits these numeric insulin and C-peptide cut-offs, which are the most relevant ones for this project, and uses the older BOHB/FFA values. Add the Table 1 values and state that guidelines differ. Rec 1.1 is Grade 1, moderate (verified). Status "established, insulin supportive" is right.
- **Row 24.** Rec 1.4 ("We Recommend Screening all Children Whose Hyperinsulinism Occurs after the Age of 2 years of Life for Insulinoma") is Grade 1 with low-quality evidence (two circles), not "very low/low". Wording of the file otherwise fine.
- **Row 26.** The BOHB >1.8 mmol/L before glucose <50 mg/dL criterion for diazoxide response and cure is in the text (diazoxide section and the post-surgery fasting paragraph). The grades the file attaches are mixed: 2.4 is a Grade 1 recommendation for diazoxide as first line; 3.2 and 4.1 are Grade 2. The criterion itself is narrative text, not a graded recommendation. Reword.
- **Row 22 (IACIG).** ENETS: "positive in 90-100% of cases [126; 127] and therefore should be considered in a patient where other imaging tests are negative", citing two small series. "Operator-dependent" is not in that passage. Established as a consensus-endorsed second-line test is fair; the evidence behind the figure is two small series and should be said.
- **Row 23.** "up to 18%" comes from one mono-institutional study cited in ENETS. Limited is right.
- **Row 6.** Holt 2021 verified: C-peptide only in insulin-treated people; random sample within 5 h of eating; >=600 pmol/L circumstances do not matter; <80 pmol/L no repeat; 200-600 usually T1D or MODY but may be insulin-treated T2D; "must be measured prior to insulin discontinuation"; not within 2 weeks of a hyperglycaemic emergency; "Beyond 3 years after diagnosis"; 11% reclassified. The "<200 pmol/L confirms deficiency" threshold is **not in Holt**; it is in the Jones 2013 table (stimulated <0.2 nmol/L absolute deficiency; <0.6 likely T1D). Fix attribution. LADA thresholds (<0.3, 0.3-0.7, >0.7 nmol/L) verified in Buzzetti 2020 and flagged by the panel as needing trials.
- **Row 7.** PMDI Table 3 verified: "People without obesity under the age of 30 years who are either autoantibody negative and/or have retained C-peptide levels should be tested for monogenic diabetes using a large-gene panel", Grade A. The wording is "and/or", i.e. C-peptide is one alternative of two. Fine.
- **Rows 20, 21.** Both remain "established" on abstract-level 2026 reviews and case reports, with no guideline text. I would downgrade both to "limited (expert practice, case-series level)" or relabel the status as "established clinical practice, weakly sourced". The file's own section 2 notes say so. Row 21 is also supported by the HI guideline's Table 2 listing NICTH (Doege-Potter) and paraneoplastic pro-IGF2 as hyperinsulinism mimics; this is a stronger source than the case reports and I saw it in the raw HI text.
- **Row 2.** Established is justified by PES 2015 (not re-read by me for the quote).
- **Row 3.** Fine as an "as part of the panel" entry.
- **Row 10.** See item 11 above.

## 4. Status changes I would make

| Row | File | Suggested | Why |
|---|---|---|---|
| 20, 21 | Established | Limited, or Established with explicit "expert practice / case-series only" | Abstract-level 2026 sources; no guideline text read |
| 22 | Established | Established (specialist), evidence two small series | ENETS wording "should be considered" |
| 13 | Limited | Limited (unchanged) but fix the ADA conflict in sections 5-6 | Rec 3.13 does say "evidence of insulin resistance and prediabetes" |
| 14 | Limited | Limited (unchanged); add Delphi and fix AASLD note | Two weak consensus sources, no management change |
| 36 | Unsupported | Unsupported (unchanged) | ES 2017 evidence paragraph supports it |
| 8 | Research-only | Research-only for routine care, and note regulatory-surrogate use via row 29 | Teplizumab label |
| 12 | Limited | Limited; remove "invalid on exogenous insulin" | JDS says value "may depend on" treatment |

All IR rows remain limited, research-only or unsupported. The bottom-line verdict (no established clinical utility for routine IR measurement) stands, and the primary-source reads strengthened it: ADA 3.13 and AACE R 9.4 name "insulin resistance" as a condition but neither names an assay or threshold.

## 5. Kind assignments and counts

- Counts: 45 rows, 13 established, 11 limited, 10 research-only, 11 unsupported, as the file states, but they depend on the status mapping and the rows I would change (20, 21). I did not recount every row against the file's list; the totals add to 45.
- Row 29 (teplizumab) and rows 10, 29 are "Secretion", and rows 6, 7, 31 "Classification"; the asterisked judgements are reasonable. Rows 26, 30, 34 are negative entries counted as "unsupported"; they inflate the "unsupported" total. Report negative entries separately.
- Row 35 is a hybrid: part (a) is an established glucose-based GCK test and part (b) is a research IR use. Count it once as IR/research-only, as done, but do not let (a) appear as an established use.

## 6. Missing uses (item 5 of the brief): not completed

I did not get to search for uses the reviewers missed. Candidates I would check next, all unverified here: (a) pancreas-transplant candidate eligibility by C-peptide in transplant allocation policy (OPTN) and in Igls pre-transplant testing; the Igls text does say pre-transplant C-peptide testing is "critical to inform posttransplant monitoring" and candidates beyond T1D need C-peptide to identify elevated levels consistent with insulin resistance, which is already a sourced sentence from the file's Igls document; (b) C-peptide as a regulatory surrogate endpoint beyond the teplizumab label (FDA T1D guidance); (c) ADA Standards 2026 section 2 or 9 statements on C-peptide (blocked earlier; the raw PMC HTML route worked for section 3 and may work for section 2).

## 7. Verdict

Top problems:
1. The open ADA 3.13 conflict is wrong in the file (the recommendation does say "evidence of insulin resistance and prediabetes"); the IRIS citation claim is also wrong.
2. Row 4 omits the HI guideline's numeric insulin (>1.25 uU/mL) and C-peptide (>0.5 ng/mL) cut-offs and uses older BOHB/FFA values (1.5 and 1.0-1.5 versus 1.8 and 1.7).
3. Row 10's Igls threshold is not "recall": the document gives no numeric threshold but questions fasting <0.3 and postprandial <0.6 ng/mL.
4. Rows 20 and 21 are called "established" on abstract-level 2026 case material.
5. Attribution errors: "<200 pmol/L" is Jones, not Holt; Funakoshi (24843502) does not address stopping insulin; the ABCD/DSS naming question is answered by the PMID 22963817 title.

Statuses I would change: rows 20 and 21 (down to limited or heavily caveated); wording changes to 12 and 8. Nothing else changes category.

Confidence in the list as a whole: moderate to high for the IR rows and for the load-bearing guideline-based established rows I read (1 via ENETS, 4, 6, 7, 10, 29); moderate-low for rows resting on abstracts only (5, 9, 11, 19, 25, 27, 28, 32, 33, 39-45), which I did not re-verify, and for coverage, since the missing-use search was not done (it is done in Part 2 below).

---

# Part 2 (2026-10-19): completion of the items Part 1 left open

Part 1 already covers the open conflicts (ADA 3.13, AACE R 9.4, JDS, ES 2017 Rec 1.7, teplizumab label, row 4 age cutoff, Igls threshold, SIEDP/Delphi, DiaPep277). I did not redo them. Part 2 adds a correction to Part 1, abstract-level checks, newly read primary sources, missing uses with search strings, and the closing summary. Same method: raw PMC HTML, FDA PDF and NCBI efetch; Scholar Sidekick is not subscribed.

## 2.1 Correction to Part 1

Section 1 of Part 1 says the title of PMID 22963817 settles the ABCD / Diabetes Surgery Score question. That was too strong. The title lists age, BMI, C-peptide, duration (the letters of ABCD), but the abstract itself names the score "Diabetes Surgery Score" (10-point scale; derivation n=63, validation n=176, remission 65.3% at 1 year; read in the efetch abstract). So the paper uses the name DSS with the same four variables as the "ABCD" score in SOS. Whether they are formally the same score is still unconfirmed. Journal year is 2013 (Epub 2012).

## 2.2 DiaPep277 (PMID 24757230): final confirmation

- PubMed publication type "Retracted Publication"; Crossref `updated-by` lists retraction notice 10.2337/dc15-rt01.
- Grep of usecases-verified.md: the PMID appears once, in row 8, in the sentence "Do not cite DiaPep277 ... listed as retracted". It is not in any key-sources cell and is absent from usecases-draft.md. It is not cited as support anywhere. Confirmed.

## 2.3 Abstract-level re-checks (efetch abstracts read)

| Row | Check | Result |
|---|---|---|
| 9 | PancreasFest 2012 (23890130) | Verbatim: 2.1 fasting glucose and HbA1c; 2.2 OGTT; 2.3 "absent pancreatic polypeptide response ... a specific indicator of type 3c"; 2.4 assess functional beta-cell mass for TPIAT. No C-peptide threshold. File matches; "limited" supported. |
| 9 | Woodmansey 2017 (28860126) | 87.8% of 559 cases classified as T2D, 2.7% as exocrine-pancreas diabetes; insulin within 5 years 45.8% after chronic pancreatic disease. File matches. |
| 11 | Lee 2013 (22963817) | Matches (see 2.1). The abstract makes no comparison with duration alone. |
| 28 | D'Elia 2019 (30794834) | 87 T2D patients; glucose/C-peptide ratio varies with renal function; abstract says it "may be useful" to guide secretagogue dosing (hypothesis). Matches. |
| 28 | Zhou 2022 (36465621) | n=85; UCPCR <=1.13 nmol/g, sensitivity 88.4%, specificity 95.2%, AUC 0.978 for "severe insulin deficiency". Matches; single centre, unit is nmol/g (not the nmol/mmol of the MODY literature). |
| 33 | Elzahar 2020 (32052124) | 50 T1D vs 30 T2D, duration >=2 years, no renal impairment; UCPCR >=0.28 nmol/nmol: sensitivity 97%, specificity 88% to identify T2D. Matches. |
| 31 | Funakoshi (24843502) | 201 Japanese T2D patients, retrospective; CPR indices compared between a group requiring insulin and one not requiring it to reach target. It concerns who needs insulin, not safe withdrawal; reword. Year 2011. |

Not content-checked (identity only): rows 5 (Salehi, Lupoli), 19, 25, 27 (39994886, 38895780), 32 (Balasubramanyam), 39 (Katznelson), 41, 45 postpartum cohorts.

## 2.4 Newly read primary sources and what they change

1. **ADA Standards 2026 Section 2 (PMID 41358893, PMC12690183), raw HTML.** It reproduces the Holt algorithm: C-peptide "only indicated in people receiving insulin treatment"; random sample within 5 h of eating; >=600 pmol/L (>=1.8 ng/mL) circumstances do not matter; <80 pmol/L (<0.24 ng/mL) no repeat; "C-peptide must be measured prior to insulin discontinuation to exclude severe insulin deficiency"; "Do not test C-peptide within 2 weeks of a hyperglycemic emergency"; 200-600 pmol/L usually T1D or MODY but may be insulin-treated T2D. This closes the file's "ADA Section 2 unread" gap: **rows 6 and 31 now have two independent consensus sources and "established" stands.** It also lists "severe insulin resistance in the absence of obesity" among features prompting monogenic testing (clinical, no assay), and describes fulminant checkpoint-inhibitor diabetes with "low or undetectable levels of C-peptide as a marker of endogenous beta-cell function" (descriptive, not a recommendation).
2. **ADA Standards 2026 Section 9 (PMC12690185).** States there are "no approved therapies for preservation of C-peptide ... in individuals with established stage 3 type 1 diabetes" and that teplizumab "is not indicated for those with established stage 3 type 1 diabetes". This conflicts on its face with the FDA label (rev 06/2026) read in Part 1, which has a Stage 3 pediatric indication. The conflict is chronological: the ADA Standards were published December 2025; the Stage 3 accelerated approval is in the 06/2026 supplement. Row 29 should note that ADA 2026 predates and does not endorse the Stage 3 indication, which is an accelerated approval on a surrogate (C-peptide decline). The same section says higher C-peptide is associated with better A1C and lower retinopathy, nephropathy and severe hypoglycaemia (descriptive association).
3. **Whole AASLD 2023 (PMC10735173)** searched end to end: no HOMA-IR, fasting insulin or C-peptide recommendation outside reference titles. Row 14's partial-negative caveat can be removed.
4. Not re-read: ISPAD 2022 classification (not in PMC; Wiley 403), ISPAD CFRD and monogenic list items, PMDI neonatal rows (the Table 3 C-peptide wording was read and matches). Rows 19, 33 and 34 stand on the reviewers' reads.

## 2.5 Missing uses (sourced) and negatives

Search strings (PubMed via NCBI esearch/esummary and the PubMed connector; WebSearch for OPTN; raw PMC HTML for texts):
- `fulminant type 1 diabetes[Title] AND (criteria OR guideline OR consensus)` (34 hits); `Japan Diabetes Society fulminant type 1 diabetes diagnostic criteria revised` (1 hit, PMID 24843620); `slowly progressive insulin-dependent type 1 diabetes diagnostic criteria Japan Diabetes Society` (4 hits; PMIDs 38264233 and 38184802 are the 2023 criteria).
- `immune checkpoint inhibitor diabetes guideline C-peptide diagnosis recommendations` (0 hits); `pancreas transplant candidate selection C-peptide type 1 diabetes recommendations review` (0 hits). The connector ANDs every term, so these zeros are not evidence of absence.
- WebSearch: `OPTN policy 11 pancreas transplant candidate C-peptide ≤ 2 ng/mL eligibility simultaneous pancreas kidney`.
- Raw-text greps for "C-peptide" in ADA Standards 2026 sections 2, 9, 11 and 14-adjacent PMC12690182 / PMC12690176 (the last two had no mention).

Additions I can source:

| Proposed row | Use | Test | Status | Source and read level |
|---|---|---|---|---|
| A | Fulminant type 1 diabetes (ketoacidosis soon after hyperglycaemic symptoms, near-normal HbA1c) | Urinary C-peptide <10 ug/day, or fasting serum C-peptide <0.3 ng/mL (<0.10 nmol/L) and <0.5 ng/mL (<0.17 nmol/L) after glucagon or a meal, at onset; criterion 3 of three | Classification. **Limited**: national (Japan) expert criteria; no accuracy data read | Imagawa et al., Japan Diabetes Society committee, J Diabetes Investig 2012, PMID 24843620 (PMC4015434), full text read. |
| B | Slowly progressive type 1 diabetes (SPIDDM) | Fasting serum C-peptide <0.6 ng/mL defines progression to an insulin-dependent state; SPIDDM is "confirmed when a patient progresses" to it | Classification. **Limited**: national expert criteria (2023) | Japan Diabetes Society Committee on T1D, J Diabetes Investig 2024, PMID 38184802 (PMC10804889), full text read; Diabetol Int copy PMID 38264233, not read. |

Both are the same kind of use as row 6 and were missed by all three reviewers. I found no Western guideline using a C-peptide cut-off for fulminant T1D.

Found but not added:
- OPTN kidney-pancreas candidacy: a WebSearch summary (secondary; OPTN pages returned 403/redirect) says waiting-time qualification required insulin treatment plus C-peptide <=2 ng/mL (or >2 with BMI <=30) from the 2014 allocation system, and that BMI and C-peptide were removed from waiting-time criteria on 2019-07-11 (Board approval June 2018). If right, this is a withdrawn regulatory use. I could not read the OPTN policy text, so it is not added; it needs a primary read of the OPTN board report and Policy 11.
- Checkpoint-inhibitor diabetes: ADA s2 is descriptive; Baden 2019 (PMID 30800564) is a 22-patient national survey. Not a use row.
- C-peptide-based pump/AID eligibility is a coverage rule (out of scope).
- No further sourced uses found; absence is search-limited.

## 2.6 Consolidated summary (Parts 1 and 2)

Top problems
1. Two wrong "open conflicts" in the file: ADA Rec 3.13 does say "evidence of insulin resistance and prediabetes", and the IRIS top-quartile sentence is cited (refs 19, 20). ADA 3.13 and AACE R 9.4 name insulin resistance as a condition; neither names an assay or threshold.
2. Row 4 omits the HI guideline Table 1 insulin (>1.25 uU/mL) and C-peptide (>0.5 ng/mL) values and uses older BOHB/FFA cut-offs; neonatal limit is 48 h in PES and 72 h (retest) in the HI guideline.
3. Row 10: Igls 2018 gives no numeric "clinically significant" C-peptide threshold; it questions fasting <0.3 and postprandial <0.6 ng/mL.
4. Rows 20 and 21 are "established" on abstract-level 2026 case material.
5. Attribution slips: "<200 pmol/L" is Jones 2013, not Holt; Funakoshi concerns who needs insulin, not stopping it; DSS/ABCD naming is partly unresolved.
6. Row 29 relies on a 06/2026 label supplement that ADA Standards 2026 (Dec 2025) predates and contradicts on its face; say so.
7. Coverage gaps: two sourced Japanese classification uses (rows A, B) missed; OPTN historical criterion needs a primary read.

Statuses I would change
- Rows 20, 21: Established -> Limited (or Established with an explicit "expert practice, case-series level" caveat).
- Rows 6, 31: keep Established; add ADA Standards 2026 s2 as a second source.
- Row 8: keep Research-only for routine care; cross-reference row 29 as a regulatory surrogate use.
- Rows 12, 14: status unchanged; fix wording (JDS value "may depend on" treatment; add the Delphi paper).
- New rows A and B: Limited.
- No insulin-resistance row moves above Limited.

Confidence in the list as a whole
- High for the insulin-resistance verdict (every IR row is limited, research-only or unsupported, and the primary wordings I read agree).
- Moderate-high for the guideline-backed established rows read at raw-text level (1 via ENETS, 4, 6, 7, 10, 29, 31).
- Moderate-low for rows resting on abstracts, titles or secondary reads not re-opened (5, 11, 19, 25, 27, 32, 34, 35 cohorts, 39-45) and for absence claims, which are search-limited.
- Not verified: ISPAD classification/CFRD/monogenic wording, AAP 2023, OPTN Policy 11 text, Cryer 2009 full text (thresholds only second-hand via ENETS).
