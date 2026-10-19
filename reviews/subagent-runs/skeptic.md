# Skeptic review: clinical utility of insulin resistance (IR) measurement (Set B)

Role: ir-skeptic. Reviewed: ir-endocrinologist.md, ir-scientist.md, ir-pcp.md, ir-biostatistician.md. No other files in ir-team/ were read. Coverage and reimbursement are out of scope. Date of run: 2026-10-18.

## 0. Method and tool status

- **Scholar Sidekick failed.** `auditBibliography` and `verifyCitation` both returned "You are not subscribed to this API." I fell back as instructed.
- **Identity checks (fallback).** I retrieved PubMed metadata (title, first author, year, journal, DOI) for about 75 PMIDs. These covered every PMID the four reports use for a numeric or load-bearing claim, plus most of the supporting ones. I compared each against the report's description. **No fabricated, mismatched or wrong-year citations were found.** Every PMID resolved to the stated title, first author and year.
- **Retraction checks (fallback).** I queried the Crossref `updated-by` field for about 65 DOIs. **No retractions and no expressions of concern.** Two corrections turned up on the EASL-EASD-EASO MASLD guideline (a correction notice on the Diabetologia version, doi 10.1007/s00125-024-06196-3, and an erratum on the Obesity Facts version, doi 10.1159/000539371). Neither is a retraction. Caveat: Crossref `updated-by` is less complete than the Retraction Watch database, so "none found" is not a guarantee.
- **Primary text read, not just abstracts.**
  - 2023 International PCOS Guideline, full text (PMC10505534).
  - EASL-EASD-EASO MASLD 2024 guideline, full text (PMC11299976).
  - AASLD 2023 NAFLD guidance, full text (PMC10735173), searched for IR content.
  - Liu 2022 TyG meta-analysis, full text (PMC9250255).
  - Abstracts for all the load-bearing cohort and trial papers: Kernan, Spence, Viscoli, Hu, Schmiegelow, Poon, Carobene, Stern, Dennis, Gast, Isokuortti, Che, Liu 2026, Xu, Guerrero-Romero, McLaughlin, Sumner, Bonora, Luo, Brown, Tahapary and others.
- **Not done.** I did not verify claims marked [U] or "not retrieved" that no report supports with a source (for example DPP-independent claims about guideline practice for obesity drugs). I ran two quick PubMed searches for IR-stratified treatment RCTs. The connector returned noisy results and nothing usable, so absence of such a trial here is again only "not found".
- **Citation-count caveat.** The reports cite several 2025-2026 papers (Liu 2026 in Front Cardiovasc Med, Xu 2026 in Clinics, Glynn 2026, Lambadiari 2026). They resolve in PubMed and Crossref, but they have had no time to be tested or replicated. The biostatistician's "prediction is negative" case leans on two of them.

## 1. Ranked problems

### P1 (High): The EASL MASLD guideline is mischaracterised by two reports, because only the abstract was read

- **Claims.**
  - Endocrinologist: "IR measurement is not in the stated algorithm", and "Evidence strength: high that fibrosis staging, not IR, drives management".
  - PCP, scenario 6: "Don't test IR ... None. IR does not alter FIB-4 pathway".
- **Check against the source.** The EASL-EASD-EASO 2024 full text contains a recommendation under the question "Is the assessment of metabolic abnormalities (e.g. insulin sensitivity/resistance) useful for risk stratification or management of adults with MASLD?" It reads: "Assessment of insulin resistance (... using HOMA-IR or estimates derived from the oral glucose tolerance test) may be considered to clarify metabolic dysfunction in adults with (suspected) MASLD and without an established diagnosis of type 2 diabetes." Consensus agreement was 92%. The text also says "interpretation of HOMA-IR and Adipo-IR requires standardised measurement of insulin and/or C-peptide". HOMA-IR also appears in the guideline's comorbidity work-up table. The evidence grade was not captured in the text I extracted.
- **Why it matters.** Both reports said they read abstracts only, but stated the absence of IR as fact. The accurate position is that a major guideline gives IR assessment a permissive "may be considered" recommendation. Its stated purpose is to "clarify metabolic dysfunction", not to change fibrosis work-up or therapy. That still supports "no demonstrated management change", but it contradicts "not in the guideline".
- **The "high" grade is also wrong in kind.** Absence of IR from an algorithm is not evidence about IR. Evidence strength for a negative claim should be "not tested", not "high".
- **Fix.** Report the recommendation as stated, with its wording and 92% agreement. Treat "IR does not change MASLD management" as plausible but unproven. AASLD 2023 (full text) has no HOMA or IR-measurement content, so its silence is real.

### P2 (High): The endocrinologist's "clinically actionable niches" are not supported as test-driven decisions

The endocrinologist lists four niches. Checked against sources:
1. **Lipodystrophy / severe IR.** The cited guideline (Brown 2016) states: "diagnosed by clinical phenotype, supplemented by genetic testing". The abstract contains no recommendation to measure insulin or IR for diagnosis or monitoring. The claim "marked hyperinsulinaemia supports diagnosis and monitoring" is tagged [U] and is not in the cited source. The evidence grade "moderate" is also inconsistent with the report's own statement that the guideline is "largely expert opinion". It should be low.
2. **Pioglitazone selection.** IRIS used HOMA-IR >3.0 as an entry criterion (Kernan 2016, verified). See P3 for why this is not test-and-treat evidence.
3. **Hypoglycaemia / hyperinsulinism work-up.** The report itself says this is hypersecretion, "a different question from IR". It is not an IR niche and should be dropped from the count.
4. **Risk-stratification adjunct.** This is the claim the other three reports contradict (P4).

Net: after removing the non-IR niche and the unverified lipodystrophy use, the only verified niche is the IRIS entry criterion.

### P3 (High): IRIS is treated as the "decision-impact" anchor but cannot carry it

Verified from the abstracts (Kernan 2016, Viscoli 2014, Spence 2019):
- IRIS enrolled only non-diabetic stroke/TIA patients with HOMA-IR >3.0. All were IR-selected. There is no non-IR comparator, so IRIS cannot show that IR status predicts benefit. The endocrinologist makes this point, and it is correct.
- Absolute effect: primary outcome 9.0% vs 11.8% over 4.8 years (HR 0.76, 0.62-0.93). By my arithmetic that is an absolute risk reduction of 2.8 points, NNT about 36 over 4.8 years. This is a benefit with weight gain >4.5 kg in 52% vs 34%, oedema 36% vs 25%, and fracture needing surgery or hospitalisation 5.1% vs 3.2%. None of the reports states the NNT or sets benefit against these harms.
- Spence 2019 (verified): benefit was shown in prespecified subgroups defined by fasting glucose and HbA1c (prediabetes, ITT HR 0.70, 0.56-0.88). This points to glycaemic category as a possible substitute selector. The paper's own text says "insulin resistance is not commonly measured in clinical practice".
- The entry threshold of 3.0 sits well above reported adult upper limits of normal (1.9-2.35; Isokuortti, Matli). With within-person CV about 27-30% and inter-laboratory CV about 25% (all verified), a patient near 3.0 would often fall on either side of the cut-off on repeat or at another lab. A threshold from a trial protocol is not a validated clinical decision rule (the biostatistician says this).
- Biostatistician says the IRIS primary result was "not retrieved". The endocrinologist did retrieve it (PMID 26886418, verified here). Minor inconsistency.

### P4 (Medium-High): Role conflict on prognostic evidence

- Endocrinologist: "IR as prognostic marker (CV, diabetes): moderate".
- Biostatistician and PCP: no incremental prediction beyond glucose, HbA1c, BMI, HDL-C.
- The disagreement is mostly about words. "Prognostic" in the endocrinologist's report rests on association meta-analyses (Ding 2021; Liu 2022). Those do not show prediction or reclassification. The word "moderate" should be limited to "association".
- Even the association is weaker than "moderate" for composite outcomes. Liu 2022 (full text read) rated CAD as moderate certainty (3 studies, 30,054 people), but CVD, MI, CV mortality and all-cause mortality as very low. It found **no association** of TyG with CV mortality (HR 1.10, 0.82-1.47) or all-cause mortality (HR 1.08, 0.92-1.27). The endocrinologist cites this paper only by title and the pooled ASCVD result from Ding (HR 1.61), and does not mention the null mortality findings. PCP states the GRADE pattern correctly.
- Che 2023 (UK Biobank, n=403,335): highest-quartile HR for TyG only 1.19 (TG/HDL-C 1.29), with 45.8% of the TyG association mediated by dyslipidaemia, 27.0% by diabetes, 15.0% by hypertension. The PCP's point that the signal is mostly carried by variables already measured is supported.

### P5 (Medium): The negative-prediction evidence base is narrower than the reports' ratings suggest

The PCP calls the "don't test" verdict "moderate" and the biostatistician rates Hu 2024 and Liu 2026 "Moderate". The evidence is:
- Hu 2024 (verified): 5,578 people, 94.7% male, one Japanese occupational cohort, 10-year horizon, internal validation only. HOMA-IR and HOMA-beta added nothing beyond HbA1c plus BMI. FPG added to AUC (0.79 to 0.84). Because HOMA-IR is computed from fasting glucose, it is partly mathematically coupled to FPG. The test of insulin's own contribution is model 4 (FPG plus HOMA terms). That also showed no material gain, so the finding holds, but only in this population.
- Schmiegelow 2015 (verified): 15,288 postmenopausal women without diabetes. Association disappeared after HDL-C adjustment. HDL-C is itself a component of the IR phenotype, so this shows redundancy with a routinely measured lipid, not that IR carries no information. For the question "does an insulin assay add anything", the conclusion stands.
- Liu 2026 (verified): TyG added to Framingham gave a pooled C-index gain of 0.0004 (-0.0092 to 0.0100) from five cohorts, GRADE very low, and the result was "heavily influenced" by one cohort. This is TyG, not HOMA-IR. The biostatistician's own text calls the extrapolation to HOMA-IR "Low" but still rates the row "Moderate".
- Xu 2026 (verified): NHANES, no C-statistic gain from TyG or HOMA-IR. HOMA-IR had a lower subdistribution hazard for CVD mortality, a J-shape consistent with reverse causation.
- So the honest statement is: **no study shows HOMA-IR adds to a model containing glucose, HbA1c, BMI and lipids, and the few tests done were negative, but they are few and narrow**. "Moderate" overstates this. "Low (consistent, but few and non-representative)" is fairer. This does not rescue the case for utility; absence of positive evidence remains.

### P6 (Medium): Source wording vs report wording

- Biostatistician on Bonora 2000: "kappa 0.63 means substantial misclassification at category level". The source abstract says "good agreement ... in the categorization (weighted k = 0.63)". Conventionally kappa 0.61-0.80 is "substantial agreement". The biostatistician's gloss reverses the tone of the source. Whether 0.63 is adequate for a clinical threshold is an open question, but the report should say that the authors called it good and the reviewer considers it inadequate.
- Scientist's "Best cited discrimination figures: TyG vs clamp AUC 0.86 (PMID 20484475)". The 0.858 AUC and the 96.5%/85.0% sensitivity/specificity come from an in-sample optimal cut-off in n=99 (verified). The biostatistician's cited systematic review (Sanchez-Garcia 2020: 15 studies, AUC 0.59-0.88, low-to-moderate quality) shows 0.86 is near the top of the range. The scientist presents the top of the range as "best cited".
- Scientist cites Chavez 2009 (PMID 19487637) for "the clamp primarily reflects muscle". That is a parenthetical in an FGF-21 paper at one insulin dose. The wording matches, but it is a weak source for a foundational claim. Better primary sources exist (and the scientist cites the Abdul-Ghani 2008 tracer clamp paper nearby).
- Scientist labels "HOMA-IR mostly hepatic" as [uncited], which is honest. But it sits uneasily with the biostatistician's verified HOMA-vs-clamp correlation (Bonora r = -0.82), because the clamp is mostly muscle. The two claims are not reconciled.
- Endocrinologist on PCOS: the report paraphrases the guideline as "available tests are not clinically validated in PCOS" ([U], marked to verify). The actual text (verified, below) says assays are "of limited clinical relevance", and the summary says routine measures are "inaccurate". The conclusion is the same, the paraphrase is looser.

### P7 (Medium): Cross-role gaps and inconsistencies that did not change conclusions

- Scientist: "I have no retrieved paper quantifying within-person CV of HOMA-IR." The other three all cite Poon 2018 (CV 30.4%, ICC 0.70, MDC95 2.3, verified) and PCP also cites EuBIVAS (Carobene 2024: HOMA-IR within-subject CV 26.7% in 90 non-diabetic adults, ten weekly samples, verified). The physiology memo missed a key measurement-limit paper.
- Poon also reports TG/HDL-C ICC 0.80, CV 23.0% (verified), better than HOMA-IR. The scientist's later table lists TG/HDL-C without this repeatability advantage. EuBIVAS also reports QUICKI CV 4.1%, but that low figure comes from the log transform and does not mean QUICKI is more informative. No report claims otherwise.
- Endocrinologist's Dennis 2019 summary ("simple features predicted progression as well as or better") is accurate. It omits the abstract's finding that the severe insulin-resistant cluster showed particular benefit from thiazolidinediones. The same abstract also says simple clinical features outperformed clusters for selecting therapy. So the omission matters only for completeness, and the net message (IR clusters add nothing beyond age, BMI, HbA1c, eGFR) is correct.
- McLaughlin 2003 (cited by the scientist): TG/HDL-C 3.0 gave sensitivity 64% and specificity 68% (verified). Insulin itself at its best cut-off gave sensitivity 57%, specificity 85% against the insulin suppression test. So fasting insulin was not clearly superior to triglycerides, a point nobody makes.

## 2. PCOS guideline: previously unverified claim now verified from primary text

Both the endocrinologist ([U]) and PCP ("not verified") left the 2023 PCOS guideline's IR statement unconfirmed. In the full text (Teede 2023, J Clin Endocrinol Metab, PMC10505534):
- Practice point 1.9.12: "Insulin resistance is a pathophysiological factor in PCOS; however, clinically available insulin assays are of limited clinical relevance and are not recommended in routine care."
- Practice point 3.1.10: "...should not be used in routine care."
- Guideline summary: "routinely available measures of insulin resistance are inaccurate and clinical measurement is not currently recommended."
- Both are labelled PP (practice points, consensus-level, not graded evidence). Metformin is recommended for adults with BMI ≥25 for outcomes "including insulin resistance", with no IR measurement or threshold required.
- Conclusion: the endocrinologist's and PCP's "don't measure IR in PCOS" is **confirmed**, but as a consensus practice point. It is not evidence of no utility; it reflects absent validated assays and absent outcome data.

## 3. Claims that survived scrutiny

1. **Measurement is noisy and non-transferable.** Poon 2018 (CV 30.4%, MDC95 2.3), EuBIVAS (CV 26.7%), Isokuortti 2017 (inter-lab CV 25%; a Helsinki 2.0 read 1.3-2.1 elsewhere), Matli 2021 (assay-specific intervals, 97.5th percentile 2.35 in the strictest group), Marcovina 2007 and the ADA 1996 task force (among-assay disagreement, a common standard did not fix it). All verified, consistent across all four reports.
2. **No universal HOMA-IR cut-off.** Tahapary 2022 (narrative review; verified wording: "high degree of variability", varies by age, sex, race); Shashaj 2015 and the other cut-off papers. Strong and consistent, though several supporting papers are small single-centre studies.
3. **Correlation with the clamp is not utility.** Rudvik 2018 verified: HOMA-IR, QUICKI and FIRI are one-to-one transformations and correlation alone is insufficient.
4. **Mechanistic ambiguity of insulin-based indices** (secretion vs clearance; ethnic differences in hepatic extraction: Osei 1997, 25-52% lower in West African ancestry; Hansen 1993 in monkeys; DeFronzo 2014 disposition-index pitfall). All verified. These are physiology, not utility, but they limit interpretation.
5. **Diabetes subtyping.** Dennis 2019: simple clinical features beat IR-defined clusters. Verified.
6. **Prediabetes management is driven by glycaemia and lifestyle.** DPP/DPS (58% and 31% reductions; verified in the DPP abstract) enrolled by glucose criteria, not IR.
7. **PCOS: do not measure IR in routine care** (see section 2).
8. **Absence of decision-impact evidence.** None of the four reports, and none of my targeted searches, found an RCT or decision-curve analysis in which measuring IR improved outcomes. This is a gap rather than proof of no benefit.

## 4. What evidence would change my view

- A test-and-treat RCT (IR-guided vs usual care) with hard outcomes, or a pre-registered incremental-value study with calibration, decision curves and external validation in at least two diverse cohorts.
- IRIS-like analysis showing that benefit varies by baseline HOMA-IR within a population that includes non-IR participants, or a head-to-head showing HOMA-IR selects responders better than glucose/HbA1c categories.
- Harmonised insulin assays with traceable reference materials and ethnicity-specific reference intervals (the endocrinologist notes the LC-MS/MS interlab work, but no bias figures were retrieved).
- A verified guideline recommendation tying an IR measurement to a specific management change (the EASL "may be considered" recommendation links to "clarify metabolic dysfunction", not to a management change).

## 5. Verdict

**The case that measuring IR (fasting insulin, HOMA-IR, TyG and similar) has demonstrated clinical utility is weak.**

- **Association with outcomes:** consistent, mostly modest, and largely carried by glucose, lipids and blood pressure. Moderate for CAD, very low or null for several other outcomes (Liu 2022).
- **Incremental prediction beyond routine variables:** not shown, with a few negative studies that are narrow and few in number.
- **Decision impact:** not shown. The only RCT using an IR threshold (IRIS) tests a drug in a selected group (NNT about 36 over 4.8 years, with weight gain, oedema and fracture harms), not the test.
- **Measurement quality:** a single HOMA-IR is imprecise (within-person CV about 27-30%, inter-lab CV about 25%) and uses non-transferable cut-offs.
- **Guideline stance:** explicit "do not measure" for PCOS (practice point); permissive "may be considered" for MASLD without T2D; no IR-measurement role found in AASLD 2023.
- **Residual plausible niches:** IRIS-type pioglitazone selection and severe IR syndromes. Neither is shown to require an IR measurement over simpler selectors.

Strength of the case for clinical utility of routine IR measurement: **about 10-15% of what would be needed to recommend it**. Confidence in the verdict "utility not demonstrated; not recommended for routine use": **about 85%**. The remaining 15% is the possibility that unreported trials, newer guidelines or assay-harmonised data would show decision-relevant value. I did not find any, but this review used targeted rather than systematic searches.
