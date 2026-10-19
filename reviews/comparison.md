# Comparison of two independent runs of the 4-role IR clinical-utility analysis

Set A = separate sessions, `ir-team/ir-*.md`. Set B = subagents, `ir-team/subagents/ir-*.md`. All eight files were read in full. `ir-skeptic.md` was not read. Coverage and reimbursement are out of scope.
Everything below comes from the files, except the PubMed spot-check in section 3.5, which is labelled. No citation was checked from memory. PMIDs were extracted from each file by script, with DOIs stripped first.

---

## 1. Per-role comparison

### 1.1 Endocrinologist

**Agree**
- IR measurement (HOMA-IR, fasting insulin, TyG) does not change specialist management in T2D, prediabetes, PCOS, MASLD or obesity. Evidence strength is "low".
- Insulin and C-peptide are useful in a narrow set of settings that are not IR screening: hypoglycaemia and hyperinsulinism work-up, lipodystrophy and severe IR, and C-peptide for diabetes classification.
- IRIS (PMID 26886418, pioglitazone, HOMA-IR above 3.0 entry) is the one outcome trial where IR defined enrolment. It had no non-IR arm, so it cannot show that testing is needed.
- Ahlqvist 2018 (29503172) and Dennis 2019 (31047901) are cited: IR-based clusters are prognostic, but simple clinical features do as well for treatment choice.
- The claim that the 2023 PCOS guideline says not to test IR (PMID 37580314) is not confirmed from the abstract in either set.
- The same test limits are listed: no agreed cutoff, assay variability, beta-cell failure, exogenous insulin.

**Differ in emphasis**
- Set A has 29 PMIDs, mostly guideline and trial anchors: ACT NOW, GRADE, PIVENS, resmetirom, semaglutide/ESSENCE, Cryer hypoglycaemia, PCOS physiology, Wagner prediabetes subphenotypes. It verified identity (title and journal) only. Its numeric and content claims are tagged **[recall]** or **[opinion]**.
- Set B has 27 PMIDs, mostly about test performance. It cites within-person CV 30.4% and MDC 2.3 (29618016), the HOMA/QUICKI/FIRI one-to-one transformation point (29940866), TyG meta-analyses, LC-MS/MS harmonisation, and a T1D "double diabetes" eGDR section. It marks abstract-read versus title-only per item and uses **[U]** for unverified.
- Set A rates IR phenotypes as moderate for prognosis. Set B says "moderate for prognostic association" and "moderate" for IRIS effect.
- Set A states IRIS enrolment (HOMA-IR above 3.0) as **[recall]**. Set B read the abstract and reports HR 0.76 (0.62-0.93), incident diabetes HR 0.48, and the weight, oedema and fracture harms.

| Verdict | Set A | Set B |
|---|---|---|
| Prediabetes | No established decision; prognostic only. Low | No decision change; plausible but unproven. Low |
| T2D drug choice | No; C-peptide high-strength for classification | Little; C-peptide as practical test [U]. Low for decisions, moderate for prognosis |
| PCOS | No; screen glycaemia in all. Low | No; treat on phenotype. Low |
| MASLD | No; fibrosis staging dominates. Low | No; "high" that fibrosis staging, not IR, drives care. Low for IR |
| Obesity/CVD | No. Low | No. Low |
| Lipodystrophy / severe IR | Supports diagnosis. Moderate-low | Supports diagnosis/monitoring [U]. Moderate |
| Hypoglycaemia / hyperinsulinism | Yes (insulin/C-peptide). High | Yes [U]. Not graded |
| IR-targeted pioglitazone | Plausible, untested | Moderate for effect; low for IR as predictor |

### 1.2 Scientist (physiology)

**Agree**
- IR is tissue-specific. The clamp is mainly whole-body, muscle-weighted disposal.
- HOMA-IR and QUICKI are fasting, hepatic-weighted and carry the same information. Neither set treats QUICKI as an independent confirmation.
- TyG and TG/HDL-C are lipid-based and weighted to hepatic and adipose IR. TG/HDL-C validity is ethnicity-dependent.
- Selective hepatic IR (Brown & Goldstein 18249166) is mouse-derived, with Petersen & Shulman (30067154) as the competing view.
- C-peptide measures secretion, not IR.
- Fasting insulin cannot separate secretion from clearance.
- HOMA-IR understates IR when beta cells fail.
- Cutoffs are assay- and population-specific.
- Neither set shows that acting on a surrogate improves outcomes.

**Differ in emphasis**
- Set A (26 PMIDs) builds the compensation logic: Reaven 1988, the Kahn hyperbola, Kodama ancestry meta-analysis, Polonsky C-peptide extraction, the Matsuda/Abdul-Ghani muscle-vs-liver indices, Czech on hyperinsulinaemia causality. It has no verified PCOS citation, and says so. It flags the Muniyappa/QUICKI author-bias risk.
- Set B (34 PMIDs) covers adipose lipolysis (Basu, Kelsey), tissue discordance (23% in 19046218), hepatic extraction (monkey 56%, West African ancestry), pulsatility, age, pregnancy, and the assay literature (ADA 1996 task force, proinsulin cross-reactivity). It gives a measure-by-measure divergence-from-clamp table. It has no Ahlqvist, no Kahn hyperbola citation, and no PCOS section at all.
- Set A cites the hepatic C-peptide non-extraction claim (6373457, 6389599). Set B tags it **[uncited]** and uses the C-peptide/insulin ratio as a clearance proxy. Set B lists "no within-person CV paper" as a gap, although Set B's biostatistician has one (29618016).

| Verdict | Set A | Set B |
|---|---|---|
| Does one test measure "IR"? | No; tests answer different questions (4.1) | No; muscle, liver and adipose differ, 23% discordant |
| HOMA tissue weighting | Hepatic/basal; mechanistic reading of Wallace 2004 | "Mostly hepatic" **[uncited]** |
| Individual-level precision | Poor: CV ~31% (Matthews), kappa 0.63 | Same, plus pulsatility and extraction as reasons |
| TyG vs clamp | r -0.68, AUC 0.86, n=99, same-sample cutoff | Same figures; notes 19067533 was validated against HOMA, not the clamp |
| Outcome evidence | None retrieved | None retrieved |

### 1.3 PCP

**Agree**
- Do not test IR routinely in primary care.
- Use glucose/HbA1c, BMI/waist, lipids, ALT and FIB-4 instead.
- No trial shows IR-guided care improves outcomes.
- Hu 2024 (38191206) shows HOMA-IR adds nothing beyond FPG and HbA1c (AUC 0.79 to 0.84 with FPG). Both sets flag it as 94.7% male, one cohort.
- DPP (11832527) entered by glucose, not IR.
- The PCOS guideline wording on IR is unverified in both.
- Both report the ~31% CV in Matthews 1985 (3899825) and the absence of a validated cutoff.
- Both route lipodystrophy, hyperinsulinism and discordant PCOS to the endocrinologist.

**Differ in emphasis**
- Set A: 10 evidence items (incl. Gast, Bonora 2002, USPSTF) and 9 scenarios, all "Don't test". Evidence is graded mostly **Low** (one **Moderate** for glucose/A1c screening sufficiency). It labels item E10 (a 2026 perspective found via Consensus, no PMID) as unverified.
- Set B: 12 scenarios and 26 PMIDs. It adds the WHI negative reclassification result (25944628), Stern 2005 clinical rule (15677489), biological-variation (38987271), Matli reference interval (34380182), TyG/UK Biobank mediation, 1-hour OGTT glucose, pregnancy, and paediatrics. It grades the "don't test" verdicts **Moderate** in most scenarios and marks paediatrics and the "patient asks" case as **Unclear**.
- Set B notes that some findings rest on Consensus abstracts with no PMID. It uses these only as illustration.

| Scenario | Set A | Set B |
|---|---|---|
| Adult with overweight/obesity | Don't test. Moderate (glucose/A1c screening); low for IR | Don't test. Moderate |
| Prediabetes | Don't test. Low | Don't test; 1-h OGTT glucose is better supported. Moderate |
| PCOS | Don't test for diagnosis. Low | Don't test [not verified vs guideline]. Low-moderate |
| Fatty liver / ALT | Don't test; FIB-4 [judgment]. Low | Don't test; FIB-4 then elastography. Moderate |
| Hypertriglyceridaemia | Don't test. Low | Don't test. Moderate |
| CVD risk estimation | Don't test. Low-moderate association, low decision value | Don't test (25944628 negative). Moderate |
| Established T2D | Don't test. Low | Don't test. Low |
| Pregnancy / paediatrics | Not covered | Pregnancy: don't test, low. Paediatrics: unclear, low |

### 1.4 Biostatistician

**Agree**
- Association is strong. Incremental prediction is nil or negligible where tested (Hu 2024).
- Within-person CV is ~27-30% (EuBIVAS 38987271; ARIC 29618016, ICC 0.70, MDC 2.3).
- Inter-assay variation is large (Matli 34380182; the Gast 23300589 RR 1.64 high-vs-low and RR 1.46 per SD).
- No cutoff has been externally validated, and incorporation bias applies where the reference is glycaemia.
- IRIS cannot test effect modification by IR.
- No decision-curve, net-benefit or calibration analysis exists for HOMA-IR.
- Both caution against NRI inflation.

**Differ in emphasis**
- Set A (31 PMIDs) covers T2D and CVD prediction (Framingham Offspring 17533210, ARIC rules 16043747, Wang 2022 35700159: null in normoglycaemia), natural history (Whitehall 19515410), Dennis 2019, cutoff studies (Lee, Horáková), and ethnicity (SWAN, Trikudanathan as `[C-only]`). It lists eight `[C-only]` items with no resolved identifier.
- Set B (26 PMIDs) adds a TyG meta-analysis (42569452, C-index gain 0.0004), NHANES (42702103), the Gonzalez 2022 meta-analysis (36181637), Isokuortti inter-lab CV 25% (28660493), Marcovina 2007 (17272483), paediatric percentiles, and a detailed NRI methods list.
- Set B did not retrieve the IRIS primary NEJM paper (cites the design paper 25458644 and Spence 2019 30734043 instead). Set A has it (26886418).
- Cutoff range stated: A "about 1.4 to 3.6"; B "about 1.6 to 3.4" (adults). These are different sampled studies, not a conflict.

| Verdict | Set A | Set B |
|---|---|---|
| HOMA-IR adds to T2D prediction beyond clinical model + glucose | No (Framingham AROC 0.85 to 0.850-0.854; Hu 2024) | No (Hu 2024; TyG meta-analysis) |
| CVD prediction | Association only; no ΔC/NRI/net-benefit found | Same; NHANES null C-statistic |
| Within-person variability | CV 26.7% (EuBIVAS), 30.4% (ARIC) | CV ~30% (ARIC), MDC 2.3 |
| Inter-assay variability | Manley: ~twofold; Matli; Rosli CV 1.7-23.2% | Marcovina: CV 12-66%; Isokuortti 25%; Matli |
| Cutoffs | Not validated; range 1.4-3.6 | Not validated; range 1.6-3.4 |
| Decision-impact evidence | None (IRIS IR-selected only) | None (IRIS design/post hoc only) |
| IR-specific MR | Thin (Ross 2015 `[C-only]`) | Not covered |

---

## 2. Cross-role synthesis

### 2.1 Conclusions that hold in both sets across all four roles
1. No role in either set found a clinical decision that routine IR measurement (HOMA-IR, fasting insulin, surrogate indices) changes in unselected primary care, prediabetes, T2D, PCOS, MASLD or obesity.
2. No outcome or decision-impact trial of IR-guided care was found. IRIS selected on HOMA-IR above 3.0 and had no non-IR comparison.
3. The measurement is imprecise. Matthews CV ~31%, within-person CV ~27-30%, and assay-specific values with no accepted universal cutoff.
4. Glucose, HbA1c, BMI/waist and lipids already carry most of the signal. HOMA-IR adds nothing beyond FPG/HbA1c in the best-designed incremental-value paper (38191206).
5. Insulin/C-peptide has real roles that are not IR screening: hypoglycaemia/hyperinsulinism, lipodystrophy/severe IR, and C-peptide for classification (endocrinologist; PCP routes to endocrinology).
6. Fasting indices are weak when beta cells fail or exogenous insulin is present. C-peptide separates secretion from clearance.
7. TyG and TG/HDL-C avoid the insulin assay but are indirect, and TG/HDL-C validity varies by ethnicity.
8. All eight files recorded that the PCOS guideline wording on IR testing was not confirmed from the retrieved text.

### 2.2 Contradictions or tensions between roles within a set
- **Set A, endocrinologist vs biostatistician (prognosis).** The endocrinologist calls IR phenotypes "moderate" for prognostic information (Wagner, Ahlqvist). The biostatistician finds HOMA-IR adds ~0 discrimination (Framingham, Hu) and "very low" for incremental CVD prediction. These are different constructs (multi-variable phenotypes vs a single index), but the "moderate prognostic" label is not backed by an incremental-value test.
- **Set A, scientist gaps closed by other roles.** The scientist lists "within-person variability" and "assay harmonisation" as unverified gaps. The biostatistician and endocrinologist hold 29618016, 38987271, 18535197, 17363420 and 34380182.
- **Set A, endocrinologist PMID 12087016 labelled "IRAS".** See 3.4.
- **Set B, biostatistician vs endocrinologist on IRIS.** The biostatistician says the IRIS primary report was not retrievable. The endocrinologist read the abstract (26886418, HR 0.76). The numbers do not conflict; the retrieval status does.
- **Set B, scientist vs biostatistician.** The scientist says no within-person variability paper was retrieved and no harmonisation evidence. The biostatistician and PCP hold both.
- **Set B, evidence grades.** The PCP grades the "don't test" verdicts **Moderate**. The endocrinologist grades "IR changes decisions" **Low**. They grade different questions, but the PCP moderate rests on two negative cohorts (94.7% male Japanese workers; postmenopausal WHI women) plus measurement papers.
- **Set B, scientist vs bio on assays.** The scientist cites modern immunoassays with little proinsulin cross-reaction (25172526, 30027696) and also says no universal standardisation was found. The biostatistician and endocrinologist stress incomplete harmonisation. This is emphasis, not conflict.

---

## 3. Citation check

### 3.1 PMIDs cited in both sets (29 distinct; pooled across roles)
Both sets, with role in parentheses where it differs:
`382871`, `3899825`, `10480510`, `10857969`, `10902785`, `11832527`, `14623617`, `17099194`, `18249166`, `19067533`, `19336687`, `20484475`, `23300589`, `26886418`, `27710244`, `27931981`, `29503172`, `29618016`, `30067154`, `31047901`, `32256572`, `34380182`, `35939943`, `36727674`, `37363821`, `37580314`, `38191206`, `38987271`, `39651986`.
Note: each appears in both sets but not necessarily in the same role. For example, 29618016 is Set A biostatistician only and Set B endocrinologist/PCP/biostatistician. 38987271 is Set A biostatistician and Set B PCP. Only some are role-for-role matches (e.g. 3899825, 38191206, 37580314, 36727674, 34380182, 29618016 for bio).

### 3.2 PMIDs unique to one set
- **Set A only (45 after dropping the overlap):** mostly endocrinology anchors (ACT NOW 21428766, GRADE 36129996, PIVENS 20427778, Pio-NASH 27322798, resmetirom 38324483, semaglutide 40305708, Cryer 19088155, C-peptide 23413806, PCOS 23065822/23476073/27459230, Wagner 33398163, Hanley 12087016, Manley 17363420 and 18535197), scientist (Reaven 3056758, Kahn 8405710, Kodama 23704681, Polonsky 6373457/6389599, Czech 28697184, Wallace 15161807, Muniyappa 17957034, Abdul-Ghani 17192339, Giannini 21730284), PCP (Gast is shared with bio; USPSTF 34427594, Bonora 2002 12087010, Peña 40069730), biostatistician (Wilson 17533210, Schmidt 16043747, Wang 35700159, Tabak 19515410, Lee 27658115, Horáková 31108989, Staten 20040676, Kerr 24240655, Cook 17309939, Pencina 17569110).
- **Set B only (about 70):** endocrinologist (repeatability and transformation papers 29940866/20545928, TyG meta-analyses 33812373/35778731/37415168, LC-MS/MS 38549041/36750430, PCOS inositol 38163998, eGDR 42178592/41257477, lipodystrophy update 41713690, EASL 38869512/38852583, ML subtypes 39168869, Dutch South Asian 40353919), scientist (Basu 11350782, tissue discordance 19046218, Kanat 21553243, Sumner 15983289, Osei 9005969, pulsatility 8473402/8325993/8739916/8572190/8964829, ADA task force 8549870, Goetz 7476300, DeFronzo 2014 24937535, Chavez 19487637, Hansen 16353355), PCP (WHI 25944628, Stern 15677489, Kitabchi 16046308, Finnish DPS 11333990, 1-h OGTT 26274345/38458916, Gastaldelli 35894085, UK Biobank 36797706, Zhu 39717101), biostatistician (Marcovina 17272483, Isokuortti 28660493, Liu 2026 42569452, Xu 2026 42702103, Gonzalez 36181637, Shashaj 26070771, IRIS design 25458644, Spence 30734043, NRI methods list).

### 3.3 Same study cited with different identifiers
- **EASL-EASD-EASO MASLD guideline:** Set A endocrinologist PMID 38851997; Set B endocrinologist 38869512 (executive summary) and 38852583 (full text). See 3.5: these are the same guideline in three journals, not a conflict.
- **Manley insulin-assay work:** Set A endocrinologist cites 17363420 (Clin Chem 2007, 11 assays); Set A biostatistician cites 18535197 (Diabetes Care 2008, HOMA estimates). These are two different Manley papers. See 3.5.
- **TG/HDL-C ethnicity evidence:** A scientist uses Giannini 2011 (21730284, obese youth); B scientist uses Sumner 2005 (15983289, African American adults). Same conclusion, different studies.
- **Kitabchi 2005 DPP:** A biostatistician tags it `[C-only]` (no PMID); B PCP lists 16046308 (id-matched, abstract via Consensus).

### 3.4 Same PMID described differently, or claim stronger than the cited abstract
- **12087016 (Set A endocrinologist).** Described as "Hanley 2002, HOMA-IR and incident CVD (IRAS)", with "I recall attenuation after adjustment for other metabolic syndrome components **[recall]**". The PubMed record (section 3.5) is the San Antonio Heart Study, not IRAS. Its abstract reports that extra adjustment "only modestly reduced" the association (quintile 5 vs 1 OR 2.52 to 1.94, still significant). The recalled attenuation is therefore stronger than the abstract supports, and the cohort name is wrong.
- **39651986 (ADA Standards 2025, sec. 2).** Set A endocrinologist uses it to support "diagnose by glucose and HbA1c, not IR". The file's own policy says only title identity was verified. Set B PCP lists 39651986 and 39651971 as "id-matched only, content not read" and still uses them as the basis for the glycaemic-screening recommendation. Both claims rest on unread sources.
- **Set B biostatistician bottom line 4** cites four PMIDs (28660493, 34380182, 26070771, 17272483) for "inter-lab CV of HOMA-IR about 25%". Only 28660493 (25%) and 17272483 (among-assay insulin CV median 24%) report such a figure. 34380182 reports unsatisfactory correlation, and 26070771 is paediatric percentiles.
- **Set B PCP verdict strength.** Scenario 7 ("IR indices add nothing once HDL-C is in the model", 25944628) and the "Moderate" label generalise from one postmenopausal-women cohort (no diabetes). The file itself lists this caveat but the verdict is stated more broadly.
- **Set A biostatistician Gast 2012:** rated Low-Moderate for association and Very low for prediction, consistent with the abstract. Set A PCP E3 states "association only", also consistent.
- **Set A endocrinologist:** ACT NOW HR ~0.28, IRIS HOMA-IR above 3.0, and PCOS guideline content are all tagged **[recall]**. Set B endocrinologist read the IRIS abstract and confirms HOMA-IR above 3.0 and HR 0.76.
- **Set A biostatistician Dennis 2019 (31047901)** mentions TZD benefit in the severe-IR cluster. Set B endocrinologist's description is age at diagnosis and renal function. Both agree simple features did as well or better.

### 3.5 Spot-check with PubMed (this analysis, not from memory)
PubMed `get_article_metadata` was run on 17363420, 18535197, 38851997, 38852583, 38869512, 12087016 and 12087010. Results:
- 38851997 is the EASL-EASD-EASO MASLD guideline in J Hepatol 2024; 38852583 is the same guideline in Obes Facts; 38869512 is the Executive Summary in Diabetologia. The abstract text is identical apart from wording, so no discrepancy between sets.
- 17363420 (Manley 2007, Clin Chem, 11 assays, 150 samples) and 18535197 (Manley 2008, Diabetes Care, 11 assays, 97 subjects, HOMA) are two separate papers. Both support the twofold-variation statements.
- 12087016 is the San Antonio Heart Study (Hanley 2002), with the adjusted OR 1.94 above, not IRAS.
- 12087010 is Bonora 2002, Verona Diabetes Complications Study (1,326 T2D, OR 1.56 per log unit incident CVD), matching Set A PCP's description.
No other citations were checked.

### 3.6 Flags for unverified, uncited and not-verified material
- **Set A endocrinologist:** every content statement is **[recall]** or **[opinion]**. IDs only were verified. First-author names for entries without a DOI are from memory.
- **Set B endocrinologist:** **[U]** items include DPP magnitudes (58%, 31%), PCOS IR-testing statement, hypoglycaemia practice, eGDR definition. Several items are "title only".
- **Set A scientist:** **[uncited]** for muscle dominance of the clamp, exogenous-insulin invalidity, renal C-peptide clearance, TG confounders, causal direction of hyperinsulinaemia, and gaps for PCOS, pulsatility, Adipo-IR, within-person CV, assay harmonisation.
- **Set B scientist:** **[uncited]** for "mostly hepatic" HOMA weighting, C-peptide negligible extraction, TG confounders, hyperinsulinaemia causality, clamp-GIR confounding.
- **Set A PCP:** **[PCP judgment, uncited]** in scenarios C, E, F, I and the referral statement. E10 (Jiao 2026 perspective) is "not verified in PubMed". E9 is existence only.
- **Set B PCP:** **[PCP judgment]** and **[not verified]** for PCOS guideline wording and paediatric cutoffs. Many items are "PMID not retrieved" (Consensus-only), including the hypertension HOMA-IR mortality cohort, Nutrients 2026 prevalence review, MJA FIB-4 consensus, Hivert 2015, GLP-1 RA/tirzepatide HOMA-IR effects. The "non-diabetogenic" hyperinsulinaemia genetics paper has no PMID.
- **Set A biostatistician:** `[C-only]` unresolved: Kitabchi 2005, Aroda 2019, Knowler 2025, Xing 2025, Torréns 2004, Trikudanathan 2013, Tian 2022, Ross 2015. Several `[V-cit]` items had abstracts unread, with claims from general knowledge.
- **Set B biostatistician:** Not retrieved: IRIS primary NEJM, Framingham/ARIC/MESA reclassification analyses. Consensus-only, not used: Vladu 2021, So 2020, Li 2025, Qiu 2025, the SGLT2i HOMA-IR study, a 2025 TyG C-statistic paper. All figures are from abstracts only.

---

## 4. Which set is more reliable, per role

| Role | More reliable | Why |
|---|---|---|
| Endocrinologist | **Set B** (modest margin) | Reads and quotes abstracts for IRIS, repeatability, transformation, and EASL. Tags every item V/U. Set A has the wider guideline and trial anchor set, but verifies only titles. Its content claims are mostly recall, and one recalled claim (Hanley) conflicts with the abstract. Use Set A's list as a source of leads; use Set B's numbers. |
| Scientist | **Set B** (modest margin) | Broader verified coverage (tissue discordance, extraction, pulsatility, ancestry, age, assays) with abstract-level detail and an explicit divergence-from-clamp table. Set A is stronger on compensation logic (Reaven, Kahn, Kodama) and C-peptide extraction, and states its bias and gap items well. Neither covers PCOS physiology with verified sources. |
| PCP | **Set B** | More scenarios (12 vs 9), more direct negative evidence (WHI, Stern), measurement studies, and explicit "Unclear" cases. Set A is more conservative on strength (mostly Low) and has fewer unread sources. Set B's "Moderate" grades and its use of unread ADA PMIDs overstate the evidence slightly. |
| Biostatistician | **Set A** (modest margin) | More primary prediction data (Framingham, ARIC, Wang 2022, Whitehall) and a clear list of unresolved identifiers. Set B has better recent meta-analytic evidence (TyG ΔC-index, NHANES) and inter-lab CV, but failed to retrieve IRIS and mis-attributes the 25% CV across four PMIDs. |

Overall caution: reliability ranking reflects documentation and retrieval depth in the files. Neither set is a systematic review. Both are purposive, abstract-level samples.

---

## 5. Bottom line
1. Routine IR measurement (HOMA-IR, fasting insulin, TyG, TG/HDL) has no verified decision-changing role in primary care, prediabetes, T2D, PCOS, MASLD or obesity.
2. Insulin and C-peptide testing is useful for hypoglycaemia/hyperinsulinism, lipodystrophy/severe IR and diabetes classification. This is not IR screening.
3. HOMA-IR adds little beyond glucose, HbA1c, BMI and lipids, and its precision (CV ~27-30%, ~twofold inter-assay variation) limits individual use.
4. Biggest gaps: IR-guided vs usual-care trials, ΔC/calibration/net-benefit for CVD, assay-harmonised and ethnicity-specific cutoffs, and the verbatim PCOS 2023 guideline text on IR testing.
5. IRIS shows pioglitazone helps IR-selected post-stroke patients, not that testing is needed.
