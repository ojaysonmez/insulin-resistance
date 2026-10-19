# IR clinical utility: evidence set (ir-evidence-searcher)

Run date: 2026-10-18. Independent retrieval. No file in `ir-team/` was read (the folder was only listed, not opened). Coverage and reimbursement out of scope. No evidence is graded or interpreted here; one-line design descriptions only.

Conventions
- Identifier check: every PMID/DOI below was returned by an NCBI E-utilities (PubMed) esummary/efetch record in this session, and the title shown matches that record. Crossref was not queried. The Scholar Sidekick verifier failed (rate-limit / "not subscribed"), so no second check was possible.
- Read level codes:
  - **FT-grep**: full text retrieved (Europe PMC or NCBI PMC efetch), then searched programmatically for IR terms (and, where stated, read in the matching passages). Not read cover to cover.
  - **FT-WF**: full text fetched through WebFetch, which returns a small-model extract of a window of the page. Windows were partial and each had its own truncation. A "no match" from FT-WF is NOT proof of absence. Windows are stated.
  - **ABS**: abstract only (PubMed record). **TITLE**: title/listing only.
- Preprints are flagged UNREVIEWED.
- "Count" in the log is what the database reported; I screened titles of the top 4-25 hits per string, not every hit.

---

## Question 1. Randomized or pragmatic trials of IR-guided or IR-stratified care

**Headline retrieval result: no randomized "strategy" trial was found that compares care guided by an IR measurement (fasting insulin, HOMA-IR, OGTT insulin, C-peptide, TyG, TG/HDL-C) against care without it.** See negative-result log (S-Q1 strings). Closest items are below, in three groups.

### 1a. Completed RCTs where randomization was stratified by, or analysed by, IR status

| Identifier | Design (one line) | Population | N | Outcome | Read |
|---|---|---|---|---|---|
| PMID 34531293, doi 10.2337/db21-0526 (Diabetes 2021, PLIS) | Multicentre RCT; participants stratified into high-/low-risk phenotype using thresholds of insulin secretion, insulin sensitivity and liver fat, then randomized within phenotype (conventional vs intensified lifestyle; control in low-risk) | Prediabetes (ADA glucose criteria) | 1,105 | Post-challenge glucose change, liver fat, CV risk, 3-y glucose normalisation | ABS |
| PMID 15897479, doi 10.1038/oby.2005.79 (Obes Res 2005) | RCT in pre-defined strata: insulin-sensitive (fasting insulin <10) vs insulin-resistant (>15 microU/mL), each randomized to high-CHO/low-fat or low-CHO/high-fat hypocaloric diet, 16 wk | Obese non-diabetic women | 21 | % body weight, Si, RMR, lipids | ABS |
| PMID 26638192, doi 10.1002/oby.21331 (Obesity 2016) | Pilot 2x2 RCT, low-fat vs low-carb by IR status (median split of OGTT insulin AUC) | Adults BMI 28-40 | 61 | 6-mo weight change; diet x IR interaction not significant per abstract | ABS (PMC5898445 exists, not read) |
| PMID 39756404, doi 10.1002/oby.24201 (Obesity 2025) | RCT low-fat vs low-CHO, 10 wk controlled feeding; SI and acute insulin response from IVGTT tested as modifiers | African American women with obesity | 69 | Fat mass, REE/TEE | ABS |
| PMID 29466592, doi 10.1001/jama.2018.0245 (DIETFITS) | RCT low-fat vs low-carb 12 mo; pre-specified test of diet x INS-30 (30-min insulin on glucose challenge) interaction | Adults 18-50, BMI 28-40, no diabetes | 609 | 12-mo weight; diet x INS-30 interaction P=0.47 in abstract | ABS (the PMC copy PMC5839290 held only ~10k chars: key points + abstract) |
| PMID 38177805, doi 10.1038/s42255-023-00943-3 (Nat Metab 2024) | Open-label RCT semaglutide vs dapagliflozin 6 mo in T2D with severe insulin-deficient (SIDD) or severe insulin-resistant (SIRD) features | T2D | 239 | HbA1c; abstract reports no significant drug x subgroup interaction; continuous insulin secretion/resistance variables reported as informative | ABS (PMC10822775 exists, not read) |
| PMID 38599278, doi 10.1016/j.metabol.2024.155910 (Metabolism 2024; DEXLIFE + EGIR-RISC) | Cluster/regression analysis of RCT cohort by baseline insulin sensitivity/secretion vs response to weight-loss lifestyle | High T2D risk | 373 (DEXLIFE) | Glucose tolerance after weight loss | ABS |

### 1b. IR-enriched (eligibility defined by an IR measure) RCT

| Identifier | Design | Population | N | Outcome | Read |
|---|---|---|---|---|---|
| PMID 26886418, doi 10.1056/NEJMoa1506930 (IRIS, NEJM 2016); NCT00091949 | Double-blind RCT pioglitazone vs placebo; entry required HOMA-IR >3.0 measured in central labs | Recent ischemic stroke/TIA, no diabetes | 3,876 | Stroke or MI (HR 0.76 per abstract); diabetes onset; no IR-negative comparator group | FT-grep (PMC4887756, 49.5k chars; read the HOMA-IR, assay, subgroup and discussion passages) |
| PMID 27465265, doi 10.2337/dc16-0798; PMID 29084736, doi 10.1161/CIRCULATIONAHA.117.030458 | IRIS secondary analyses (diabetes prevention; stroke) | as above | as above | | TITLE |

### 1c. Registered trials with IR-defined or IR-guided allocation (none has results)

| Registry ID | Source | Design (one line) | N | Status | Read |
|---|---|---|---|---|---|
| CTRI/2026/09/117733 (CTRI, via WHO ICTRP) | "Phenotype-guided add-on pharmacotherapy vs lifestyle alone" in prediabetes. Fasting phenotype defined partly by HOMA-IR >3.8 (men) / >3.46 (women) gets metformin; post-prandial phenotype gets voglibose; stratified randomization | 180 target | Not yet recruiting; first enrolment 25-09-2026 | ICTRP record page, read |
| IRCT20170812035642N11 | Stratified permuted-block randomization by three metabolic profiles (insulin resistance / lipid / combined) for personalised diet plans | 144 | Recruiting | ICTRP record page, read |
| NCT07710274 (PRISM-I) | Pilot RCT of precision lifestyle in metabolic syndrome with HOMA-IR >=2.5; primary outcome HOMA-IR; feasibility aim | 200 est. | Recruiting | CT.gov API record, read |
| ISRCTN74144960 (MET-HFpEF) | Metformin vs placebo in HFpEF; eligibility via FIRI >=2.7 OR prediabetes OR BMI >=30 (IR is one of three entry routes) | 66 | Recruiting | ICTRP record page, read |
| ChiCTR2400085828 | Non-randomized: "precision typing intervention" vs none in elderly early T2D, typing based on islet function tests | 628 + 628 | Pending | ICTRP record page, partial read |
| NCT06856291 (TRIM-IR) | Observational, semaglutide response in non-diabetic obesity by degree of IR | 40 | Completed | CT.gov API record, read |

---

## Question 2. Incremental value / reclassification (delta C-statistic, NRI/IDI, calibration, decision curves)

Search note: for HOMA-IR/fasting insulin the yield of formal incremental-value analyses was small (items 2a). Most TyG items are association studies, many from Chinese cohorts (CHARLS, CHNS). Decision-curve / calibration hits (S: "TyG ... decision curve OR calibration", 110 hits) were listed but mostly not individually screened.

### 2a. Studies that explicitly test added discrimination/reclassification

| Identifier | Design | Population | N | Index / comparator | Reported incremental outcome | Read |
|---|---|---|---|---|---|---|
| PMID 25944628, doi 10.1161/CIRCOUTCOMES.114.001563 (WHI) | Prospective cohort, 10-y CVD, Cox + discrimination/reclassification | Postmenopausal women, no CVD/AF/diabetes | 15,288 (894 events) | Fasting insulin, HOMA-IR, TG/HDL-C, IFG added to traditional factors | Abstract: no improvement in discrimination/reclassification | ABS |
| PMID 38191206, doi 10.1136/bmjdrc-2023-003680 | Cohort, prediction models, 10-y incident diabetes; AUC, cNRI, IDI, calibration | Japanese workers (94.7% men) | 5,578 (943 events) | HOMA-IR + HOMA-beta added to BMI/HbA1c model; FPG added | FPG improved; HOMA-IR/HOMA-beta did not materially improve (abstract) | ABS (PMC10806829 exists, not read) |
| PMID 39117485, doi 10.1016/j.numecd.2024.06.010 | Population cohort, ~15 y MACE; C-index, continuous NRI | Healthy general-population adults | 1,970 (332 MACE) | TyG added to SCORE risk factors +/- HMOD | C-index +0.005 (P=0.042) per abstract | ABS (retrieved via Consensus abstract and PubMed record) |
| PMID 42569452, doi 10.3389/fcvm.2026.1804411 | Cohort (CHNS) + meta-analysis of incremental value | Adults 45-80 without CVD | cohort not extracted; meta-analysis 5 cohorts | TyG added to Framingham score | C-index 0.731 to 0.732 (cohort); pooled gain 0.0004 (95% CI -0.0092 to 0.0100); certainty "very low" | ABS (full abstract via Consensus). PMC13449919 exists, not read |
| PMID 32534586, doi 10.1186/s12933-020-01054-z | Cohort, 3-y MACE; C-statistic, IDI, NRI | Diabetes + acute coronary syndrome | 2,531 | TyG added to prognostic model | Improved C, IDI, NRI per abstract (AUC of TyG alone 0.560) | ABS |
| PMID 26683265, doi 10.1111/eci.12583 | Cohort (VMCUN), ~10 y, Cox + ROC vs Framingham model | Apparently healthy adults | 5,014 | TyG added to Framingham variables | Reported ROC comparison; numbers not extracted | ABS (partial) |
| PMID 24098646, doi 10.1371/journal.pone.0074410 | Clamp-derived ISI-cal vs HOMA-IR; ROC for incident diabetes and CVD in independent cohort | Asian men (derivation 253) | derivation 253 + independent cohort | ISI-cal vs HOMA-IR | CVD AUC 0.74 vs 0.61; diabetes 0.77 vs 0.76 (per Consensus abstract) | ABS |
| PMID 41178693, doi 10.1111/dom.70270 | Derivation (ATTICA) + external validation of TyG prognostic cutoff; plus registry for subclinical disease | General population / primary prevention | 1,677 derivation; 1,237 validation; 1,170 registry | TyG cutoff for composite CV endpoint | Cutoff derived and externally validated (details not extracted) | ABS (PMC12803534 exists, not read) |
| PMID 37906402, doi 10.1007/s12020-023-03574-6 | Retrospective cohort; C-statistics, NRI, IDI of four non-insulin IR indices vs HOMA-IR for diabetic kidney disease | New T2D | 521 | TyG, TG/HDL, TyG-BMI, METS-IR vs HOMA-IR | C-statistic 0.652 for TyG and TG/HDL; positive incremental effects | ABS |
| PMID 35771773, doi 10.2337/dc22-0272 (EUROASPIRE V) | Cross-sectional screening accuracy of HOMA-IR, HOMA2 (insulin, C-peptide) vs OGTT for dysglycemia | Coronary disease, no known dysglycemia | 3,534 | HOMA indices, thresholds by Youden | Thresholds and accuracy reported (not extracted) | ABS |

### 2b. Comparative / association evidence that other roles may cite (design only)

| Identifier | Design | N | Read |
|---|---|---|---|
| PMID 23300589, doi 10.1371/journal.pone.0052036 | Meta-analysis of cohorts: fasting glucose vs fasting insulin vs HOMA-IR and incident CVD (pooled CHD RR high vs low 1.52 per abstract) | 65 studies, 516,325 | ABS (PMC3532497 exists, not read) |
| PMID 33812373, doi 10.1186/s12933-021-01268-9 | Meta-analysis, TyG and ASCVD incidence (HR 1.61 highest vs lowest) | 8 cohorts, 5,731,294 | ABS |
| PMID 39180024, doi 10.1186/s12933-024-02392-y | Umbrella review of TyG meta-analyses | 32 meta-analyses | ABS |
| PMID 35778731, doi 10.1186/s12933-022-01546-0; PMID 37415168, doi 10.1186/s12933-023-01906-4; PMID 32928692, doi 10.1016/j.pcd.2020.09.001 | TyG meta-analyses (general-population CVD; CAD; incident T2D) | | TITLE |
| PMID 42298603, doi 10.1186/s12933-026-03244-7 | NHANES cohort, ten IR indices (HOMA-IR, McAuley, QUICKI, TyG, eGDR etc.) vs all-cause/CV mortality in hypertensive adults | 7,548 | ABS (via Consensus) |
| PMID 42062547, doi 10.1038/s41598-026-51393-2 | MASHAD cohort, nine IR indices, 10-y CAD | 7,858 | ABS |
| PMID 40887654, doi 10.1186/s13098-025-01933-z | CHARLS cohort, nine IR surrogates and incident CVD | 7,662 | ABS |
| PMID 40741171, doi 10.3389/fendo.2025.1508667 | SPRINT post hoc, TyG and CV events | 9,323 | ABS |

Preprints (UNREVIEWED, Europe PMC index): PPR1266531 (medRxiv, doi 10.64898/2026.04.02.26350088) composite metrics beyond TyG for AF risk prediction; PPR1338612 (Research Square, doi 10.21203/rs.3.rs-11285131/v1) proposed "hepatic insulin resistance syndrome" classification framework. Titles only. No preprint reporting HOMA-IR/fasting-insulin incremental value was found.

---

## Question 3. Treatment-by-baseline-IR interaction in major trials

| Identifier | Trial / design | Population, N | IR measure and split | Interaction result in abstract/text | Read |
|---|---|---|---|---|---|
| PMID 42145088, doi 10.1161/STROKEAHA.125.056010 | LAMP post hoc (liraglutide + standard vs standard; open-label RCT) | T2D with minor stroke/high-risk TIA; 510 of 636 enrolled analysed | HOMA-IR, cutoff 2.5 "based on prior studies in Asian populations" | P for interaction 0.02 (stroke recurrence, composite vascular events); ARR 12.3% in HOMA-IR >=2.5; none in <2.5. Paper states analysis was post hoc, not pre-specified, small sample/events, open-label | FT-grep (PMC13281981, 45k chars; results, methods, limitation passages read) |
| PMID 26886418 (IRIS) | see Q1b | | HOMA-IR >3.0 eligibility | 13 pre-specified subgroups; text says no significant differences in any subgroup. Whether HOMA-IR tertile was one of them was not extracted | FT-grep |
| PMID 29466592 (DIETFITS) | see Q1a | | INS-30 | diet x insulin-secretion P=0.47 | ABS |
| PMID 38151465, doi 10.2337/dc23-1420 | FIDELITY pooled (finerenone vs placebo) | T2D + CKD, 13,026 | eGDR (waist, HbA1c, hypertension; not an insulin assay), median split | P interaction 0.23 (CV), 0.28 (kidney) | ABS |
| PMID 40916719, doi 10.1002/ejhf.70034 | FINEARTS-HF exploratory | HF, 5,851 | eGDR, median 5.1 | Treatment effect by eGDR evaluated (numbers not extracted) | ABS |
| PMID 38190619, doi 10.2337/dc23-1059 | GRADE (glimepiride vs liraglutide vs sitagliptin added to metformin) | T2D, ~3,784 in this analysis | HOMA2-%S and C-peptide responses over time | Heterogeneity P-values 0.001 to 0.025 for sitagliptin vs others on some outcomes | ABS |
| PMID 38285957, doi 10.2337/dc23-1782 | GRADE baseline factors and differential effectiveness | T2D, 5,047 | multivariable baseline factors | not extracted | ABS |
| PMID 40311647, doi 10.1016/S2213-8587(25)00022-1 | DPP/DPPOS 21-y heterogeneity of lifestyle and metformin effects | Prediabetes, 3,195 analysed | baseline risk indices (abstract: greater ILS effect with higher fasting glucose, HbA1c and multivariable risk indices) | Whether insulin-based variables were among them not confirmed | ABS (PMC12414453 exists, not read) |
| PMID 40497454, doi 10.1210/clinem/dgaf350 | DPP post hoc, k-means on 22 biomarkers | Prediabetes, 3,145 | Subgroup 1 "severe insulin resistance with severe obesity" (31%) vs subgroup 2 | Metformin benefit greater in subgroup 1 (P interaction <.05); clinical variable model discriminated risk better than clusters | ABS |
| PMID 31047901, doi 10.1016/S2213-8587(19)30087-7 | ADOPT-based data-driven clusters vs simple clinical-feature models | T2D, 4,351 | Cluster membership vs continuous features | not extracted | ABS |
| PMID 31647106, doi 10.1093/humupd/dmz029 | IPD meta-analysis of first-line ovulation induction in PCOS | PCOS | baseline serum insulin | Interaction for CC+metformin vs CC (live birth interaction RR 1.03, 95% CI 1.01-1.06); letrozole effect modified by testosterone | ABS |
| PMID 38177805 (Nat Metab) | see Q1a | | | no significant drug x SIDD/SIRD interaction | ABS |
| PMID 15897479, 26638192, 39756404 | see Q1a | | | Cornier: weight loss favoured the diet matched to IR state; 2016 pilot: no diet x IR interaction; 2025: low-CHO advantage in low-SI subgroup | ABS |
| PMID 41293821, doi 10.1161/HYPERTENSIONAHA.125.24666 | SPRINT post hoc, IR and response to intensive BP treatment on cognitive outcomes | 7,427 analysed | IR index not extracted | not extracted | ABS |

Other Q3 items located by title only: PMID 22639398 (HOMA-S and HbA1c reduction with GLP-1 analogue), PMID 36811468 (carbohydrate-insulin model reanalysis of DIETFITS), PMID 34959879 (baseline IR and sdLDL response to diets).

---

## Question 4. Guideline recommendations on IR measurement

Statements are paraphrased from what the text extraction returned. "No hit" means no matching sentence in the text segment actually read, not a statement that the guideline is silent.

| Guideline (PMID, doi) | What was found about measuring IR | Read |
|---|---|---|
| International evidence-based PCOS guideline 2023 (Hum Reprod, PMID 37580037, doi 10.1093/humrep/dead156; same guideline also PMID 37580314, 37580861, 37589624) | Practice points 1.9.12 and 3.1.10 state IR is a pathophysiological factor, but clinically available insulin assays are of limited clinical relevance and should not be used in routine care. Also states routinely available IR measures are inaccurate and clinical measurement is not currently recommended. Metformin recommendation 4.3.1 for adults with BMI >=25 | FT-grep (PMC10477934, 115k chars; all 7 matching sentences read) |
| EASL-EASD-EASO MASLD CPG 2024 (Obes Facts copy PMID 38852583, doi 10.1159/000539371; Diabetologia executive summary PMID 38869512, doi 10.1007/s00125-024-06196-3; J Hepatol version PMID 38851997 not retrievable) | Recommendation (LoE 3, weak, consensus): assessment of IR (e.g., HOMA-IR or OGTT-derived estimates) may be considered to clarify metabolic dysfunction in adults with suspected MASLD and without established T2D. Text says HOMA-IR can use fasting insulin or C-peptide with glucose, and that interpretation requires standardised insulin/C-peptide measurement | FT-grep (PMC11299976, 346k chars; PMC11519095, 64k chars) |
| AASLD practice guidance on NAFLD 2023 (PMID 36727674, doi 10.1097/HEP.0000000000000323) | IR discussed as pathogenic and near-universal in NAFLD; initial evaluation includes physical-exam signs of IR; no recommendation to measure insulin/HOMA-IR found among 45 matched sentences (first 40 inspected incl. all body-text ones). Pioglitazone improves histology and IR in NASH with/without dysglycemia | FT-grep (PMC10735173 author manuscript, 235k chars) |
| AACE comprehensive diabetes care plan guideline 2022 (PMID 35963508, doi 10.1016/j.eprac.2022.08.002) | Recommendation: in persons with insulin resistance, prediabetes or T2D and prior TIA/stroke, pioglitazone should be considered to reduce recurrent stroke. No HOMA-IR, fasting-insulin or C-peptide measurement statement matched in a 1.05M-char text | FT-grep (PMC10200071) |
| ADA Standards of Care 2026, section 3 Prevention (PMID 41358891, doi 10.2337/dc26-S003) | Recommendation 3.13: in people with stroke history and evidence of insulin resistance and prediabetes, pioglitazone may be considered; supporting text cites IRIS (HOMA-IR >=3.0). No other IR measurement statement in the window read | FT-WF (PMC12690170, chars 0-100,000 of 159,129) |
| ADA 2026 section 2 Diagnosis/Classification (PMID 41358893, doi 10.2337/dc26-S002) | IR appears in narrative and in risk-factor tables (e.g., signs of IR as testing criterion). C-peptide test only for classification in people on insulin; no HOMA-IR/fasting insulin hit | FT-WF (PMC12690183, chars 0-100,000 of 275,002) |
| ADA 2026 section 10 CV disease and risk management (PMID 41358899, doi 10.2337/dc26-S010) | No IR/HOMA-IR/TyG hit | FT-WF (PMC12690187, chars 0-100,000 of 373,023) |
| Standards of Care in Overweight and Obesity 2026, screening/staging (PMID 42242835, doi 10.1136/bmjdrc-2026-006247) | One generic mention of IR as a mechanism of obesity-related disease; no measurement statement | FT-grep (PMC13266248, 190k chars) |
| Definition and diagnostic criteria of clinical obesity, Lancet D&E Commission 2025 (PMID 39824205, doi 10.1016/S2213-8587(24)00316-4) | No IR/HOMA-IR/fasting-insulin measurement criterion found | FT-grep (PMC11870235, 263k chars) |
| ESC 2023 diabetes and CVD (PMID 37622663, doi 10.1093/eurheartj/ehad192) | IR mentioned: "markers of insulin resistance such as acanthosis nigricans or fatty liver" as a criterion for regular screening (section 3.3); T2D described as IR plus relative insulin deficiency; C-peptide for unclear T1D cases. No recommendation to measure IR found | FT-WF (publisher page 309,963 chars; windows 0-100k, 100-200k, 200-300k; each window itself truncated, so coverage is partial) |
| ESC 2021 CVD prevention (PMID 34458905, title matched; doi not recorded) | IR only in narrative (adiposity sequelae, ED risk factors). No measurement recommendation found | FT-WF (page text 216,746 chars; the text served ended in section 4.2.3; later sections not seen) |
| ACC/AHA 2019 primary prevention (PMID 30879355, doi 10.1161/CIR.0000000000000678) | One narrative T2D sentence about IR; no HOMA-IR/fasting insulin/measurement recommendation in window read | FT-WF (PMC7734661 page; window 0-100,000 of 533,008) |
| Endocrine Society PCOS guideline 2013 (PMID 24151290, doi 10.1210/jc.2013-2350) | Recommends OGTT (fasting + 2-h glucose) to screen for IGT/T2D (rec 2.11); no insulin-assay recommendation matched | FT-grep (PMC5399492, 170k chars) |

Not retrieved (see list below): ADA 1997 consensus on insulin resistance, ACE 2003 position statement on the IR syndrome, ISPAD 2022, NICE NG28/NG246, AHA 2023 CKM advisory, KDIGO 2022, AHA 2022 NAFLD statement, AACE 2026 T2D algorithm, 2018 Endocrine Society paediatric obesity guideline (PMC copy is 6k chars), ADA 2026 remaining sections and the unread tails of the WebFetch windows.

---

## Question 5. Assay standardization and cutoff validation

### 5a. Insulin / C-peptide assay standardization and variability

| Identifier | Design | Content | Read |
|---|---|---|---|
| PMID 17272483, doi 10.1373/clinchem.2006.082214 (Clin Chem 2007) | ADA Workgroup comparison of 12 commercial insulin methods from 9 manufacturers | Within-assay CV 3.7-39.0%; among-assay CV 12-66% (median 24%); a common reference preparation did not change among-assay CV (per abstract) | ABS |
| PMID 17586588, doi 10.1373/clinchem.2007.088393 | Pilot IDMS (isotope dilution LC-MS/MS) standardization | | TITLE |
| PMID 19325009, doi 10.1373/clinchem.2008.118380 (Clin Chem 2009) | 39 single-donor sera x 10 commercial methods vs IDMS reference procedure calibrated with recombinant insulin | Approaches to harmonize results | ABS |
| PMID 20040676, doi 10.2337/dc09-1206 (Diabetes Care 2010) | Workgroup summary | Recommendations on assay specificity, sample type, SI units (pmol/L), traceability to IDMS; says cutoffs for insulin and insulin sensitivity can follow once standardized | FT-grep (PMC2797975, 12.6k chars, complete) |
| PMID 18535197, doi 10.2337/dc08-0097 (Diabetes Care 2008) | 11 insulin assays in serum + 1 in plasma; HOMA estimates vs calculator version; 97 participants | HOMA-IR ranged 0.8-2.0 (normoglycaemia), 1.9-3.2 (prediabetes), 1.5-2.9 (T2D) across assays; ~15% difference by calculator; states C-peptide has no advantage over insulin for HOMA | FT-grep (PMC2518363, 33k chars) |
| PMID 27665422, doi 10.1515/cclm-2016-0439 | Comparison of three routine insulin immunoassays | | TITLE |
| PMID 18076356, doi 10.1515/CCLM.2008.020 | Assay-dependent variability of insulin during OGTT, effect on reference intervals and cut-offs | | TITLE |
| PMID 11701722, doi 10.1210/jcem.86.11.7880 | Repeatability of fasting IR indices against clamp | | ABS |
| PMID 12401750, doi 10.2337/diacare.25.11.2022 | Biological variation of HOMA-IR over 10 occasions in 12 women with T2D and 11 without | | ABS |
| PMID 38987271, doi 10.1515/cclm-2024-0672 (EuBIVAS) | Biological variation of HOMA-IR and QUICKI in 90 non-diabetic adults | | ABS |
| PMID 20704534, doi 10.1515/CCLM.2010.303; PMID 21127151, doi 10.1373/clinchem.2010.152025 | HOMA computational method effects on IR definition | | TITLE |
| PMID 40781799, doi 10.1177/19322968251362848; PMID 36630986, doi 10.1055/a-1998-6889 | C-peptide standardization / comparability | | TITLE |
| PMID 26886418 (IRIS) | Discussion text: insulin is not globally standardized, all HOMA-IR in IRIS was run in central labs, other laboratories would need IRIS assays or calibration to replicate the cutoff | | FT-grep |

### 5b. Original index definitions and cutoff / diagnostic-accuracy studies

| Identifier | Design | Read |
|---|---|---|
| PMID 3899825, doi 10.1007/BF00280883 (HOMA, 1985); PMID 9839117, doi 10.2337/diacare.21.12.2191 (HOMA2 computer program, 1998) | Index definition papers | TITLE |
| PMID 20484475, doi 10.1210/jc.2010-0288 | TyG vs euglycemic-hyperinsulinemic clamp, Mexico; originally 11 non-obese controls plus obese and T2D groups | ABS |
| PMID 19067533, doi 10.1089/met.2008.0034 | TyG as surrogate for IR in apparently healthy subjects | TITLE |
| PMID 14623617, doi 10.7326/0003-4819-139-10-200311180-00007 | TG/HDL-C and other markers to identify insulin-resistant overweight adults (cross-sectional) | ABS |
| PMID 32256572, doi 10.1155/2020/4678526 | Systematic review, diagnostic accuracy of TyG vs clamp or other biochemical IR | ABS (PMC7085845) |
| PMID 40560922, doi 10.1371/journal.pone.0326179 | Systematic review, TyG and TG/HDL accuracy for IR in children/adolescents | ABS |
| PMID 32916555, doi 10.1016/j.dsx.2020.08.017; PMID 26251318, doi 10.1111/pedi.12303; PMID 41948418, doi 10.1007/s13340-026-00883-9 | TyG vs clamp (youth; obese adolescents; Japanese adults, anthropometry-adjusted TyG) | TITLE |
| PMID 16804799, doi 10.1055/s-2006-924233 | Proposed cutoffs for insulin sensitivity indices | TITLE |
| PMID 38715798, doi 10.3389/fendo.2024.1343641 | Surrogate IR indices with Matsuda index as reference in adult men | TITLE |
| PMID 41484350, doi 10.1038/s41366-025-01993-1 | New IR thresholds in metabolic syndrome | TITLE |
| PMID 40917357, doi 10.3389/fendo.2025.1646258 | Global prevalence of IR in adults, systematic review | TITLE |
| PMID 35771773 (EUROASPIRE V) | see Q2 | ABS |
| PMID 42145088 (LAMP) | HOMA-IR cutoff 2.5 "based on prior Asian studies"; CTRI/2026/09/117733 uses 3.8 (men) / 3.46 (women); IRIS uses >3.0; PRISM uses >=2.5; MET-HFpEF uses FIRI >=2.7 (cutoffs differ across the items retrieved) | FT-grep / registry text |

---

## Negative results (searches that returned nothing relevant)

Exact strings are in the log. Highlights:
- IR-guided strategy RCT, PubMed: `"insulin resistance"[ti] AND (guided OR stratified OR "insulin resistance-based") AND randomized[tiab]` returned 23 hits; none was a measurement-guided strategy trial (screened by title).
- Treatment-effect heterogeneity by baseline IR: `("baseline HOMA-IR" OR "baseline insulin resistance") AND ("heterogeneity of treatment effect" OR ...)` returned 1 hit (vitamin K, not relevant). `"by baseline insulin resistance"` returned 14,327 (phrase not honoured); top hits screened.
- Statin / PCSK9 / colchicine / canakinumab / icosapent trials with baseline HOMA-IR or TyG subgroup: `0` hits.
- Emerging Risk Factors Collaboration + insulin: `0` hits.
- `"HOMA-IR" AND ("net reclassification" OR "NRI") AND (cardiovascular OR CHD)`: 3 hits, none an HOMA-IR incremental-value analysis (one eGDR, two TyG/other).
- `"fasting insulin" AND (NRI OR C-index OR discrimination) AND (CHD OR CVD) AND prospective`: 1 irrelevant hit.
- `"HOMA-IR" AND ("reference interval" OR ...)`: 0 hits. Guerrero-Romero author string: 0 hits (the paper was found by title).
- ICTRP: `"triglyceride-glucose" AND guided` and `"insulin resistance" AND "baseline HOMA-IR"`: no records (count text absent).
- CT.gov: no interventional trial found where allocation or treatment decisions are driven by a TyG value. TyG registry hits are observational (CAD, STEMI, nephropathy) or use TyG as an outcome (e.g., IRCT dapagliflozin on TyG).
- Preprints: no medRxiv/bioRxiv item on HOMA-IR/fasting-insulin incremental value or IR-guided randomization.
- Guidelines: no sentence recommending routine fasting insulin / HOMA-IR measurement was found in the segments read, other than the weak EASL-EASD-EASO MASLD recommendation; the PCOS guideline recommends against routine insulin assays.

## What could not be retrieved or was only partly retrieved

- Full text blocked or absent: ADA 1997 consensus (PMID 9540000, no abstract in PubMed; publisher 403), ACE 2003 position statement (PMID 12924350, no abstract, not in PMC), ISPAD 2022 T2D chapter (PMID 36161685; abstract only, publisher 403) and classification chapter (PMID 36537527), NICE NG28 and NG246 (WebFetch 403; web_fetch returned navigation text only), AHA CKM advisory (PMID 37807924), KDIGO 2022 (PMID 36272764), AHA NAFLD statement (PMID 35418240), AACE 2026 algorithm (PMID 41842862), EASL J Hepatol version (PMID 38851997; the Obes Facts and Diabetologia versions were read instead).
- PMC copies that held only metadata/abstract: ADA 2026 S3 and S10 (PMC efetch, ~3k chars), ACC/AHA 2019 (4.8k chars), Endocrine Society paediatric obesity 2017 (6k chars), DIETFITS (10k chars).
- WebFetch windows were partial for ADA 2026 S2/S3/S10, ACC/AHA 2019, ESC 2023 and ESC 2021, so those rows cannot support a claim of absence.
- Primary papers with PMC full text available but not read (abstract only): PLIS (no PMC record seen), Nat Metab semaglutide/dapagliflozin (PMC10822775), DPP heterogeneity (PMC12414453), Hu 2024 (PMC10806829), Gast 2012 (PMC3532497), Liu 2026 (PMC13449919), ATTICA TyG (PMC12803534), GRADE papers (PMC10973903, PMC10973909).
- Numeric results not extracted for several Q2/Q3 rows (marked "not extracted").
- Scholar Sidekick resolve/verify tools were unusable (rate limit, "not subscribed").

## Search gaps

- Coverage of Q2 relies on string searches over PubMed, a 3-result Consensus cap, and Amass semantic search that returned off-target items. Decision-curve and calibration analyses for HOMA-IR/TyG were not systematically screened.
- Only the PubMed index was searched with Boolean strings; Embase, Scopus, Web of Science, and Cochrane were not searched. No Chinese-language database (CNKI) search.
- WHO ICTRP was queried through the public portal basic search (phrase search on the front page). Advanced field searches (condition, intervention, recruitment status) were not run. Counts for "insulin resistance" (2,787 records) were not screened beyond the narrowed strings.
- ClinicalTrials.gov term searches were noisy (full-text term matching); results were screened by title only. Result postings for IRIS-type trials were not reviewed.
- Trial-level covariate analyses in large CV outcome trials (e.g., GLP-1RA, SGLT2i, statin trials) using HOMA-IR or fasting insulin were searched only by a few strings; other indices (eGDR, TyG) appear more often than insulin-based measures.
- bioRxiv/medRxiv MCP tool has no keyword search (date/category only), so preprint coverage came from the Europe PMC preprint index.
- Pediatric-specific guidelines (ISPAD, Endocrine Society paediatric obesity), NICE, WHO and IDF documents were not read.
- Non-English literature not searched.

---

## Search log

### A. Strings run through scripts (PubMed E-utilities esearch, ClinicalTrials.gov API v2, WHO ICTRP portal, Europe PMC preprints, full-text greps)

Each row: serial, date, database, exact string, count reported. Rows for "EuropePMC fulltext" record the grep pattern applied to a retrieved full text and the number of matching sentences. S001 is an early test run of the same helper (repeated at a later row). PubMed esearch was sorted by relevance; the top 3-25 hits were screened by title.

| ID | Date | Database | String | Count |
|---|---|---|---|---|
| S001 | 2026-10-18 | PubMed | `"insulin resistance"[ti] AND (guided OR stratified OR "insulin resistance-based") AND randomized[tiab]` | 23 |
| S002 | 2026-10-18 | PubMed | `"insulin resistance"[ti] AND (guided OR stratified OR "insulin resistance-based") AND randomized[tiab]` | 23 |
| S003 | 2026-10-18 | PubMed | `(HOMA-IR OR "insulin resistance") AND (post hoc OR subgroup OR "effect modification" OR heterogeneity) AND ("baseline HOMA-IR" OR "baseline insulin resistance") AND randomized controlled trial[pt]` | 5 |
| S004 | 2026-10-18 | PubMed | `pioglitazone AND "insulin resistance" AND stroke AND (Kernan OR IRIS)` | 37 |
| S005 | 2026-10-18 | PubMed | `("insulin resistance" OR HOMA-IR) AND ("post hoc" OR secondary analysis) AND (semaglutide OR tirzepatide OR liraglutide) AND randomized[tiab]` | 28 |
| S006 | 2026-10-18 | PubMed | `(HOMA-IR OR "insulin resistance") AND "treatment-by-subgroup" OR ("by baseline insulin resistance")` | 14328 |
| S007 | 2026-10-18 | PubMed | `"by baseline insulin resistance"` | 14327 |
| S008 | 2026-10-18 | PubMed | `("baseline HOMA-IR" OR "baseline insulin resistance") AND ("heterogeneity of treatment effect" OR "differential treatment effect" OR "treatment interaction" OR "effect modifier")` | 1 |
| S009 | 2026-10-18 | PubMed | `("Diabetes Prevention Program") AND (insulin OR HOMA) AND (metformin OR lifestyle) AND baseline AND (subgroup OR predictors)` | 11 |
| S010 | 2026-10-18 | PubMed | `("Look AHEAD" OR "Diabetes Prevention Program Outcomes Study") AND ("insulin resistance" OR HOMA-IR)` | 16 |
| S011 | 2026-10-18 | PubMed | `("polycystic ovary syndrome") AND ("insulin resistance" OR HOMA-IR) AND (metformin) AND ("subgroup" OR "stratified") AND (randomized[tiab])` | 14 |
| S012 | 2026-10-18 | PubMed | `("polycystic ovary syndrome") AND ("insulin resistance" OR hyperinsulinemia) AND (letrozole OR clomiphene OR metformin) AND (ovulation OR "live birth") AND ("baseline insulin" OR "baseline HOMA")` | 1 |
| S013 | 2026-10-18 | PubMed | `("MASLD" OR NAFLD OR NASH OR steatohepatitis) AND (pioglitazone OR resmetirom OR semaglutide OR lanifibranor OR saroglitazar) AND ("insulin resistance" OR HOMA-IR) AND ("subgroup" OR "baseline") AND randomized[tiab]` | 11 |
| S014 | 2026-10-18 | PubMed | `(NAFLD OR NASH OR MASLD) AND pioglitazone AND "insulin resistance" AND histolog* AND randomized[tiab]` | 24 |
| S015 | 2026-10-18 | PubMed | `(prediabetes OR "impaired glucose tolerance") AND ("insulin resistance" OR "insulin secretion") AND (subphenotype OR phenotype OR subtype) AND (randomized OR trial) AND (response OR "treatment effect")` | 20 |
| S016 | 2026-10-18 | PubMed | `("insulin resistant" OR "insulin sensitive") AND (obese OR overweight) AND ("low glycemic" OR "low-carbohydrate" OR "high-carbohydrate") AND randomized[tiab] AND "weight loss"` | 5 |
| S017 | 2026-10-18 | ClinicalTrials.gov API v2 | `AREA[BriefTitle]"insulin resistance" AND (guided OR stratified OR "insulin resistance-based" OR personalized)` | 15 |
| S018 | 2026-10-18 | ClinicalTrials.gov API v2 | `("HOMA-IR" OR "insulin resistance") AND (stratified randomization OR "stratified by" OR stratification) AND AREA[DesignPrimaryPurpose]TREATMENT` | 50 |
| S019 | 2026-10-18 | ClinicalTrials.gov API v2 | `"insulin resistance" AND ("guided therapy" OR "guided treatment" OR "tailored" OR "precision")` | 220 |
| S020 | 2026-10-18 | ClinicalTrials.gov API v2 | `("fasting insulin" OR "HOMA-IR") AND ("point-of-care" OR "screening" OR "risk stratification") AND AREA[StudyType]INTERVENTIONAL` | 242 |
| S021 | 2026-10-18 | ClinicalTrials.gov API v2 | `AREA[Condition]"insulin resistance" AND AREA[StudyType]INTERVENTIONAL AND ("allocation based on" OR "randomized according to" OR "assigned according to" OR "baseline HOMA-IR" OR "HOMA-IR >")` | 191 |
| S022 | 2026-10-18 | ClinicalTrials.gov API v2 | `"TyG" OR "triglyceride-glucose index" OR "triglyceride glucose index"` | 108 |
| S023 | 2026-10-18 | ClinicalTrials.gov API v2 | `("triglyceride-glucose" OR "TyG index") AND AREA[StudyType]INTERVENTIONAL` | 50 |
| S024 | 2026-10-18 | ClinicalTrials.gov API v2 | `("insulin resistance") AND ("clinical decision" OR "decision support" OR "treatment algorithm" OR "algorithm-guided")` | 21 |
| S025 | 2026-10-18 | ClinicalTrials.gov API v2 | `AREA[Condition]"insulin resistance" AND AREA[Condition]"polycystic ovary syndrome" AND AREA[StudyType]INTERVENTIONAL AND ("HOMA-IR" OR "insulin resistant")` | 14 |
| S026 | 2026-10-18 | ClinicalTrials.gov API v2 | `("HOMA-IR" OR "insulin resistance") AND ("responder" OR "predictor of response") AND (GLP-1 OR semaglutide OR tirzepatide OR metformin) AND AREA[StudyType]OBSERVATIONAL` | 1 |
| S027 | 2026-10-18 | PubMed | `("fasting insulin" OR "HOMA-IR" OR "insulin resistance") AND ("incremental value" OR "added value" OR "improvement in discrimination" OR "net reclassification") AND (diabetes OR cardiovascular) AND (predict* OR prognos*)` | 319 |
| S028 | 2026-10-18 | PubMed | `"triglyceride-glucose" AND ("C-statistic" OR "C statistic" OR "area under" OR "net reclassification" OR "integrated discrimination") AND "cardiovascular" AND (incremental OR "added" OR "improve")` | 133 |
| S029 | 2026-10-18 | PubMed | `"triglyceride glucose index" AND "net reclassification"` | 173 |
| S030 | 2026-10-18 | PubMed | `("TyG" OR "triglyceride-glucose") AND ("decision curve" OR "calibration") AND (cardiovascular OR "coronary")` | 110 |
| S031 | 2026-10-18 | PubMed | `"HOMA-IR" AND ("net reclassification" OR "NRI") AND ("cardiovascular" OR "coronary heart disease")` | 3 |
| S032 | 2026-10-18 | PubMed | `"fasting insulin" AND ("net reclassification" OR "C-index" OR "discrimination") AND ("coronary heart disease" OR "cardiovascular disease") AND prospective` | 1 |
| S033 | 2026-10-18 | PubMed | `(insulin[ti] OR "insulin resistance"[ti]) AND "Emerging Risk Factors Collaboration"` | 0 |
| S034 | 2026-10-18 | PubMed | `"fasting insulin" AND "type 2 diabetes" AND ("prediction model" OR "risk score") AND (validation OR "external")` | 10 |
| S035 | 2026-10-18 | PubMed | `("insulin resistance" OR HOMA-IR OR "fasting insulin") AND ("Framingham risk" OR "Pooled Cohort Equations" OR "SCORE2" OR "PREVENT equations") AND (reclassification OR "C statistic" OR "C-statistic" OR "C-index") AND cardiovascular` | 8 |
| S036 | 2026-10-18 | PubMed | `"insulin resistance" AND "incident cardiovascular" AND "meta-analysis"[pt] AND (HOMA-IR OR "fasting insulin")` | 1 |
| S037 | 2026-10-18 | PubMed | `("triglyceride-glucose") AND "meta-analysis"[pt] AND (cardiovascular OR "coronary")` | 43 |
| S038 | 2026-10-18 | PubMed | `("triglyceride-glucose") AND "meta-analysis"[pt] AND (diabetes OR prediabetes) AND (incident OR risk)` | 37 |
| S039 | 2026-10-18 | PubMed | `("triglycerides/HDL" OR "TG/HDL" OR "triglyceride to high-density lipoprotein") AND ("insulin resistance") AND ("sensitivity" AND "specificity") AND (clamp OR HOMA)` | 55 |
| S040 | 2026-10-18 | PubMed | `("insulin resistance" OR HOMA-IR OR "fasting insulin") AND (prediabetes OR "impaired fasting glucose") AND ("progression to diabetes" OR "incident diabetes") AND ("C statistic" OR AUC OR "area under the curve") AND (prospective)` | 2 |
| S041 | 2026-10-18 | PubMed | `"2-hour insulin" OR "OGTT insulin" OR "insulin response" AND "oral glucose tolerance test" AND ("type 2 diabetes" AND predict*) AND (Matsuda OR "insulinogenic")` | 6 |
| S042 | 2026-10-18 | PubMed | `"C-peptide" AND ("insulin resistance" OR "HOMA2-IR") AND ("cardiovascular" OR "mortality" OR "type 2 diabetes") AND (cohort OR prospective) AND (incremental OR reclassification OR "C statistic")` | 5 |
| S043 | 2026-10-18 | PubMed | `"Standards of Care in Diabetes" AND 2026[dp]` | 2127 |
| S044 | 2026-10-18 | PubMed | `"Standards of Care in Diabetes-2025"` | 24 |
| S045 | 2026-10-18 | PubMed | `"Recommendations from the 2023 international evidence-based guideline for the assessment and management of polycystic ovary syndrome"` | 22 |
| S046 | 2026-10-18 | PubMed | `"EASL-EASD-EASO Clinical Practice Guidelines on the management of metabolic dysfunction-associated steatotic liver disease"` | 19 |
| S047 | 2026-10-18 | PubMed | `"AASLD Practice Guidance on the clinical assessment and management of nonalcoholic fatty liver disease"` | 5 |
| S048 | 2026-10-18 | PubMed | `"2021 ESC Guidelines on cardiovascular disease prevention in clinical practice"` | 1 |
| S049 | 2026-10-18 | PubMed | `"2023 ESC Guidelines for the management of cardiovascular disease in patients with diabetes"` | 41 |
| S050 | 2026-10-18 | PubMed | `"2019 ACC/AHA Guideline on the Primary Prevention of Cardiovascular Disease"` | 56 |
| S051 | 2026-10-18 | PubMed | `("insulin resistance") AND (guideline[ti] OR "consensus statement"[ti] OR "position statement"[ti] OR "scientific statement"[ti] OR "practice guideline"[pt])` | 126 |
| S052 | 2026-10-18 | EuropePMC fulltext | `PMID 37580037 grep insulin resist\|HOMA\|fasting insulin\|hyperinsulin` | 7 |
| S053 | 2026-10-18 | EuropePMC fulltext | `PMID 36727674 grep insulin resist\|HOMA\|fasting insulin\|hyperinsulin\|C-peptide` | 45 |
| S054 | 2026-10-18 | EuropePMC fulltext | `PMID 38852583 grep insulin resist\|HOMA\|fasting insulin\|hyperinsulin\|C-peptide` | 28 |
| S055 | 2026-10-18 | EuropePMC fulltext | `PMID 38869512 grep insulin resist\|HOMA\|fasting insulin\|hyperinsulin\|C-peptide` | 3 |
| S056 | 2026-10-18 | EuropePMC fulltext | `PMID 30879355 grep insulin resist\|HOMA\|fasting insulin\|hyperinsulin\|C-peptide` | 0 |
| S057 | 2026-10-18 | PubMed | `"2021 ESC Guidelines on cardiovascular disease prevention in clinical practice" AND Visseren` | 0 |
| S058 | 2026-10-18 | EuropePMC fulltext | `PMID 42242835 grep insulin resist\|HOMA\|fasting insulin\|hyperinsulin\|C-peptide` | 1 |
| S059 | 2026-10-18 | PubMed | `"Prevention or Delay of Diabetes and Associated Comorbidities" AND "Standards of Care in Diabetes-2026"` | 6 |
| S060 | 2026-10-18 | PubMed | `Visseren[au] AND "cardiovascular disease prevention in clinical practice" AND 2021[dp]` | 0 |
| S061 | 2026-10-18 | PubMed | `"American Association of Clinical Endocrinology" AND ("prediabetes" OR "insulin resistance") AND (consensus OR guideline) AND 2020:2026[dp]` | 4 |
| S062 | 2026-10-18 | PubMed | `"Endocrine Society" AND guideline AND ("insulin resistance" OR "prediabetes" OR "polycystic ovary")` | 35 |
| S063 | 2026-10-18 | PubMed | `"cardiovascular-kidney-metabolic" AND "presidential advisory" AND "American Heart Association"` | 24 |
| S064 | 2026-10-18 | PubMed | `"KDIGO" AND "diabetes" AND guideline AND 2022[dp]` | 15 |
| S065 | 2026-10-18 | PubMed | `"NICE" AND ("type 2 diabetes prevention" OR "obesity: identification, assessment and management") AND guideline` | 3 |
| S066 | 2026-10-18 | EuropePMC fulltext | `PMID 41358891 grep insulin resist\|HOMA\|fasting insulin\|hyperinsulin\|C-peptide` | 0 |
| S067 | 2026-10-18 | EuropePMC fulltext | `PMID 35963508 grep insulin resist\|HOMA\|fasting insulin\|hyperinsulin\|C-peptide` | 57 |
| S068 | 2026-10-18 | EuropePMC fulltext | `PMID 24151290 grep insulin resist\|HOMA\|fasting insulin\|hyperinsulin\|C-peptide` | 18 |
| S069 | 2026-10-18 | EuropePMC fulltext | `PMID 41358899 grep insulin resist\|HOMA\|fasting insulin\|hyperinsulin\|C-peptide` | 0 |
| S070 | 2026-10-18 | PubMed | `ESC Guidelines cardiovascular disease prevention clinical practice 2021 European Society of Cardiology Visseren` | 0 |
| S071 | 2026-10-18 | PubMed | `insulin AND (assay OR immunoassay) AND (standardization OR harmonization OR harmonisation) AND (IFCC OR "Working Group" OR "reference measurement")` | 90 |
| S072 | 2026-10-18 | PubMed | `"insulin immunoassays" AND (comparison OR variability OR "between-method") AND (HOMA OR "insulin resistance")` | 4 |
| S073 | 2026-10-18 | PubMed | `Manley[au] AND "insulin" AND "assay" AND "Diabetes Care"[ta]` | 1 |
| S074 | 2026-10-18 | PubMed | `Miller WG[au] AND insulin AND standardization AND 2009:2023[dp]` | 2 |
| S075 | 2026-10-18 | PubMed | `"HOMA-IR" AND (cutoff OR "cut-off" OR threshold) AND (validation OR "receiver operating") AND ("euglycemic" OR "clamp") AND adults` | 14 |
| S076 | 2026-10-18 | PubMed | `"HOMA-IR" AND ("reference interval" OR "reference range" OR "population-based cut") AND (NHANES OR "general population")` | 0 |
| S077 | 2026-10-18 | PubMed | `"triglyceride-glucose index" AND ("euglycemic" OR "clamp") AND (cutoff OR validation OR "diagnostic accuracy" OR sensitivity)` | 8 |
| S078 | 2026-10-18 | PubMed | `"homeostasis model assessment" AND ("Levy" OR "HOMA2" OR "updated") AND computer model` | 14 |
| S079 | 2026-10-18 | PubMed | `(insulin[ti] AND ("pre-analytical" OR "preanalytical" OR hemolysis OR "sample handling" OR "insulin degradation" OR "storage")) AND (assay OR immunoassay)` | 1136 |
| S080 | 2026-10-18 | PubMed | `"fasting insulin" AND "coefficient of variation" AND (biological variation OR "within-subject" OR reproducibility OR "intra-individual")` | 8 |
| S081 | 2026-10-18 | PubMed | `"HOMA-IR" AND ("biological variation" OR "intra-individual variation" OR "day-to-day variability" OR "test-retest")` | 10 |
| S082 | 2026-10-18 | PubMed | `Guerrero-Romero[au] AND "triglyceride" AND "glucose" AND "insulin resistance" AND "hyperinsulinemic-euglycemic clamp"` | 0 |
| S083 | 2026-10-18 | PubMed | `McLaughlin[au] AND "triglyceride" AND "HDL" AND "insulin resistance" AND "Ann Intern Med"[ta]` | 1 |
| S084 | 2026-10-18 | PubMed | `"HOMA-IR" AND "cut-off" AND "systematic review" AND (definition OR "diagnostic threshold" OR "optimal")` | 3 |
| S085 | 2026-10-18 | PubMed | `"insulin resistance" AND (consensus OR "no consensus" OR "lack of standard") AND (definition OR cutoff) AND (HOMA-IR) AND (clinical practice)` | 5 |
| S086 | 2026-10-18 | PubMed | `"insulin sensitivity" AND "euglycemic clamp" AND "surrogate indices" AND "systematic review" AND validation` | 0 |
| S087 | 2026-10-18 | PubMed | `("insulin resistance" OR HOMA-IR) AND (ethnic OR ethnicity OR race) AND (cutoff OR "cut-off" OR threshold) AND (clamp) AND (diabetes OR "cardiometabolic")` | 10 |
| S088 | 2026-10-18 | PubMed | `"Matsuda index" AND validation AND clamp AND "OGTT"` | 7 |
| S089 | 2026-10-18 | PubMed | `"C-peptide" AND "HOMA" AND (standardization OR harmonization OR "assay") AND "insulin" AND "reference"` | 14 |
| S090 | 2026-10-18 | PubMed | `"insulin" AND "mass spectrometry" AND "assay" AND (clinical OR "routine laboratory" OR "reference method") AND 2015:2026[dp]` | 134 |
| S091 | 2026-10-18 | PubMed | `"ADA Workgroup" OR "American Diabetes Association Workgroup" AND insulin AND standardization` | 3 |
| S092 | 2026-10-18 | EuropePMC fulltext | `PMID 29466592 grep INS-30\|insulin secretion\|interaction` | 11 |
| S093 | 2026-10-18 | EuropePMC fulltext | `PMID 26886418 grep HOMA\|insulin resistance (stratum\|subgroup\|quartile)\|interaction\|assay\|fasting insulin` | 16 |
| S094 | 2026-10-18 | PubMed | `GRADE[ti] AND ("insulin sensitivity" OR "insulin resistance" OR HOMA) AND (glycemia OR "glycaemic" OR durability) AND (metformin OR glimepiride OR sitagliptin OR liraglutide OR glargine)` | 6 |
| S095 | 2026-10-18 | PubMed | `(HOMA-IR OR "insulin resistance") AND "baseline" AND (predictor OR determinant) AND ("response to" OR "treatment response") AND (tirzepatide OR semaglutide OR liraglutide OR dulaglutide OR exenatide) AND (randomized OR "post hoc")` | 8 |
| S096 | 2026-10-18 | PubMed | `(metformin) AND "treatment response" AND ("baseline insulin" OR "HOMA-IR" OR "insulin resistance") AND (prediabetes OR obesity OR "type 2 diabetes") AND randomized[tiab]` | 3 |
| S097 | 2026-10-18 | PubMed | `("MASLD" OR "NAFLD" OR "NASH") AND ("insulin resistance" OR HOMA-IR) AND ("effect modification" OR "differential" OR "responders" OR "baseline") AND randomized[tiab] AND (resmetirom OR semaglutide OR lanifibranor OR pioglitazone OR vitamin E OR obeticholic)` | 19 |
| S098 | 2026-10-18 | PubMed | `(PIVENS OR "FLINT" OR "ESSENCE" OR "MAESTRO-NASH" OR "NATIVE") AND ("insulin resistance" OR HOMA-IR)` | 525 |
| S099 | 2026-10-18 | PubMed | `(obesity OR overweight) AND "insulin resistance" AND ("weight loss" OR "bariatric") AND "predict" AND ("response" OR "outcome") AND (HOMA-IR OR "fasting insulin") AND randomized[tiab] AND (semaglutide OR liraglutide OR phentermine OR orlistat OR "lifestyle")` | 1 |
| S100 | 2026-10-18 | PubMed | `"insulin resistance" AND (statin OR "PCSK9" OR "colchicine" OR "canakinumab" OR "icosapent") AND ("cardiovascular outcomes") AND ("baseline" AND (HOMA-IR OR "fasting insulin" OR "TyG")) AND (subgroup OR "post hoc")` | 0 |
| S101 | 2026-10-18 | PubMed | `"triglyceride-glucose" AND ("post hoc" OR subgroup) AND (randomized) AND (treatment OR intensive) AND (SPRINT OR ACCORD OR "Look AHEAD" OR "intensive blood pressure" OR "intensive glycemic")` | 5 |
| S102 | 2026-10-18 | PubMed | `"Insulin Resistance and Risk of Cardiovascular Disease in Postmenopausal Women" AND Schmiegelow` | 2 |
| S103 | 2026-10-18 | PubMed | `"Triglyceride-glucose index improves risk prediction beyond traditional risk factors and hypertension mediated organ damage in healthy adults"` | 1 |
| S104 | 2026-10-18 | PubMed | `"Triglyceride-glucose index predicts adverse cardiovascular events in patients with diabetes and acute coronary syndrome"` | 18 |
| S105 | 2026-10-18 | PubMed | `"New Measure of Insulin Sensitivity Predicts Cardiovascular Disease Better than HOMA Estimated Insulin Resistance"` | 3 |
| S106 | 2026-10-18 | PubMed | `"Head-to-head comparison of fasting-insulin-based versus non-insulin-based insulin resistance surrogates"` | 1 |
| S107 | 2026-10-18 | PubMed | `"The product of triglycerides and glucose, a simple measure of insulin sensitivity"` | 28 |
| S108 | 2026-10-18 | PubMed | `Simental-Mendia[au] AND "triglycerides and glucose"` | 18 |
| S109 | 2026-10-18 | PubMed | `"Measures of Insulin Resistance as a Screening Tool for Dysglycemia in Patients With Coronary Artery Disease"` | 1 |
| S110 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"insulin resistance" AND guided` | 9 records for 9 trials |
| S111 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"insulin resistance" AND stratified` | 5 records for 5 trials |
| S112 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `HOMA-IR AND personalized` | 3 records for 3 trials |
| S113 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"triglyceride-glucose" AND guided` | no count text |
| S114 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"insulin resistance" AND "baseline HOMA-IR"` | no count text |
| S115 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"insulin resistance"` | 2787 records for 2725 trials |
| S116 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"triglyceride glucose"` | 69 records for 69 trials |
| S117 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"TyG index"` | 31 records for 31 trials |
| S118 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `HOMA-IR` | 88 records for 87 trials |
| S119 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"fasting insulin"` | 46 records for 44 trials |
| S120 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"insulin resistance" AND "precision"` | 8 records for 8 trials |
| S121 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"insulin resistance" AND "algorithm"` | 3 records for 3 trials |
| S122 | 2026-10-18 | ClinicalTrials.gov API v2 | `AREA[EligibilityCriteria]"HOMA-IR" AND AREA[StudyType]INTERVENTIONAL AND AREA[Phase]PHASE3` | 17 |
| S123 | 2026-10-18 | ClinicalTrials.gov API v2 | `("insulin resistance" OR HOMA-IR) AND (phenotype OR subtype OR "precision") AND AREA[Condition]prediabetes` | 25 |
| S124 | 2026-10-18 | ClinicalTrials.gov API v2 | `AREA[Condition]PCOS AND AREA[Condition]"insulin resistance" AND AREA[EligibilityCriteria]"HOMA-IR" AND AREA[DesignAllocation]RANDOMIZED` | 5 |
| S125 | 2026-10-18 | ClinicalTrials.gov API v2 | `("MASLD" OR "NAFLD" OR "steatohepatitis") AND AREA[EligibilityCriteria]"HOMA-IR" AND AREA[DesignAllocation]RANDOMIZED` | 29 |
| S126 | 2026-10-18 | ClinicalTrials.gov API v2 | `"pioglitazone" AND "insulin resistance" AND (stroke OR "cardiovascular events") AND AREA[StudyType]INTERVENTIONAL` | 12 |
| S127 | 2026-10-18 | ClinicalTrials.gov API v2 | `("TyG" OR "triglyceride glucose") AND (AREA[StudyType]INTERVENTIONAL) AND ("guided" OR "stratified" OR "primary outcome")` | 6 |
| S128 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"insulin resistance" AND "stratif*"` | 9 records for 9 trials |
| S129 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `HOMA-IR AND "phenotype"` | 2 records for 2 trials |
| S130 | 2026-10-18 | WHO ICTRP portal (trialsearch.who.int basic search) | `"insulin resistance" AND "individualized"` | 9 records for 9 trials |
| S131 | 2026-10-18 | EuropePMC preprints (medRxiv/bioRxiv/ResearchSquare/SSRN/Preprints.org) | `"insulin resistance" AND (reclassification OR "incremental value" OR "C-statistic") AND (HOMA-IR OR TyG OR "triglyceride-glucose")` | 24 |
| S132 | 2026-10-18 | EuropePMC preprints (medRxiv/bioRxiv/ResearchSquare/SSRN/Preprints.org) | `"HOMA-IR" AND (guided OR stratified OR "treatment effect") AND randomized` | 12 |
| S133 | 2026-10-18 | EuropePMC preprints (medRxiv/bioRxiv/ResearchSquare/SSRN/Preprints.org) | `"triglyceride-glucose index" AND (reclassification OR "net reclassification" OR "added value")` | 20 |
| S134 | 2026-10-18 | EuropePMC preprints (medRxiv/bioRxiv/ResearchSquare/SSRN/Preprints.org) | `"insulin" AND "assay" AND (harmonization OR standardization) AND "HOMA"` | 5 |
| S135 | 2026-10-18 | PubMed | `"insulin resistance syndrome" AND ("position statement" OR "consensus" OR "American College of Endocrinology")` | 19 |
| S136 | 2026-10-18 | PubMed | `"Consensus Development Conference on Insulin Resistance" AND "American Diabetes Association"` | 2 |
| S137 | 2026-10-18 | PubMed | `("ISPAD" OR "International Society for Pediatric and Adolescent Diabetes") AND "Clinical Practice Consensus Guidelines" AND "type 2 diabetes" AND 2022[dp]` | 5 |
| S138 | 2026-10-18 | PubMed | `(guideline[ti] OR recommendation*[ti]) AND (prediabetes) AND (diagnosis OR screening) AND ("fasting insulin" OR "HOMA-IR" OR "insulin resistance") AND (not recommended OR "should not")` | 4 |
| S139 | 2026-10-18 | PubMed | `"AACE" AND "obesity" AND "clinical practice guideline" AND 2025:2026[dp]` | 0 |
| S140 | 2026-10-18 | PubMed | `"Lancet Diabetes Endocrinol" AND "clinical obesity" AND "Commission" AND 2025[dp]` | 3 |
| S141 | 2026-10-18 | PubMed | `"2025 ESC" OR "2024 ESC" AND guideline AND ("diabetes" OR "prevention" OR "dyslipidaemia")` | 26 |
| S142 | 2026-10-18 | PubMed | `"American Heart Association" AND "scientific statement" AND "insulin resistance" AND (cardiovascular OR "prediabetes" OR "metabolic")` | 16 |
| S143 | 2026-10-18 | PubMed | `"Endocrine Society" AND "pediatric obesity" AND guideline` | 8 |
| S144 | 2026-10-18 | EuropePMC fulltext | `PMID 39824205 grep HOMA\|fasting insulin\|insulin resistance (is\|should\|testing\|measure\|assess)\|measur\w+ (of )?insulin\|insulin level\|C-peptide\|not recommended\|routine` | 4 |
| S145 | 2026-10-18 | EuropePMC fulltext | `PMID 28359099 grep HOMA\|fasting insulin\|insulin resistance (is\|should\|testing\|measure\|assess)\|measur\w+ (of )?insulin\|insulin level\|C-peptide\|not recommended\|routine` | 0 |
| S146 | 2026-10-18 | EuropePMC fulltext | `PMID 20040676 grep cut.?off\|cutoff\|CV\|reference\|traceab\|harmoni\|IFCC\|recommend` | 10 |
| S147 | 2026-10-18 | EuropePMC fulltext | `PMID 18535197 grep differ\|fold\|range\|CV\|cut.?off\|HOMA-IR (was\|values)` | 36 |
| S148 | 2026-10-18 | PubMed | `"Homeostasis model assessment: insulin resistance and beta-cell function from fasting plasma glucose and insulin concentrations in man"` | 15 |
| S149 | 2026-10-18 | PubMed | `"Correct use of the homeostasis model assessment" OR "Levy JC" AND "HOMA2" AND "Diabetes Care"[ta] AND 1998[dp]` | 0 |
| S150 | 2026-10-18 | PubMed | `(HOMA-IR OR "insulin resistance") AND (percentile OR "reference population") AND (cutoff OR "cut-off") AND (NHANES OR "national survey" OR "population-based") AND (adults) AND (ethnic OR race)` | 2 |
| S151 | 2026-10-18 | PubMed | `"HOMA-IR" AND ("cut-off" OR cutoff) AND ("nonalcoholic fatty liver" OR NAFLD OR MASLD) AND (optimal OR ROC) AND adults` | 26 |
| S152 | 2026-10-18 | PubMed | `"HOMA-IR" AND ("polycystic ovary syndrome") AND (cutoff OR "cut-off" OR threshold) AND (clamp OR "diagnostic")` | 34 |
| S153 | 2026-10-18 | PubMed | `"insulin resistance" AND "prevalence" AND "HOMA-IR" AND ("different cut-offs" OR "varying definitions" OR "depending on the cut")` | 10 |
| S154 | 2026-10-18 | PubMed | `"TyG" AND ("optimal cut-off" OR "optimal cutoff") AND ("insulin resistance") AND ("HOMA-IR" OR clamp) AND adults AND systematic` | 1 |
| S155 | 2026-10-18 | PubMed | `"Call for Standardization of C-Peptide Measurement"` | 2 |
| S156 | 2026-10-18 | PubMed | `Levy[au] AND Matthews[au] AND Hermans[au] AND "homeostasis model assessment" AND 1998[dp]` | 1 |
| S157 | 2026-10-18 | PubMed | `"Correct use of the homeostasis model assessment"` | 694 |
| S158 | 2026-10-18 | PubMed | `"Insulin resistance" AND "Look AHEAD" AND (HOMA OR insulin) AND (weight loss) AND (cardiovascular OR "diabetes remission") AND predictors AND baseline` | 0 |
| S159 | 2026-10-18 | EuropePMC fulltext | `PMID 42145088 grep HOMA\|interaction\|participants\|randomi` | 51 |

### B. Strings run directly through MCP tools (not captured in the table above)

| ID | Date | Tool / database | String | Count / result |
|---|---|---|---|---|
| M01 | 2026-10-18 | PubMed MCP search_articles | `(insulin resistance[Title/Abstract]) AND (HOMA-IR OR "fasting insulin") AND (stratified OR guided OR "tailored") AND randomized controlled trial[Publication Type]` | 44 (20 PMIDs returned) |
| M02 | 2026-10-18 | PubMed MCP | `"insulin resistance" AND ("insulin-resistance guided" OR "guided by insulin resistance" OR "stratified by insulin resistance" OR "HOMA-IR guided")` | 3,320 (phrases not honoured; top 20 PMIDs not screened individually) |
| M03 | 2026-10-18 | PubMed MCP | `(insulin sensitivity OR insulin resistance) AND diet[Title] AND (low-carbohydrate OR low-fat) AND (baseline insulin secretion OR insulin resistance) AND "treatment interaction"` | 1 (irrelevant) |
| M04 | 2026-10-18 | PubMed MCP | `(HOMA-IR OR "fasting insulin" OR "triglyceride-glucose index") AND ("net reclassification" OR "C-statistic" OR "C statistic" OR "incremental value") AND (cardiovascular OR diabetes)` | 188 (25 returned) |
| M05 | 2026-10-18 | PubMed MCP | `(HOMA-IR OR "fasting insulin") AND ("net reclassification improvement" OR "integrated discrimination improvement") AND "type 2 diabetes" prediction` | 7 (PMIDs 38191206 and 37906402 relevant; the rest were genetic-score or biomarker papers) |
| M06 | 2026-10-18 | PubMed MCP | `"triglyceride-glucose index" AND (reclassification OR discrimination OR "decision curve") AND (cardiovascular OR diabetes)` | 373 (25 returned, not individually screened) |
| M07 | 2026-10-18 | PubMed MCP | `Pioglitazone after ischemic stroke or transient ischemic attack insulin resistance IRIS trial` | 79 |
| M08 | 2026-10-18 | PubMed MCP | `DIETFITS healthy low-fat vs low-carbohydrate diet insulin secretion genotype pattern weight loss randomized` | 1 |
| M09 | 2026-10-18 | PubMed MCP | `(insulin resistance[tiab] OR "insulin sensitivity"[tiab] OR "insulin secretion"[tiab]) AND ("low-fat" OR "low-carbohydrate" OR "low glycemic") AND (weight loss) AND (interaction OR "effect modification" OR "predict") AND Randomized Controlled Trial[pt]` | 22 |
| M10 | 2026-10-18 | PubMed MCP | `Diabetes Prevention Program metformin lifestyle baseline fasting insulin HOMA-IR treatment effect heterogeneity` | 0 |
| M11 | 2026-10-18 | PubMed MCP | `(polycystic ovary syndrome) AND metformin AND (baseline insulin resistance OR HOMA-IR) AND (response OR predictor) AND (randomized OR trial)` | 30 |
| M12 | 2026-10-18 | PubMed MCP | `Dennis "Disease progression and treatment response in data-driven subgroups of type 2 diabetes" ADOPT RECORD` | 1 |
| M13 | 2026-10-18 | PubMed MCP get_article_metadata | PMIDs 38191206, 37906402, 30518023, 30204299, 27298332, 27007680, 24057154, 25180479 | 8 records; only 38191206 and 37906402 relevant |
| M14 | 2026-10-18 | Amass BiomedCore | `randomized trial insulin resistance-guided or insulin resistance-stratified treatment allocation HOMA-IR` (type: RCT, limit 10) | 10 returned; none a guided-care trial |
| M15 | 2026-10-18 | Amass BiomedCore | `treatment effect heterogeneity by baseline insulin resistance HOMA-IR randomized trial interaction` (from 2015, limit 6) | 6 returned; none relevant |
| M16 | 2026-10-18 | Amass TrialCore | `insulin resistance guided treatment randomized HOMA-IR stratified allocation` (interventional, limit 15) | 15 returned (CT.gov, IRCT, PACTR, ISRCTN); none an IR-guided strategy trial |
| M17 | 2026-10-18 | Amass TrialCore | `triglyceride-glucose index TyG guided` (limit 15) | 15 returned (CT.gov, ChiCTR, TCTR, IRCT); observational or outcome-use only |
| M18 | 2026-10-18 | global_trial_search | `insulin resistance HOMA-IR stratified guided treatment allocation` (Drug, size 8) | 1 (semaglutide in schizophrenia with MetS; not relevant) |
| M19 | 2026-10-18 | Consensus (free tier, 3 results max) | `randomized trial of insulin resistance-guided treatment versus standard care HOMA-IR stratified` | 3; none relevant |
| M20 | 2026-10-18 | Consensus (medical_mode) | `does adding HOMA-IR or fasting insulin improve cardiovascular risk prediction net reclassification` | 3; WHI 2015, NHANES 2026 mortality, ISI-cal 2013 |
| M21 | 2026-10-18 | Consensus | `triglyceride-glucose index incremental predictive value beyond traditional risk factors C-statistic reclassification` | 3; Liu 2026, Blicher 2024, Wang 2020 |
| M22 | 2026-10-18 | Scholar Sidekick resolveIdentifier (x3) | PMID batches | Error: too many requests / not subscribed |
| M23 | 2026-10-18 | WebFetch | diabetesjournals.org ADA S2; ahajournals AHA 2019; jacc.org; doi.org/10.2337/dc26-S002; NICE NG28; NICE NG246; Wiley ISPAD; diabetesjournals ADA 1997 | HTTP 403 |
| M24 | 2026-10-18 | WebFetch | PMC12690183 (ADA S2), PMC12690170 (ADA S3), PMC12690187 (ADA S10), PMC7734661 (ACC/AHA 2019), academic.oup.com ESC 2023 (4 windows), academic.oup.com ESC 2021 (3 windows) | partial windows, see Q4 |
| M25 | 2026-10-18 | web_fetch (parallel) | NICE NG28; ADA 1997 consensus | NICE: navigation text only; ADA: network error |
| M26 | 2026-10-18 | ICTRP trial pages (Trial2.aspx) | CTRI/2026/09/117733, ChiCTR2400085828, ISRCTN74144960, IRCT20170812035642N11, NCT07618663 | Pages read |
| M27 | 2026-10-18 | CT.gov API v2 get | NCT07710274, NCT06856291 | Records read |
| M28 | 2026-10-18 | PubMed E-utilities efetch (abstracts) | PMID batches for items listed in sections Q1-Q5 | Abstracts read |
| M29 | 2026-10-18 | Not run | bioRxiv MCP search_preprints/search_published_preprints: schema supports date/category only, no keywords | Not used for keyword search |
