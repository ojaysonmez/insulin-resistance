# Steelman: the strongest honest case that measuring insulin resistance (IR) is clinically useful

Role: ir-steelman. Run date 2026-10-18. Coverage and reimbursement out of scope. `merged-conclusion.md` not edited.
Scope of my work: I read merged-conclusion.md, both evidence-searcher reports (Set A lines 1-292 of 533, Set B lines 1-290 of 413: the evidence tables and Set B's full search log), ir-skeptic-merged.md in full, and grepped the endocrinologist and comparison files. I did not read the other analyst or skeptic files end to end.
Identifier check: every PMID/DOI I introduce was returned by an NCBI E-utilities (PubMed) efetch record in this session, title matched. Registry IDs came from the ClinicalTrials.gov API v2. I did not verify the team's own citations.
Read levels: **ABS** = PubMed abstract only. **FT-grep** = Europe PMC full text, searched by regex. **Title** = title only. **[recall]** = from memory, not retrieved.
Tools: PubMed E-utilities (relevance sort; I screened the top 5-10 titles per string, except one 126-record string that I screened completely), ClinicalTrials.gov API v2, Europe PMC. Not used: Embase, Cochrane CENTRAL, ICTRP, Consensus, Amass. Several guideline PDFs I tried could not be retrieved (see §6).

---

## 1. The strongest case for utility

**Bottom line: the conclusion "no established utility for *routine* measurement" survives. The softer claim "shown not to add value" is weaker than the file says, and several specific uses have more support than the team recorded.**

1. **IR is a causal, actionable biology, and one drug class works in IR-selected patients.** IRIS (selection on HOMA-IR above 3.0) cut stroke/MI by 2.8 points absolute. ADA 2026 Rec 3.13 and AACE 2022 already write IR into treatment wording. Mendelian randomization points the same way: genetically predicted IR phenotypes (instruments are fasting insulin, HDL-C and triglycerides, so it is a mixed construct) carry OR 1.79 for CAD and 1.80 for small-artery stroke (PMID 32398352, ABS). The weakness is the one the team named: no non-IR comparator, so the trial supports the drug and not the test.
2. **Baseline insulin or HOMA-IR modifies treatment effect in randomized oncology trials, with hard outcomes.** The team looked only at metabolic, cardiovascular and weight-loss trials. In the 200-woman presurgical metformin trial, Ki-67 fell with metformin only in women with HOMA above 2.8 (interaction P = 0.045; PMID 22564993, ABS; DOI 10.1200/JCO.2011.39.3769). In the 3,649-woman adjuvant trial MA.32, metformin did nothing overall (PMID 35608580), but an exploratory analysis with baseline fasting insulin and HOMA found statistically significant interactions with distant recurrence-free survival in luminal cancer, with *potential harm at low* insulin/HOMA (PMID 42063220, ABS; NCT01101438). That is a large RCT in which a baseline insulin assay changed the sign of a hard-outcome effect. The authors concluded these variables "did not identify subgroups" who benefit, so I treat this as hypothesis-generating. It still falsifies "no baseline-IR interaction on hard outcomes anywhere".
3. **Where a decision sits far from the cutoff, the chemist's variability argument loses most of its force.** The merged file's own arithmetic (a value 1.5x the cutoff misreads about 6% of the time, 2x under 1%) means severe hyperinsulinaemia is reliably detectable. Uses that sit there: severe and syndromic IR (JDS 2022 criteria: fasting insulin 30 µU/mL, PMID 35463863), lipodystrophy work-up, and IRIS-type entry (the HOMA-IR above 3.0 group is the top quartile in people without diabetes). The conclusion that measurement is poor near a cutoff does not generalise to extreme values.
4. **Prediction beyond a risk score has at least one positive, externally validated result, and the team mischaracterised it.** ATTICA (PMID 41178693, ABS) reports TyG at or above 8.46 added to SCORE2: NRI 0.668 / 0.469 and delta Harrell's C 0.054 / 0.044 in derivation and external validation cohorts (p<0.05 for all). The merged file filed this under "small or no gain". Another cohort (PMID 39117485, ABS, n=1,970, 15-year MACE) gave delta C 0.005 (P = 0.042) for TyG over SCORE risk factors. Those are conflicting results with a wide spread (0.0004 pooled to 0.054), not a consistent null. TyG is not an insulin assay, and both are abstract-level.
5. **Decision-curve analyses exist** (see §3), and IR-related indices appear in surgical and other selection scores (C-peptide in the Diabetes Surgery Score: PMID 22963817; scores' AUC 0.79-0.88 for 2-year remission, PMID 32873586).
6. **Regulators of the *definition* already use it.** The MAFLD consensus (PMID 32278004) lets HOMA-IR of 2.5 or more count as a metabolic risk abnormality in lean adults with steatosis (criterion confirmed second-hand in full texts PMC8280082 and PMC11925433; the primary paper is not open access). Korean guideline authors criticise it for being "not frequently used in clinical practice" (PMC11925433), so it is a definitional use, not a management one. The EASL 2024 recommendation (already in the file) also exists.
7. **Direct randomized evidence that an IR-defined phenotype can be matched to treatment**, though small and short: PERSON (PMID 36599304, ABS; n=242; muscle-IR vs liver-IR phenotype-matched diet): the primary outcome (disposition index) was *null*, but insulin sensitivity, glucose homeostasis, triglycerides and CRP improved more in the matched arm. The merged file had "no result" for it.
8. **A randomized crossover shows an IR-based subgroup with differential drug response.** In TriMaster (n=309 with all three drugs), a cluster built from routine features plus HOMA showed the severe insulin-resistant diabetes cluster responded differently to SGLT2i vs TZD (P = 0.005, one cluster-drug pair; PMID 42312889, ABS). The same paper found a routine-features model beat the clusters (0.27% vs 0.16% HbA1c), which supports the team's "IR is not needed" reading for glycaemic choice.

Honest weight: items 1, 2 and 7 are the best. None is a test-and-treat trial, and none shows a better outcome from measuring.

---

## 2. What the team missed (table)

| # | Item | Source (read level) | Design / size / result | What weakens it | What it would change |
|---|---|---|---|---|---|
| 1 | Metformin x baseline HOMA, breast cancer, presurgical RCT | PMID 22564993; PMID 25253174 (ABS) | n=200; Ki-67 down only in HOMA > 2.8; P(int) 0.045, 0.07 in follow-up | Surrogate endpoint (Ki-67); overall null; small | Opens oncology as a setting; shows a HOMA threshold used as an effect modifier in an RCT |
| 2 | Metformin x baseline insulin/HOMA/leptin, MA.32 | PMID 42063220 (ABS); NCT01101438; main trial PMID 35608580 | n=3,649; interaction on distant recurrence-free survival in luminal cancer, possible harm at low values | Exploratory, subtype-split, multiplicity unclear; authors say not usable to select | Overturns "no baseline-IR interaction with hard outcomes in a large RCT" (§3, claim 4) |
| 3 | TyG over SCORE2: delta C 0.054 / 0.044, NRI 0.67 / 0.47 | PMID 41178693 (ABS) | n=1,677 + 1,237, composite CV events | Abstract only; cut-off derived in cohort 1; TyG is not an insulin assay | Merged file lists it as "small or no gain"; it is the largest reported gain over a current European score |
| 4 | Other TyG-over-SCORE: delta C 0.005 (P 0.042) | PMID 39117485 (ABS) | n=1,970, 15 y | Small gain | Shows spread across studies |
| 5 | Decision-curve analyses exist for IR indices | Search 145 records, e.g. PMIDs 40241176, 40223076 (eGDR), 36093151 (TyG, team table) (titles + team abstracts) | Mostly Chinese/NHANES cohort models | I read none of the 145 in detail; DCA of a *model* is not net benefit of *measuring* | Weakens "no decision-curve analysis" (§3) |
| 6 | MAFLD definition uses HOMA-IR 2.5 | PMID 32278004; criterion via PMC8280082 and PMC11925433 (FT-grep, secondary) | International consensus, lean adults need 2 of several abnormalities | Definitional; criticised as impractical | Counter-example to "no guideline/consensus uses an IR value" |
| 7 | Pediatric IR consensus update | PMID 36465645 (ABS) | Review updating 2010 consensus; says early detection of IR is "fundamental"; says standardisation still unresolved | Narrative review, abstract has no testing recommendation | Sits against Endocrine Society 2017 |
| 8 | TRIO-BD: metformin in bipolar depression selected for IR | PMID 35120288 (ABS); NCT02519543 | n=45; 11 "converters" (10 on metformin); converters improved on MADRS | Analysis compares post-randomisation converters with non-converters; tiny; psychiatric setting | New setting (psychiatry) with IR-defined entry and IR reversal as the mediator |
| 9 | Pioglitazone x IR in depression | PMID 26602230 (ABS) | n=37, randomized across insulin-sensitivity range; improvement tied to glucose-metabolism improvement only in IR | Tiny, short | Same |
| 10 | C-peptide in surgical remission scores | PMIDs 22963817, 32873586 (ABS) | Validated n=176; SOS comparison n=363: AUC 0.79-0.88 at 2 y, falling to 0.70-0.76 at 10 y, no better than diabetes duration alone | Secretion marker, not IR; duration alone predicts as well | A routine setting (bariatric surgery selection) where a C-peptide result is an input |
| 11 | eGDR in type 1 diabetes: HR 0.79 per unit for MACE; 16 studies, 29,075 | PMID 40841970 (ABS) | Meta-analysis of observational studies | eGDR uses waist, BP, HbA1c, not insulin | IR measured without an insulin assay in a population the team did not cover |
| 12 | Longitudinal HOMA-IR change tracks fibrosis change in non-diabetic NAFLD | PMID 34674510 (ABS) | n=15,728; OR 2.25 (NFS) for HOMA-IR rise over 1; effect absent in women and BMI < 25 | Ultrasound/NFS/APRI surrogates, 86% men, one centre | MASLD without T2D: supports monitoring value, not tested |
| 13 | PERSON primary result (null), secondary favouring matched diet | PMID 36599304 (ABS) | See §1 item 7 | Primary null; 12 weeks; surrogate outcomes | Fills the team's "no result" cell |
| 14 | TODAY: insulin sensitivity did not differ across racial/ethnic groups | PMID 27803118 (ABS) | Youth T2D | Supports team (adiponectin, not IR, explained failure) | Survives: no help here |
| 15 | MR: IR causal for CAD and small-vessel stroke | PMID 32398352 (ABS); also 34797599 (title) | Two-sample MR, 53 SNPs, mixed insulin/lipid instruments | MR on a composite; causal role does not imply measurement utility | Strengthens plausibility for treating IR |
| 16 | STAR model-based insulin sensitivity for ICU/neonatal glucose control | PMIDs 24739335, 29930148, 32607009 (titles) | Clinical protocols; observational | A different construct (computed from response to insulin), no RCT found | A real setting where an IR-type measure steers dosing |
| 17 | Quantose IR test (insulin + non-glycaemic biomarkers) | PMID 23439165 (title only) | Commercial fasting test | Not read | Lead only |
| 18 | LIRA-ADD2SGLT2i, TriMaster and PCOS predictor studies point away from IR | PMIDs 34132018, 36477733, 34983571 (ABS) | Clinical features (BMI, eGFR, androgens) beat IR | – | Supports the team |

---

## 3. Claims of absence my searches overturned or weakened

1. **"No decision-curve analysis" (merged lines 9 and 74).** Weakened, partly overturned. `"insulin resistance" AND "decision curve"` returns 145 PubMed records; `HOMA-IR AND "decision curve analysis" AND (predict* OR prognos*)` returns 27; `"triglyceride-glucose" AND "decision curve" AND (net benefit)` returns 71. The searcher's own table already lists Pang 2022 (PMID 36093151, decision-curve reported). Caveat: I screened titles only. They are almost all prediction-model papers from Chinese cohorts and NHANES, and I do not know whether any compares against a standard risk score. "No DCA of the *decision to measure*" survives; "no DCA at all" does not.
2. **"No delta-C over current score showing a clear gain."** Weakened. ATTICA gives delta C 0.054 / 0.044 over SCORE2 with an external cohort (PMID 41178693), and the merged file's own searcher table has it. The merged file calls it "small or no gain". Evidence on this question is conflicting, not null.
3. **"IR-stratified therapy evidence ... no run closed" and "no prespecified interaction test beyond DIETFITS" (gaps 3).** Weakened. A 200-patient presurgical RCT reports a HOMA-threshold interaction (P 0.045) and a 3,649-patient RCT reports baseline insulin/HOMA interactions on recurrence-free survival (§2 rows 1-2). Neither is confirmatory.
4. **"No baseline-IR interaction analysis in large trials with hard outcomes."** Overturned for MA.32 (cancer, not CV). The CV claim survives (§4).
5. **PERSON "no result reported".** Filled: primary null, secondary improvements (PMID 36599304).
6. **"The only verified IR-threshold niche is IRIS" and "no guideline/consensus uses an IR value".** Already weakened by JDS; now also MAFLD (HOMA-IR 2.5, definitional).
7. **"Searches that would find a decision-curve/reclassification study were incomplete"**: confirmed; one of the unscreened result sets (S030, 110 records for TyG decision curve) contains DCA papers, but its top hits are not IR-over-standard-score comparisons.
8. **Guideline negatives that rest on windows or regex.** Not overturned, but I could not close them either (§6).

Where the team's *evidence* is weaker than recorded: the team lists ATTICA beside Liu 2026 as showing small or no gain; ATTICA shows the opposite. That is the only error of fact I found in the merged text.

---

## 4. Claims of absence that survived (with my strings)

Counts are PubMed totals; I screened the top 5-10 titles.

| Claim | Strings I ran | Result |
|---|---|---|
| No RCT of IR-guided care vs usual care | `"Insulin Resistance"[Mesh] AND "Randomized Controlled Trial"[pt] AND (stratified OR selected OR guided)` 305 (top 5 screened, not strategy trials); `"Insulin Resistance"[Mesh] AND RCT[pt] AND (interaction[tiab] OR "effect modification"[tiab] OR "effect modifier"[tiab] OR "treatment heterogeneity"[tiab])` 286 (top 8: DIETFITS, FINEARTS-HF eGDR, SIRD/SIDD, plus unrelated) | Survives. These two strings are the MeSH search the skeptic said nobody ran; I did not screen past the top 8. |
| No STAR-type or closed-loop RCT of IR measurement | several strings, 0-1 hits (see log) | My STAR strings were poor; the strategy absence is not tested. |
| IR measurement does not reliably beat clinical features for glycaemic drug choice | TriMaster searches (3 hits) | Survives (routine-features model outperformed clusters). |
| PCOS: IR does not predict metformin response better than clinical features | `PCOS[Mesh] AND metformin[tiab] AND (HOMA OR "insulin resistance") AND predict* AND response` 12 | Survives (top hits: hyperandrogenism, LH/HDL). |
| Pregnancy: early-pregnancy IR measure predicting GDM | `hyperinsulin*[ti] AND "gestational diabetes"[ti] AND (first trimester OR early pregnancy) AND predict*` 0; broader 352 (screened 8, mostly environmental) | **Not tested**; only NCT03388697 and PMID 23439165 (Quantose, title-level) are leads. |
| Dementia: IR-selected trial | `(Alzheimer* OR MCI) AND "insulin resistance" AND randomized AND (metformin OR pioglitazone OR liraglutide OR intranasal) AND (subgroup OR stratif*)` 2 | Not found; weak search. |
| HFpEF: IR-selected RCT | `"heart failure with preserved" AND (metformin OR ...) AND "insulin resistance" AND randomized` 2 | Not found (MET-DIME design paper only, PMID 24515256, title). |
| IRIS shows a HOMA-IR dose-response | `pioglitazone AND stroke AND (HOMA OR "insulin resistance") AND (post hoc OR secondary OR subgroup)` 27 | Not found; the secondary analyses retrieved are about glycaemia (30734043) and dose (35253334, treatment-dose strata, not HOMA strata). |
| DPP/Look AHEAD treatment x baseline insulin sensitivity, hard outcome | two strings, 9 and 10 | Only the DPP k-means paper (already in file). |

---

## 5. The single study that would most change the conclusion

**A pragmatic randomized test-and-treat trial in one narrow, adequately sized population, with a pre-registered treatment-by-baseline-insulin interaction on a hard outcome.** The best-powered version: patients with recent ischaemic stroke/TIA without diabetes, randomized to pioglitazone vs placebo with *all* HOMA-IR strata enrolled (IRIS excluded those under 3.0), central insulin assay traceable to an isotope-dilution reference, prespecified interaction on stroke/MI, and a second randomization of a "measure and treat if HOMA-IR over 3.0" arm against "treat by glycaemic category" (Spence 2019 suggests prediabetes may do the selecting). Reason: IRIS is the only existing IR-selected hard-outcome RCT, its benefit is documented, the guideline wording already depends on IR, and the missing piece is exactly whether the IR value or the glycaemic category identifies responders. A positive interaction would convert "IR as a label" into "IR as a test"; a null would settle the "shown not to add value" question for the one setting where it matters. If a second study is allowed, the MA.32 insulin/HOMA interaction would need confirmation in a trial that prespecifies it.

---

## 6. Limits and what I could not do

- Everything I introduce is abstract-level except the two MAFLD full-text greps. I did not read any new paper in full.
- I could not retrieve ADA/EASD 2026 T2D consensus (PMIDs 42825450, 42825923: no PMC copy; Springer redirected to a cookie handshake), AACE 2026 algorithm (41842862) or AHA 2023 CKM advisory (37807924). These stay unread.
- The Endocrine Society 2017 Rec 1.7 claim stays single-source; I did not try to confirm it.
- Several of my strings were weak because PubMed's automatic term mapping broadened them (the "MA.32 HOMA OR insulin OR C-peptide" string returned 526,026 records and is unusable; the PCOS metformin-predictor string without field tags returned 44,274). Those two returned nothing I used; I re-ran tagged versions.
- I did not search ICTRP, CTIS, Embase, CENTRAL or Chinese databases, and I did not screen the 145 decision-curve records beyond title.
- Selection effect: I looked for support for utility. The items in §2 rows 14 and 18 are what I found going the other way, and I did not try to find more.

---

## Appendix: search log (2026-10-18; PubMed E-utilities, relevance-sorted unless stated)

| ID | String | Count |
|---|---|---|
| P1 | `"insulin resistance"[majr] AND randomized controlled trial[pt] AND (stratified OR selected OR guided)` | 305 |
| P2 | `"insulin resistance" AND "decision curve"` | 145 |
| P3 | `HOMA-IR AND "decision curve analysis" AND (predict* OR prognos*)` | 27 |
| P4 | `"triglyceride-glucose" AND "decision curve" AND (net benefit)` | 71 |
| P5 | `STAR glycaemic control insulin sensitivity model-based randomised` | 0 |
| P6 | `MAFLD HOMA-IR 2.5 international expert consensus diagnosis` | 1 |
| P7 | `metabolic associated fatty liver disease new definition Eslam international expert consensus` | 5 |
| P8 | `"insulin resistance" AND "model-based" AND "glycaemic control" AND (critically ill OR ICU) AND randomi*` | 0 |
| P9 | `closed-loop insulin delivery insulin sensitivity adaptation randomized type 1 diabetes` | 1 |
| P10 | `C-peptide AND (predict* OR guide*) AND (response OR remission) AND (sulfonylurea OR GLP-1 OR bariatric)` | 138 |
| P11 | `TriMaster pioglitazone sitagliptin canagliflozin` | 3 |
| P12 | `Stewart STAR stochastic targeted glycemic control insulin sensitivity` | 0 |
| P13 | `metformin AND breast cancer AND (insulin OR HOMA OR C-peptide) AND (baseline) AND (interaction OR subgroup) AND randomized` | 9 |
| P14 | `pioglitazone IRIS HOMA-IR tertile OR quartile baseline insulin resistance treatment effect` | 65 (off target) |
| P15 | `MA.32 metformin invasive disease-free survival breast cancer randomized` | 4 |
| P16 | `metformin cancer randomized "insulin resistance" selected OR stratified HOMA` | 807 (off target) |
| P17 | `Goodwin MA.32 HOMA OR insulin OR C-peptide metformin effect by baseline` | 526,026 (unusable) |
| P18 | `fasting insulin OR C-peptide breast cancer recurrence prognosis cohort` | 65,020 (unusable) |
| P19 | `pioglitazone NASH randomized trial insulin resistance baseline response predictor` | 0 |
| P20 | `HOMA-IR predicts fibrosis progression NAFLD paired biopsy` | 0 |
| P21 | `Adipo-IR pioglitazone OR vitamin E histologic response NASH` | 22 |
| P22 | `polycystic ovary syndrome metformin response predictor baseline HOMA-IR OR insulin randomized` | 44,274 (unusable) |
| P23 | `early pregnancy HOMA-IR OR fasting insulin predict gestational diabetes prospective` | 352 |
| P24 | `Quantose IR prediabetes type 2 diabetes prediction` | 1 |
| P25 | `"Insulin Resistance"[Mesh] AND RCT[pt] AND (interaction[tiab] OR "effect modification"[tiab] OR "effect modifier"[tiab] OR "treatment heterogeneity"[tiab])` | 286 |
| P26 | `("HOMA-IR"[tiab] OR "insulin resistance"[ti]) AND fibrosis[tiab] AND progression[tiab] AND (NAFLD OR MASLD) AND (longitudinal OR "paired biopsy" OR "serial biops*" OR cohort)` | 12 |
| P27 | `PCOS[Mesh] AND metformin[tiab] AND (HOMA OR "insulin resistance") AND predict* AND response` | 12 |
| P28 | `hyperinsulin*[ti] AND "gestational diabetes"[ti] AND (first trimester OR early pregnancy) AND predict*` | 0 |
| P29 | `("insulin resistance") AND (guideline[ti] OR "consensus statement"[ti] OR "position statement"[ti] OR "scientific statement"[ti] OR "practice guideline"[pt])` (all 126 titles screened) | 126 |
| P30 | `TRIO-BD metformin treatment-resistant bipolar depression insulin resistance` | 1 |
| P31 | `(depression OR bipolar OR schizophrenia)[ti] AND ("insulin resistance" OR HOMA) AND randomized AND (metformin OR pioglitazone OR liraglutide OR semaglutide) AND (inclusion OR eligib* OR "with insulin resistance")` | 4 |
| P32 | `"fasting insulin"[tiab] AND "Mendelian randomization" AND (coronary OR cardiovascular)` | 57 |
| P33 | `"insulin resistance"[tiab] AND "Mendelian randomization" AND (Alzheimer* OR dementia OR stroke)` | 23 |
| P34 | `CORDIOPREV insulin resistance OR TyG OR HOMA Mediterranean diet low-fat cardiovascular recurrence` | 26,068 (off target) |
| P35 | `"Diabetes Prevention Program" AND metformin AND (insulin sensitivity OR resistance OR HOMA) AND baseline AND (interaction OR heterogeneity OR "treatment effect")` | 9 |
| P36 | `"Look AHEAD" AND (insulin OR HOMA) AND baseline` | 10 |
| P37 | `TyG AND (SCORE2 OR "Pooled Cohort" OR PREVENT OR QRISK* OR Framingham) AND (C-statistic OR C-index OR reclassification OR "area under")` | 39 |
| P38 | `pioglitazone AND (stroke OR IRIS) AND (HOMA OR "insulin resistance") AND (post hoc OR secondary OR subgroup)` | 27 |
| P39 | `("stochastic targeted" OR STAR[ti]) AND glycemic AND (intensive care OR critically ill) AND "insulin sensitivity"` | 9 |
| P40 | `"insulin sensitivity" AND T1D AND outcome* AND (eGDR) AND (complication* OR cardiovascular)` | 8 |
| P41 | `(semaglutide OR tirzepatide) AND (HOMA-IR OR "insulin resistance") AND baseline AND "weight loss" AND (predict* OR modif* OR subgroup) AND obesity` | 3 |
| P42 | `bariatric AND (fasting insulin OR HOMA-IR OR C-peptide) AND remission AND predict* AND (prediction model OR score)` | 13 |
| P43 | `TODAY study AND (insulin sensitivity OR C-peptide OR HOMA) AND (failure OR predict* OR rosiglitazone)` | 36 |
| P44 | `"heart failure with preserved" AND (metformin OR pioglitazone OR empagliflozin) AND "insulin resistance" AND randomized` | 2 |
| P45 | `(Alzheimer* OR MCI) AND "insulin resistance" AND randomized AND (metformin OR pioglitazone OR liraglutide OR intranasal) AND (subgroup OR stratif* OR "with insulin resistance")` | 2 |
| C1 | CT.gov: `AREA[EligibilityCriteria]("HOMA-IR" OR "insulin resistance") AND AREA[StudyType]INTERVENTIONAL AND AREA[ResultsFirstPostDate]RANGE[MIN,MAX]` | 122 (12 screened: IRIS, NCT02519543 TRIO-BD, HIV/clozapine pioglitazone, adolescents, none a test-and-treat design) |
| C2 | CT.gov: `AREA[EligibilityCriteria]"HOMA-IR" AND AREA[StudyType]INTERVENTIONAL AND AREA[Phase](PHASE3 OR PHASE4)` | 32 (12 screened) |
| E1 | Europe PMC: `"MAFLD" AND "HOMA-IR" AND "2.5" AND "metabolic risk abnormalities" AND OPEN_ACCESS:y` | 83 (top 5 reviewed; two full texts grepped) |
