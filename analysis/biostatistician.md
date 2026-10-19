# Biostatistician / epidemiologist appraisal: quantitative evidence for insulin resistance (IR) measures as clinical tools

Scope: incremental predictive value, cutoff derivation and validation, assay and biological variability, and study biases. Coverage and reimbursement are out of scope.
Date of search: 2026-10-18. Tools: PubMed (NCBI E-utilities connector) and Consensus. Amass was **not** queried (see "Limits of this review").

## 0. How to read this report

- **Citation tags.** Every cited item is tagged one of three ways:
  - `[V]` = PMID resolved and title/abstract read in this session.
  - `[V-cit]` = PMID resolved by journal/volume/page lookup, but the abstract was not read here. The claim about it comes from general knowledge and is labelled as such.
  - `[C-only]` = surfaced by Consensus with abstract read. No PMID or DOI was obtained here, so identifier is given as author/journal/year only. **Treat as unverified identifier; the skeptic should resolve before reuse.**
- Evidence type is stated for each study: **A** = association, **P** = prediction, **C** = causal or decision-impact (a trial or a strong causal design).
- Numbers are quoted from abstracts. I did not have full texts, so adjustment sets and methods are taken from abstracts only.

## 1. Bottom line

1. **Association is well established; incremental prediction is weak or untested.** IR indices (mostly HOMA-IR) are associated with incident CVD and T2D, but in the studies that tested added discrimination beyond routine clinical variables and fasting glucose, the gain was nil to negligible (Framingham Offspring, Hu 2024, ARIC). No study I found reports calibration, decision-curve net benefit or NRI for HOMA-IR added to a CVD risk equation.
2. **Measurement noise is large relative to the cutoffs.** Within-person CV of HOMA-IR is about 27–30% on repeat testing (EuBIVAS, ARIC). Between-assay differences in calculated HOMA-IR reach about twofold on the same samples. A single fasting HOMA-IR value is an unreliable individual-level classifier.
3. **There is no defensible universal cutoff.** Published thresholds range from about 1.4 to 3.6 depending on population, reference standard (dysglycemia vs T2D vs metabolic syndrome) and insulin assay. Most are derived by Youden/ROC in the same sample, against an outcome (glycemia) that is mathematically part of the index (incorporation bias). External validation is rare.
4. **Decision-impact (causal) evidence is almost absent.** The one large IR-selected RCT (IRIS, pioglitazone) enrolled only HOMA-IR >3.0 patients, so it cannot show that measuring IR improves outcomes versus not measuring it. DPP/DPPOS heterogeneity analyses point to glucose and HbA1c, not IR indices, as modifiers.
5. **Biggest threats to validity:** confounding by adiposity/TG/glucose (IR indices are partly functions of these), regression dilution, assay non-comparability, incorporation bias, and ethnicity-specific calibration.

## 2. Ranked appraisal of key evidence

Rating scale: **High / Moderate / Low / Very low** certainty that the study supports the stated use (not general scientific quality).

| # | Study (design, n) | Evidence type | Key effect size | Main biases | Rating for "IR measure adds clinical value" |
|---|---|---|---|---|---|
| 1 | Kernan 2016, IRIS RCT, 3876 non-diabetic post-stroke/TIA pts, HOMA-IR >3.0 `[V]` PMID 26886418, DOI 10.1056/NEJMoa1506930 | C (treatment effect in IR-selected pop.) | Stroke/MI HR 0.76 (95% CI 0.62–0.93); incident diabetes HR 0.48 (0.33–0.69); all-cause mortality HR 0.93 (0.73–1.17); weight gain >4.5 kg 52.2% vs 33.7%, fracture 5.1% vs 3.2% | Selection on IR but no non-IR comparison arm → cannot test effect modification by IR; single-assay HOMA-IR cutoff; benefit–harm trade-off not IR-specific | **Moderate** for "pioglitazone helps this IR-selected group". **Low** for "measuring IR improves decisions" |
| 2 | Wilson 2007, Framingham Offspring, 7-yr T2D prediction `[V]` PMID 17533210, DOI 10.1001/archinte.167.10.1068 | P | AROC 0.72 (age/sex/BMI/parental hx); 0.85 simple clinical model (adds MetS traits, impaired fasting glucose); complex models with 2-h glucose, fasting insulin, CRP, Gutt ISI or HOMA-IR/HOMA-B 0.850–0.854 | Single, mostly white middle-aged cohort; in-sample discrimination; no NRI/calibration in abstract | **High** that HOMA-IR adds ~0 to simple clinical model for T2D prediction (in this population) |
| 3 | Hu 2024, 5578 workers, 943 incident T2D, 10-yr models `[V]` PMID 38191206, DOI 10.1136/bmjdrc-2023-003680 | P | Base model (age, sex, BMI, smoking, lipids, BP, HbA1c) AUC 0.79 (0.78–0.81); + FPG 0.84 (0.83–0.85), cNRI 0.61 (0.56–0.70), IDI 0.09 (0.08–0.10); + HOMA-IR/HOMA-β "did not further materially improve" | 94.7% male; occupational cohort; continuous NRI is known to inflate (see §3); no external validation | **Moderate–High** that HOMA indices add little beyond glucose/HbA1c |
| 4 | Schmidt 2005, ARIC T2D risk rules, 7915 pts, 1292 cases `[V]` PMID 16043747, DOI 10.2337/diacare.28.8.2013 | P | Clinical variables AUC 0.71; + fasting glucose 0.78; + TG and HDL 0.80 | Insulin not the predictor tested; shows that lipids/glucose already capture much of the signal | **Moderate** (indirect: relevant to what IR must beat) |
| 5 | Gast 2012, meta-analysis, 65 cohort/nested case–control studies, 516,325 pts `[V]` PMID 23300589, DOI 10.1371/journal.pone.0052036 | A (prognostic association) | CHD, high vs low: HOMA-IR RR 1.64 (1.35–2.00), I² 0%; glucose 1.52 (1.31–1.76), I² 62.4%; insulin 1.12 (0.92–1.37), I² 41%. Per 1 SD, CHD: HOMA-IR 1.46 (1.26–1.69); glucose 1.21 (1.13–1.30); insulin 1.04 (0.96–1.12) | Mixed adjustment sets (abstract does not state per-study adjustment for BMI, lipids); few HOMA-IR studies pooled (count not extracted); no C-statistic/NRI; authors say "may be useful to add" (speculation, not tested); I² of 0% with few studies has low power | **Low–Moderate** for independent association; **Very low** for incremental prediction |
| 6 | Wang 2022, China Cardiometabolic Disease and Cancer cohort, 111,576 adults `[V]` PMID 35700159, DOI 10.2337/dc22-0202 | A | HOMA-IR Q4 vs Q1 CVD HR: normal glucose tolerance 1.03 (0.82–1.30); prediabetes 1.23 (1.07–1.42); diabetes 1.61 (1.30–2.00); per SD 1.04 / 1.12 / 1.15; interaction P = 0.011 | Abstract-listed covariates: age, sex, education, alcohol, smoking, physical activity, diet quality (no BMI, BP, lipids); quartiles defined within each glucose stratum; single HOMA-IR measurement | **Moderate** that IR adds nothing detectable CV signal in normoglycemia; supports effect modification by glycemia |
| 7 | Dennis 2019, ADOPT/RECORD trials, 4351 + 4447 pts `[V]` PMID 31047901, DOI 10.1016/S2213-8587(19)30087-7 | P + C (treatment-response prediction) | Data-driven clusters (incl. HOMA2-IR–based SIRD) differ in progression and glycaemic response (TZD benefit in the severe insulin-resistant cluster), but age at diagnosis alone explained similar progression, and "simple clinical features outperformed clusters to select therapy" | Trial populations; post hoc; clusters unstable at boundaries | **Moderate** that IR-based subgrouping adds little beyond simple features |
| 8 | Tabak 2009, Whitehall II, 6538 pts, 505 incident T2D `[V]` PMID 19515410, DOI 10.1016/S0140-6736(09)60619-X | A (temporal trajectory) | HOMA insulin sensitivity fell steeply in the ~5 years before diagnosis (to 86.7%); fasting glucose rose from 5.79 to 7.40 mmol/L starting ~3 yr before diagnosis | Retrospective trajectories; 91% white; HOMA-S from single assays; shows IR change is late and parallels glucose | **Moderate** for natural-history description; does not show incremental value |
| 9 | Bonora 2000, HOMA vs 4-h clamp, n=115 `[V]` PMID 10857969, DOI 10.2337/diacare.23.1.57 | Validity (criterion) | r = −0.820 vs clamp glucose disposal; weighted κ = 0.63 for categorisation | Small, single centre, one assay; correlation ≠ agreement; high r still leaves ~33% of variance unexplained (r² ≈ 0.67, my arithmetic) | **Moderate** as population-level surrogate; **Low** for individual classification |

Other items (association-grade or methods papers) are cited in the sections below.

## 3. Incremental value: how to judge it, and what the data show

### 3.1 What the right yardsticks are
- **C-statistic/AUC** is insensitive to modest additions once the base model is strong (Cook 2007, PMID 17309939 `[V-cit]`, DOI 10.1161/CIRCULATIONAHA.106.672402: general critique, abstract not read here).
- **NRI/IDI.** Kerr 2014 `[V]` PMID 24240655 (DOI 10.1097/EDE.0000000000000018) recommends reporting event and non-event components separately, cautions against category-free NRI (it "can mislead investigators by overstating the incremental value of a biomarker, even in independent validation data"), prefers regression-coefficient tests for the null, and names **net benefit** as the preferred summary. Pencina 2008 `[V-cit]` PMID 17569110 introduced NRI/IDI.
- **Decision curves.** Vickers & Elkin 2006 `[V-cit]` PMID 17099194 is the standard citation. I found no decision-curve analysis for any IR index in the retrieved literature.
- **Calibration** was not reported in any abstract I read.

### 3.2 T2D prediction (P)
- Framingham Offspring (PMID 17533210): AROC 0.85 → 0.850–0.854 when HOMA-IR/HOMA-β, fasting insulin or Gutt ISI were added. No incremental gain.
- Hu 2024 (PMID 38191206): glucose adds a lot (AUC 0.79 → 0.84; cNRI 0.61), HOMA indices add "not materially". Note the large cNRI for FPG illustrates the inflation Kerr warns about; the AUC step is the safer summary.
- ARIC clinical rules (PMID 16043747): AUC 0.71 → 0.78 with fasting glucose → 0.80 with TG/HDL. Triglycerides and HDL are already the inputs of several non-insulin IR proxies, so the "IR signal" may be largely carried by routine lipids.
- Cheaper IR surrogates built from routine labs (TyG, METS-IR) compete directly with insulin-based indices. See §5.
- **Interpretation:** for T2D prediction in general populations, the evidence supports "no added discrimination beyond glucose/HbA1c + BMI + routine lipids". Contexts not covered by these data: normoglycemic people with obesity, young adults, non-white populations, and long horizons (>10 yr).

### 3.3 CVD prediction (A, not P)
- Gast 2012 (PMID 23300589): HOMA-IR per-SD RR 1.46 for CHD vs glucose 1.21 and insulin 1.04. Higher relative risk per SD does not equal higher discrimination, because discrimination depends on separation of distributions *conditional on the other predictors*.
- Wang 2022 (PMID 35700159): in normal glucose tolerance, per-SD HR 1.04 (0.92–1.18), i.e. null; in diabetes 1.15 (1.09–1.21). The IR signal is concentrated where glycemia is already abnormal, which is where glucose/HbA1c already carry risk information.
- No CVD risk-equation paper retrieved reports ΔC, NRI or net benefit for HOMA-IR. **This is the main missing analysis.**

### 3.4 Treatment-effect modification (C-type, the relevant standard for "should we test?")
- IRIS (PMID 26886418) has no IR-negative arm, so effect modification by IR is untestable.
- DPP/DPPOS: Consensus-retrieved abstracts report greater absolute benefit with higher baseline fasting glucose and HbA1c (Aroda et al., Diabetes Care 2019, "Long-term effects of metformin on diabetes prevention: identification of subgroups that benefited most" `[C-only]`), and lifestyle benefit greater at higher baseline glucose, HbA1c and multivariable risk indices; metformin benefit larger in younger participants (Knowler et al., Lancet Diabetes Endocrinol 2025, "Long-term effects and effect heterogeneity of lifestyle and metformin…over 21 years" `[C-only]`). Neither abstract names an IR index as an effect modifier. Kitabchi 2005, Diabetes, "Role of insulin secretion and sensitivity in the evolution of type 2 diabetes in the Diabetes Prevention Program" `[C-only]`, reports baseline insulin sensitivity associated with lower diabetes hazard (hazard-rate ratio 0.62–0.94 per SD depending on arm/measure), which is prognostic association, not treatment selection.
- Dennis 2019 (PMID 31047901): IR-based clusters did not beat simple clinical features for choosing therapy.

## 4. Cutoffs: derivation and validation

### 4.1 What was derived
| Study | Population / n | Reference standard | Cutoff | Performance | Notes |
|---|---|---|---|---|---|
| Lee 2016 `[V]` PMID 27658115, DOI 10.1371/journal.pone.0163424 | Hong Kong Chinese, 2649 cross-sectional + 872 persistently normoglycemic at 15 yr | WHO glycemia | 1.37 (dysglycemia); 1.97 (T2D) | AUC 0.735 (0.713–0.758) and 0.807 (0.777–0.886); sens/spec 65.6/71.3% and 65.5/82.9% | Cutoffs matched 75th (1.44) and 90th (2.03) percentile of the persistently-NGT reference |
| Horáková 2019 `[V]` PMID 31108989, DOI 10.3390/medicina55050158 | Czech, 3539 | Glycemia | 3.63 (T2D vs non-diabetic); 1.82 (NGT vs prediabetes) | T2D: sens 0.56, spec 0.86, AUC 0.73; prediabetes: sens 0.60, spec 0.66 | Optimal point maximises sens+spec in-sample; OR for T2D 1.2 per unit |
| Matli 2021 `[V]` PMID 34380182, DOI 10.1515/cclm-2021-0643 | Gutenberg Health Study, 10,340 with data; 1065 stringent reference | Percentile-based reference interval | 97.5th percentile 2.35 (median 1.09, IQR 0.85/1.42) in stringent reference group | Three insulin assays gave "unsatisfactory correlation" and systematic HOMA-IR differences → assay-specific intervals needed | Reference-interval approach rather than outcome-anchored |
| Xing 2025 (ARIC, 12,543; Nutr Metab Cardiovasc Dis) `[C-only]` | Middle-aged non-diabetic | Incident T2D at 3/6/9 yr | HOMA-IR 2.4–3.2 (women), 2.8–3.2 (men) | HOMA-IR AUC 0.69–0.78; fasting glucose ranked best of eight predictors | Youden-derived, sex-specific, same-sample |

### 4.2 Appraisal
- **Spread of 1.4–3.6 for "IR" is a measurement/population artefact as much as biology.** Compare Lee (T2D at 1.97) with Horáková (T2D at 3.63) and ARIC (2.4–3.2 for *future* T2D). Same index, similar target, 2-fold different threshold.
- **Incorporation bias.** Where the reference standard is glycemia (Lee, Horáková), the index contains fasting glucose, so AUC is inflated and cutoff is partly a re-labelling of dysglycemia. The Czech sens/spec (0.56/0.86 for T2D) shows modest accuracy even so.
- **Data-driven optimal points** (Youden, max sens+spec) are unstable and optimistic in-sample. None of the retrieved cutoff studies reports bootstrap optimism correction or an independent validation cohort. Lee 2016 partly addresses this with a prospective normoglycemic reference.
- **Binary threshold loses information.** HOMA-IR is continuous and approximately log-normal. Dichotomising at a point also throws away power (standard methodological point; no study here shows that the cutoff improves decisions over the continuous value).
- **Ethnicity.** SWAN (Torréns 2004, Diabetes Care, "Ethnic differences in insulin sensitivity and beta-cell function in premenopausal or early perimenopausal women…" `[C-only]`): HOMA%S lower in African American, Chinese American and Japanese American women than in non-Hispanic white women after correcting for waist; difference persisted only for African Americans after adding triglycerides. Trikudanathan 2013, Metabolism, "Comparison of insulin sensitivity measures in South Asians" `[C-only]`, n = 41 (23 South Asian, 18 Caucasian): HOMA-IR, QUICKI and TG/HDL correlated with clamp insulin sensitivity in South Asians but *not* in Caucasians in that small sample. Tiny samples; the result may be chance, but it shows criterion validity is not guaranteed to transport across ethnic groups.
- **Age, sex, BMI.** Matli found no significant sex difference and a non-significant upward trend with age in the stringent reference group; Xing found sex-specific cutoffs. I did not find a study that jointly models BMI-, age-, sex- and ethnicity-specific reference curves with validation.
- **Bottom line on cutoffs:** no cutoff meets the standard of (i) derivation against a non-circular outcome, (ii) correction for optimism, (iii) external validation, (iv) demonstration that acting on it improves outcomes. Using a single published cutoff (e.g. ">2.5") clinically is not evidence-supported.

## 5. Measurement: assay, calculator, biological variation

### 5.1 Assay and calculator
- **Manley 2008** `[V]` PMID 18535197, DOI 10.2337/dc08-0097: 97 subjects, **11 insulin assays** on the same samples. Median HOMA-IR ranged 0.8–2.0 (normoglycemia, P = 0.0007), 1.9–3.2 (pre-diabetes, NS) and 1.5–2.9 (T2D, P < 0.0001). Insulin ~15% lower in heparinised plasma than serum; choice of HOMA calculator changed IR by ~15%. Authors call this a "twofold variation".
- **Matli 2021** (PMID 34380182): three assays gave unsatisfactory correlation and systematic HOMA-IR differences.
- **Rosli 2022**, J Clin Lab Anal `[V-cit-by-search]` PMID 35622611 (matched on author/topic search; abstract read via Consensus): seven kits (4 ELISA, 3 CLIA) gave relative SD 1.7–23.2%; traceability chains and unit conversion factors are not harmonised; no commutable reference material.
- **Staten et al. 2010** `[V]` PMID 20040676, DOI 10.2337/dc09-1206 is the assay-standardisation effort (title verified; abstract not read). A Heinemann comment on SI-units reporting is PMID 20508228 (title verified, not read in detail).
- **Implication:** published cutoffs (§4) are tied to a specific assay and cannot be pooled or transferred without harmonisation. Meta-analytic pooling of HOMA-IR effect sizes (Gast 2012) mixes assay scales; per-SD scaling partly protects this but not completely.

### 5.2 Within-person variability and reliability
- **EuBIVAS** (Carobene 2024) `[V]` PMID 38987271, DOI 10.1515/cclm-2024-0672: 90 non-diabetic adults, 10 weekly samples. Within-subject CV (CVI) of HOMA-IR **26.7% (25.5–28.3)**, driven by insulin; QUICKI CVI 4.1% (log transform compresses). Authors state this "limits the value of single measurements".
- **ARIC repeatability** (Poon 2018) `[V]` PMID 29618016, DOI 10.1210/jc.2017-02437: 102 adults aged 68–88, repeat at mean 46 days. HOMA-IR ICC 0.70, within-person CV 30.4%; insulin ICC 0.68, CV 28.8%; glucose ICC 0.70, CV 5.6%; TG/HDL-C ICC 0.80, CV 23.0%. Minimum detectable change (95%) for HOMA-IR **2.3**, i.e. larger than the difference between most proposed cutoffs and the population median.
- **Consequences for risk estimates** (my derivation using classical measurement-error theory, not a result from these papers): with ICC ≈ 0.70, a single-measurement regression coefficient is attenuated towards roughly 70% of the true-exposure coefficient (regression dilution), and the more error-prone HOMA-IR will lose to the better measured glucose and lipid terms in multivariable models. This biases head-to-head comparisons against HOMA-IR and in favour of precisely measured covariates, and it also means that observed per-SD HRs (e.g. 1.46) understate the true-exposure association. Conversely, measurement error in covariates (e.g. BMI) leaves residual confounding.
- **Diagnostic consequence:** a person whose true HOMA-IR is at a cutoff will be classified IR-positive on a repeat test roughly half the time; people near the boundary flip classification.
- Reference-standard evidence: Bonora 2000 (r = −0.82) was derived on single-sample assays in n = 115; it predates modern assay variation.

### 5.3 Non-insulin proxies
- **TyG** (ln[TG × glucose/2]): Guerrero-Romero 2010 `[V]` PMID 20484475, DOI 10.1210/jc.2010-0288: n = 99 (11 + 34 + 22 + 32), r = −0.681 with clamp M-value, cutoff 4.68 chosen from the same data giving sens 96.5%, spec 85.0%, AUC 0.858 (optimistic, in-sample). Simental-Mendía 2008 `[V]` PMID 19067533, DOI 10.1089/met.2008.0034: n = 748 IFG/IGT cohort; "IR" defined by HOMA-IR; cutoff Ln 4.65 gave sens 84.0%, spec 45.0% (poor specificity); reference standard is another surrogate rather than clamp.
- TyG as mediator: Tian 2022, Cardiovasc Diabetol, "Insulin resistance mediates obesity-related risk of CVD" (Kailuan, 94,136, 7327 CVD cases) `[C-only]` reports 47.81% of the overweight–CVD association mediated by TyG. TyG contains TG, itself a CVD risk factor, so "mediated by IR" is not separable from "mediated by triglyceride and glucose". Mediation requires no unmeasured mediator–outcome confounding, which is unlikely here.

## 6. Study designs and biases

| Bias | How it appears in this literature | Evidence / example |
|---|---|---|
| **Confounding by adiposity** | HOMA-IR and TyG correlate strongly with BMI, waist, TG, glucose. A BMI-adjusted association may be understated (overadjustment if adiposity causes IR) or an unadjusted association overstated (confounding). Which applies is a causal-structure question that most studies do not state. | Wang 2022 adjusted for lifestyle covariates only per abstract (PMID 35700159). Tian 2022 treats TyG as a mediator `[C-only]`. SWAN ethnic differences depend on adjustment for waist and TG `[C-only]` |
| **Reverse causation / timing** | IR indices change late (≈3–5 years pre-diagnosis) and move with glycemia and disease processes (cancer, heart failure, illness) that also affect outcomes. | Tabak 2009 (PMID 19515410) |
| **Incorporation bias** | The index contains the outcome/reference variable (glucose). | Lee 2016, Horáková 2019 (§4) |
| **Measurement error / regression dilution** | Single measurement, CVI ≈ 27–30%. | PMIDs 38987271, 29618016 |
| **Assay non-comparability** | Between-assay differences up to ~twofold in HOMA-IR; cutoffs assay-specific. | PMIDs 18535197, 34380182, 35622611 |
| **Data-driven cutoff / optimism** | Youden-type optimum in same sample; no optimism correction or external validation reported. | §4.1 |
| **Selection** | Occupational, volunteer or hospital outpatient samples (94.7% male workers in Hu 2024; mostly white civil servants in Whitehall II; 91% white). Generalisation to primary care patients is unsupported. | PMIDs 38191206, 19515410 |
| **Survivorship / healthy-volunteer** | Cohorts that need fasting insulin at baseline over-represent healthier, compliant participants; older cohorts (ARIC repeatability, ages 68–88) exclude those who died or declined. | Design inference; not quantified in sources |
| **Publication bias / small-study effects** | Gast 2012 reports I² only; I did not see a funnel plot or Egger test in the abstract. Cutoff-study literature is dominated by single-centre, positive-by-design reports; I did not find a study quantifying publication bias for IR cutoffs. | PMID 23300589 |
| **Heterogeneity** | Gast: I² 0% HOMA-IR vs 62.4% glucose for CHD high-vs-low. No prediction intervals in abstract. Low heterogeneity with few studies is weak reassurance. | PMID 23300589 |
| **Multiple testing / forking paths** | IR indices (HOMA-IR, QUICKI, TyG, METS-IR, TG/HDL, Matsuda…) × outcomes × subgroups × cutoffs; many sub-analyses (e.g., Wang 2022 stratified by glucose tolerance with an interaction P = 0.011) are not corrected. | Design inference |
| **Spectrum / case-mix bias** | IRIS and DPP-based work show IR operates in populations with dysglycemia/stroke; extrapolating to normoglycemic primary care is unsupported. | PMIDs 26886418, 35700159 |

## 7. Causality
- Association with CVD and T2D is consistent across cohorts (Gast 2012), but this does not show that *lowering IR* lowers risk.
- IRIS shows a treatment benefit in an IR-selected group (HR 0.76 for stroke/MI), but pioglitazone has other actions beyond IR, so this is not a clean test of the IR hypothesis, and the trial lacks a comparison with non-IR patients.
- Mendelian randomization evidence (Consensus search): Ross et al. 2015, Eur Heart J `[C-only]`, found causal support for diabetes and HbA1c on CAD, a non-significant effect for fasting glucose (OR 1.18, 0.97–1.42 per mmol/L), and reported "no significant differences" between loci grouped as beta-cell vs insulin-resistance. I did not retrieve an MR study of an IR-specific instrument against CVD. **IR-specific causal evidence is thin in what I found.**

## 8. Summary of incremental-value findings (one paragraph)
In general-population cohorts, HOMA-IR/fasting insulin add essentially nothing to AUC once standard clinical variables and glucose/HbA1c (± lipids) are in the model (Framingham Offspring AROC 0.85 → 0.850–0.854; Hu 2024 AUC 0.84 with FPG and no further gain; ARIC rules AUC 0.80 with clinical variables, fasting glucose, TG and HDL). For CVD, HOMA-IR is an independent risk marker with pooled RR 1.64 for high vs low (I² 0%), but no study found reports ΔC, NRI/IDI, calibration or net benefit for CVD prediction, and the association is null in normoglycemia (HR 1.03, 0.82–1.30). No trial tests whether IR measurement improves outcomes; IRIS enrolled only IR-positive patients.

## 9. Missing analyses (what would change my view)
1. **CVD:** pre-specified ΔC-statistic, event/non-event NRI at clinically meaningful thresholds, calibration (slope, calibration-in-the-large) and net benefit/decision curves for HOMA-IR (and TyG, TG/HDL) added to PCE/SCORE2 with an external validation cohort. Use bootstrap-optimism correction.
2. **T2D:** same package in non-white, younger and normoglycemic-obese populations; compare insulin-based indices against TG/HDL, TyG and HbA1c; include a clinically useful horizon (5 and 10 yr).
3. **Repeat-measure designs:** risk models with two or more insulin measurements per person (regression-calibration or SIMEX correction) to estimate the true-exposure HR and the attainable discrimination if measurement error were removed.
4. **Assay-harmonised cutoffs:** multi-assay, traceable reference interval study, with cutoffs derived against clamp-measured insulin sensitivity (not glycemia) and validated externally. Report as continuous risk curves rather than a single threshold.
5. **Effect modification:** trials or IPD meta-analyses (DPP, Look AHEAD, ADOPT, IRIS-like) testing treatment × baseline IR interaction with pre-specified models, comparing it with interaction on glucose/HbA1c/BMI. A "stratified-care" RCT (IR-guided vs usual care) with patient-relevant outcomes.
6. **Causal design:** MR with IR-specific instruments (e.g. clamp-based or lipodystrophy-pattern loci), multivariable MR conditioning on BMI and TG; mediation with proper sensitivity analyses.
7. **Meta-research:** systematic review of IR-cutoff studies with publication-bias assessment, prediction intervals and risk-of-bias rating (QUADAS-2 for diagnostic accuracy, PROBAST for prediction models). I did not find one.
8. **Selection/spectrum:** primary-care or referral-population validation (current evidence is from cohorts and volunteer samples).

## 10. Limits of this review
- **Search tools were weak.** The PubMed connector returned nothing for quoted-title queries and most natural-language queries, so I relied on direct citation lookup (for classic papers) plus Consensus (maximum 3 results per query on the free tier). Coverage is therefore not systematic; it is an appraisal of a deliberately selected, high-yield set, not a systematic review.
- **Amass was not used** (the role file lists it). Gap: trial registry and regulatory material, which could show whether any IR-guided-care RCT exists.
- **Abstract-level reading only.** Adjustment sets, missing-data handling and sensitivity analyses come from abstracts. Where a PMID is tagged `[V-cit]`, I did not read its abstract and the sentence attached to it is from general methodological knowledge.
- **`[C-only]` items have no resolved identifier.** They are included because their abstract content was read, but should be resolved before being relied on: Kitabchi 2005 (Diabetes), Aroda 2019 (Diabetes Care), Knowler 2025 (Lancet Diabetes Endocrinol), Xing 2025 (Nutr Metab Cardiovasc Dis), Torréns 2004 (Diabetes Care), Trikudanathan 2013 (Metabolism), Tian 2022 (Cardiovasc Diabetol), Ross 2015 (Eur Heart J).
- Items I wanted but did not find or verify: HOMA-IR in a CVD risk-score reclassification study; reproducibility data on HOMA2; a TyG meta-analysis with PMID I could verify (candidate PMIDs appeared in search results but were not opened, so none is cited); Hanson/Katz/Lorenzo-type cutoff validation studies in IRAS/San Antonio.

## 11. Reference list (verified identifiers only)
| PMID | DOI | Short cite |
|---|---|---|
| 3899825 | n/a (not retrieved) | Matthews 1985, Diabetologia (original HOMA) `[V-cit]` |
| 15161807 | 10.2337/diacare.27.6.1487 | Wallace 2004, Use and abuse of HOMA modeling `[V]` |
| 10902785 | n/a | Katz 2000, QUICKI `[V-cit]` |
| 10480510 | n/a | Matsuda & DeFronzo 1999 `[V-cit]` |
| 10857969 | 10.2337/diacare.23.1.57 | Bonora 2000, HOMA vs clamp `[V]` |
| 23300589 | 10.1371/journal.pone.0052036 | Gast 2012 `[V]` |
| 30170598 | 10.1186/s12933-018-0762-4 | Ormazabal 2018 (review, mechanisms; abstract read, no effect sizes used) `[V]` |
| 26886418 | 10.1056/NEJMoa1506930 | Kernan 2016, IRIS `[V]` |
| 17533210 | 10.1001/archinte.167.10.1068 | Wilson 2007, Framingham Offspring `[V]` |
| 16043747 | 10.2337/diacare.28.8.2013 | Schmidt 2005, ARIC `[V]` |
| 38191206 | 10.1136/bmjdrc-2023-003680 | Hu 2024 `[V]` |
| 35700159 | 10.2337/dc22-0202 | Wang 2022 `[V]` |
| 31047901 | 10.1016/S2213-8587(19)30087-7 | Dennis 2019 `[V]` |
| 29503172 | 10.1016/S2213-8587(18)30051-2 | Ahlqvist 2018 (clusters) `[V]` |
| 19515410 | 10.1016/S0140-6736(09)60619-X | Tabak 2009 `[V]` |
| 19067533 | 10.1089/met.2008.0034 | Simental-Mendía 2008, TyG `[V]` |
| 20484475 | 10.1210/jc.2010-0288 | Guerrero-Romero 2010, TyG vs clamp `[V]` |
| 18535197 | 10.2337/dc08-0097 | Manley 2008 `[V]` |
| 34380182 | 10.1515/cclm-2021-0643 | Matli 2021 `[V]` |
| 38987271 | 10.1515/cclm-2024-0672 | Carobene 2024, EuBIVAS `[V]` |
| 29618016 | 10.1210/jc.2017-02437 | Poon 2018, ARIC repeatability `[V]` |
| 27658115 | 10.1371/journal.pone.0163424 | Lee 2016, HK cutoffs `[V]` |
| 31108989 | 10.3390/medicina55050158 | Horáková 2019, Czech cutoffs `[V]` |
| 20040676 | 10.2337/dc09-1206 | Staten 2010, insulin assay standardisation `[V]` |
| 20508228 | 10.2337/dc10-0034 | Staten response to Heinemann `[V]` |
| 35622611 | n/a | Rosli 2022, insulin assay comparability (PMID matched by author/topic search) |
| 24240655 | 10.1097/EDE.0000000000000018 | Kerr 2014, NRI critique `[V]` |
| 17309939 | 10.1161/CIRCULATIONAHA.106.672402 | Cook 2007, ROC `[V-cit]` |
| 17569110 | n/a | Pencina 2008, NRI/IDI `[V-cit]` |
| 17099194 | n/a | Vickers & Elkin 2006, decision curves `[V-cit]` |
| 11832527 | n/a | Knowler 2002, DPP primary `[V-cit]` (not used for numbers) |
