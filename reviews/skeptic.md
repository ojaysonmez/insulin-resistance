# Skeptic review: clinical utility of insulin resistance (IR) measurement

Reviewer: ir-skeptic session. Date: 2026-10-18. Scope: the four reports in this folder (endocrinologist, scientist, PCP, biostatistician). Coverage and reimbursement are out of scope.

## 0. How this review was done, and a tooling failure

- **Scholar Sidekick did not work.** `verifyCitation`, `checkRetraction` and `auditBibliography` returned "Too many requests" on the first try and then "You are not subscribed to this API" on every later try. The role file asks for these tools, so this is a gap in my process, not a clean result.
- **What I did instead (same checks, different tools):**
  - *Identity check.* I fetched the PubMed record for about 70 PMIDs (all load-bearing ones across the four reports) and compared the returned title, first author, journal and year with what each report claims. This is the same title-vs-record test that `verifyCitation` performs.
  - *Retraction check.* I queried the Crossref API (`updated-by` field, which is the source Scholar Sidekick uses) for 33 DOIs: IRIS, Wilson, Hu, Gast, Wang, Dennis, Tabak, Bonora 2000 and 2002, Manley 2007 and 2008, Carobene, Poon, Guerrero-Romero, Simental-Mendia, Rosli, Hanley, Teede, Wagner, Ahlqvist, Matli, Lee, Horáková, ACT NOW, Schmidt, USPSTF, Peña, Matthews, Matsuda, Katz, DPP and Moghetti. **None has a retraction, correction or expression of concern.** Crossref can lag Retraction Watch; I did not check the older papers without a DOI in the reports (e.g. Reaven 1988, Polonsky 1984).
  - *Abstract check.* For the claims that carry the argument I read the PubMed abstract and compared the numbers with the report text (Hu, Wang, Dennis, Hanley, Manley 2008, Wagner, Moghetti, EuBIVAS, Poon, Rosli, Jiao, Aroda, Tian, Trikudanathan, Teede, Peña, USPSTF, EASL).
- Not done: full-text reading, anything that needs paywalled text. The AASLD guidance has no abstract in PubMed, so nobody has read what it says about IR.

## 1. Headline

**Fabricated citations: none found.** Every PMID I checked resolves to the paper the report says it is. Teammates' honesty about what they did and did not verify was good, and mostly accurate.

**The citation problem is not fabrication. It is thin sourcing of the central negative claims**, and a few places where a report says more than its source does. The four reports agree (measuring IR has not been shown to change management beyond glucose, HbA1c, BMI and lipids), but that agreement is weaker than it looks (Problem 1).

## 2. Ranked problems

Severity: **High** = could change the verdict or mislead a reader; **Medium** = overstated or unsupported, conclusion probably survives; **Low** = housekeeping.

### P1 (High). The four reports are not four independent confirmations
**Claim:** the team consensus that IR measurement adds nothing actionable.
**Why it fails as stated:** all four reports lean on the same small set of papers (Matthews 1985, Bonora 2000, Manley, IRIS, Dennis 2019, Ahlqvist 2018, DPP, Teede 2023), found with the same two or three tools. They agree because they read the same sources, not because separate lines of evidence converge. Searches were also weak: the biostatistician says the PubMed connector failed on most natural-language queries and did not use Amass; the endocrinologist retrieved no trial registrations; the scientist listed seven topics with no source. The PCP's "I found no trial in which IR-guided care improved outcomes" and the biostatistician's "no IR-guided-care RCT" are statements about their searches. Nobody searched a trial registry for such a trial. (I attempted a ClinicalTrials.gov query; the connector rejected the call, so I also did not close this gap.)
**What would fix it:** a registry search (ClinicalTrials.gov, WHO ICTRP) for IR-stratified or IR-guided randomized care, and a structured literature search for incremental-value studies, reported with its search string.

### P2 (High). "No incremental value" is a negative claim built on three studies, one of which did not test insulin
**Claim (biostatistician §1, §3.2, §8; PCP Scenario A):** HOMA-IR adds nothing beyond glucose/HbA1c/BMI/lipids.
**What the evidence actually is:**
- Wilson 2007 (Framingham Offspring): one largely white middle-aged cohort, in-sample AROC. Biostatistician rates it "High" certainty. That grade is not earned by an abstract-level read of a single cohort with no NRI or calibration; "Moderate" at most.
- Hu 2024: confirmed from the abstract: 5578 workers, 94.7% male, 943 incident diabetes, HOMA models added "not materially". The authors themselves end with "further studies are needed". This is the PCP's only evidence for Scenario A, which the PCP grades "Moderate"; with one male, Japanese occupational cohort plus guideline silence, it is **Low**.
- Schmidt 2005 (ARIC): **insulin was not a predictor in that paper.** The biostatistician flags it as "indirect", but §3.2 and the §8 summary then list its AUC steps (0.71, 0.78, 0.80) beside the Framingham/Hu results as if HOMA-IR were tested. It was not. It shows lipids add something; it does not show insulin adds nothing.
- Hanley (below) and Gast are association studies. No CVD incremental-value study for HOMA-IR was found by anyone. The team states this, but the PCP and endocrinologist summaries then speak as if the question is settled.
- I ran one search of my own (triglyceride-glucose index plus reclassification). It surfaced several clinical cohorts that report positive but tiny gains when TyG is added (for example ΔC 0.755 to 0.768 in aortic stenosis, PMID 37660027; 0.715 to 0.719 in premature CAD, PMID 35906587). These are small selected-patient studies, so they do not overturn the team's view; they show a literature the team did not engage and that reports "significant" increments of the size the team calls negligible. A reader should know the "none" claim is a claim about a partly searched field.
**Counter-force the team did note but under-weighted:** the biostatistician's own regression-dilution argument (ICC ≈ 0.70) means head-to-head comparisons of a noisy insulin-based index against well-measured glucose are biased against the insulin index. That cuts against "adds nothing" as a statement about *true* IR, even if it supports "adds nothing as currently measured".
**Fix:** a pre-specified incremental-value package (ΔC, NRI split by events/non-events, calibration, decision curve) for HOMA-IR/TyG over PCE or SCORE2 in an external cohort. The biostatistician's §9 already lists this; it is the single most important missing study.

### P3 (High). The endocrinologist overreaches on IR phenotypes being "moderate" prognostic information
**Claim (endocrinologist §2):** "IR phenotype carrying prognostic information, *moderate*", citing Wagner 2021.
**Why it fails:** the Wagner abstract (confirmed) says the six clusters came from OGTT-derived variables, **MRI body-fat distribution, liver fat and genetic risk**, and that findings were replicated "using simple anthropomorphic and glycemic constructs". It is not an insulin-resistance-index result, and its highest-complication cluster (cluster 6) is the one with moderate diabetes risk but excess kidney disease and mortality. Using it as evidence that measuring IR carries prognostic information is a category slip. At most it shows that pathophysiological heterogeneity exists.
**Fix:** drop Wagner as support for IR-measurement utility, or restate as "heterogeneity exists; the discriminating variables are imaging and genetics".

### P4 (High). The "validated against the clamp" argument compares different constructs, and the teammates disagree about what IR is
**Conflict:** the scientist says HOMA-IR/QUICKI reflect the basal, hepatic-weighted feedback loop and are "not a direct measure of tissue insulin action", while the clamp is a muscle-dominant, supraphysiologic-insulin measure; the endocrinologist and biostatistician treat HOMA-IR, QUICKI, Matsuda and TyG as whole-body IR surrogates validated by clamp correlation (r 0.7 to 0.9). Both cannot be true in the form stated. The scientist's "clamp is muscle-dominant" is **[uncited]** in her own report, so the foundation of the disagreement is unsourced.
**Consequence:** correlations of 0.7 to 0.9 in mixed populations (obese vs lean, T2D vs NGT) show between-person spread, not that the index measures the same thing as the clamp. Bonora 2000 (kappa 0.63, abstract title says HOMA "closely mirrors" the clamp) is correctly read by the scientist and biostatistician as weak at individual level. The endocrinologist does not carry this into her statements. The team never settles which "IR" a clinical test is supposed to represent (hepatic, muscle, adipose), which matters for any claim of actionability.
**Fix:** state explicitly in the combined conclusions that surrogate indices measure a basal/hepatic-weighted phenotype with modest agreement to whole-body clamp sensitivity.

### P5 (Medium). PCOS conclusions rest on recalled or unread guideline text
**Claim:** guideline does not support IR testing for PCOS (endocrinologist; PCP Scenario D).
**Status:** the endocrinologist writes "I recall ... verify the exact wording [recall]". The PCP's Teede (E7) abstract does not mention IR (I confirmed this; the abstract is generic), and the Peña adolescent paper (E8) confirms diagnosis uses cycles plus hyperandrogenism, not IR. The only source stating a position on routine insulin/HOMA testing is Jiao et al. (E10).
**Effect of the PCP's open item (E10):** I resolved it: it is real (PMID 42856833, Front Endocrinol 2026, DOI 10.3389/fendo.2026.1909495), the PCP quotes it accurately, and the PCP correctly labels it a perspective. Two things the PCP does not say: it is an opinion piece by authors at a history-of-medicine institute, and it frames IR as "an actionable management hub" while arguing only that testing should not be a *diagnostic requirement*. So E10 supports "don't require IR to diagnose PCOS" but does not support "IR testing has no management value" and certainly does not count as guideline evidence.
**Net:** "don't use IR to diagnose PCOS" is well supported (diagnostic criteria are known not to include it, E8). "IR testing adds nothing to PCOS management" is unsupported in either direction: no one retrieved a trial of IR-stratified metformin and no one read the guideline recommendation text. Moghetti 2013 (confirmed) shows 71.4% of the 137 women were insulin resistant by clamp, and the frequency differed by phenotype (80.4% classic, 65.0% ovulatory, 38.1% normoandrogenic), and the authors suggest phenotype could guide who gets metabolic screening. That is a decision-relevant signal the team uses only to say "single index may misclassify".
**Fix:** read the guideline recommendation text on IR/insulin/HOMA; search for IR-stratified metformin trials in PCOS.

### P6 (Medium). Endocrinologist's HOMA-CVD citation is mislabeled and the recalled finding is stated more weakly than the source
**Claim (endocrinologist §6):** "HOMA-IR associated with incident CVD in the Insulin Resistance Atherosclerosis Study (PMID 12087016); I recall attenuation after adjustment."
**Verified:** PMID 12087016 is Hanley et al. 2002 from the **San Antonio Heart Study**, not IRAS. In the abstract the HOMA-IR association remained after adjustment for LDL, TG, HDL, SBP, smoking, alcohol, exercise and waist: quintile 5 vs 1 OR 2.52 (1.46 to 4.36) before, **1.94 (1.05 to 3.59)** after. "Only modestly reduced" is the authors' phrase. The report's "attenuation" is not wrong in direction (OR fell) but gives the impression of a fragile association; the lower bound is just above 1, which is the proper concern. It is also the only adjusted CVD association I found in the four reports that includes waist and lipids; Wang 2022 adjusted for lifestyle covariates only (per its abstract), and Gast pooled mixed adjustment sets.
**Why it matters:** the biostatistician and PCP accept "association exists, increment unproven". The better statement: an association survives adjustment for waist and lipids in at least one cohort (San Antonio), with imprecision.
**Fix:** correct the cohort name; quote the adjusted OR.

### P7 (Medium). PCP and biostatistician overgrade a few conclusions
- PCP Scenarios C, F, I and others rely on **[PCP judgment, uncited]**. These are honestly labeled and I do not penalize them, but they carry the "don't test" verdict for wellness, low-risk and hyperTG patients. Judgment, not evidence.
- PCP Scenario A is graded "Moderate that glucose/A1c-based screening suffices". USPSTF 2021 (confirmed) recommends screening by age and BMI with glucose/A1c; it did not evaluate IR testing, so its silence on IR is not evidence about IR. See P2 for Hu.
- PCP Scenario G lists "no study showing better discrimination ... than standard calculators": true to the search, but see P2 on search depth.
- Biostatistician Wang 2022 (rated "Moderate that IR adds nothing detectable in normoglycemia"): HR 1.04 (0.92 to 1.18) per SD in NGT, which also does not exclude a modest effect (upper bound 1.18). "Nothing detectable" is fine; "adds nothing" is not. And the adjustment set omits BMI, BP and lipids, which the biostatistician notes.

### P8 (Medium). Several biostatistician claims depend on citations she could not resolve
The biostatistician flagged eight `[C-only]` items. I tried to resolve them:
- **Resolved and match the report's description:** Aroda 2019 = Diabetes Care 42:601 (PMID 30877090), metformin benefit larger at higher baseline fasting glucose/HbA1c and with prior GDM; Tian 2022 = Cardiovasc Diabetol (PMID 36564775), 47.81% of overweight-CVD association mediated by TyG; Trikudanathan 2013 = Metabolism (PMID 23906497), n = 23 + 18, HOMA/QUICKI/TG:HDL correlated with clamp in South Asians but not in Caucasians; Torréns 2004 = PMID 14747213 (title match only).
- **Not resolved by me:** Kitabchi 2005, Knowler 2025, Xing 2025, Ross 2015. They are used for supporting detail (DPP heterogeneity, one cutoff table, MR), not for the central conclusions, but they should be treated as unverified.
- **A logic gap in §3.4:** "Neither DPP abstract names an IR index as an effect modifier" is used as evidence that glucose and HbA1c, not IR, modify treatment benefit. The Aroda abstract analyses subgroups by glucose, HbA1c and GDM; it does not say IR was tested and found null. Absence from an abstract is not a null result. That IR was or was not tested as a modifier in DPP is unknown from what was read.
- Rosli 2022 (PMID 35622611, "matched by author/topic"): confirmed, with the seven kits and RSD 1.7 to 23.2% as stated.

### P9 (Medium). IRIS is stretched in both directions
The biostatistician and endocrinologist correctly say IRIS (HOMA-IR above 3.0 at entry, no non-IR comparator) cannot show that measuring IR improves decisions. Two missing points:
1. The enrollment cutoff was a single HOMA-IR value on one assay and one draw. With a 27 to 30% within-person CV (EuBIVAS, Poon) and up to twofold assay differences (Manley 2008, confirmed), the trial's own inclusion criterion is not reproducible in a different lab. IRIS shows pioglitazone helps *some people who passed this screen*, not that "HOMA-IR above 3.0" identifies them elsewhere.
2. Pioglitazone also lowered incident diabetes (HR 0.48) and has benefits independent of IR (PIVENS, Pio-NASH in MASH); its benefit in a non-IR post-stroke group is untested. The endocrinologist acknowledges untested; the others should not cite IRIS as supporting IR measurement.

### P10 (Medium). Dennis 2019 is cited both ways without reconciling
Biostatistician (confirmed from abstract): clusters differed in glycaemic response, "with a particular benefit for thiazolidinediones" in the severe insulin-resistant cluster, but "simple clinical features outperformed clusters to select therapy". The endocrinologist reads this as "clusters add little", the PCP does not cite it, the scientist cites Ahlqvist only. Fair conclusion: a **signal** that IR-heavy clusters respond differently to TZD exists; the **decision value** over BMI/age/HbA1c is not shown. The single most decision-relevant finding in the whole set (TZD response in high-IR phenotype) is the one least pursued: no one searched for a prospective test of IR-stratified TZD use outside IRIS.

### P11 (Low). Smaller errors and loose ends
- Scientist cites Muniyappa as 2008; PubMed says 2007 (PMID 17957034). Endocrinologist dates Cryer "2009", PubMed 2008 (online). Neither matters.
- Endocrinologist's reference list says "ADA Standards 2025 diagnose by glucose/HbA1c, not IR": true of the title; the section text was not read, as the endocrinologist states.
- AASLD guidance (PMID 36727674): no abstract in PubMed. The endocrinologist says neither AASLD nor EASL requires an IR measurement (**[recall; verify]**). I confirmed the EASL-EASD-EASO abstract describes case-finding with FIB-4 then elastography and mentions no IR measurement; AASLD content is unread by anyone.
- Biostatistician's Poon summary: age 68 to 88, repeat at mean 46 days, abstract says HOMA-IR repeatability "fair to good". The report's MDC95 = 2.3 and ICC = 0.70 are exact. The author's characterization of this as meaning "a single value is unreliable" is the biostatistician's inference, not the paper's wording.
- The PCP and scientist quote Matthews' "CV about 31%" as individual precision. That is the model's estimation precision in 1985; the EuBIVAS (26.7%) and ARIC (30.4%) figures are the proper support and agree.
- The scientist's Brown & Goldstein, Reaven, DeFronzo 2009 and Czech citations support framing, not clinical claims. She flags this. Fine.

## 3. Conflicts between teammates (summary)

| Topic | Positions | Verdict |
|---|---|---|
| What HOMA-IR measures | Scientist: basal, hepatic-weighted, not tissue insulin action. Endocrinologist/biostatistician: whole-body IR surrogate validated by clamp. | Unreconciled (P4). Scientist's position is the better reasoned but is partly uncited. |
| Strength of prognostic IR phenotypes | Endocrinologist: moderate (Wagner, Ahlqvist). Scientist: registry cluster analysis, does not show management change. Biostatistician: Dennis shows clusters do not beat simple features. | Endocrinologist overreaches on Wagner (P3). |
| IRIS | Endocrinologist and biostatistician agree it cannot test measurement value. Endocrinologist calls it the largest outcome trial with IR-defined enrollment. | Consistent; add assay-dependence of the entry criterion (P9). |
| HOMA-IR to CVD | Endocrinologist (recall): attenuated. Biostatistician: pooled RR 1.64, association only. PCP: association, no decision value. | Consistent on "association, no proven increment"; endocrinologist's cohort label wrong (P6). |
| Strength of "don't test" | PCP: "Don't test" in all nine scenarios, mostly Low evidence. Endocrinologist: "no" except hypoglycemia, C-peptide, lipodystrophy. | Agree. Note both are concluding from absence. |
| Variability numbers | Scientist/PCP cite Matthews CV 31%; biostatistician cites EuBIVAS 26.7% and ARIC 30.4%. | Consistent; use the latter. |

## 4. Claims that survived scrutiny

- **IR measures are not part of diagnostic criteria for T2D, prediabetes, PCOS (Peña adolescent diagnosis, confirmed) or MASLD (EASL case-finding, confirmed).** Solid: it is the definition.
- **Assay non-comparability is real.** Manley 2007 (11 assays, Clin Chem), Manley 2008 (11 assays, 97 subjects; median HOMA-IR ranges 0.8 to 2.0 normoglycemic, 1.5 to 2.9 T2D; the prediabetes difference was not significant, P = 0.842), Matli 2021 (three assays, unsatisfactory agreement) and Rosli 2022 (seven kits) all agree. Caveat: the normoglycemic subgroup is only 12 people, so "twofold" is a descriptive range of medians, not a stable estimate.
- **Within-person variability of HOMA-IR is about 27 to 30%.** EuBIVAS (90 non-diabetic adults, 10 weekly samples) and Poon/ARIC (102 older adults, 46 days) agree. Poon's own MDC95 for HOMA-IR is 2.3.
- **Cutoffs are not portable.** Lee 2016 (T2D at 1.97) and Horáková 2019 (T2D at 3.63) differ by nearly twofold; both use glycemia as the reference, which contains the index's own glucose input (incorporation bias).
- **IR phenotype ≠ decision.** Dennis 2019 (simple features beat clusters for therapy selection) and IRIS (no non-IR arm) are accurately described.
- **C-peptide and insulin have defined roles outside IR** (hypoglycemia work-up, classification, exogenous insulin). The endocrinologist keeps this separate from IR testing, which is correct and important: it protects against the common conflation.
- **HOMA-IR association with CVD** (Gast: RR 1.64 high vs low; per-SD 1.46) and its concentration where glucose is already abnormal (Wang: HR 1.03 NGT, 1.23 prediabetes, 1.61 diabetes; interaction P = 0.011) are accurately quoted.
- **Citation integrity:** all checked identifiers resolve to the claimed titles; no retractions found (Crossref).

## 5. Gaps no teammate closed (what would change the verdict)

1. Trial-registry search for IR-guided or IR-stratified randomized care (P1).
2. A pre-specified incremental-value study (ΔC, NRI by events/non-events, calibration, decision curve) for HOMA-IR/TyG added to PCE or SCORE2 (P2).
3. The actual PCOS guideline text on insulin/HOMA testing, and any IR-stratified metformin trial (P5).
4. Treatment-by-baseline-IR interaction in DPP/DPPOS, Look AHEAD, ADOPT or other IPD (P8, P10).
5. Assay-harmonized, clamp-anchored cutoffs validated externally (biostatistician §9.4).
6. AASLD guidance content on IR.

## 6. Verdict

**The case for the clinical utility of measuring insulin resistance, as a general-purpose test, is weak, and the team's "weak" is itself only moderately certain.**

- **Strong:** IR *as a biological construct* is real and associated with disease (T2D, CVD, MASLD, PCOS). Measurement is hampered by assay differences, large within-person noise and cutoffs that do not transport. These points are well sourced and consistent across reports.
- **Supported but narrower than stated:** that IR measurement has not been shown to add to glucose/HbA1c/BMI/lipids for prediction (three or four cohorts, mostly male, white or Japanese, none for CVD reclassification) or to change management (no randomized test found in a search that did not cover registries). The honest statement is "not shown", not "shown not to".
- **Not supported by the evidence cited:** that IR phenotypes carry decision-relevant prognostic information (Wagner is not an IR measure; Dennis shows a TZD-response signal that did not beat simple features); that PCOS management is unaffected by IR (unread guideline, unsourced).
- **Where measuring insulin does change care**, it is for other questions: hypoglycemia/insulinoma and factitious insulin (insulin plus C-peptide), diabetes classification (C-peptide) and suspected lipodystrophy/extreme insulin resistance in specialist referral. These are real, but they are not general IR screening and should not be reported as support for it.
- **Evidence grade for "measuring IR improves a clinical decision or outcome" in prediabetes, T2D, PCOS, MASLD, obesity or cardiovascular risk: low, with a ceiling set by absent trials rather than by negative trials.** If asked for one number: I trust the "no established utility today" conclusion at roughly 80%, and the "it has been shown not to add value" version much less (closer to 40 to 50%), because the studies that would test it were mostly not done and the searches were incomplete.
