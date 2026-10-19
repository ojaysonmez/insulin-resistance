# Skeptic review, round 2: independent subagent run (Set B) and comparison.md

Reviewer: ir-skeptic session. Date: 2026-10-18. Scope: `subagents/ir-*.md` (Set B) and `comparison.md`. Set A is the first-run session reports; my first review is `ir-skeptic.md`. Coverage and reimbursement are out of scope.

## 0. Method, and what changed in tooling

- **Scholar Sidekick was still unusable** ("You are not subscribed to this API"), so I repeated the substitute method from round 1:
  - PubMed records for about 85 Set B PMIDs, compared with the claimed title, first author and year. All resolve to the claimed paper. I did not check the Set B items with no PMID.
  - Crossref `updated-by` for 28 load-bearing DOIs (WHI/Schmiegelow, Liu 2026, Xu 2026, Gonzalez-Gonzalez, Isokuortti, Marcovina, Stern, Kitabchi, the TyG meta-analyses, UK Biobank/Che, Gastaldelli, Osei, Sumner, Rudvik, Chavez, DeFronzo 2014, Spence, Luo, IRIS design, Abdul-Ghani 2008, Fiorentino, Rosli, Peña, Vasques, Jiao, Aroda, Tian). **No retractions, corrections or expressions of concern.** Together with round 1, 60 distinct DOIs have been checked; the older papers without DOIs were not.
- **I read primary text this round, which neither set did:**
  - The 2023 PCOS guideline (JCEM, PMC10505534, full text via Europe PMC).
  - ADA Standards of Care 2025 sections 2 and 3 (PMC11635041, PMC11635039; I searched them for IR statements, I did not read them end to end).
  - AASLD NAFLD guidance (PMC10735173; keyword search of the text, not a full read).
  - Abstracts for the claims below.

## 1. The five flags in comparison.md

| # | Flag | Verdict |
|---|---|---|
| 1 | PMID 12087016 labelled "IRAS" in Set A endocrinologist | **Confirmed.** It is Hanley 2002, San Antonio Heart Study. Abstract: HOMA-IR quintile 5 vs 1 OR 2.52 (1.46-4.36) age/sex/ethnicity-adjusted; 1.94 (1.05-3.59) after adding LDL, TG, HDL, SBP, smoking, alcohol, exercise, waist; authors say "only modestly reduced". "Attenuation" understates persistence. Already in my round-1 P6. |
| 2 | Set B biostatistician's "inter-lab CV about 25%" cited to four PMIDs, "only two report it" | **Confirmed, and worse than stated.** Only 28660493 (Isokuortti: HOMA-IR inter-lab CV 25%, from 10 samples in 7 labs) reports a HOMA-IR figure. 17272483 (Marcovina) reports an **insulin immunoassay** among-assay CV of 12-66%, median 24%, a different quantity. 34380182 (Matli) reports "unsatisfactory correlation", no CV. 26070771 (Shashaj) is paediatric percentiles. So the one HOMA-IR number rests on one small study. The claim is also internally inconsistent: Marcovina's assays are insulin-only, but the bottom line labels it HOMA-IR. |
| 3 | Set B PCP "Moderate" grades rest on one 94.7%-male cohort and one postmenopausal-women cohort | **Confirmed.** Hu 2024 (5578 workers, 94.7% male) and Schmiegelow/WHI 2015 (15,288 women, no diabetes) are both abstract-confirmed. See P2 for the additional overadjustment problem in WHI. |
| 4 | ADA recommendations cited by PMID without reading the text | **Confirmed as a process gap. The conclusion survives.** I read the ADA Standards. Section 2 (diagnosis) contains no recommendation to measure insulin or HOMA; it states HOMA of β-cell function "not recommended for screening outside the research setting" (in the cystic-fibrosis section). Section 3 (prevention) describes IRIS in its narrative, defining IR as HOMA-IR ≥3.0, but its recommendations I saw (3.12 to 3.14) concern weight, cardiovascular risk and pharmacotherapy, not an IR test. So "ADA guidance does not make IR measurement part of screening or prevention" is correct, but it was asserted without reading. |
| 5 | PCOS 2023 guideline wording on IR testing unverified | **Resolved.** Practice point 1.9.12: "Insulin resistance is a pathophysiological factor in PCOS; however, clinically available insulin assays are of limited clinical relevance and are not recommended in routine care (refer to 3.1.10)." Practice point 3.1.10 repeats it ("should not be used in routine care"). The guideline's conclusion adds: "routinely available measures of insulin resistance are inaccurate and clinical measurement is not currently recommended." Three caveats: (a) these are **practice points** (consensus-based), not graded evidence-based recommendations; (b) the reason given is assay inaccuracy and limited relevance, not a demonstration of no benefit; (c) metformin recommendations 4.3.1 to 4.3.3 are indexed to BMI, with IR listed as an outcome improved, not a selection criterion. The "don't test IR in PCOS" verdict in both sets, and the recalled statement in Set A and Set B endocrinologists, are correct. |

## 2. New and remaining problems in Set B

### P1 (High). Set B PCP's graded verdicts are overstated, and one study is misused
- **Moderate grades.** Scenarios 1-7 mostly carry "Moderate" for the "don't test" verdict. Evidence behind them: Hu (male Japanese workers), WHI (postmenopausal women without diabetes), UK Biobank and meta-analysis associations, and measurement papers. None is a decision study. The same set's own gap section says "evidence that IR testing changes outcomes ... none found". "Moderate" is not defensible for the verdicts; Set A's "Low" is the better calibration. The "no routine IR testing" conclusion itself is well founded (e.g. the PCOS practice point and ADA/EASL/AASLD silence); the grade is the problem.
- **WHI adjusts away the exposure.** In Schmiegelow's abstract, HOMA-IR, insulin and TG/HDL-C "remained associated with increased CVD risk after adjusting for most CVD risk factors" and lost significance only after adjusting for HDL-C (HR 1.06, 0.98-1.15). HDL-C is part of the IR phenotype and arguably downstream of it, so adjusting for it removes what the index is supposed to carry. The correct reading is "an IR index is redundant once HDL-C is known", which is a fair decision-level point, not "IR is unrelated to CVD". Scenario 7 ("IR indices add nothing once HDL-C is in the model") also applies a women-only cohort without diabetes to all hypertriglyceridaemia patients.
- **1-hour OGTT glucose "better supported than insulin".** The cited Fiorentino 2015 paper compares 1-h glucose with *impaired fasting glucose*, not with insulin or HOMA-IR; the IDF statement is guidance. The comparison with insulin is not in either source.
- **DPP statement.** "Everyone in every arm got an intervention" (Kitabchi 2005, confirmed from abstract) is inexact: there was a placebo arm. The abstract's useful finding is that baseline insulin sensitivity and secretion each predicted lower diabetes hazard in all arms (HR 0.62-0.94 per SD), i.e. IR is prognostic; whether it modifies treatment effect is not tested in that paper.
- **Positive note.** Stern 2005 (confirmed): a clinical/lipid rule without insulin or HOMA-IR had aROC 85.1% vs 90.0% for the rule that included HOMA-IR, against clamp-defined IR. The PCP's "a little, at best" is a fair reading, though 5 aROC points is not nothing.

### P2 (Medium). Set B scientist rests two key physiology statements on weak sources
- **"Clamp GIR primarily reflects muscle" is sourced to Chavez 2009 (PMID 19487637).** That is an FGF-21 paper; the phrase "whole-body (primarily reflects muscle) insulin sensitivity" appears only as a parenthetical in its abstract. The statement is textbook-correct, but the citation does not establish it. (Set A flagged the same statement **[uncited]**, which is the more honest treatment.)
- **"HOMA is mostly hepatic" is tagged [uncited]** in Set B, and 19046218 (Abdul-Ghani 2008, which the report uses for "23% discordant") is titled "*Strong association* between IR in liver and skeletal muscle" (r = 0.68). The 23% discordance is accurate from the abstract; the framing in the report emphasises discordance more than the authors do.
- **Kanat 2011 (21553243)** is cited for "IFG subjects show hepatic IR with normal muscle sensitivity"; in the abstract that is a statement about the authors' *earlier* work ("We recently demonstrated ..."). The report calls it a background statement, which is accurate, but it should not be counted as support.
- **Proinsulin claim.** The report says modern assays show little proinsulin cross-reaction (25172526, 30027696). 25172526 is about **insulin analogue** cross-reactivity, and Marcovina 2007 (in Set B's biostatistician report) found des(64,65)-proinsulin cross-reactivity above 40% for 9 of 10 assays. The sentence is not supported as written.
- **Omissions the report states honestly:** no PCOS section, no within-person variability citation (it exists in the same folder, 29618016), no hyperbolic compensation (Kahn) or ancestry meta-analysis (Kodama).
- Verified and fine: Osei 1997 (hepatic insulin extraction reduced 25-52% in people of West African ancestry, abstract exact), Hansen 1993 (monkeys), Sumner 2005 (TG and TG/HDL not markers of IR in African Americans), Robbins 1996 (ADA task force).

### P3 (Medium). Set B endocrinologist: sound but thinner, and carries several unread items
- Coverage gaps relative to Set A: no ACT NOW, GRADE, PIVENS, resmetirom, semaglutide, Cryer hypoglycaemia guideline or C-peptide review. Hypoglycaemia work-up, DPP magnitudes, and the PCOS statement are **[U]**. The PCOS statement is now confirmed (item 5 above), as is the direction of Set A's recall.
- Verified well: IRIS (abstract), repeatability, the "one-to-one transformation" paper (Rudvik 2018, PMID 29940866, abstract confirmed), EASL executive summary and full text (38869512, 38852583: same guideline in two journals, as comparison.md says), Lambadiari 2026 lipodystrophy update (title).
- Several items are "title only" (TyG meta-analyses 35778731/37415168, LC-MS/MS 38549041, commutability 36750430, eGDR 42178592/41257477, South Asian 40353919). They resolve to the right titles but support only "this literature exists".
- "High that fibrosis staging drives care" (MASLD) rests on the EASL abstract. Strong claim, plausible, still abstract-level.

### P4 (Medium). Set B biostatistician: good new material, two grading problems
- **New and useful:** Liu 2026 (CHNS cohort plus 5-cohort meta-analysis: pooled C-index gain 0.0004, CI -0.0092 to 0.0100, very low GRADE, heavily dependent on one cohort; 0.0051 after excluding it), Xu 2026 (NHANES, 8735 non-diabetic adults ≥45: no significant C-statistic gain from TyG or HOMA-IR; HOMA-IR J-shaped for CVD mortality under competing risks), Gonzalez-Gonzalez 2022 (38 cohorts: HOMA-IR T2D HR 1.87, non-fatal MACE HR 1.46, hypertension HR 1.35; no association with fatal MACE). All numbers match their abstracts.
- **Overgrading.** Marcovina 2007 is rated "High" while the report notes platform currency is unverified; it is a 2007 comparison of assays from that era (but see P1 of comparison: still the best standardisation data cited). Liu 2026 is graded "Moderate" for TyG, but is a very-low-GRADE meta-analysis of five cohorts with one dominant study, on a different index.
- **Hanging claim.** Bottom line 4 (inter-lab CV about 25%): see flag 2.
- **Failed IRIS retrieval.** It cites the design paper (25458644) and a post hoc analysis (Spence, 30734043: ITT in prediabetes HR 0.70 (0.56-0.88); adherence-based HR 0.57 (0.39-0.84), which the report rightly rates low) instead of the primary NEJM report. Set A has the primary paper and the report's conclusion is unaffected.

### P5 (Medium). Evidence is now somewhat better for "no incremental prediction", but still one population type per study
Set B adds two CVD incremental-value analyses that I said did not exist in round 1: WHI (HOMA-IR, insulin and TG/HDL-C did not improve discrimination or reclassification, with the overadjustment caveat in P1) and NHANES (no C-statistic gain; mortality outcome, age ≥45). With Framingham (T2D), Hu (T2D) and the TyG meta-analysis, "not shown to add to standard predictors" is better supported than after round 1. It remains: mostly older, largely non-diabetic, white/Japanese/US populations; no decision-curve or calibration analysis; the TyG literature includes small studies reporting statistically significant but tiny increments (round 1: ΔC 0.755 to 0.768, 0.715 to 0.719), which the Set B biostatistician mentions but does not rate.

### P6 (Low). Housekeeping in Set B
- PCP's IR-in-pregnancy item (HOMA-IR ≤2, AUC 0.91 vs OGTT, n = 182, PMID 34500513) is a single-centre diagnostic-accuracy study with an HOMA cutoff derived in the same sample; the report says "not replicated" and keeps it to "Low". Fine.
- PCP "Unclear" for children and "patient asks" are honest.
- Set B scientist cites DeFronzo 2014 (24937535) correctly: the paper's title is that the disposition index "does not reflect β-cell function" in IGT after pioglitazone.
- NRI methods references (Leening 2014 ×2, Pencina 2010 and 2014, Mühlenbruch 2015, Zheng 2012) all resolve to methods papers; no clinical claim depends on them.

## 3. comparison.md: does it hold up?

**What it gets right (checked):**
- The overlap statistics are right. I recounted PMIDs from the files: 29 shared, 45 Set A only, about 69 Set B only.
- Section 2.1's eight "convergent" conclusions are fairly stated. The PubMed spot-checks in 3.5 (Manley ×2, EASL ×3, Hanley, Bonora 2002) all match.
- The five flags above are real, including the Hanley mislabel, and the writer correctly declined to read my first review.

**Errors and overreach in comparison.md:**
- **"All eight files recorded that the PCOS guideline wording was not confirmed" (§2.1 item 8).** The Set A and Set B scientists do not discuss the PCOS guideline at all (the first says it has no PCOS citation; the second has no PCOS section). Six of eight is nearer the truth. Now moot: the wording is verified (flag 5).
- **§1.4 table.** "Inter-assay variation is large (Matli; the Gast RR 1.64 ...)" mixes assay variability with an association result; Gast has nothing to do with assays.
- **§2.1 item 4 calls Hu 2024 "the best-designed incremental-value paper".** It is a 94.7%-male occupational cohort with internal validation and a stated "further studies needed". Best of the few found, not best-designed.
- **§3.4 says only two of four PMIDs report an inter-lab CV;** one reports a HOMA-IR figure, one an insulin-assay figure (flag 2).
- **It repeats the "Set A PCP E10 unverified" caveat but not that E10 is verifiable** (PMID 42856833, Front Endocrinol 2026, a perspective by authors at a history-of-medicine institute; the PCP's quotes of it are accurate).
- **§4 "more reliable" calls.** My judgement:

| Role | comparison.md says | My view |
|---|---|---|
| Endocrinologist | B, modest margin | **Defensible but marginal.** B's abstract-read numbers are better documented; A's verified-identity list covers far more of the guideline and trial landscape (GRADE, PIVENS, Cryer, hypoglycaemia). Neither tested the PCOS statement; both recalled it correctly. Use both: B for numbers, A for leads. The single Set A error (Hanley label and "attenuation") is real but small. |
| Scientist | B, modest margin | **Not clearly justified.** B has more verified physiology (ancestry extraction, pulsatility, tissue discordance), but its two central claims (muscle-weighted clamp, hepatic-weighted HOMA) are respectively weakly sourced and uncited, and it has no PCOS section and wrongly says no variability data exist. A is stronger on compensation logic and on flagging what is uncited. Call it a tie; merge. |
| PCP | B | **Not justified on reliability.** B is broader (12 scenarios, WHI, Stern) but over-grades ("Moderate"), misattributes a comparison to Fiorentino, misstates DPP, and cites unread ADA items for a recommendation. A's grades are better calibrated. Best: B's scenarios and sources with A's grades. The comparison itself notes the overstatement and still ranks B first. |
| Biostatistician | A, modest margin | **Justified, and for slightly more than the stated reasons.** A's primary prediction data (Framingham, Wang, Whitehall, Dennis) are strong and its `[C-only]` list is honest; B has the inter-lab mislabel, a lost IRIS primary report and a few overgrades. But B adds the WHI-adjacent and NHANES incremental analyses and the Liu 2026 meta-analysis that A lacks; the best product is the union. |

- **Structural point the comparison does not make:** neither set is a systematic review and the two sets share tooling, role files and probably searches, so agreement between them (§2.1) is not as independent as "two independent runs" implies. It is a reproducibility check on retrieval and reading, not a second source of evidence. Treat convergence as "these are the easy-to-find papers", and divergence (what only one set found) as a measure of how incomplete each search was: about 70 of 98 Set B PMIDs and 45 of 74 Set A PMIDs appear in only one set.

## 4. Claims that survived scrutiny (round 2 additions)

- PCOS guideline: IR assays "not recommended in routine care" (PP 1.9.12, 3.1.10); IR is a "key feature" but clinical measurement not recommended; metformin is indexed to BMI.
- ADA Standards 2025: no IR measurement in diagnosis or prevention; IRIS cited narratively only.
- AASLD NAFLD guidance (text searched): initial work-up lists FPG, HbA1c and lipids and "signs of insulin resistance" on physical examination (acanthosis); insulin or HOMA measurement does not appear in the work-up passages that matched. EASL abstract (round 1): FIB-4 then elastography.
- Assay variation: Marcovina 2007 (12 assays, 9 manufacturers, among-assay CV median 24%, reference preparation did not harmonise), Isokuortti 2017 (one HOMA-IR of 2.0 read 1.3 to 2.1 across six labs), plus round-1 Manley/Matli/Rosli.
- Biological variation: EuBIVAS 26.7% and ARIC 30.4% (round 1) are consistent with Set B.
- IRIS, Dennis, Ahlqvist, Hu, Gast and Wang: Set B quotes match the abstracts.
- Citation integrity: no mismatched identifiers in Set B; no retractions.

## 5. Does round 1's verdict change?

- **"No established utility today": unchanged, slightly stronger.** The PCOS guideline now explicitly states it for one condition; ADA and AASLD text I read does not use IR measurement; the WHI and NHANES analyses add CVD negatives. I put this at roughly 85%.
- **"Shown not to add value": modestly up** (from roughly 40-50% to roughly 55-60%) because two more incremental-value studies exist. Still limited by population (older, mostly non-diabetic, few ethnicities), absence of decision-curve/calibration work, an overadjusted WHI analysis, and no trial registry search by either set.
- **Unchanged:** niche roles for insulin/C-peptide (hypoglycaemia, classification, lipodystrophy), the IRIS entry-criterion portability problem (single HOMA-IR >3.0 on one assay, with ~27-30% within-person CV and up to ~2× assay differences), and the signal in Dennis that TZD response differs in the high-IR cluster without beating simple features.
- **Remaining gaps no run closed:** a trial-registry search for IR-guided care; ADA/AASLD recommendation text read in full; external validation of any cutoff; head-to-head incremental value for non-white and younger populations.

## 6. One-line verdict on comparison.md

Mechanically accurate and useful (counts, flags, spot-checks hold up), but its per-role "more reliable set" rankings are only fully justified for the biostatistician; the PCP and scientist calls are not supported, and a few sentences conflate or overstate; treat the two sets as complementary and not as independent confirmation.
