# Clinical chemist report: can a lab result for insulin, C-peptide or a derived IR index support an individual decision?

Role: ir-clinical-chemist (new role, owns measurement quality). Independent run: no earlier analyst or skeptic reports in `ir-team/` were read. Coverage and reimbursement out of scope. Date: 2026-10-18.

## 0. Method and evidence-reading status (read this first)

Sources: PubMed (search, metadata) and Consensus (one query). Every PMID/DOI below was returned by a PubMed metadata record in this session. Reading depth per source:

| Source | Depth |
|---|---|
| Carobene 2024 EuBIVAS (PMID 38987271) | Abstract only (PubMed, also Consensus) |
| Marcovina 2007 ADA workgroup (PMID 17272483) | Abstract only |
| Miller 2009 (PMID 19325009) | Abstract only |
| Isokuortti 2017 (PMID 28660493) | Abstract only |
| Zhou 2022, 94 Chinese labs (PMID 35177563) | Abstract only |
| ARIC repeatability 2018 (PMID 29618016) | Abstract only (PMC record returned empty full text) |
| Jayagopal 2002 (PMID 12401750) | Abstract only |
| Borai 2013 (PMID 23548151) | Abstract only |
| Tohidi 2014 (PMID 24530467) | Abstract only |
| Geloneze 2009 BRAMS (PMID 19466221) | Abstract only |
| Peplies 2014 IDEFICS (PMID 25376219) | Abstract only |
| Wiedmeyer 2007, Little 2008, Little 2017 (PMIDs 17332147, 18420730, 28646033) | Abstract only |
| Deng 2023 C-peptide EQA (PMID 37141618) | Abstract only |
| Bojsen-Møller 2017 (PMID 28202439) | Abstract only |
| **Interlaboratory LC-MS/MS insulin and C-peptide, Clin Chem 2024 (PMID 38549041, PMC12052497)** | **Full text read** |
| Ann Lab Med 2023 ID-LC-MS/MS C-peptide China (PMID 36843403) | Title only seen. Not used for any figure. |

Bottom line on rigor: only one source was read in full. Numbers quoted from abstracts are what the abstract states. Arithmetic marked "my calculation" is mine, not from a paper.

## 1. Headline conclusions

1. **Fasting insulin is not harmonized.** There is no accepted reference measurement procedure or common calibration for insulin (the full-text 2024 LC-MS/MS paper states there is no reference measurement procedure available for insulin; accuracy was therefore not assessable). Among-assay CV across commercial immunoassays was median 24% (range 12–66%) in the ADA workgroup (2007), and bias vs an ID-LC-MS/MS comparator exceeded 15.5% for 7/10 methods (2009). A 2022 survey of 94 Chinese labs found inter-laboratory CV 21.8% and inter-measurement-system CV 22.4% for insulin. These are consistent across two continents and 15 years, but the **platforms in the 2007/2009 ADA work are old generations**; current-platform multi-vendor figures were not retrieved (gap).
2. **The "~25% inter-laboratory CV" claim for HOMA-IR rests on one small design**: 10 individuals analyzed in 7 European labs (Isokuortti 2017). The insulin-driven CV (25%) is independently echoed by Marcovina 2007 (median 24%) and Zhou 2022 (21.8–22.4%), so the magnitude is plausible, but each study is its own sample of assays and they are not independent proof of current-generation performance. Isokuortti's practical translation is the more striking figure: the same patient with HOMA-IR 2.0 in Helsinki would read 1.3 to 2.1 in six other labs.
3. **Biological variation is the larger problem than analytical imprecision for HOMA-IR.** EuBIVAS (90 non-diabetic adults, 10 weekly samples): CVI of HOMA-IR 26.7% (95% CI 25.5–28.3), QUICKI 4.1%. ARIC older adults (n=102, ~46 days apart): HOMA-IR within-person CV 30.4%, ICC 0.70. Within-run analytical imprecision of most insulin assays is 3.7–10.6% (ADA 2007) and ~2.7% intra-laboratory in the Chinese survey, so most of the observed noise is biological plus between-assay bias.
4. **A single HOMA-IR cannot support an individual decision near a cutoff.** The reference change value is roughly 70–90% (see section 3). Single values far from any threshold (very high or very low) are informative; values within a factor of about 1.5 of a cutoff are not.
5. **Cutoffs are assay-, population- and age-specific, were derived from distributional percentiles in most cases, and are not portable.** Published HOMA-IR upper limits range from 1.9 (Finland, 95th percentile, healthy non-obese) to 2.7 (Brazil, 90th percentile, healthy subgroup) to a 95% interval of 0.63–2.68 (Iran) with different insulin assays and definitions of "healthy" (section 4).
6. **QUICKI is analytically and biologically much more stable than HOMA-IR** in relative terms (CVI 4.1% vs 26.7%) because of the log transform, but its range is narrow (0.33–0.42 in the Tehran reference sample), so a small absolute change spans a large fraction of the interval. A lower CV does not mean better discrimination.
7. **C-peptide has a better standardization story than insulin** (a reference measurement procedure and an NIDDK-led standardization effort exist), but routine methods still disagree, especially at higher concentrations, and normalization to the reference method works only when calibrators are real serum, not WHO reagent.

## 2. Measure-by-measure table

"CVa" analytical; "CVI" within-person biological. n.r. = not retrieved.

| Measure | Analytical performance (source) | Biological variation (source) | Comment |
|---|---|---|---|
| **Fasting insulin (immunoassay)** | Within-assay CV 3.7–39.0%, 7/10 assays ≤10.6%; among-assay CV 12–66%, median 24%; common reference preparation did not reduce among-assay CV; 6/10 assays agreed within 32% total error allowable on biological-variability criteria; cross-reactivity with intact proinsulin <2% in 9/10; with des(64,65) proinsulin >40% for 9/10 (Marcovina 2007, PMID 17272483, abstract). Bias vs ID-LC-MS/MS >15.5% for 7/10 methods in 36–100% of samples; only 4/10 had ≥95% of results within 32% of IDMS; calibration with native-serum panel was most effective harmonization (Miller 2009, PMID 19325009, abstract). Intra-lab CV 2.7%, inter-lab 21.8% (Zhou 2022, PMID 35177563, abstract). | RCV of fasting serum insulin 68.5% (NGT), 79.0% (IFG), 93.4% (IGT), two samples 10 days apart, n=33 (Borai 2013, PMID 23548151, abstract). Within-person CV of insulin ~28.8% (ARIC, PMID 29618016, abstract). | Old-generation ADA assays; Chinese survey is a more recent but different market. |
| **Insulin (LC-MS/MS)** | Antibody-free multiplex LC-MS/MS across 3 labs: total imprecision 4.1–9.2% in verification; inter-lab median imprecision of single measurements 22.2% (IQR 20.9) for insulin using single-point calibration, 15.3% when averaged over 2 days. Reference method for insulin: none available (Clin Chem 2024, PMID 38549041, **full text**). | n.r. | Research-grade; not a routine clinical test. Inter-lab imprecision for insulin by LC-MS/MS was not better than immunoassay in this study. This is a limit on "just use mass spec". |
| **C-peptide (immunoassay)** | 15 labs, 9 methods: within-run CV <2% to >10%, between-run <2% to >18%; sample-based normalization to a mass-spec reference method removed significant between-lab differences (Little 2008, PMID 18420730, abstract). Between-lab variability grew with concentration; WHO reference reagent normalization did not help (Wiedmeyer 2007, PMID 17332147, abstract). Inter-lab CV 16.4%, inter-system 24.5%; after recalibration with two serum pools the inter-system CV fell to 5.7% (Zhou 2022, PMID 35177563, abstract). | n.r. | Recalibration with real serum gives large gains for C-peptide, much less for insulin (22.4% to 17.2%). |
| **C-peptide (LC-MS/MS)** | Slope 1.044, r=0.99, mean bias 5.2% vs University of Missouri reference method across 3 labs; inter-lab imprecision 13.4% single, 10.8% averaged (Clin Chem 2024, PMID 38549041, **full text**). Reference measurement system overview (Little 2017, PMID 28646033, abstract). Commutability: WHO ISR 13/146-derived materials not commutable on >half of six immunoassays; frozen human serum pools commutable on most (Deng 2023, PMID 37141618, abstract). | n.r. | Best-standardized of the analytes. |
| **HOMA-IR (derived from fasting insulin and glucose)** | Inherits insulin bias. Inter-lab CV 25% from insulin (25%) rather than glucose (5%); 10 individuals, 7 labs; HOMA-IR 2.0 in Helsinki read 1.3, 1.6, 1.8, 1.8, 2.0, 2.1 elsewhere (Isokuortti 2017, PMID 28660493, abstract). | CVI 26.7% (95% CI 25.5–28.3), n=90, 10 weekly samples, 5 countries (EuBIVAS, PMID 38987271, abstract). Within-person CV 30.4%, ICC 0.70, minimum detectable change 2.3 (ARIC, PMID 29618016, abstract). In T2D women (n=12), a repeat sample must rise >90% or fall >47% to differ significantly; intraindividual variation 1.05 vs 0.15 in controls (Jayagopal 2002, PMID 12401750, abstract). | Minimum detectable change of 2.3 is larger than most published cutoffs (1.9–2.7). |
| **QUICKI** | Inherits insulin bias, damped by log transform. | CVI 4.1% (95% CI 3.9–4.3) (EuBIVAS, PMID 38987271, abstract). | Tehran healthy reference interval 0.33–0.42 (PMID 24530467, abstract). |
| **Matsuda / OGTT indices** | n.r. (needs 4–5 timed insulin and glucose values, so insulin assay bias enters at every point). | n.r. A direct reproducibility study was not retrieved. | Gap. Separately, after RYGB, fasting and OGTT surrogates did not track clamp-measured change (Bojsen-Møller 2017, PMID 28202439, abstract): a validity, not precision, problem in one surgical population. |
| **TyG, TG/HDL-C** | No insulin assay involved. Glucose and lipid assays are well harmonized (general knowledge, not source-verified here). | TG/HDL-C within-person CV 23.0%, ICC 0.80, minimum detectable change 1.4 (ARIC, PMID 29618016, abstract). TyG: no repeatability study retrieved (searches returned nothing). | The advantage of these indices is assay portability, not precision. TG alone has CV 20.6% in ARIC. |

## 3. What single-value use can and cannot support

All arithmetic here is my calculation unless a source is named.

**Reference change value.** RCV = 1.414 x Z x sqrt(CVa^2 + CVI^2), Z=1.96 for 95%.
- HOMA-IR: using EuBIVAS CVI 26.7% and an assumed CVa of about 5% (assumption, based on the 3.7–10.6% range for good assays), RCV is about 75% symmetric; log-normal asymmetric form would be roughly +100% / -50%. This agrees with the empirical Jayagopal figures in T2D (+90% / -47%) and with Borai's insulin RCV 68.5–93.4%. ARIC reports minimum detectable change 2.3 HOMA units over ~46 days (abstract).
- QUICKI: CVI 4.1% with CVa about 1% gives RCV about 11%, i.e. roughly 0.04 QUICKI units, which is about half the Tehran healthy interval width (0.33–0.42).
- Implication: a "change in insulin resistance" of less than about 70% in HOMA-IR cannot be distinguished from noise in one person from two samples. Treatment-response monitoring by HOMA-IR in an individual is not supported at plausible effect sizes (a reduction of 20–40% is typical in trial reporting; not verified here).

**Probability of crossing a cutoff on repeat.** Illustration (my calculation; assumes log-normal, CV 27%, no between-assay bias): a patient whose true mean HOMA-IR is 25% above the cutoff has about a 20% chance of reading below it on a single repeat; a patient exactly at the cutoff has 50%. Add the between-laboratory spread (25% CV) when the repeat is at a different lab and the misclassification zone widens further. Not measured in any retrieved study: an empirical cutoff-crossing rate on repeat testing. That is a gap.

**Index of individuality.** CVG (between-person) for HOMA-IR was not in the retrieved abstract, so the index of individuality cannot be stated from verified data. A CVI near 27% against a typical population spread suggests a population reference interval is moderately useful for screening at the extremes but poor for monitoring; confirm CVG from the EuBIVAS full text before relying on this.

**Supported:**
- Population-level ranking, research use, epidemiology (noise averages out).
- Very high fasting insulin or HOMA-IR in a single patient as a prompt for confirmatory repeat, preferably in the same laboratory with the same method.
- C-peptide for endogenous insulin secretion (diabetes classification, hypoglycemia work-up) with awareness of method differences.

**Not supported:**
- Classifying an individual as insulin resistant or not from one HOMA-IR near any published cutoff.
- Applying a cutoff from a paper to a result from a different assay.
- Tracking an individual's response to therapy with HOMA-IR over short intervals unless the change exceeds roughly 70–90%.
- Comparing results across laboratories or over time if the lab changed method or lot.

## 4. Cutoff and reference interval problems

1. **No common measurand.** Without a reference measurement procedure or common calibration, an insulin value is method-defined. Isokuortti 2017 (abstract) states standardisation of insulin assays "would be the first step" to define HOMA-IR normal values.
2. **Different derivations.** Published thresholds come from at least four different logics: healthy-subgroup percentile (Finland: 95th percentile 1.9 and 2.0 in two cohorts, PMID 28660493; Brazil: 90th percentile, HOMA1-IR >2.7, PMID 19466221), reference interval by IFCC nonparametric method (Iran: HOMA1-IR 0.63–2.68, HOMA2-IR 0.40–1.80, QUICKI 0.33–0.42; fasting insulin 2.11–12.49 uU/mL, n=309 healthy non-obese, PMID 24530467), outcome-anchored ROC cutoff (Finland: 1.9 for liver fat >=5.56%, sensitivity 87%, specificity 79%; Brazil: >2.3 for metabolic syndrome, sensitivity 76.8%, specificity 66.7%), and pediatric percentile curves (IDEFICS: median HOMA-IR 0.5/0.4 at age 3–<3.5 girls/boys rising to 1.7/1.4 at 10.5–<11; PMID 25376219). All abstract-read.
3. **Assay generation and platform.** The IDEFICS values are tied to one electrochemiluminescence immunoassay; the Tehran study also used electrochemiluminescence. Given the 12–66% among-assay CV in the ADA work, none transfers to another platform without a conversion, and no such conversion factors were found.
4. **Population dependence.** Insulin and HOMA-IR rise with age through childhood and differ by sex in children (IDEFICS); in adults insulin fell with age in Tehran. Healthy definitions differ (non-obese, normal fasting glucose, no drugs). Ethnic and BMI portability was not externally validated in any retrieved paper; the two Finnish cohorts agree with each other (1.9 vs 2.0) but that is internal replication within one country and one lab family.
5. **Percentile-based cutoffs are prevalence-defined**, not risk-defined. A 95th percentile of the healthy group classifies 5% of the healthy as abnormal by construction, regardless of clinical meaning.
6. **Cutoff plus noise.** With CVI about 27% and inter-lab CV about 25%, the uncertainty band around a single result (roughly +/-70% combined at 95%, my calculation: sqrt(27^2+25^2) = 37% SD, times 1.96 = 73%) exceeds the gap between published cutoffs (1.9 to 2.7, about 40%). The disagreement between published cutoffs is smaller than the measurement noise on a single patient.
7. **Pre-analytical.** Hemolysis, delay to separation and insulin degradation matter for insulin (the LC-MS/MS paper observed leftover clinical samples with low insulin relative to C-peptide "consistent with insulin degradation", full text). The 2024 paper also flags that exogenous insulin and genetic variants affect LC-MS/MS and immunoassay differently. I did not retrieve quantitative hemolysis or stability data and can state none (gap).

## 5. Cross-reactivity and analogs

Verified only at abstract level and for old assays: in the ADA 2007 workgroup, 9/10 assays cross-reacted <2% with intact proinsulin, 8/10 <3% with split (32,33) proinsulin, but 9/10 exceeded 40% with des(64,65) proinsulin (PMID 17272483). The full text of the 2024 paper notes antibody cross-reactivity with proinsulin and therapeutic analogs is often undisclosed and that immunoassays vary in detecting analogs. Current-assay analogue cross-reactivity tables (glargine, detemir, degludec, etc.) were not retrieved. Practical consequence: in patients on insulin therapy or with high proinsulin (long-standing T2D, beta-cell stress), insulin and insulin-based indices are not interpretable.

## 6. Comparison notes for the team (weakest and strongest claims)

- **Strong:** the existence of large inter-assay disagreement (consistent across ADA 2007, 2009, China 2022). Biological variation of HOMA-IR from EuBIVAS (n=90, 10 occasions, formal CV-ANOVA, includes CIs) supported by ARIC and by T2D small studies.
- **Weak:** the single "25%" figure as a universal number. It comes from 10 individuals x 7 labs and should be cited as "about 22–25% across three independent studies of different assay sets", not as a single established value. Treat all as order-of-magnitude.
- **Weak:** Jayagopal 2002 (12 T2D women, 11 controls, postmenopausal, diet-controlled, 2002 assays) and Borai 2013 (33 subjects, two samples) are small; both agree with larger EuBIVAS in order of magnitude.
- **Extrapolation risk:** EuBIVAS is non-diabetic adults; ARIC is age 68–88 without diabetes. No biological variation data retrieved for adolescents, PCOS, MASLD, pregnancy or on treatment.

## 7. Gaps (not found or not verified)

1. Current-generation multi-vendor insulin comparison with traceability to an IDMS or similar reference; any CAP or EQA survey summary with 2020+ data.
2. Biological variation for insulin itself and C-peptide from EuBIVAS or the EFLM biological variation database (not directly retrieved; only HOMA-IR and QUICKI from EuBIVAS abstract, plus ARIC and small studies for insulin). CVG and index of individuality not verified.
3. Matsuda index, OGIS and HOMA2 reproducibility; TyG repeatability (search returned nothing, which is not evidence of absence).
4. Empirical rate at which patients cross HOMA-IR cutoffs on repeat testing.
5. Quantitative pre-analytical data: hemolysis interference, time-to-separation, tube type, fasting duration, posture and circadian effects on insulin.
6. Conversion factors between insulin assays, and any external validation of HOMA-IR cutoffs across ethnicities, BMI strata and age.
7. Full text of EuBIVAS, ARIC, Marcovina 2007, Miller 2009 and Isokuortti 2017 (only abstracts were available to me; PMC full text exists for none of these except ARIC, whose PMC record came back empty).
8. Analytical performance specifications for insulin/HOMA-IR derived from biological variation (EuBIVAS keywords indicate it addresses this, but I did not read the content).

## 8. References (all verified against PubMed metadata in this session)

1. Carobene A, et al. The biological variation of insulin resistance markers: data from the European Biological Variation Study (EuBIVAS). Clin Chem Lab Med 2024;63(1):110-117. PMID 38987271. doi:10.1515/cclm-2024-0672.
2. Marcovina S, et al. Standardization of insulin immunoassays: report of the American Diabetes Association Workgroup. Clin Chem 2007;53(4):711-6. PMID 17272483. doi:10.1373/clinchem.2006.082214.
3. Miller WG, et al. Toward standardization of insulin immunoassays. Clin Chem 2009;55(5):1011-8. PMID 19325009. doi:10.1373/clinchem.2008.118380.
4. Isokuortti E, et al. Use of HOMA-IR to diagnose non-alcoholic fatty liver disease: a population-based and inter-laboratory study. Diabetologia 2017;60(10):1873-1882. PMID 28660493. doi:10.1007/s00125-017-4340-1.
5. Zhou W, et al. Current status of serum insulin and C-peptide measurement in clinical laboratories: experience from 94 laboratories in China. Ann Lab Med 2022;42(4):428-437. PMID 35177563. doi:10.3343/alm.2022.42.4.428.
6. Interlaboratory comparison of antibody-free LC-MS/MS measurements of C-peptide and insulin. Clin Chem 2024. PMID 38549041. doi:10.1093/clinchem/hvae034. (Full text read via PMC12052497.)
7. ARIC short-term repeatability of insulin resistance indexes in older adults. J Clin Endocrinol Metab 2018. PMID 29618016. doi:10.1210/jc.2017-02437.
8. Jayagopal V, et al. Biological variation of homeostasis model assessment-derived insulin resistance in type 2 diabetes. Diabetes Care 2002;25(11):2022-5. PMID 12401750. doi:10.2337/diacare.25.11.2022.
9. Borai A, et al. Reference change values for insulin and IGFBP-1 in individuals with varying degrees of glucose tolerance. Scand J Clin Lab Invest 2013;73(4):274-8. PMID 23548151. doi:10.3109/00365513.2013.771281.
10. Tohidi M, et al. Age- and sex-specific reference values for fasting serum insulin levels and insulin resistance/sensitivity indices in healthy Iranian adults. Clin Biochem 2014;47(6):432-8. PMID 24530467. doi:10.1016/j.clinbiochem.2014.02.007.
11. Geloneze B, et al. HOMA1-IR and HOMA2-IR indexes in identifying insulin resistance and metabolic syndrome: BRAMS. Arq Bras Endocrinol Metabol 2009;53(2):281-7. PMID 19466221. doi:10.1590/s0004-27302009000200020.
12. Peplies J, et al. Percentiles of fasting serum insulin, glucose, HbA1c and HOMA-IR in pre-pubertal normal weight European children from the IDEFICS cohort. Int J Obes 2014;38 Suppl 2:S39-47. PMID 25376219. doi:10.1038/ijo.2014.134.
13. Little RR, et al. Standardization of C-peptide measurements. Clin Chem 2008;54(6):1023-6. PMID 18420730. doi:10.1373/clinchem.2007.101287.
14. Wiedmeyer HM, et al. International comparison of C-peptide measurements. Clin Chem 2007;53(4):784-7. PMID 17332147. doi:10.1373/clinchem.2006.081570.
15. Little RR, et al. Implementing a reference measurement system for C-peptide: successes and lessons learned. Clin Chem 2017;63(9):1447-1456. PMID 28646033. doi:10.1373/clinchem.2016.269274.
16. Deng Y, et al. Exploration of suitable external quality assessment materials for serum C-peptide measurement. Clin Chem Lab Med 2023;61(9):1597-1604. PMID 37141618. doi:10.1515/cclm-2023-0215.
17. Bojsen-Møller KN, et al. Variable reliability of surrogate measures of insulin sensitivity after Roux-en-Y gastric bypass. Am J Physiol Regul Integr Comp Physiol 2017;312(5):R797-R805. PMID 28202439. doi:10.1152/ajpregu.00291.2016.
