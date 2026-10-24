# Specialty review: oncology (2026-10-24)

Reviewer role: specialty reviewer (oncology), subagent. Inputs read: `merged-conclusion.md` (whole file, including the scope note), `reviews/scope-audit.md` (whole file), the oncology-related rows of `usecases-verified.md` (rows 1, 3, 5, 21-24, 40; read by keyword), and the oncology sections of `reviews/skeptic-steelman.md` (problems 2 and 3, plus summary lines) and a keyword scan of `reviews/skeptic-merged.md` (no oncology hits). No analyst reports or other specialty reviews were read. No deliverable, score or claims file was edited.

Budget: 20 PubMed, registry or web look-ups were allowed and 20 were used (log in section 7). Loading tool schemas is not counted.

Assumptions recorded (unattended run):
- A1. "Oncology" covers cancer risk, cancer prognosis, anticancer treatment selection, and metabolic toxicity of anticancer drugs. Insulinoma and non-islet-cell tumour hypoglycaemia are secretion uses that belong to the use-case reviewers; I touch them only where the merged conclusion does.
- A2. Measure tags follow `reviews/scope-audit.md`: FASTING (fasting insulin, HOMA-IR), POSTLOAD, SURROGATE (TyG, TG/HDL-C), CPEPTIDE, UNSPEC. If an abstract does not say whether a sample was fasting, I tag it UNSPEC.
- A3. "Guidance" includes expert consensus (Delphi) and drug-label monitoring text when no ASCO or ESMO guideline on the question was found. I label it as consensus, not guideline.

---

## 1. Documents checked, with read levels

Read level codes: FT = full text read end to end; FT-win = full text, keyword windows only; ABS = PubMed abstract; REG = registry record; WEB = search-engine excerpt only (not read at source); TITLE = title only.

| Source | PMID | DOI | Measure | Read level |
|---|---|---|---|---|
| Goodwin 2022, MA.32 main trial, JAMA | 35608580 | https://doi.org/10.1001/jama.2022.6147 | n/a (primary outcome) | ABS (PMC9131745 exists, not read) |
| Goodwin 2026, MA.32 BMI and metabolic factors as predictors, JNCI Cancer Spectr | 42063220 | https://doi.org/10.1093/jncics/pkag045 | FASTING (central insulin; HOMA with locally measured glucose) | ABS (the skeptic read FT; not re-read here) |
| Goodwin 2021, MA.32 metformin effect on metabolic factors, NPJ Breast Cancer | 34103538 | https://doi.org/10.1038/s41523-021-00275-z | FASTING | ABS |
| Goodwin 2015, MA.32 first 492 patients, JNCI | 25740979 | https://doi.org/10.1093/jnci/djv006 | FASTING | ABS |
| Bonanni 2012, presurgical metformin RCT, JCO | 22564993 | https://doi.org/10.1200/JCO.2011.39.3769 | FASTING (HOMA) | ABS |
| DeCensi 2014, presurgical follow-up, BCRT | 25253174 | https://doi.org/10.1007/s10549-014-3141-1 | FASTING, CPEPTIDE | ABS (the skeptic read FT) |
| Niraula 2012, window study of metformin, BCRT | 22933030 | https://doi.org/10.1007/s10549-012-2223-1 | FASTING | ABS |
| Hadad 2011, window RCT, BCRT | 21655990 | https://doi.org/10.1007/s10549-011-1612-1 | UNSPEC (serum insulin) | ABS |
| Hadad 2015, window RCT biomarkers, BCRT | 25682077 | https://doi.org/10.1007/s10549-015-3307-5 | UNSPEC | ABS |
| Laskov 2014, endometrial window study, Gynecol Oncol | 24972190 | https://doi.org/10.1016/j.ygyno.2014.06.014 | FASTING | ABS |
| Soliman 2016, endometrial window study, Gynecol Oncol | 27745917 | https://doi.org/10.1016/j.ygyno.2016.10.011 | UNSPEC, CPEPTIDE | ABS |
| Gillessen 2025, STAMPEDE metformin arm, Lancet Oncol | 40639383 | https://doi.org/10.1016/S1470-2045(25)00231-1 | none (HbA1c below 6.5% for entry) | ABS (first 2,500 characters; PMC12303861 not read) |
| Fakhri 2026, metformin with ADT meta-analysis, Prostate Cancer Prostatic Dis | 42875601 | https://doi.org/10.1038/s41391-026-01165-w | none (glucose, HbA1c outcomes) | ABS |
| Goodwin 2002, fasting insulin and outcome in early breast cancer, JCO | 11773152 | https://doi.org/10.1200/JCO.2002.20.1.42 | FASTING | ABS |
| Goodwin 2012, time course of insulin prognostic associations, JCO | 22162568 | https://doi.org/10.1200/JCO.2011.36.2723 | FASTING, CPEPTIDE | ABS |
| Duggan 2011, HEAL cohort, HOMA and breast cancer mortality, JCO | 21115858 | https://doi.org/10.1200/JCO.2009.26.4473 | FASTING (HOMA) | ABS |
| Gunter 2009, WHI-OS insulin and breast cancer risk, JNCI | 19116382 | https://doi.org/10.1093/jnci/djn415 | FASTING | ABS |
| Tsujimoto 2017, NHANES hyperinsulinaemia and cancer death, Int J Cancer | 28390156 | https://doi.org/10.1002/ijc.30729 | FASTING (insulin of 10 µU/mL or more) | ABS |
| Albers 2025, Melbourne case-cohort, ER-positive breast cancer, CEBP | 39808164 | https://doi.org/10.1158/1055-9965.EPI-24-1304 | UNSPEC (plasma insulin), CPEPTIDE | ABS |
| Wang 2023, TyG and cancer risk meta-analysis, Front Endocrinol | 36714554 | https://doi.org/10.3389/fendo.2022.1098492 | SURROGATE | ABS |
| Hopkins 2018, insulin feedback and PI3K inhibitors, Nature | 30051890 | https://doi.org/10.1038/s41586-018-0343-4 | mouse insulin and C-peptide (ELISA) | FT (PMC6197057, author manuscript, read end to end including extended-data legends) |
| Gallagher 2024, alpelisib hyperglycaemia and rash, Delphi consensus, NPJ Breast Cancer | 38297009 | https://doi.org/10.1038/s41523-024-00613-x | none (FPG, HbA1c, BMI, age) | FT (PMC10831089, read end to end; supplementary tables not read) |
| Goncalves 2022, management of PI3K-inhibitor hyperglycaemia, Integr Cancer Ther | 35075945 | https://doi.org/10.1177/15347354211073163 | none for testing | ABS, plus WEB excerpt of the PMC page |
| Moore 2024, prevention of PI3K-inhibitor hyperglycaemia, Clin Breast Cancer | 39462728 | https://doi.org/10.1016/j.clbc.2024.09.017 | none (FBG, HbA1c, postprandial glucose) | ABS |
| Shen 2023, MSKCC alpelisib cohort, Cancer | 37743730 | https://doi.org/10.1002/cncr.34928 | none (HbA1c) | ABS |
| Carrillo-Lopez 2024, C-peptide and BMI in alpelisib, Endocrine | 38963515 | https://doi.org/10.1007/s12020-024-03924-y | CPEPTIDE (fasting status not stated in abstract) | ABS |
| Percik 2023, alpelisib hyperinsulinaemia case series, Biologics | 37163178 | https://doi.org/10.2147/BTT.S395817 | UNSPEC (insulin) | ABS |
| Noch 2023, buparlisib in glioblastoma, insulin feedback, Neuro Oncol | 37399061 | https://doi.org/10.1093/neuonc/noad117 | glucose (and tissue insulin-receptor activation) | ABS |
| Vernieri 2021, EVERMET everolimus glycaemia, Clin Cancer Res | 33785482 | https://doi.org/10.1158/1078-0432.CCR-20-4928 | glucose only | ABS |
| TIFA trial, NCT05090358 (MSKCC) | n/a | n/a | glucose and HbA1c eligibility; no insulin selection | REG |
| PMC11558917 (review, hyperglycaemia secondary to PI3K inhibition, 2024) | not resolved | not resolved | none | WEB |
| PMC12161310 (consensus on checkpoint-inhibitor hyperglycaemia; table quoting ASCO 2021 and ESMO 2022) | not resolved | not resolved | CPEPTIDE (non-IR use) | WEB |

ASCO and ESMO guideline documents themselves were not retrieved or read. Everything I say about them comes from secondary sources (WEB) and is unverified.

---

## 2. Claims checked and verdicts

Verdicts: HOLDS; NEEDS CORRECTION; MISSING CAVEAT.

| # | Claim in merged-conclusion.md (short) | Measure | Source checked | Verdict | Reason |
|---|---|---|---|---|---|
| C1 | Bottom line 2: "The oncology interaction trials ... do not lower it: the two oncology trials point in opposite directions and are chance-compatible by their own authors' statements" | FASTING (HOMA, insulin) | 35608580 ABS; 42063220 ABS; 22564993 ABS; 25253174 ABS; plus 34103538 and 25740979 ABS | HOLDS, with a MISSING CAVEAT | The direction and the chance statement agree with the abstracts and with the skeptic's full-text read. Missing caveat: MA.32 also tested whether metformin's *metabolic* effect depends on baseline insulin. Over 6 months metformin lowered insulin (metformin/placebo ratio 0.85) and HOMA (0.83) with "no qualitative interactions with baseline BMI or insulin" (34103538); the first 492 patients showed the same (25740979). So baseline fasting insulin did not modify the outcome or the intermediate metabolic pathway, which makes the null harder to explain away. |
| C2 | Trials table, presurgical metformin row: n=200, Ki-67 at 4 weeks, overall null, P(interaction) 0.045 for HOMA above 2.8, within-subgroup changes not significant, follow-up 0.07 is a different test, C-peptide P = 0.3 | FASTING, CPEPTIDE | 22564993 ABS; 25253174 ABS | HOLDS | The figures match the abstract: mean proportional change +4.0% (-5.6 to 14.4), -10.5% (-26.1 to 8.4) for HOMA above 2.8, +11.1% (-0.6 to 24.2) at or below 2.8. HOMA is defined in the abstract as fasting glucose (mmol/L) x insulin (mU/L)/22.5, so the row correctly calls it fasting-based. |
| C3 | MA.32 row: n=3,649; main trial null (HR 1.01); exploratory analysis has 72 interaction tests; IDFS interactions null; only HOMA 1.3 has a CI excluding 1; authors "failed to predict metformin effect" | FASTING | 35608580 ABS; 42063220 ABS | HOLDS, with a MISSING CAVEAT | HR 1.01 (0.84-1.21), P = .93, in 2,533 ER/PgR-positive patients matches the abstract. Missing caveat on measurement: insulin was assayed centrally, but glucose for HOMA was "measured locally" (34103538, 25740979). HOMA in MA.32 therefore carries uncalibrated between-site glucose variation, which bears on the merged file's own assay section. Also worth stating: MA.32 enrolled non-diabetic patients only, so it says nothing about effect modification in people with diabetes. |
| C4 | Trials table header and measure sentence: "the presurgical metformin trial ... [and] the MA.32 analysis ... used HOMA-IR or fasting insulin" | FASTING | as above | HOLDS | Both abstracts state fasting samples. |
| C5 | Steelman section, "Oncology": "They show that such analyses exist, not that insulin or HOMA changes a treatment effect. Do not read them together as 'oncology is an opening'." | FASTING | as above, plus the window studies 22933030, 21655990, 25682077, 24972190, 27745917 | HOLDS, with a MISSING CAVEAT | The merged file says "the two breast-cancer metformin RCTs", but the literature has more metformin window trials (breast and endometrial) in which insulin is an *outcome* (metformin lowered insulin, HOMA or C-peptide), not an effect modifier. In the abstracts read, none of them tests baseline insulin as a selector. Niraula 2012 (n=39, single-arm) found a Ki-67 fall with a HOMA fall of -0.21; Laskov 2014 (n=11 versus 10 controls) found lower insulin and Ki-67. These are mechanistic, not selection, evidence. The caveat should say so, so readers do not take "two trials" as the whole field. |
| C6 | Bottom line 1: "No established clinical utility today for routine fasting insulin, HOMA-IR or TyG/TG-HDL-C measurement" (oncology is not named as a setting) | FASTING, SURROGATE | Gallagher 2024 Delphi FT; Moore 2024 ABS; Goncalves 2022 ABS; Shen 2023 ABS; TIFA REG; WEB excerpts on ASCO/ESMO | HOLDS for oncology (MISSING CAVEAT: oncology is not listed) | In the one oncology setting where IR is directly provoked by a drug (PI3K-alpha and AKT inhibitors), risk stratification in the consensus (Delphi, full text) uses age 70 or older, BMI 30 or more and HbA1c 5.7-6.4%, monitoring uses fasting glucose and HbA1c, and no insulin, C-peptide, HOMA-IR or TyG test is recommended. The TIFA trial selects by fasting glucose and HbA1c only. I found no ASCO or ESMO text recommending insulin measurement (WEB-level search only; the documents were not read). |
| C7 | usecases-verified.md row 40 (alpelisib hyperglycaemia: "None specific", "Unsupported as a test", "Insulin mentions are mechanistic only") | none, CPEPTIDE | Gallagher 2024 FT; Carrillo-Lopez 2024 ABS; Percik 2023 ABS | HOLDS (no contradiction found) | The consensus does not use an insulin assay. The two small reports that measured C-peptide or insulin (n=14 and n=4) are hypothesis-level and do not change the row. I do not extend the use-case list; see open question Q3. |
| C8 | Measurement section: insulin therapy and analogue cross-reactivity make insulin-based indices uninterpretable | FASTING | Gallagher 2024 FT; Goncalves 2022 ABS | HOLDS, with an oncology caveat | In PI3K-inhibitor care, insulin is a last-line glucose-lowering agent because it reactivates PI3K signalling (Goncalves 2022; Delphi: "generally not appropriate first- or second-line"). Any on-treatment insulin or C-peptide reading is drug-perturbed (acute IR caused by the drug), so a baseline IR value would not carry over to the on-treatment state. This strengthens, rather than changes, the merged conclusion. |
| C9 | Open gap 3: "Adequately sized, prespecified treatment-by-baseline-measure interaction evidence with hard outcomes ... (the only prespecified test found, DIETFITS ...)" | FASTING | 42063220 ABS; skeptic-steelman problem 3 (FT) | NEEDS CORRECTION (minor) | The skeptic records that the MA.32 interaction analyses were protocol-specified, with distant recurrence-free survival (DRFS) as the prespecified outcome. MA.32 is therefore a prespecified (though unadjusted, multi-test) treatment-by-baseline-fasting-insulin/HOMA analysis with a hard outcome, and it was null for the primary outcome. "The only prespecified test found, DIETFITS" understates this. Suggested wording is in section 5. |
| C10 | Confidence for BL2 (about 40% for fasting insulin/HOMA-IR) | FASTING | as above | HOLDS overall; stronger in one narrow setting | MA.32 is the largest trial of any setting in the files with a baseline fasting insulin/HOMA interaction analysis on a hard outcome. For the narrow claim "baseline fasting insulin/HOMA does not identify non-diabetic early breast cancer patients who benefit from adjuvant metformin", I would put the probability around 70-75% (judgement). This does not move the pooled BL2 figure, which concerns incremental value across settings. |

---

## 3. Missed evidence (oncology)

Each item says the measure type and what it does and does not show.

### 3.1 Insulin as a prognostic or risk biomarker in cancer (FASTING, CPEPTIDE, SURROGATE): associations, no decision studies found
- **Breast cancer prognosis, fasting insulin.** Goodwin 2002 (11773152, ABS; n=512 non-diabetic, early-stage): highest versus lowest quartile of fasting insulin, adjusted HR 2.1 (1.2-3.6) for distant recurrence and 3.3 (1.5-7.0) for death; insulin correlated with BMI (r = 0.59). Goodwin 2012 (22162568, ABS; n=535): insulin-related variables (fasting insulin, HOMA, C-peptide) were associated with outcome only in the first 5 years (insulin Q4 vs Q1 HR 2.32 for DDFS), while BMI and leptin associations were constant over time. HEAL (Duggan 2011, 21115858, ABS; n=527): HOMA HR 1.12 (1.05-1.20) for breast-cancer mortality.
- **Breast cancer risk.** WHI-OS case-cohort (Gunter 2009, 19116382, ABS): fasting insulin Q4 vs Q1 HR 1.46 (1.00-2.13), and 2.40 (1.30-4.41) among non-users of hormone therapy (interaction P = .01). Contrast: Melbourne case-cohort (Albers 2025, 39808164, ABS; 347 ER-positive cases): insulin RR 0.97 (0.82-1.14) and C-peptide RR 1.01 (0.80-1.26) per doubling, so no association. The risk evidence is inconsistent.
- **Cancer mortality.** NHANES 1999-2010 (Tsujimoto 2017, 28390156, ABS; n=9,778 without diabetes): fasting insulin of 10 µU/mL or more, adjusted HR 2.04 (1.24-3.34) for cancer death; 1.89 (1.07-3.35) in non-obese people. This is a single assay cut-off with no reclassification analysis.
- **TyG and cancer.** Meta-analysis of 6 observational studies (36714554, ABS): pooled effect 1.14 (1.08-1.20) for high versus low TyG. This is a non-insulin surrogate with small relative risks.
- **What this does not show.** None of these papers tests whether adding fasting insulin, HOMA-IR, C-peptide or TyG to standard prognostic tools (stage, grade, receptor status, genomic scores) improves discrimination, reclassification or decisions. I did not find such a study, but my search for it was not targeted (section 7), so read this as "not found", not as "absent". The 2012 time-varying result also argues against a single baseline value as a stable prognostic marker, which fits the merged file's variability argument.

### 3.2 PI3K/AKT-inhibitor hyperglycaemia and insulin feedback (drug-induced IR; insulin as a resistance mechanism)
- **Mechanism (preclinical only).** Hopkins 2018 (30051890, FT): in mice, PI3K-pathway inhibitors caused hyperglycaemia and a rise in insulin and C-peptide. Insulin at the level seen after dosing (10 ng/mL) partly reactivated PI3K signalling in tumour cells. Knocking down the insulin receptor, a ketogenic diet or an SGLT2 inhibitor improved response, and exogenous insulin removed the diet's benefit. Metformin pretreatment had "only minimal impact" on the insulin rise in this model. **All of these data are murine or in vitro.** The full text contains no human insulin data and no test of whether a measured insulin level predicts PI3K-inhibitor efficacy.
- **Human evidence that measured insulin matters for efficacy: none found beyond very small series.** Percik 2023 (37163178, ABS) states that "insulin levels were not tested in the clinical trials that evaluated alpelisib" and reports 4 patients pretreated with pioglitazone on the basis of high baseline insulin (case series; no comparator). Carrillo-Lopez 2024 (38963515, ABS; n=14): baseline C-peptide above 10.5 ng/mL together with BMI above 27 gave AUC 0.819 for needing three or more glucose-lowering drugs (HbA1c AUC 0.556); this is an in-sample cut-off in 14 patients and the outcome is treatment intensity, not cancer outcome. Noch 2023 (37399061, ABS): in a buparlisib glioblastoma phase 2 trial, on-treatment *hyperglycaemia* was independently associated with worse PFS; the abstract reports glucose, not a blood insulin assay, as the clinical predictor.
- **Current practice tools.** The Delphi consensus (38297009, FT) stratifies risk by age, obesity and HbA1c, recommends weekly or more frequent fasting glucose and prophylactic metformin for HbA1c 5.7-6.4%, and does not mention insulin, C-peptide or HOMA testing. The reviews (35075945 and 39462728, ABS) recommend fasting glucose, HbA1c and, in one, postprandial glucose. A real-world cohort (37743730, ABS; n=247) found baseline HbA1c associated with hyperglycaemia (P < .001) and with dose reduction or discontinuation (P = .015). The TIFA RCT (NCT05090358, REG; phase 2, enrolment 15, active not recruiting, primary completion 2027-10) tests a ketogenic diet, a low-carbohydrate diet and canagliflozin to prevent grade 3/4 hyperglycaemia; eligibility is fasting glucose of 140 mg/dL or less and HbA1c below 8%. No insulin-based selection is recorded.
- **mTOR inhibitor.** EVERMET (33785482, ABS; n=809, retrospective): glucose (not insulin) dynamics were associated with everolimus PFS.
- **Net for the project.** The oncology case for measuring insulin rests on a strong preclinical mechanism (insulin feedback) and on human data at the level of glucose. No trial uses an insulin or C-peptide value to select or adapt treatment, and the ongoing trial (TIFA) does not measure the selector the mechanism would suggest. This is a gap that would make the use more viable (see Q2), not evidence of utility.

### 3.3 Other metformin cancer trials not in the files
- **STAMPEDE metformin arm** (Gillessen 2025, 40639383, ABS; n=1,874 non-diabetic men, metastatic prostate cancer): overall survival HR 0.91 (P = 0.15), not significant (meta-analysis 42875601, ABS). Entry used HbA1c below 6.5%. The abstract read reports no baseline insulin or HOMA subgroup. A high-volume-disease subgroup HR 0.79 has a non-significant interaction (P = 0.12). STAMPEDE therefore adds a second large null adjuvant-metformin trial, but not an insulin interaction test. Whether insulin was measured was not determined (full text not read).
- **Window trials** (section 2, C5) show metformin lowers insulin, HOMA or C-peptide over 1-5 weeks. They are evidence of the drug's mechanism, not of insulin as a selector.

### 3.4 Distinguish: C-peptide in checkpoint-inhibitor diabetes (non-IR)
- A consensus paper (PMC12161310, WEB excerpt only) quotes ASCO 2021 and ESMO 2022 guidance: measure ketones, anion gap, C-peptide and autoantibodies when checkpoint-inhibitor-induced diabetes is suspected. This is a C-peptide classification (insulin-deficiency) use, not IR measurement. It is the only ASCO/ESMO insulin-axis test I found mentioned, and it was not read at source. I pass it to the use-case reviewers (Q3); it does not touch the IR verdict.

---

## 4. Overreach risks

1. **Association read as utility.** The breast-cancer prognosis and risk associations (Goodwin 2002, WHI, HEAL, NHANES) are strong enough to be quoted as "insulin matters in cancer". None tests incremental value or a decision, the risk results conflict (WHI vs Melbourne), and the prognostic effect fades after 5 years (Goodwin 2012). They should not be added to the steelman as support for measuring fasting insulin.
2. **Mechanism read as a clinical rationale.** Hopkins 2018 is murine. Citing it as "insulin is a resistance mechanism, so measure insulin before PI3K inhibitors" goes beyond the evidence; in that model metformin did not blunt the insulin rise, which also argues against reading MA.32-type metformin data across to PI3K inhibitors.
3. **Small C-peptide or insulin series read as predictors.** Carrillo-Lopez (n=14, in-sample cut-off, outcome = number of drugs) and Percik (n=4, no comparator) are hypothesis-generating only.
4. **MA.32 generalised too far in the other direction.** MA.32 shows that baseline fasting insulin/HOMA did not identify metformin responders in non-diabetic early breast cancer. It does not show that insulin is irrelevant to PI3K-inhibitor therapy, to other cancers or to patients with diabetes.
5. **"Two oncology trials" as the field.** Calling the presurgical trial and MA.32 "the oncology interaction trials" without noting STAMPEDE (no insulin interaction reported) and the window studies (insulin as outcome) could suggest more selection evidence than exists, or less trial activity than exists.
6. **HOMA in MA.32 used as a clean measure.** Glucose was measured locally, so HOMA mixes central insulin with unstandardised glucose.

---

## 5. Suggested changes (exact sentences; not applied)

S1. In "Randomized or trial-based interaction evidence", MA.32 row, append to the Result cell:
> "Planned metabolic analyses in the same trial found that metformin lowered fasting insulin (6-month metformin/placebo ratio 0.85) and HOMA (0.83) with no qualitative interaction with baseline BMI or insulin (PMID 34103538, DOI 10.1038/s41523-021-00275-z, abstract). Insulin was assayed centrally but glucose locally, so HOMA mixes a central and a local measurement. Non-diabetic patients only."

S2. In "Added by the steelman run", bullet "Oncology", after the first sentence, insert:
> "Other metformin cancer trials in the literature do not add selection evidence. In preoperative window studies in breast and endometrial cancer (for example PMIDs 22933030, 24972190), insulin, HOMA or C-peptide was an outcome that metformin lowered, not an effect modifier. The STAMPEDE metformin arm in metastatic prostate cancer (PMID 40639383, DOI 10.1016/S1470-2045(25)00231-1, abstract) was null for overall survival (HR 0.91, P = 0.15) and reports no baseline insulin subgroup in its abstract."

S3. Add a new steelman-section bullet "PI3K/AKT inhibitors (drug-induced IR)":
> "PI3K-alpha and AKT inhibitors cause acute, on-target insulin resistance with compensatory hyperinsulinaemia. In mice the insulin feedback partly reactivates tumour PI3K signalling and limits efficacy (Hopkins 2018, PMID 30051890, DOI 10.1038/s41586-018-0343-4, full text, murine and in vitro data only). In patients, risk stratification and monitoring use age, BMI, HbA1c and fasting glucose, not an insulin assay (alpelisib Delphi consensus, PMID 38297009, DOI 10.1038/s41523-024-00613-x, full text). Insulin was not measured in the alpelisib registration trials (stated in PMID 37163178, abstract), and the human reports that measured C-peptide or insulin have 14 and 4 patients. No trial was found that selects or adapts treatment by an insulin or C-peptide value; the TIFA RCT (NCT05090358) targets insulin feedback but selects by glucose and HbA1c. Mechanism only; this does not support routine measurement."

S4. Add to "What is not supported as stated" (as a guard, since no file currently claims it):
> "That cancer-risk or cancer-prognosis associations of fasting insulin or HOMA-IR (for example PMIDs 11773152, 19116382, 21115858, 28390156) show clinical utility. They are associations without incremental-value or decision analyses; the risk findings conflict (PMID 39808164 found none for insulin or C-peptide in ER-positive breast cancer), and the prognostic association in early breast cancer was confined to the first 5 years (PMID 22162568)."

S5. Open gap 3: replace "(the only prespecified test found, DIETFITS, is null and on weight loss; ...)" with:
> "(prespecified tests found: DIETFITS, post-load insulin, null, weight-loss outcome; and the MA.32 baseline fasting insulin/HOMA interaction analyses, protocol-specified with distant recurrence-free survival as their outcome, 72 unadjusted tests, null for invasive disease-free survival and compatible with chance; TZD response signal in Dennis 2019 is unreplicated)."

S6. Bottom line 1, after "in primary care, prediabetes, T2D, PCOS, MASLD or obesity.", optionally add:
> "In oncology, the setting with drug-induced insulin resistance (PI3K/AKT inhibitors) manages risk with age, BMI, HbA1c and fasting glucose, and no ASCO or ESMO recommendation to measure insulin was found (search-excerpt level; the guideline texts were not read)."

---

## 6. Open questions

- Q1. Did MA.32 or STAMPEDE report baseline insulin, HOMA or C-peptide subgroups for overall survival in their full texts or supplements (PMC9131745, PMC12303861)? Not read here.
- Q2. What would make an insulin-based use viable in oncology (D-30): a prespecified analysis in a PI3K/AKT-inhibitor trial (SOLAR-1, INAVO120, CAPItello-291, or TIFA if insulin is banked) testing whether baseline or on-treatment insulin/C-peptide predicts PFS, beyond HbA1c and BMI. I found no such analysis. A registry search for banked insulin in these trials was not done (budget).
- Q3 (for the use-case reviewers, not done here): (a) C-peptide in suspected checkpoint-inhibitor diabetes (ASCO 2021, ESMO 2022, WEB excerpt only); (b) whether row 40 should cite the Delphi consensus (PMID 38297009) as a stronger source than PMC8997133.
- Q4. Is there any incremental-value study of fasting insulin or C-peptide over standard prognostic factors in breast, colorectal or endometrial cancer? Not searched in a targeted way.
- Q5. Do TyG and cancer-outcome studies (36714554 and later) include any reclassification analysis? Not screened.

---

## 7. Search log (20 look-ups)

| # | Tool / database | Query | Results | Used |
|---|---|---|---|---|
| 1 | PubMed | alpelisib hyperglycemia (baseline insulin OR HOMA-IR OR "insulin resistance") predictors | 0 | negative |
| 2 | PubMed | metformin randomized cancer (baseline insulin OR HOMA) subgroup interaction (endometrial OR prostate OR colorectal OR breast) | 1 (42063220) | already in files |
| 3 | PubMed | alpelisib hyperglycemia risk factors baseline | 4 | 39462728, 38963515, 37743730, 35075945 |
| 4 | PubMed | metformin window of opportunity trial insulin cancer Ki-67 | 5 | 27745917, 25682077, 24972190, 22933030, 21655990 |
| 5 | PubMed metadata | 9 PMIDs from 3 and 4 | 9 | abstracts read |
| 6 | PubMed | Hopkins BD "Suppression of insulin feedback enhances the efficacy of PI3K inhibitors" | 2 | 30051890 |
| 7 | PubMed | (fasting insulin OR C-peptide OR hyperinsulinemia) cancer (incidence OR mortality) meta-analysis prospective | 42 (20 returned) | low precision; 36714554 kept |
| 8 | PubMed metadata | 12 PMIDs (30051890 plus 11 from #7) | 12 | titles and abstract heads read; most off-topic |
| 9 | PubMed | (Goodwin PJ[Author] AND "fasting insulin" AND breast cancer AND prognosis) OR (Irwin ML[Author] AND HOMA AND breast cancer mortality) OR (Gunter MJ[Author] AND "insulin, insulin-like growth factor-I, and risk of breast cancer") OR (Tsujimoto T[Author] AND hyperinsulinemia AND cancer mortality) | 14 | 11773152, 22162568, 21115858, 19116382, 28390156, 39808164, 25740979 |
| 10 | PubMed | MA.32 metformin breast cancer insulin Goodwin | 4 | 42063220, 34485814, 34103538, 25740979 |
| 11 | PubMed metadata | 20 PMIDs (from 9 and 10, plus 35608580, 22564993, 25253174) | 20 | abstracts read |
| 12 | Web (Parallel) | ESMO guideline PI3K inhibitor hyperglycaemia monitoring fasting glucose HbA1c; alpelisib hyperglycemia consensus recommendations insulin C-peptide baseline; ASCO guideline alpelisib hyperglycemia management | 10 | Delphi PMC10831089; PMC11558917; PMC12161310 (ICI); label excerpts. No ASCO/ESMO text recommending insulin |
| 13 | PubMed | Mendelian randomization "fasting insulin" cancer risk | 55 (15 returned) | titles/abstract heads only; none carried |
| 14 | PubMed | STAMPEDE metformin prostate cancer randomised | 4 | 40639383, 42875601 |
| 15 | PubMed metadata | 10 PMIDs (from 13 and 14) | 10 | abstracts read for STAMPEDE items |
| 16 | PMC full text | PMC10831089 (Delphi, PMID 38297009) | 1 | read end to end |
| 17 | PMC full text | PMC6197057 (Hopkins 2018) | 1 | read end to end |
| 18 | PubMed | (alpelisib OR PI3K inhibitor OR capivasertib OR inavolisib OR buparlisib) (C-peptide OR "serum insulin" OR hyperinsulinemia) (progression-free survival OR efficacy OR response) patients | 24 (20 returned) | top 10 screened: 37163178, 37399061, 33785482 kept |
| 19 | PubMed metadata | 10 PMIDs from 18 | 10 | abstracts read |
| 20 | ClinicalTrials.gov | NCT05090358 (TIFA) | 1 | registry record read |

Not searched (budget): Embase, Cochrane, ESMO and ASCO guideline sites directly, NCCN, FDA labels at source, SOLAR-1/INAVO120/CAPItello-291 insulin sub-analyses, colorectal adenoma metformin prevention trials, endometrial metformin RCTs with clinical outcomes, cancer cachexia and insulin resistance, and pancreatic cancer hyperinsulinaemia (new-onset diabetes) studies.

---

## 8. Could not retrieve or did not read

- ASCO and ESMO guideline texts: not retrieved. Statements about them are WEB-excerpt level and unverified.
- Full texts of MA.32 main (PMC9131745), MA.32 metabolic (PMC8187713), STAMPEDE metformin (PMC12303861), Shen 2023 (PMC10863751) and Carrillo-Lopez 2024 (PMC11489167): available but not read (budget). The 2012 presurgical report has no PMC copy.
- Alpelisib, capivasertib and inavolisib labels: not read at source; label monitoring text is known only from secondary excerpts.
- PMIDs and DOIs for PMC11558917 and PMC12161310 were not resolved (WEB only).
- The Delphi supplementary tables were not read.
