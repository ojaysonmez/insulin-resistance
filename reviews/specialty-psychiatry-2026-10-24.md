# Specialty review: psychiatry (2026-10-24)

Scope. Psychiatry view of `merged-conclusion.md` (scope note read first: bottom lines cover fasting insulin, HOMA-IR, TyG and TG/HDL-C; post-load and C-peptide were not weighed as predictors), the psychiatric row of `usecases-verified.md` (row 43, plus the absence notes at its lines 140 and 165), `reviews/scope-audit.md` (psychiatry entries), and `reviews/skeptic-merged.md` and `reviews/skeptic-steelman.md` for what was already corrected. Analysis reports were not read. Other specialty reports were not read; while listing `reviews/` to check the file layout, the first five lines (title and scope paragraph) of `reviews/specialty-cardiology-2026-10-23.md` were displayed, and nothing beyond them was read. No deliverable, score file or claims file was edited.

Assumptions and limits.
- Look-up limit 20 (task prompt). I used 20 (log in section 6). Two of those were failed downloads.
- The web-fetch tool returns query-focused excerpts of the full page, not the whole document. "Excerpts of full text" means that; it never means read end to end. A "not found" from me means not found in the excerpts retrieved.
- Measure-type codes: F = fasting insulin or HOMA-IR; T = TyG or TG/HDL-C; P = post-load (OGTT insulin or glucose, OGTT-derived index); C = C-peptide; G = glucose or HbA1c only (no insulin); MIX = composite definition mixing these.
- Confidence figures are judgements, not computations.
- No DOI is given in the PubMed record for the two CAMESA papers (PMIDs 21804853, 21804854, 23115501); PubMed links are given instead.

---

## 1. Specialty and documents checked

| Document | Identifier | Read level | Measure |
|---|---|---|---|
| ADA/APA/AACE/NAASO 2004 consensus, antipsychotics, obesity and diabetes | PMID 14747245, https://doi.org/10.2337/diacare.27.2.596 | Table 3 (monitoring protocol) seen in two excerpts: the publisher page and a court-filed copy of the article (OCR, CourtListener docket 4225087, doc 1324-11). The publisher full text could not be fetched (fetch error), so it was not read end to end | G |
| APA Practice Guideline for Schizophrenia, 3rd ed., 2020 | PMID 32867516, https://doi.org/10.1176/appi.ajp.2020.177901 | Excerpts of the full guideline PDF (UNC-hosted copy), targeted to insulin, HOMA, metformin, glucose and Table 2. Not read end to end | G |
| NICE CG155 (children and young people, psychosis), monitoring table and recommendations 1.3.x | NICE CG155 (2013, updated) | Excerpts of the NICE web pages | G |
| NICE 2023 exceptional surveillance of CG155 and CG178 | NCBI Bookshelf NBK597541 | Search excerpt only | G |
| NICE CG178 (adults) and CG185 (bipolar) recommendation text | NICE CG178, CG185 | **Not retrieved directly**; adult content known only through the 2023 surveillance excerpt | G |
| CAMESA monitoring guideline (Pringsheim 2011) | PMID 21804853, PMC3143700, https://pubmed.ncbi.nlm.nih.gov/21804853/ (no DOI in record) | Excerpts of PMC full text: Table 1 (grading), Table 3 (laboratory monitoring), Table 4 (monitoring form) and footnotes | F |
| CAMESA management recommendations (Ho 2011) | PMID 21804854 (J Can Acad Child Adolesc Psychiatry, PMC3143701) and PMID 23115501 (Paediatr Child Health, PMC3223901); same title, published twice; no DOI in either record | Excerpts of PMC3223901 (the PMC full-text tool returned empty; the web page was fetched) | F, P |
| AACAP 2011 practice parameter, antipsychotics in children | AACAP web PDF | Search excerpt only | G |
| AHRQ PQMP toolkit, antipsychotics in children (2021) | AHRQ web PDF | Search excerpt only | F, G |
| Maudsley Prescribing Guidelines | not retrieved | [recall] only, unverified | n/a |
| TRIO-BD (Calkin 2022) | PMID 35120288, https://doi.org/10.4088/JCP.21m14022; NCT02519543 | PubMed abstract; ClinicalTrials.gov API record (excerpts: eligibility, outcomes, description). Full text not available to me | F |
| Pioglitazone for unremitted depression (Lin 2015) | PMID 26602230, https://doi.org/10.1016/j.psychres.2015.10.013, PMC4978223 | **Full text** (PMC; tables not shown in the tool output) | MIX |
| Calkin 2015, IR and outcome in bipolar disorder | PMID 25323142, https://doi.org/10.1192/bjp.bp.114.152850 | Abstract | F |
| Pillinger 2017, glucose homeostasis in first-episode schizophrenia (meta-analysis) | PMID 28097367, https://doi.org/10.1001/jamapsychiatry.2016.3803 | Abstract | F, P, G |
| Greenhalgh 2017, antipsychotic-naive non-affective psychosis (meta-analysis) | PMID 27743650, https://doi.org/10.1016/j.schres.2016.09.026 | Abstract | F, P, G |
| Metformin trials for antipsychotic weight gain or metabolic change (11 records) | listed in section 3.4 | Abstracts | F (as outcome) |
| SNIFF intranasal insulin trial (Craft 2020) | PMID 32568367, https://doi.org/10.1001/jamaneurol.2020.1840 | Abstract | none (insulin as treatment) |
| Intranasal detemir (Claxton 2015) | PMID 25374101, https://doi.org/10.3233/JAD-141791 | Abstract | unspecified IR measure |
| Rosiglitazone pilot (Watson 2005); liraglutide fMRI (Watson 2018); extracellular-vesicle IR biomarkers (Mustapic 2019) | PMID 16286438, https://doi.org/10.1176/appi.ajgp.13.11.950; PMID 30099030, https://doi.org/10.1016/j.bbr.2018.08.006; PMID 30958348, https://doi.org/10.3233/JAD-180578 | Abstracts | none / G / neuronal EV markers |

---

## 2. Claims checked and verdicts

| # | Claim (location) | Source checked | Verdict | Reason |
|---|---|---|---|---|
| 1 | Row 43: antipsychotic metabolic monitoring uses no insulin or C-peptide test; "Not evaluated (original guideline blocked; secondary summaries only)" (`usecases-verified.md` row 43) | ADA/APA 2004 Table 3 (excerpts, two copies); APA 2020 Table 2 (excerpts); NICE CG155 table (excerpts) | **Holds for adults, needs correction for children; status can be upgraded** | ADA/APA 2004 Table 3 lists personal/family history, weight (BMI), waist, blood pressure, fasting plasma glucose and fasting lipid profile at baseline, 4, 8 and 12 weeks, quarterly, annually and every 5 years; no insulin, HOMA or C-peptide (G). APA 2020 Table 2: fasting blood glucose or HbA1c at baseline, at 4 months after a new treatment and at least annually; insulin resistance appears only as a clinical risk factor ("clinical conditions associated with insulin resistance (e.g., severe obesity, acanthosis nigricans)") and as a mechanism ("some patients ... develop insulin resistance early in the course of antipsychotic treatment"), never as a test (G). NICE CG155: fasting blood glucose or HbA1c and lipid profile at baseline, 12 weeks and every 6 months (G). The table itself has now been seen, so "original blocked" no longer applies to Table 3. **But** the Canadian paediatric CAMESA guideline (2011) recommends fasting insulin (F) in antipsychotic monitoring (claim 3). So "no insulin test found for antipsychotics" (`usecases-verified.md` line 165) is false for paediatric guidance. |
| 2 | "No guideline read requires a fasting insulin, HOMA-IR or OGTT-derived estimate, or ties one to a change in treatment" (merged, "What is well supported", first bullet) | CAMESA 2011 (PMID 21804853, Table 3, Table 4 footnote 7); CAMESA management (PMID 21804854 / 23115501) | **Needs correction** (true for the guidelines the team read; not true for psychiatric paediatric guidance) | CAMESA Table 3 grades fasting insulin monitoring by drug and time point: olanzapine "STRONG 1A" at baseline and 3 months; risperidone, quetiapine and clozapine "WEAK 3"; aripiprazole "Not recommended" at all time points; ziprasidone "WEAK 3" at baseline only. Table 4 gives a normal value of "≤ 100 pmol/L" with the footnote "For fasting insulin levels >100pmol/L, consideration should be given to performing an OGTT. Normal reference range may vary between centres." The management paper says: "If the fasting insulin is above the upper limit of normal for the assay being used, consider the oral glucose tolerance test (OGTT) and specialist consultation (Grade of recommendation: 3)." So a guideline does require fasting insulin (for olanzapine, strongly graded) and ties a high value to a change in **work-up** (OGTT and referral). It does not tie it to a change in **treatment**: metformin is suggested for impaired fasting glucose (6.1 to 6.9 mmol/L), not for high insulin. Caveats a psychiatrist would add: (a) CAMESA's Table 1 grades the evidence "that the specific side effect occurs", not evidence that monitoring improves outcomes, so "STRONG 1A" means "olanzapine raises insulin in RCTs", not "measuring insulin helps"; (b) the action step is grade 3 (expert opinion); (c) the guideline itself flags assay dependence ("reference range may vary between centres"), which matches the project's measurement findings; (d) it is 2011, and I found no update; (e) it conflicts in substance with Endocrine Society 2017 Rec 1.7 against insulin measurement in children evaluated for obesity, although the populations differ (antipsychotic-treated versus obesity work-up). |
| 3 | Bottom line 1: no established clinical utility of routine F/T measurement "in primary care, prediabetes, T2D, PCOS, MASLD or obesity" (merged BL1) | ADA/APA 2004; APA 2020; NICE CG155; CAMESA 2011 | **Holds; missing a psychiatric setting and caveat** | Psychiatric adult guidance uses glucose or HbA1c and lipids (G), consistent with BL1. Psychiatry is not named in BL1's list, although people on antipsychotics are one of the largest groups under scheduled metabolic testing. The one exception (CAMESA, paediatric) is a recommendation, not evidence of utility, so it refines BL1 rather than reversing it. |
| 4 | TRIO-BD: "the published primary is a post-randomisation split of metformin-arm 'converters' vs non-converters; the randomised metformin-vs-placebo MADRS contrast is not in the abstract and not checked. Hypothesis-generating at most." (merged, Psychiatry bullet) | PMID 35120288 abstract; NCT02519543 registry record | **Holds; missing caveats** | Abstract confirms: the primary outcome was MADRS change at 14 weeks "between those who no longer met IR criteria (converters) and those who still did (non-converters)"; 10 of 20 on metformin and 1 of 25 on placebo converted. Additions: (a) measure is F: entry required "HOMA-IR ≥ 1.8" (registry eligibility), a low threshold, and conversion was defined by HOMA-IR; (b) the registry's detailed description says the investigators "will compare the effects of treating IR (with metformin) versus placebo", and the registered primary outcome is whether "the effect of metformin on improvement in MADRS scores at week 14 is mediated by conversion of IR to insulin sensitivity (determined using ... HOMA-IR)"; the published primary (converters versus non-converters, pooled across arms) is not that randomised or mediation contrast, so possible outcome-reporting deviation should be noted (registry seen as excerpts; the version history was not checked); (c) with a within-person CV of about 27% for HOMA-IR (the project's EuBIVAS figure), "conversion" across a 1.8 cutoff in a single repeat sample is partly regression to the mean and measurement noise, and converters are a post-randomisation selected group, so the converter contrast is confounded by whatever made people both convert and improve (adherence, weight loss, mood itself). |
| 5 | Pioglitazone in depression (PMID 26602230): "a within-treatment association with post-randomisation change in glucose metabolism, not a baseline-IR x treatment interaction" (merged, Psychiatry bullet; `reviews/skeptic-steelman.md`) | Full text, PMC4978223 | **Needs correction** (the abstract-level reading missed a baseline-stratified comparison) | The full text states two a priori aims; aim 2 compared treatment outcomes "between IR and insulin sensitive (IS) participants" defined at baseline. Results: overall no difference (HDRS decline 24% versus 23%, t(29) = -1.22, P = 0.23); within the baseline-IR group, "the active IR group declined in HDRS-21 scores an average of 7.15 points more than that of the placebo IR group" after age adjustment; no difference between active and placebo IS groups. So it **is** a baseline-IR-stratified randomised comparison. It remains very weak: (a) cells of about 9 and 6 participants (t-test df 8 and 5); (b) no formal interaction P value in the text read (tables not visible to me); (c) baseline HDRS and OGTT differed between arms; (d) the placebo-IR cell (n about 6) not improving drives the contrast; (e) metabolic data were multiply imputed; (f) the IR definition is MIX: any of fasting glucose ≥ 100 mg/dL, 2-hour OGTT glucose ≥ 140 mg/dL, fasting insulin ≥ 15 mIU/L, or HOMA-IR > 3.8, so a glucose-only definition would have classified most of the same people and the result cannot be attributed to insulin measurement. "Hypothesis-generating at most" still holds. |
| 6 | "Not tested by anyone ... randomised trials selecting or stratifying by fasting insulin or HOMA-IR in dementia" (merged, steelman section) | PubMed search P19 (5 records) | **Holds, with one addition** | No randomised dementia trial that selected or stratified by F was found. Closest: intranasal detemir (Claxton 2015, n = 60, three arms) reports "higher insulin resistance at baseline predicted greater improvement with the 40 IU dose (r = 0.54, p < 0.02)" (abstract; IR measure not named in the abstract; MeSH lists glucose tolerance test), a within-arm correlation in about 19 people, not a stratified or interaction test. The larger SNIFF trial (n = 289, PMID 32568367) was null overall and did not select by IR (abstract). Search was narrow (one string), so this is "not found", not absence. |
| 7 | Scope audit lists TRIO-BD and pioglitazone-depression as UNSPECIFIED measure (`reviews/scope-audit.md`, UNSPECIFIED list) | Registry record; full text | **Can now be specified** | TRIO-BD: F (HOMA-IR ≥ 1.8 entry; HOMA-IR conversion). Pioglitazone-depression: MIX (fasting glucose, 2-hour OGTT glucose, fasting insulin, HOMA-IR; any one criterion). |
| 8 | Steelman table (`reviews/steelman.md` row 8, cited in scope audit): TRIO-BD is a "new setting (psychiatry) with IR-defined entry and IR reversal as the mediator" | Registry; abstract | **Missing caveat** | IR-defined entry is correct (HOMA-IR ≥ 1.8). "IR reversal as the mediator" was the registered aim but the published analysis is not a formal mediation analysis in the abstract; the abstract's own language ("offers a path out of TRBD") is stronger than the design supports. |

Confidence figures. Psychiatric evidence does not move BL1 (80-85%) for adults: four psychiatric monitoring documents other than CAMESA use G only (adult: ADA/APA 2004, APA 2020, NICE via its 2023 surveillance; paediatric: NICE CG155 and the AACAP 2011 excerpt). For paediatric antipsychotic monitoring a guideline does recommend F, so BL1's "no guideline" support is weaker there, but utility (better outcomes from measuring) is still not shown, so I would not lower BL1's figure, only add the exception. BL2 (about 40% for F that "shown not to add value" is true): psychiatry has no incremental-value or adequately powered interaction study, so it neither raises nor lowers the figure.

---

## 3. Missed evidence

### 3.1 CAMESA 2011 paediatric guideline recommends fasting insulin (F)
Covered in claim 2. This is the one psychiatric guideline found that makes fasting insulin part of scheduled monitoring and attaches an action to it. It is still listed by AHRQ's 2021 PQMP toolkit as one of eight guidelines on metabolic monitoring of children prescribed antipsychotics (search excerpt: "fasting glucose, fasting insulin, and fasting lipid profile ... Fasting insulin is not recommended for youth on aripiprazole but is appropriate for all other AAAs"), and its documents are hosted by BC Children's Hospital in files dated 2024-2025 (search excerpts), so it appears to remain in use. Whether CAMESA has been formally updated was not checked.

Relevance to the project: it weakens the absence claim "no insulin test found" for antipsychotics (`usecases-verified.md` line 165) and the "no guideline requires" sentence. It does not strengthen the case for utility, because its grading measures evidence of harm, not of benefit from measuring.

### 3.2 IR in drug-naive psychosis (F, P, G)
Two meta-analyses show that people with first-episode, antipsychotic-naive schizophrenia already have higher fasting insulin and HOMA-IR than controls:
- Pillinger 2017 (PMID 28097367, abstract): 16 studies, 731 patients; fasting insulin g = 0.41 (0.09 to 0.72), HOMA-IR g = 0.35 (0.14 to 0.55), 2-hour OGTT glucose g = 0.61, fasting glucose g = 0.20, HbA1c g = -0.08 (not different).
- Greenhalgh 2017 (PMID 27743650, abstract), cited in APA 2020's reference list: effect sizes 0.21 to 0.58 across fasting glucose, 2-hour glucose, insulin and IR.

Relevance: this is the strongest psychiatric argument **for** insulin-based measures. HbA1c, which APA 2020 and NICE allow as the only glycaemic test, does not detect the early defect, while post-load glucose (P) shows it most clearly. The meta-analyses are group-level associations and do not show that measuring insulin in an individual changes management or outcome. They argue more for OGTT glucose than for fasting insulin.

### 3.3 IR and course of bipolar disorder (F)
Calkin 2015 (PMID 25323142, abstract): fasting glucose and insulin in 121 adults with bipolar disorder; IR or T2D was associated with chronic course (OR 3.07), rapid cycling (OR 3.13) and lithium non-response (OR 8.40; 36.7% versus 3.2%), robust to antipsychotic exposure and BMI in sensitivity analyses. Cross-sectional, single centre, retrospective life-chart course ratings, HOMA-IR threshold not stated in the abstract ([recall]: 1.8, matching TRIO-BD's entry; unverified). This is the background for TRIO-BD and the strongest prognostic association in psychiatry, but it is association, not incremental prediction and not treatment selection.

### 3.4 Metformin for antipsychotic-induced weight gain: IR is an outcome, not a selector
Eleven randomised trials found by P15 (abstracts) use fasting insulin or HOMA-IR (F) as an outcome or co-primary outcome: Wu 2008 (PMID 18245179, https://doi.org/10.1176/appi.ajp.2007.07010079), Wu 2016 pooled analysis (PMID 26809842, https://doi.org/10.1038/mp.2015.221; a Chinese-language version of the same pooled data is PMID 31857506, https://doi.org/10.11817/j.issn.1672-7347.2019.180379), Wang 2012 (PMID 22398127, https://doi.org/10.1016/j.schres.2012.02.021), Baptista 2006 (PMID 16618011, https://doi.org/10.1177/070674370605100310), Baptista 2007 (PMID 17490862, https://doi.org/10.1016/j.schres.2007.03.029), Carrizo 2009 (PMID 19515536, https://doi.org/10.1016/j.schres.2009.05.007), Klein 2006, paediatric (PMID 17151157, https://doi.org/10.1176/ajp.2006.163.12.2072), Rado 2016 (PMID 26872112, https://doi.org/10.1097/JCP.0000000000000469; HOMA-IR co-primary), and two 2026 active-comparator trials (empagliflozin, PMID 42135901, https://doi.org/10.1002/hup.70047; topiramate, PMID 42550195, https://doi.org/10.1007/s00406-026-02319-6). None of the abstracts reports selection by, or a treatment-by-baseline interaction with, fasting insulin or HOMA-IR. The guideline selectors for metformin are weight gain (APA 2020: metformin "has been shown to be safe in individuals without hyperglycemia") and deteriorating HbA1c or fasting glucose (NICE 2023 surveillance excerpt quoting a recommendation 1.19.1, apparently from another NICE guideline; source guideline not identified by me). So in psychiatry the treatment decision is driven by weight and glucose (G), consistent with the merged conclusion.

Klein 2006 is a small exception in kind: baseline "elevated ... fasting glucose and insulin values" identified two subjects with overt diabetes, and post-study OGTT found three more with impaired glucose tolerance in the placebo arm (abstract). This is case detection by glucose testing, with insulin incidental.

### 3.5 Dementia and cognitive decline
See claim 6. Additional items found: Watson 2005 rosiglitazone pilot (n = 30, PMID 16286438) and Watson 2018 liraglutide fMRI study (PMID 30099030) both cite IR as rationale but neither selected or stratified by an insulin measure (abstracts). Mustapic 2019 (PMID 30958348) used neuronal extracellular-vesicle IRS-1 phosphorylation as "brain insulin resistance" markers; this is a different construct from peripheral F/T measures and should not be merged with them.

### 3.6 Practical measurement problems specific to psychiatric settings
- Fasting is a barrier: APA 2020 allows HbA1c as an alternative to fasting glucose; CAMESA notes that some scheduled bloods "require a twelve hour fast"; a Canadian family-practice review (Lambert 2018, Can Fam Physician 64:660; search excerpt only, PMID not verified) states that "the fasting, scheduling, and venipuncture pain associated with fasting glucose and triglyceride tests make monitoring in children and adolescents challenging". Fasting insulin adds a fasting-dependent test to a population where monitoring rates are already low (APA 2020 cites low follow-up testing; a 2025 quality-improvement study, PMC12336612, search excerpt, reported under 5% meeting guideline monitoring in 2020).
- Antipsychotics change insulin sensitivity within weeks (APA 2020 text; CAMESA olanzapine RCT data: insulin +2.71 µIU/mL), so a single baseline value is a moving target. This sharpens the project's point that one fasting insulin or HOMA-IR cannot detect individual change (within-person CV about 27%).

---

## 4. Overreach risks

1. **Citing TRIO-BD as evidence for IR-guided psychiatric treatment.** Its published contrast is post-randomisation (converters versus non-converters), its registered randomised or mediation contrast is not reported in the abstract, and "conversion" across HOMA-IR 1.8 is vulnerable to measurement noise. The authors' "offers a path out of TRBD" should not be repeated.
2. **Citing pioglitazone-depression as an insulin-measurement finding.** The IR groups were defined by a composite in which glucose criteria alone would do most of the work; the subgroup cells were about 6 to 9 people.
3. **Over-reading CAMESA's "STRONG 1A".** It grades evidence that olanzapine raises insulin, not that measuring insulin helps. If the main session adds CAMESA, it should say so in the same sentence.
4. **Treating "IR is common in psychiatric illness" as support for measuring it.** The association data (Pillinger, Greenhalgh, Calkin 2015) are real but group-level; none tests incremental value over BMI, glucose or HbA1c, or measurement-guided care.
5. **Mixing peripheral and "brain insulin resistance".** Neuronal-vesicle markers and intranasal-insulin trials are not about fasting insulin or HOMA-IR and should stay out of the measurement conclusion.
6. **Absence wording.** "No insulin test found for antipsychotics" is now contradicted for children; the remaining adult absence rests on four documents read as excerpts, not end to end, and on no direct reading of NICE CG178 or Maudsley.

---

## 5. Suggested changes (exact sentences, not applied)

S1. `merged-conclusion.md`, "What is well supported", first bullet. Replace the first sentence with:
> "No adult guideline read requires a fasting insulin, HOMA-IR or OGTT-derived estimate, or ties one to a change in treatment. One paediatric psychiatric guideline does require fasting insulin: the Canadian CAMESA guideline for children on second-generation antipsychotics (2011; PMID 21804853, PMC full-text excerpts) recommends fasting insulin at baseline and 3 months for olanzapine (graded 'STRONG 1A', a grade for evidence that the side effect occurs, not for benefit of monitoring) and weakly for risperidone, quetiapine and clozapine, and its management paper (PMID 21804854; republished as PMID 23115501) advises an OGTT and specialist consultation when fasting insulin is above the assay's upper limit (grade 3). This changes work-up, not treatment; metformin is tied to impaired fasting glucose."

S2. `merged-conclusion.md`, bottom line 1, after "in primary care, prediabetes, T2D, PCOS, MASLD or obesity". Add:
> "This also holds for metabolic monitoring of adults taking antipsychotics: ADA/APA 2004 (Table 3), APA 2020 (Table 2) and NICE use glucose or HbA1c and lipids, not insulin (excerpts read). The paediatric CAMESA guideline is the exception noted below."

S3. `merged-conclusion.md`, Psychiatry bullet, replace the pioglitazone sentence with:
> "Pioglitazone in depression (PMID 26602230, full text, n = 37): the overall comparison was null (24% versus 23% HDRS decline); a prespecified comparison by baseline IR status found a 7.15-point greater decline with pioglitazone than placebo in the IR group (about 9 versus 6 participants; no interaction P value seen) and none in the insulin-sensitive group. IR was defined by any of fasting glucose ≥ 100 mg/dL, 2-hour OGTT glucose ≥ 140 mg/dL, fasting insulin ≥ 15 mIU/L or HOMA-IR > 3.8, so the result cannot be attributed to insulin measurement. Hypothesis-generating at most."

S4. `merged-conclusion.md`, Psychiatry bullet, append to the TRIO-BD sentence:
> "Entry required HOMA-IR ≥ 1.8 (fasting-based), and 'conversion' was a single repeat HOMA-IR below 1.8, which a within-person CV of about 27% makes partly noise. The registry (NCT02519543) frames the primary outcome as metformin versus placebo, mediated by HOMA-IR conversion; the published primary pools converters across arms, so the registered contrast should be checked before TRIO-BD is cited."

S5. `usecases-verified.md`, row 43, evidence-status and notes cells. Replace "Not evaluated (original guideline blocked; secondary summaries only, not read at source)" with:
> "Unsupported for adults (ADA/APA 2004 Table 3 seen in publisher and court-filed excerpts; APA 2020 Table 2 and NICE CG155 excerpts: glucose or HbA1c, lipids, weight, waist, BP; no insulin or C-peptide). Paediatric exception: CAMESA 2011 recommends fasting insulin for most SGAs and an OGTT if it is high (see new row)."

S6. `usecases-verified.md`, new row proposed for the use-case reviewers (I did not verify it as a use-case reviewer):
> "Paediatric antipsychotic monitoring (CAMESA) | Fasting insulin (fasting-based) | OGTT and specialist referral if above assay upper limit | IR | Limited (one national guideline, 2011; grading reflects evidence of harm, not benefit of monitoring; action step grade 3) | PMIDs 21804853, 21804854, 23115501; PMC excerpts | Conflicts in substance with Endocrine Society 2017 Rec 1.7 (no insulin in paediatric obesity work-up); assay-dependent normal value ≤ 100 pmol/L"

S7. `usecases-verified.md`, line 165. Replace "'no insulin test found' for antipsychotics" with:
> "'no insulin test found' for adult antipsychotic monitoring (the paediatric CAMESA guideline does use fasting insulin)"

S8. `reviews/scope-audit.md` (if the main session updates it), UNSPECIFIED list: move TRIO-BD to FASTING and pioglitazone-depression to MIXED (composite of fasting glucose, 2-hour OGTT glucose, fasting insulin and HOMA-IR).

S9. `merged-conclusion.md`, "Not tested by anyone", dementia clause. Append:
> "The closest item is a within-arm correlation between baseline insulin resistance and response to intranasal insulin detemir (Claxton 2015, PMID 25374101, abstract, r = 0.54 in about 19 people; IR measure not named in the abstract), not a stratified or interaction test."

---

## 6. Search log (20 look-ups; counts as returned)

| # | Database / tool | String or target | Result |
|---|---|---|---|
| 1 | PubMed metadata | PMIDs 35120288, 26602230, 14747245, 32867516, 28097367, 34585948, 18212312, 32568367 | 8 records. Two of my recalled PMIDs were wrong: 34585948 is a Pseudomonas paper, 18212312 a homocysteine letter; neither is cited |
| 2 | PubMed Central full text | PMC4978223 (pioglitazone-depression) | Full text returned, tables not shown |
| 3 | ClinicalTrials.gov API (web fetch) | NCT02519543 | Record excerpts: eligibility HOMA-IR ≥ 1.8, primary outcome, description, references |
| 4 | Web fetch | diabetesjournals.org ADA/APA 2004 article page | Fetch error, nothing returned |
| 5 | Web search | "ADA APA 2004 consensus antipsychotic monitoring protocol fasting plasma glucose table"; "\"Consensus development conference on antipsychotic drugs and obesity and diabetes\" insulin resistance"; "antipsychotic consensus 2004 \"insulin resistance\" clamp monitoring J Clin Psychiatry 2004 65 267" | 10 results; Table 3 seen in publisher-page and court-filed copy excerpts |
| 6 | Web search | "APA practice guideline schizophrenia 2020 Table 2 suggested physical and laboratory assessments fasting plasma glucose hemoglobin A1C"; "APA schizophrenia guideline 2020 metabolic monitoring \"insulin\""; "psychiatryonline schizophrenia guideline third edition laboratory assessments antipsychotic" | 10 results; UNC-hosted PDF found |
| 7 | Web fetch | UNC-hosted APA 2020 PDF, queries "insulin resistance", "metformin weight gain", "Table 2 fasting blood glucose hemoglobin A1C", "HOMA" | Excerpts; no insulin or HOMA test found in them |
| 8 | curl (two attempts) | Same PDF, to scan locally | Both failed TLS verification through the proxy; nothing downloaded |
| 9 | Web search | "NICE CG178 1.3.6.1 before starting antipsychotic medication baseline investigations fasting blood glucose HbA1c"; "NICE CG185 bipolar disorder physical health monitoring HbA1c lipid profile annually"; "NICE CG155 children young people psychosis antipsychotic baseline prolactin fasting glucose" | 10 results; CG155 table and 2023 surveillance excerpts; CG178 and CG185 pages not returned |
| 10 | Web search | "CAMESA guideline monitoring second-generation antipsychotics children fasting insulin"; "Pringsheim 2011 Paediatr Child Health antipsychotic monitoring fasting plasma glucose insulin lipid"; "pediatric antipsychotic metabolic monitoring guideline HOMA-IR insulin recommended" | 10 results; CAMESA fasting insulin recommendation found |
| 11 | PubMed Central full text | PMC3223901 (CAMESA management) | Empty full text, abstract only |
| 12 | Web fetch | PMC3223901 and PMC3143700 pages | Excerpts: fasting insulin action text, Table 1, Table 3, Table 4 and footnotes |
| 13 | PubMed | `Pringsheim T[Author] AND second generation antipsychotics AND children AND monitoring AND 2011[dp]` | 5 records (23115503, 23115502, 23115501, 21804854, 21804853) |
| 14 | PubMed metadata | 21804854, 21804853, 23115501, 25323142, 27743650 | 5 records; no DOI in the CAMESA records |
| 15 | PubMed | `metformin AND (antipsychotic OR clozapine OR olanzapine) AND randomized controlled trial[pt] AND ("insulin resistance" OR HOMA-IR) AND (baseline OR subgroup OR moderat* OR predict*)` | 11 records, all screened at abstract level; none IR-selected or IR-stratified |
| 16 | PubMed metadata | the 11 PMIDs from #15 | 11 records |
| 17 | PubMed | `("insulin resistance" OR HOMA-IR OR "triglyceride-glucose") AND (depress*) AND (antidepressant response OR treatment response OR treatment-resistant OR incident) AND (cohort OR prospective OR trial)`, relevance sort | 271 records; top 20 PMIDs returned |
| 18 | PubMed metadata | top 8 of #17 | 8 records; none relevant (PCOS, sleep, NHANES androgens, myo-inositol, a GLP-1 review). The string was too loose; this is **not searched effectively**, not an absence |
| 19 | PubMed | `(Alzheimer OR "mild cognitive impairment" OR dementia) AND (pioglitazone OR metformin OR liraglutide OR "intranasal insulin" OR rosiglitazone) AND randomized controlled trial[pt] AND (HOMA OR "insulin resistance" OR "fasting insulin") AND (subgroup OR stratif OR moderat OR baseline)` | 5 records |
| 20 | PubMed metadata | the 5 PMIDs from #19 | 5 records, screened at abstract level |

Not searched (limit reached): Maudsley Prescribing Guidelines; NICE CG178 and CG185 recommendation pages directly; BAP and RANZCP schizophrenia or bipolar guidelines; CANMAT/ISBD bipolar guideline metabolic monitoring; the ESC/EPA/EASD 2009 position statement on cardiovascular disease in severe mental illness; prospective cohorts of IR predicting incident depression (for example NESDA; [recall] that such a paper exists, not verified); IR as a predictor of antidepressant or lithium response beyond Calkin 2015; ketamine or ECT with baseline IR; Embase, PsycINFO, Cochrane and trial registries other than one ClinicalTrials.gov record.

---

## 7. Open questions and what could not be retrieved

Open questions
1. Does TRIO-BD's full text report the randomised metformin-versus-placebo MADRS contrast, and does the registry history show the primary outcome changing? (Full text not available to me; registry history not checked.)
2. Does the pioglitazone-depression paper report a formal treatment-by-IR interaction P value in its tables? (Tables not visible in the PMC tool output.)
3. Has CAMESA been updated or withdrawn since 2011? Is it the guideline used in Canadian paediatric practice today? Does any other paediatric guideline (the AHRQ toolkit mentions eight) also include fasting insulin?
4. Do NICE CG178 (adults) and CG185 (bipolar) recommendation texts, and the Maudsley guidelines, contain any insulin or HOMA test? Expected not ([recall]), unverified.
5. Is there any psychiatric cohort that tests the incremental value of fasting insulin or HOMA-IR over BMI, waist, glucose or HbA1c for incident diabetes in antipsychotic-treated people? None was found; not searched directly.

Could not retrieve
- ADA/APA 2004 consensus full text (publisher fetch error; Table 3 seen only in excerpts).
- APA 2020 guideline as a whole document (excerpts only; a local download failed on TLS).
- NICE CG178 and CG185 recommendation pages; Maudsley Prescribing Guidelines (not open access).
- TRIO-BD full text; CAMESA management paper full text through the PMC tool (web excerpts used instead).
- DOIs for the CAMESA papers (none in the PubMed records).
