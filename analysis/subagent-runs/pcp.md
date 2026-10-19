# Is measuring insulin resistance (IR) useful in primary care? PCP assessment

Role: primary care physician (role file `ir-pcp.md`). Scope: who to test, when, what the result would trigger, and whether it adds to BMI/waist, glucose, HbA1c, lipids, ALT, BP and risk calculators. Coverage and reimbursement are out of scope. Independent run: no other `ir-team` files were read.

Citation policy: every PMID below was returned by a PubMed lookup in this session. Several were matched to the title/abstract (marked "abstract read"); others were matched by journal/year/volume/page (marked "id-matched"). Statements marked **[PCP judgment]** or **[not verified]** are clinical reasoning or recollection, not backed by a retrieved citation. Evidence strength is high/moderate/low, my own grading.

"IR measurement" here means what a primary-care lab can actually order: fasting insulin and HOMA-IR (calculated from fasting insulin and glucose). Clamp, IVGTT and OGTT-insulin indices are research tools. Gastaldelli's review of clamp, IVGTT, fasting indices and OGTT-based tests reports their accuracy, precision and reproducibility (PMID 35894085, abstract read).

## Bottom line

1. In an undifferentiated primary care population, routine IR measurement (fasting insulin/HOMA-IR) is **not useful**. It does not change what I do next, and it adds little over data I already have.
2. The strongest direct evidence is negative on incremental value. In a prediction model, adding HOMA-IR and HOMA-beta to BMI + HbA1c did not materially improve diabetes risk discrimination, whereas adding fasting glucose did. AUC rose from 0.79 to 0.84 with glucose, and HOMA-IR/HOMA-beta added no meaningful gain (PMID 38191206, abstract read). In postmenopausal women without diabetes, IR measures lost association with CVD after HDL-C adjustment and did not improve discrimination or reclassification (PMID 25944628, abstract read).
3. The measurement itself is a problem. HOMA-IR within-person CV is about 27 to 30% (PMID 38987271, EuBIVAS; PMID 29618016, ARIC). Insulin assays disagree: three immunoassays showed unsatisfactory correlation and systematic differences in calculated HOMA-IR, so cutoffs are assay-specific (PMID 34380182). There is no universal threshold.
4. The treatments I would use in the patients who might get tested (lifestyle, metformin, GLP-1 RA/tirzepatide, statin, BP control) are triggered by BMI, glycemic category, ALT/fibrosis score, lipids and BP. No trial I found shows that choosing or withholding them by HOMA-IR improves outcomes.
5. Evidence that IR testing changes outcomes (decision-impact or RCT data) was not found. This is a gap, not proof of no benefit.

## Why the signal is real but not actionable

- IR matters biologically. In the Diabetes Prevention Program, higher baseline insulin sensitivity and secretion were associated with lower diabetes hazard in every arm, and improved sensitivity on treatment tracked with lower risk (PMID 16046308, abstract read). But all DPP participants already had IGT or elevated glucose, and everyone in every arm got an intervention. So this explains mechanism and does not show that a baseline IR value should steer therapy.
- Surrogates of IR (TyG index, TG/HDL-C) track CVD. A meta-analysis of 8 cohorts (5.7 million people) reports HR 1.61 for ASCVD in the top TyG category (PMID 33812373, abstract read). Another meta-analysis rated certainty as moderate for CAD but very low for composite CVD, MI and mortality (PMID 35778731, abstract read). In UK Biobank the TyG and TG/HDL-C associations were largely mediated by dyslipidemia, diabetes and hypertension (PMID 36797706, abstract read). In other words, much of the "IR" signal is carried by lipids, glucose and BP that I already measure.
- A simple clinical rule using BMI, HOMA-IR and related variables identified clamp-defined IR (aROC 90%), but a rule using only clinical measures and lipids, with no insulin, performed almost as well (aROC about 85%) (PMID 15677489, abstract read). That is the core "does it add anything" question, and the answer is "a little, at best".

## Practical issues

- Fasting: 8 to 12 h, morning draw. Insulin needs a laboratory with a defined assay. Turnaround is usually days. A sample from a non-fasted visit is uninterpretable. **[PCP judgment]**
- Interpretability: HOMA-IR reference data come from specific cohorts and assays. In one German population cohort, the 97.5th percentile in a stringently selected reference group was 2.35, with assay-specific intervals required (PMID 34380182). Variation of about 27 to 30% means a "high" value can fall to "normal" on a repeat draw (PMIDs 38987271, 29618016). Patients will anchor on a single number, which risks both false reassurance (a "normal" HOMA-IR in a person with obesity and prediabetes) and overdiagnosis (a transiently high value in a lean person).
- Follow-up burden: a positive result generates repeat testing, patient questions and referrals without a defined pathway. **[PCP judgment]**
- Population IR labels are heterogeneous. Genetic work separates "non-diabetogenic" from "diabetogenic" hyperinsulinemia, which argues against reading a high insulin value as one uniform risk state. (I did not retrieve a PMID for this paper, so I do not rely on it in the verdicts.)

## Verdicts per scenario

| # | Scenario | Test IR? | Action I would take regardless | What a result would trigger | Evidence |
|---|---|---|---|---|---|
| 1 | Undifferentiated adult, no risk factors | **Don't test** | Standard screening (see 2) | Nothing | Moderate |
| 2 | Adult with overweight/obesity, or with family history of T2D | **Don't test** | Glycemic screening with HbA1c or fasting glucose (ADA Standards, PMIDs 39651986, 39651971, id-matched; Brazilian guideline recommends FPG and HbA1c first, OGTT for high-risk with normal values, PMC article in Consensus listing, no PMID retrieved). Lifestyle program; weight management | None. HOMA-IR does not change drug choice or screening interval | Moderate |
| 3 | Prediabetes (A1c or FPG in range) | **Don't test IR.** If anything, refine glycemia | Intensive lifestyle first: DPP lifestyle cut incidence 58%, metformin 31% (PMID 11832527, abstract read); Finnish DPS also 58% (PMID 11333990, abstract read). Consider metformin per ADA criteria. If glycemia is discordant or borderline and risk is high, a 1-hour OGTT glucose is better supported than insulin: 1-hour PG outperformed other markers for progression (PMID 26274345; IDF position statement PMID 38458916) | Unchanged | Moderate for the "no IR" verdict; the 1-h OGTT is promising but low-to-moderate and not yet in US guidance |
| 4 | Normal glucose and HbA1c but metabolic syndrome features (high TG, low HDL, central obesity, BP) | **Don't test insulin.** TG/HDL-C and waist already carry the information | Treat the components; recheck glycemia at 1 to 3 years | None | Moderate. TG/HDL-C within-person CV about 23% vs 30% for HOMA-IR (PMID 29618016) |
| 5 | PCOS symptoms or diagnosis | **Don't test** (HOMA-IR not needed for diagnosis or management) **[not verified against the guideline text; I could not retrieve the specific recommendation from the abstract of PMID 37580314]**. Glycemic status should be checked | Diagnose by Rotterdam-type criteria; evaluate glycemia (OGTT is the guideline-favoured screen in many documents; in a Nordic cohort of 876 women with PCOS, no normal-weight woman (BMI <25) had T2D, so routine OGTT may not be needed in that group, PMID 29040530, abstract read); lifestyle; metformin or GLP-1 RA by weight/glycemia | Not needed. Note: in 882 PCOS women, waist-to-height ratio already identified IR (cutoff 0.519) (PMID 39717101, abstract read) | Low to moderate |
| 6 | Hepatic steatosis / MASLD, raised ALT | **Don't test IR.** Use FIB-4 first, then elastography | MASLD definition already requires at least one cardiometabolic risk factor (PMID 37363821, abstract read). Fibrosis risk by FIB-4 and elastography is what drives referral (pathway comparison across six guidelines, PMID 40348110, abstract read). The cited primary-care consensus uses FIB-4 thresholds 1.3 and 2.7 (Medical Journal of Australia, 2025, via Consensus, no PMID retrieved) | None. IR does not alter FIB-4 pathway or referral | Moderate |
| 7 | Hypertriglyceridemia, atherogenic dyslipidemia | **Don't test** | Lipid and glycemic work-up, secondary causes, statin per risk | None. IR indices add nothing to risk discrimination once HDL-C is in the model (PMID 25944628) | Moderate |
| 8 | Established type 2 diabetes | **Don't test** | Standard care | None. Fasting insulin tracks CHD in diabetes (HR 1.18 per quartile), but that is not a validated decision tool (Consensus-listed cohort; PMID not retrieved) | Low |
| 9 | Pregnancy / gestational diabetes screening | **Don't test** | Use OGTT | HOMA-IR cutoff <=2 had AUC 0.91 vs OGTT in a 182-woman cross-sectional study (PMID 34500513, abstract read), but this is single-centre, not replicated, and OGTT is the standard | Low |
| 10 | Child or adolescent with obesity | **Unclear** | Screen glycemia by guideline (FPG/HbA1c from age 10 or puberty with risk factors, Brazilian guideline above); lifestyle | I found no pediatric decision-impact evidence. Pediatric HOMA-IR cutoffs are population- and puberty-specific **[not verified]** | Low |
| 11 | Patient asks for "an insulin resistance test" (symptoms: fatigue, weight gain, skin tags) | **Unclear / generally no** | Examine, check HbA1c, lipids, TSH, ALT, BP; discuss lifestyle and weight treatment | A normal HOMA-IR can falsely reassure. A high one changes nothing. Document the counselling | Low |
| 12 | Research or niche referral (suspected lipodystrophy, severe IR syndromes, hyperinsulinism work-up) | **Test, via endocrinology** | Endocrine referral | Directed work-up | Not assessed in depth (outside primary care) |

## Does it add beyond BMI, glucose, HbA1c and lipids?

- **Diabetes prediction: no meaningful addition.** PMID 38191206 (n=5,578, 94.7% male, 943 incident cases): FPG improved AUC from 0.79 to 0.84; HOMA-IR/HOMA-beta did not materially improve discrimination or calibration. Caveats: mostly male, one cohort, no external replication.
- **CVD prediction: no meaningful addition.** PMID 25944628 (n=15,288 women, 10-year follow-up): not significant after HDL-C adjustment; no improvement in discrimination or reclassification. Caveats: postmenopausal women only, no diabetes.
- **Mortality in hypertension:** HOMA-IR independently predicted all-cause mortality in 7,548 hypertensive US adults (HR 1.017 per unit) (Cardiovascular Diabetology 2026, via Consensus; PMID not retrieved, so not used for a verdict). A small hazard ratio per unit is not a decision threshold.
- **Identifying who is "insulin resistant":** BMI plus fasting glucose, lipids and BP get most of the way (PMID 15677489).
- **Counselling:** for most patients, lifestyle advice is the same whatever the HOMA-IR. **[PCP judgment]** A number can motivate some patients but there are no trials showing it improves adherence or weight loss.
- **Drug initiation:** metformin and GLP-1 RA/tirzepatide are started on glycemic and weight criteria. GLP-1 RA and tirzepatide improve HOMA-IR, partly independently of weight loss (seen in Consensus abstracts only, no PMID retrieved; see "Evidence gaps"). I found no RCT in which baseline HOMA-IR selected responders. In DPP, lifestyle and metformin improved insulin sensitivity regardless of genetic IR burden (Hivert 2015, via Consensus; PMID not retrieved).
- **Screening interval:** interval is set by glycemic category and risk factors. No evidence that HOMA-IR should lengthen or shorten it.
- **Referral:** FIB-4/elastography (MASLD), Rotterdam criteria (PCOS) and glycemic thresholds drive referral. IR does not.

## Risks of routine use

- Overdiagnosis: assay-specific, variable measurement (PMIDs 34380182, 38987271) with no consensus cutoff, plus a prevalence estimate of IR that ranges from about 15% to over 60% depending on criteria (narrative review, Nutrients 2026, via Consensus; PMID not retrieved, so only illustrative).
- False reassurance in patients with obesity or prediabetes who happen to have a normal HOMA-IR.
- Cascade: repeat tests, supplements and off-label treatments marketed against "insulin resistance". **[PCP judgment]**

## Evidence needed before routine use

1. Prospective cohorts in unselected primary care showing incremental prediction (net reclassification, calibration) of HOMA-IR over a model with BMI, glucose, HbA1c, lipids, BP, ALT. Existing data are negative or neutral (PMIDs 38191206, 25944628).
2. Harmonised, traceable insulin assays and population-agnostic thresholds. Today they do not exist (PMID 34380182).
3. A repeat-measure strategy that handles about 27 to 30% within-person variation, or a more stable index.
4. Randomised trials in which treatment is selected or intensified by IR status (for example, metformin or GLP-1 RA in prediabetes stratified by baseline HOMA-IR) with diabetes, CVD or weight outcomes. I found none.
5. Decision-impact studies: does knowing the result change clinician actions or patient behaviour?

Status today: item 1 exists and is mostly negative; items 2 to 5 do not exist (as far as my searches showed).

## Evidence gaps and limits of this review

- Search was targeted, not systematic: PubMed (title/field searches, noisy) and Consensus (3 results per query). Guideline text was read only as abstracts; I did not read the full ADA, AASLD, EASL or PCOS guideline sections on insulin testing.
- Not verified: what exactly the 2023 PCOS guideline says on IR testing (PMID 37580314, abstract only); pediatric HOMA-IR cutoffs; statements that GLP-1 RA/tirzepatide improve HOMA-IR (seen in Consensus abstracts for liraglutide, Diabetes 2023, and tirzepatide, JCEM 2020, but PMIDs not retrieved, so no weight placed on them).
- Several cohort conclusions come from single, demographically narrow populations (a cohort that was 94.7% male; postmenopausal US women). Generalisability to a mixed primary care panel is unknown.
- Items listed with "PMID not retrieved" were found via Consensus and are used only as illustration, not for verdicts.

## Reference list (PMIDs retrieved in this session)

| PMID | Citation | How verified |
|---|---|---|
| 3899825 | Matthews DR et al. Homeostasis model assessment. Diabetologia 1985;28:412-9. Reports low precision of the model estimate (CV 31% for IR) | Abstract read |
| 35894085 | Gastaldelli A. Measuring and estimating insulin resistance in clinical and research settings. Obesity 2022;30:1549-63 | Abstract read |
| 15677489 | Stern SE et al. Identification of individuals with insulin resistance using routine clinical measurements. Diabetes 2005 | Id-matched; abstract via Consensus |
| 38191206 | Hu H et al. HOMA-IR, HOMA-beta, visceral fat area and diabetes risk prediction models. BMJ Open Diabetes Res Care 2024 | Id-matched; abstract via Consensus |
| 25944628 | Schmiegelow MD et al. Insulin resistance and CVD risk in postmenopausal women (WHI). Circ Cardiovasc Qual Outcomes 2015;8:309-16 | Abstract read |
| 16046308 | Kitabchi AE et al. Role of insulin secretion and sensitivity in the evolution of T2D in the DPP. Diabetes 2005;54:2404 | Id-matched; abstract via Consensus |
| 11832527 | Knowler WC et al. DPP lifestyle or metformin. N Engl J Med 2002;346:393-403. doi:10.1056/NEJMoa012512 | Abstract read |
| 11333990 | Tuomilehto J et al. Finnish DPS. N Engl J Med 2001;344:1343-50. doi:10.1056/NEJM200105033441801 | Abstract read |
| 34380182 | Matli B et al. Distribution of HOMA-IR in a population-based cohort and reference intervals. Clin Chem Lab Med 2021 | Id-matched; abstract via Consensus |
| 38987271 | Carobene A et al. Biological variation of insulin resistance markers (EuBIVAS). Clin Chem Lab Med 2024 | Single PubMed hit; abstract via Consensus |
| 29618016 | Poon AK et al. Short-term repeatability of IR indexes: ARIC. J Clin Endocrinol Metab 2018 | Id-matched; abstract via Consensus |
| 33812373 | Ding X et al. TyG index and ASCVD incidence, meta-analysis. Cardiovasc Diabetol 2021;20:76 | Id-matched; abstract via Consensus |
| 35778731 | Liu X et al. TyG index and CVD/mortality, systematic review. Cardiovasc Diabetol 2022;21:124 | Id-matched; abstract via Consensus |
| 36797706 | Che B et al. TyG and TG/HDL-C and CVD, UK Biobank. Cardiovasc Diabetol 2023;22:34 | Id-matched; abstract via Consensus |
| 37580314 | Teede HJ et al. 2023 International PCOS Guideline recommendations. J Clin Endocrinol Metab 2023;108:2447-69. doi:10.1210/clinem/dgad463 | Abstract read |
| 29040530 | Pelanis R et al. T2D prevalence is not increased in normal-weight women with PCOS. Hum Reprod 2017 | Id-matched; abstract via Consensus |
| 39717101 | Zhu M et al. Waist-to-height ratio predicts IR in PCOS. Front Endocrinol 2024. doi:10.3389/fendo.2024.1502321 | Abstract read |
| 37363821 | Rinella ME et al. Multisociety Delphi consensus on fatty liver nomenclature. Hepatology 2023;78:1966-86. doi:10.1097/HEP.0000000000000520 | Abstract read |
| 36727674 | Rinella ME et al. AASLD practice guidance on NAFLD. Hepatology 2023;77:1797 | Id-matched only; content not read |
| 40348110 | Vidal-Trécan T et al. Six international guidelines (FIB-4, FibroScan) for MASLD in T2D. Clin Gastroenterol Hepatol 2025 | Id-matched; abstract via Consensus |
| 39651986 | ADA Standards of Care 2025, section 2 (Diagnosis and classification). Diabetes Care 2025;48:S27 | Id-matched only; content not read |
| 39651971 | ADA Standards of Care 2025, section 3 (Prevention or delay of diabetes). Diabetes Care 2025;48:S50 | Id-matched only; content not read |
| 34500513 | Paracha AI et al. HOMA-IR and QUICKI in gestational diabetes. J Coll Physicians Surg Pak 2021;31:1015-9. doi:10.29271/jcpsp.2021.09.1015 | Abstract read |
| 26274345 | Fiorentino TV et al. One-hour postload hyperglycemia predicts T2D better than IFG. J Clin Endocrinol Metab 2015 | Id-matched; abstract via Consensus |
| 38458916 | Bergman M et al. IDF position statement on 1-hour post-load plasma glucose. Diabetes Res Clin Pract 2024;209:111589 | Id-matched; abstract via Consensus |

Note on PMID 36727674, 39651986 and 39651971: these PMIDs resolved to the expected journal/volume/page. I did not read their text, so the report does not rely on specific statements from them beyond the section titles.

## Summary of evidence strength by verdict

- Don't test (general adult, overweight/obesity, prediabetes, metabolic syndrome, MASLD, dyslipidemia): moderate. Based on negative incremental-value cohorts (PMIDs 38191206, 25944628), measurement problems (PMIDs 34380182, 38987271, 29618016), and the absence of any outcome trial.
- PCOS: low to moderate; the specific guideline wording is not verified.
- Established diabetes, pregnancy: low (but standard care already covers these without IR).
- Pediatrics: low, unclear.
- Evidence of decision impact for IR testing: none found.
