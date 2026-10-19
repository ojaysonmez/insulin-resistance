# Physiology of insulin resistance and what each IR measure captures
Role: physiology scientist. Scope: mechanism, measure-by-measure meaning, physiological limits. Coverage/reimbursement excluded.
Date: 2026-10-18.

## 0. Citation policy and verification status (read first)
- Every PMID/DOI below was retrieved from PubMed metadata in this session and the title/authors checked against the claim. Of the PMIDs I first recalled from memory, roughly half pointed to unrelated papers (e.g., a nerve-regeneration letter, a diabetes-prevalence paper) and were discarded. The skeptic should treat any citation not in this list as unverified.
- A statement marked **[uncited]** is mechanistic background or my reading of the field with no verified source in this report. It should be weighed accordingly.
- Preprints: none used.
- Not located/verified (gaps, no citation given): quantitative hepatic insulin extraction in humans; insulin pulsatility; insulin-assay harmonization data; day-to-day CVs of fasting insulin/HOMA-IR; Adipo-IR validation; hepatic-insulin-clearance reviews. Section 7 lists these.

## 1. Physiology in brief

**1.1 Insulin resistance is tissue- and pathway-specific, not one state.** Insulin acts mainly on skeletal muscle (glucose uptake/disposal), liver (suppresses glucose output, drives lipogenesis) and white adipose tissue (suppresses lipolysis). A detailed review organizes IR around these three tissues and stresses cross-talk, especially adipose lipolysis feeding hepatic gluconeogenesis (Petersen & Shulman, Physiol Rev 2018; PMID 30067154, doi:10.1152/physrev.00063.2017). The same review proposes bioactive lipids (diacylglycerol, ceramide, acylcarnitine) as candidate mediators and concludes some mediators remain scientifically controversial (same source).

**1.2 Compensation and its failure.** Reaven's account: most people with IGT/T2D are resistant to insulin-stimulated glucose uptake, and glucose tolerance is preserved only while the beta cell raises secretion to maintain hyperinsulinemia; decompensation occurs when it cannot (Reaven, Banting Lecture 1988; PMID 3056758, doi:10.2337/diab.37.12.1595). Same paper notes ~25% of non-obese people with normal OGTT are insulin-resistant, i.e. IR is not synonymous with dysglycemia. Insulin sensitivity and beta-cell response follow a hyperbolic (reciprocal) relationship in people with normal glucose tolerance, SI x beta-cell function ≈ constant (Kahn et al. 1993; PMID 8405710, doi:10.2337/diab.42.11.1663). Consequence: **insulin level alone, without a sensitivity-adjusted denominator, cannot distinguish "resistant but compensating" from "sensitive and low-secreting".** The hyperbola's position differs by ancestry: African and East Asian cohorts sit at different points than Caucasian cohorts (Kodama et al. 2013, systematic review/meta-analysis of 74 cohorts; PMID 23704681, doi:10.2337/dc12-1235).

**1.3 The ominous octet / multi-organ view.** DeFronzo's Banting Lecture places muscle, liver, adipose, beta cell and other organs in a multi-organ pathogenesis of T2D (PMID 19336687, doi:10.2337/db09-9028; abstract not available in PubMed, so I cite it only for the general multi-organ framing, from its MeSH/title).

**1.4 Selective IR and the triglyceride link.** In mouse models of T2D, insulin fails to suppress hepatic gluconeogenesis but continues to drive lipogenesis, producing hyperglycemia plus hypertriglyceridemia (Brown & Goldstein 2008; PMID 18249166, doi:10.1016/j.cmet.2007.12.009). This is a **mouse-derived** commentary. Petersen & Shulman offer an alternative explanation of "selective hepatic IR" (PMID 30067154). Relevance here: it is the mechanistic rationale for using triglycerides (TyG, TG/HDL) as IR proxies, but the mechanism is contested and species-limited.

**1.5 Hyperinsulinemia: effect or cause?** Czech (Nat Med 2017; PMID 28697184, doi:10.1038/nm.4350) reviews conflicting evidence on the timing of hyperinsulinemia, obesity and IR, and notes the sequence in humans is not settled. Practical implication for measurement: elevated fasting insulin may be a marker of IR, a contributor to it, or both; the measures below do not resolve this.

**1.6 Insulin clearance.** Circulating insulin is a function of secretion *and* clearance (largely hepatic first-pass). C-peptide is secreted equimolarly with insulin and is not extracted by the liver to any significant degree (Polonsky & Rubenstein 1984; PMID 6373457, doi:10.2337/diab.33.5.486; dog data showing negligible hepatic C-peptide extraction, Polonsky et al. 1984; PMID 6389599, doi:10.1172/JCI111601). The same 1984 review warns that the large, variable hepatic extraction of insulin is a major obstacle to quantifying secretion from insulin itself, and that the C-peptide:insulin ratio as a hepatic-extraction index was not experimentally validated. I did not verify human numeric extraction fractions **[uncited]**.

## 2. Measure-by-measure account

### 2.1 Hyperinsulinemic-euglycemic clamp (reference)
- Method: insulin infused to a plateau (~100 µU/ml in the original), glucose clamped at basal; at steady state glucose infusion rate equals whole-body glucose uptake and indexes tissue sensitivity to insulin (DeFronzo, Tobin, Andres 1979; PMID 382871, doi:10.1152/ajpendo.1979.237.3.E214).
- Captures: **whole-body, insulin-stimulated glucose disposal, dominated by skeletal muscle [uncited for the muscle-dominance statement; standard teaching]** at a supraphysiologic, fixed insulin level, with endogenous secretion suppressed. With a tracer it can also separate hepatic glucose production suppression (tritiated glucose is used in Matsuda & DeFronzo 1999, PMID 10480510, and Abdul-Ghani 2007, PMID 17192339).
- Does not capture: beta-cell function, hepatic insulin clearance, adipose antilipolytic sensitivity (unless FFA measured), fasting-state (basal) IR, or glucose-stimulated physiology. It is a snapshot at one dose; dose-response is not obtained from a single-dose clamp.
- Practicality: labor- and time-intensive; reserved for research (Muniyappa et al. 2008; PMID 17957034, doi:10.1152/ajpendo.00645.2007).

### 2.2 HOMA-IR (fasting glucose x fasting insulin / 22.5)
- Basis: a computer model of the basal glucose-insulin feedback loop; the formula is its approximation. Original validation: Spearman rs = 0.88 vs euglycemic clamp, but the authors state the low precision of the estimate (CV ~31% for IR) limits its use (Matthews et al. 1985; PMID 3899825, doi:10.1007/BF00280883).
- Captures: **basal (fasting) state, predominantly the hepatic glucose output/insulin balance under feedback** and the beta-cell set-point; a product of an insulin level that reflects secretion and clearance. It is a model-dependent steady-state estimate, not a direct measure of tissue insulin action **[mechanistic reading of Wallace et al. 2004; PMID 15161807, doi:10.2337/diacare.27.6.1487]**. Wallace et al. describe the model as hepatic and peripheral glucose efflux/uptake dependent on glucose and insulin, and caution about appropriate use: suitable for cohort/epidemiological studies, inappropriate for measuring beta-cell function in isolation, and primary input data must be robust.
- Agreement with clamp in a mixed cohort of 115 subjects: r = -0.82 overall, weighted kappa 0.63 for categorization into sensitivity classes (Bonora et al. 2000; PMID 10857969, doi:10.2337/diacare.23.1.57). Interpretation: good population-level correlation, but kappa 0.63 means substantial individual misclassification.
- Physiological caveats: (a) insulin assay dependence (Section 4.3); (b) as beta-cell failure advances, fasting insulin falls and HOMA-IR can understate IR **[uncited; follows from the HOMA model in PMID 15161807 being driven by insulin level]**; (c) not valid in insulin-treated patients (exogenous insulin) **[uncited]**.

### 2.3 QUICKI (1 / [log I0 + log G0])
- A log-transform of the same two fasting inputs. Correlated r = 0.78 with clamp-derived SI in the derivation sample (n = 56 incl. nonobese, obese and T2D), better than minimal-model SI vs clamp (r = 0.57) (Katz et al. 2000; PMID 10902785, doi:10.1210/jcem.85.7.6661).
- Captures the same physiology as HOMA-IR (fasting, hepatic-weighted); differs mainly in mathematical behavior (log transform reduces skew). **QUICKI and HOMA-IR carry essentially the same information and should not be treated as independent confirmations.** Muniyappa et al. argue QUICKI is robust and reproducible and has been extensively validated against the clamp (PMID 17957034); note the senior authors of that review (Quon) are QUICKI's originators, a potential favorable bias.

### 2.4 Matsuda index (OGTT-derived)
- Formula: 10,000/√[(fasting G x fasting I) x (mean G x mean I over OGTT)]. r = 0.73 with clamp glucose disposal in 153 subjects (NGT, IGT, T2D) (Matsuda & DeFronzo 1999; PMID 10480510, doi:10.2337/diacare.22.9.1462). The same paper showed that the earlier approach of mean glucose divided by mean insulin had no correlation with clamp (r = -0.02).
- Captures: **a composite of fasting (hepatic) and post-load (peripheral/muscle) insulin sensitivity**, i.e., a dynamic test with physiological (not supraphysiologic) insulin concentrations; also influenced by gastric emptying, incretin effect and hepatic insulin extraction **[uncited]**.
- Muscle vs liver separation from OGTT: Abdul-Ghani et al. 2007 derived a hepatic IR index (glucose and insulin AUC 0-30 min product; r = 0.64 vs hepatic IR index from clamp/tracer) and a muscle index (dG/dt / mean insulin; r = 0.78 vs clamp) in 155 Mexican-American subjects (PMID 17192339, doi:10.2337/dc06-1519). Derived in one ethnic group without NGT/T2D mix and later contested in a letter (PMID 17596506). In a secondary analysis of 156 postmenopausal overweight/obese women applying those formulas, "liver IR" was associated with more dysglycemia, visceral fat and liver fat index than "muscle IR" (Elisha et al. 2017; PMID 27931981, doi:10.1016/j.ando.2016.10.003). Cross-sectional, one population, formulas not independently validated.

### 2.5 OGTT insulin (fasting, 2-h, curve shape)
- Captures: insulin secretory response to a glucose challenge relative to the glucose level achieved, i.e., **the combination of insulin sensitivity (muscle/liver), incretin-modulated secretion and hepatic clearance**. By the hyperbolic relationship (Kahn 1993; PMID 8405710), a given insulin response is interpretable only relative to sensitivity.
- Limits: single-time insulin concentrations are a poor stand-alone index; Matsuda & DeFronzo 1999 show that naive glucose/insulin ratios failed (PMID 10480510). I found no verified source in this session on curve-shape phenotypes (e.g., delayed peak) predicting outcomes **[uncited gap]**.

### 2.6 C-peptide
- Captures **secretion** (equimolar with insulin, little hepatic extraction; PMID 6373457, 6389599), not sensitivity. Fasting C-peptide is high in compensated IR and falls with beta-cell failure, so it identifies the compensation state rather than IR per se **[mechanistic inference]**.
- Complications: C-peptide has a longer half-life than insulin, which complicates ratio interpretation (PMID 6373457); renal clearance matters, so renal impairment raises it **[renal clearance: uncited here; the 1984 review lists kidney disease among its MeSH topics but I did not verify the content]**.
- Its relative advantage is for the **insulin-versus-clearance confound**: because it escapes hepatic first-pass, it separates hypersecretion from reduced clearance, which fasting insulin cannot.

### 2.7 TyG index (ln[fasting TG (mg/dL) x fasting glucose (mg/dL) / 2])
- Derivation/validation: r = -0.681 with clamp M-value in 99 Mexican adults, best cutoff 4.68 (sensitivity 96.5%, specificity 85.0%, AUC 0.858) (Guerrero-Romero et al. 2010; PMID 20484475, doi:10.1210/jc.2010-0288). Relatively small, single-ethnicity, and the cutoff was derived and evaluated in the same sample.
- Systematic review: 15 studies, 69,922 participants, quality low to moderate; AUC 0.59-0.88; cutoffs variable; authors call for standardized cutoffs and further validation (Sánchez-García et al. 2020; PMID 32256572, doi:10.1155/2020/4678526).
- Physiological meaning: TG is a **hepatic VLDL output/lipolysis-linked marker**, glucose a basal glucose-regulation marker. Plausible link: adipose and hepatic IR raise FFA flux and VLDL-TG synthesis (Petersen & Shulman, PMID 30067154). TyG therefore reflects a **hepatic/adipose-weighted, lipid-glucose phenotype**, not muscle glucose disposal directly. It is also moved by diet, alcohol, fasting duration, genetics of TG, and lipid-lowering/glucose-lowering drugs **[uncited]**. Because it needs no insulin assay, it avoids assay variability, which is its main practical (not physiological) advantage.

### 2.8 TG/HDL-C ratio
- In 258 non-diabetic overweight volunteers (insulin suppression test as reference), TG, TG/HDL-C ≥ ~3.0 (traditional units), and insulin were the best markers; sensitivity/specificity for the TG/HDL cut-point were 64%/68% (McLaughlin et al. 2003; PMID 14623617, doi:10.7326/0003-4819-139-10-200311180-00007). Performance was similar to ATP III metabolic syndrome criteria. Note: the sensitivity/specificity pairing in the abstract is listed for TG, ratio, insulin in order (67/64/57 and 71/68/85); I read the ratio as 64% sensitivity, 68% specificity.
- Ethnic dependence: in 1,452 obese youths (612 white, 357 Hispanic, 483 African American; clamp in 146), TG/HDL-C related to IR mainly in white youths; in Hispanic and African American youths the ROC AUC was non-significant and no cutoff could be set (Giannini et al. 2011; PMID 21730284, doi:10.2337/dc10-2234). Physiological reading: African American populations tend to have lower TG at a given degree of IR **[stated by the cited paper's finding only as non-significant ROC; the mechanism is uncited]**.
- Captures: same hepatic/adipose-weighted lipid phenotype as TyG, without glucose.

## 3. Table: measure → physiology reflected

| Measure | State | Tissue/axis weighted | Needs insulin assay | Key confounds | Evidence of agreement with clamp (verified) |
|---|---|---|---|---|---|
| Euglycemic clamp | Stimulated, steady state (supraphysiologic insulin) | Whole-body glucose disposal (muscle-dominant, uncited); hepatic with tracer | n/a (insulin infused) | Single dose, technical expertise | Reference (PMID 382871) |
| HOMA-IR | Fasting steady state | Hepatic/basal feedback loop; secretion + clearance | Yes | Assay, beta-cell failure, exogenous insulin | rs 0.88 (3899825); r -0.82, kappa 0.63 (10857969) |
| QUICKI | Fasting | Same as HOMA-IR | Yes | Same | r 0.78 (10902785) |
| Matsuda | Fasting + post-load OGTT | Composite hepatic + peripheral | Yes (multiple samples) | Incretins, gastric emptying, clearance | r 0.73 (10480510) |
| OGTT-derived muscle/liver indices | Post-load | Claimed separation muscle vs liver | Yes | Derived in one cohort | muscle r 0.78, liver r 0.64 (17192339) |
| OGTT insulin curve | Stimulated | Secretion relative to sensitivity | Yes | No sensitivity adjustment | none verified |
| C-peptide | Fasting or stimulated | Beta-cell secretion (not extracted by liver) | No (C-peptide assay) | Renal function, half-life | n/a: a secretion marker |
| TyG | Fasting | Hepatic/adipose lipid-glucose phenotype | No | Diet, drugs, TG genetics, ethnicity | r -0.68; AUC 0.59-0.88 across studies (20484475; 32256572) |
| TG/HDL-C | Fasting | Hepatic/adipose lipid phenotype | No | Ethnicity, drugs, diet | Se 64%/Sp 68% (14623617); non-significant AUC in Hispanic/Black youths (21730284) |

## 4. Where physiology limits clinical use

**4.1 Fasting indices answer a different question than the clamp.** Clamp = insulin-stimulated disposal at a fixed high insulin. HOMA/QUICKI = a basal feedback set-point. Correlations of 0.7-0.9 in mixed populations reflect between-person spread (obese vs lean, T2D vs NGT), and do not guarantee agreement within a narrow clinical range (inference from the validation designs: PMID 10857969, 10902785).

**4.2 Individual-level precision is low.** The original HOMA paper reports CVs of ~31% for IR estimates (PMID 3899825). Kappa 0.63 against the clamp categories (PMID 10857969) means roughly a third of individuals can be placed in different classes. **No verified source on within-person day-to-day variability of fasting insulin was found this session [gap].**

**4.3 Insulin assay.** Radioimmunoassay vs automated microparticle enzyme immunoassay gave different insulin values, attributed to proinsulin cross-reactivity in the RIA; the MEIA had lower day-to-day variability (Rood et al. 1999, n = 30 obese subjects; PMID 11474834, doi:10.1089/152091599317017). Proinsulin proportion is increased in diabetes and obesity, so assay choice can bias insulin-based indices differently in different patients. McLaughlin et al. explicitly note the absence of a standardized insulin assay when proposing cut-points (PMID 14623617). Hence **no universal HOMA-IR/QUICKI cutoff is physiologically defensible; cutoffs are assay- and population-specific.** I did not verify current harmonization status **[gap]**.

**4.4 Pulsatile secretion and sampling.** Insulin is secreted in pulses and a single fasting draw samples one point **[uncited; no verified source found]**; averaging multiple draws would reduce noise but is not routine practice.

**4.5 Hepatic extraction.** Insulin concentrations in peripheral blood are shaped by variable hepatic extraction (PMID 6373457). Reduced hepatic clearance can itself raise fasting insulin without increased secretion or greater resistance; C-peptide helps disentangle this.

**4.6 Ancestry, age, sex.** Equal insulin sensitivity maps to different insulin responses across ethnic groups (PMID 23704681), so fixed insulin-based thresholds will misclassify across groups. TG/HDL-C has ancestry-dependent validity (PMID 21730284). Age: I found no verified source this session on age effects **[gap]**.

**4.7 Heterogeneity of "IR".** Tissue-specific patterns (hepatic vs muscle vs adipose) exist (PMID 17192339, 27931981, 30067154). Data-driven clustering of newly diagnosed diabetes using HOMA2-IR, HOMA2-B, BMI, age, HbA1c and GAD antibodies identified a severe insulin-resistant cluster with higher risk of diabetic kidney disease (Ahlqvist et al. 2018; PMID 29503172, doi:10.1016/S2213-8587(18)30051-2). This shows HOMA2-IR can contribute to subphenotyping in T2D; it is a registry cluster analysis and does not prove that measuring IR changes management.

## 5. By condition (mechanism only; clinical utility is for other teammates)
- **Prediabetes/T2D:** IR plus declining compensation. The disposition-style relationship (PMID 8405710) means that interpreting IR requires secretion context. Tissue-level patterning matters for drug mechanism (e.g., hepatic vs peripheral) but I did not verify drug-mechanism citations here.
- **MASLD/NAFLD:** hepatic fat accumulation is linked to hepatic IR and lipid signaling (PMID 30067154); in one cohort, estimated liver IR was associated with higher liver fat index (PMID 27931981). Causal direction between liver fat and IR is not settled by these data.
- **PCOS:** physiology likely involves IR with hyperinsulinemia, but I have **no verified citation** for PCOS in this report **[gap]**.
- **Hypertension/cardiometabolic clustering:** Reaven proposed IR/hyperinsulinemia as shared substrate; the rat fructose model supports plausibility only (PMID 3056758). Plausible mechanistically, not shown here to matter for clinical decision-making.

## 6. Where a mechanistic argument is plausible but not shown to matter clinically
1. Hyperinsulinemia as a *cause* of obesity/disease (PMID 28697184 says timing is unresolved).
2. TG as a surrogate for hepatic selective IR (rests on mouse work, PMID 18249166, with a competing explanation, PMID 30067154).
3. OGTT-derived "liver vs muscle IR" for choosing therapy (PMIDs 17192339, 27931981: derivation/cross-sectional only).
4. Any claim that treating a number on a surrogate IR index improves outcomes: nothing in the physiology sources above tests this.

## 7. Key uncertainties and gaps for the skeptic
- No verified evidence in this report on within-person variability, assay harmonization state, pulsatility, age effects, PCOS, Adipo-IR, or numeric hepatic insulin extraction. These need either a follow-up search by the biostatistician/endocrinologist or should be stated as unknowns.
- The clamp itself is a muscle/whole-body reference at a high insulin dose; surrogate "agreement with clamp" does not equal "measures hepatic or adipose IR".
- Validation samples are small and often single-ethnicity (TyG: Mexican, n=99; Abdul-Ghani: Mexican-American, n=155).
- Reviews I cite (Muniyappa) include authors who originated the index they praise.
- DeFronzo 2009 (PMID 19336687) is cited only for framing; its abstract was not retrievable.

## 8. Reference list (all PMIDs checked against PubMed metadata this session)
1. DeFronzo RA, Tobin JD, Andres R. Am J Physiol 1979. PMID 382871. doi:10.1152/ajpendo.1979.237.3.E214
2. Matthews DR et al. Diabetologia 1985. PMID 3899825. doi:10.1007/BF00280883
3. Katz A et al. JCEM 2000. PMID 10902785. doi:10.1210/jcem.85.7.6661
4. Matsuda M, DeFronzo RA. Diabetes Care 1999. PMID 10480510. doi:10.2337/diacare.22.9.1462
5. Bonora E et al. Diabetes Care 2000. PMID 10857969. doi:10.2337/diacare.23.1.57
6. Wallace TM, Levy JC, Matthews DR. Diabetes Care 2004. PMID 15161807. doi:10.2337/diacare.27.6.1487
7. Muniyappa R et al. Am J Physiol Endocrinol Metab 2008. PMID 17957034. doi:10.1152/ajpendo.00645.2007
8. Abdul-Ghani MA et al. Diabetes Care 2007. PMID 17192339. doi:10.2337/dc06-1519
9. Bastard JP et al. (letter) Diabetes Care 2007. PMID 17596506. doi:10.2337/dc07-0622
10. Elisha B et al. Ann Endocrinol 2017. PMID 27931981. doi:10.1016/j.ando.2016.10.003
11. Polonsky KS, Rubenstein AH. Diabetes 1984. PMID 6373457. doi:10.2337/diab.33.5.486
12. Polonsky KS et al. J Clin Invest 1984. PMID 6389599. doi:10.1172/JCI111601
13. Kahn SE et al. Diabetes 1993. PMID 8405710. doi:10.2337/diab.42.11.1663
14. Kodama K et al. Diabetes Care 2013. PMID 23704681. doi:10.2337/dc12-1235
15. Reaven GM. Diabetes 1988. PMID 3056758. doi:10.2337/diab.37.12.1595
16. DeFronzo RA. Diabetes 2009. PMID 19336687. doi:10.2337/db09-9028
17. Petersen MC, Shulman GI. Physiol Rev 2018. PMID 30067154. doi:10.1152/physrev.00063.2017
18. Brown MS, Goldstein JL. Cell Metab 2008. PMID 18249166. doi:10.1016/j.cmet.2007.12.009
19. Czech MP. Nat Med 2017. PMID 28697184. doi:10.1038/nm.4350
20. Guerrero-Romero F et al. JCEM 2010. PMID 20484475. doi:10.1210/jc.2010-0288
21. Sánchez-García A et al. Int J Endocrinol 2020. PMID 32256572. doi:10.1155/2020/4678526
22. McLaughlin T et al. Ann Intern Med 2003. PMID 14623617. doi:10.7326/0003-4819-139-10-200311180-00007
23. Giannini C et al. Diabetes Care 2011. PMID 21730284. doi:10.2337/dc10-2234
24. Rood JC et al. Diabetes Technol Ther 1999. PMID 11474834. doi:10.1089/152091599317017
25. Ahlqvist E et al. Lancet Diabetes Endocrinol 2018. PMID 29503172. doi:10.1016/S2213-8587(18)30051-2

Bergman RN et al. 1979 minimal model (PMID 443421, doi:10.1152/ajpendo.1979.236.6.E667) was verified but only used as context for the minimal-model comparator in Katz 2000.
