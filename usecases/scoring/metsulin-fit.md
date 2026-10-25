---
title: "Metsulin fit: home and point-of-care capillary insulin and C-peptide against the 50 use cases"
---

DRAFT, 2026-10-24, written by a subagent. Revised 2026-10-25 by the main session at the user's request: glucose is on the device (the first brief left it out), and a grouped view was added (section 1a). Interim analysis file; it changes no deliverable and no score. Not medical advice. The user approved putting this view in the public repository.

Files read: `usecases-verified.md` (all 50 rows), `usecases/scoring/ranking.md` (tiers and composites copied as they are; no score changed), `usecases/scoring/dossiers/row-01.md`, `row-06.md`, `row-07.md`, `row-31.md`, `usecases/scoring/pathways/pathway-1-plan.md`. No report in `analysis/` was read. 15 look-ups were used (search log, section 6).

**What Metsulin is (as briefed):** a home test that measures insulin, C-peptide and glucose in capillary blood (glucose added by the user, 2026-10-25; the first brief left it out). It does not measure proinsulin, beta-hydroxybutyrate (BOHB), urine C-peptide, autoantibodies, drug screens or other analytes, and it does not run clinic-based stimulated protocols. A CLIA-based point-of-care (POC) version is also being considered. **The user's threshold:** a home or POC device only makes sense if a person needs the test about 5 to 10 or more times a year. Below that, a central laboratory test is enough.

**Labels used here.** Every frequency and every fit rating is a judgement unless a source is named. "Judgement" means no source was found or searched. A tier is the project's evidence-and-need tier from `usecases/scoring/ranking.md` (A to D). "Not scored" means the row is not in the ranking. Measure types are named as the project rules ask: fasting-based, post-load or mixed-meal, random (non-fasting), timed at hypoglycaemia, or C-peptide.

**Glucose is already on the device (user, 2026-10-25), so this file does not recommend adding it.** Almost every decision in the 50 rows reads insulin or C-peptide against a glucose drawn at the same time (for example the random C-peptide rule needing glucose of 4 mmol/L or more in rows 6 and 31, HOMA-IR, Index60, the C-peptide-to-glucose ratio in graft monitoring), and in both home dried-blood-spot cohorts results were only interpretable after adjusting for concurrent glucose (section 5). The device's glucose channel covers that need. What stays open is accuracy, not presence: hypoglycaemia criteria (glucose <55 mg/dL) use a laboratory method rather than a meter (row 1 dossier), so a device glucose may not be enough to define a hypoglycaemia sample; the accuracy of Metsulin's glucose channel was not reviewed here. The table cells were first written as "Missing: glucose" and now read "Glucose on the device"; frequencies and threshold verdicts did not change, because glucose does not change how often a test is needed.

## 1. All 50 rows

Key to columns: (a) analytes the decision needs, which ones Metsulin covers, and which missing one matters most; (b) specimen, whether capillary blood is plausible, and any known capillary or dried-blood-spot (DBS) validation; (c) sampling constraint; (d) tests per patient per year now, then in a plausible home version; (e) home fit and POC fit; (f) whether the 5-10 per year threshold is met.

Known capillary validation, used in column (b). For C-peptide: transdermal capillary plasma (Besser 2024), DBS and volumetric microsampling (Jones 2018), home DBS against the mixed-meal test (Willemsen 2018, Hendriks 2025), and an older DBS method in healthy adults (Johansson 2010). Details are in section 5. For insulin: **no capillary or DBS insulin validation was found** in two targeted searches, so "not known".

| # | Use (short) | Tier (composite) | (a) Analytes; Metsulin coverage; key missing analyte | (b) Specimen; capillary plausible? validation | (c) Sampling constraint | (d) Tests/patient/yr: current; home version (source) | (e) Home fit; POC fit | (f) Passes 5-10/yr? |
|---|---|---|---|---|---|---|---|---|
| 1 | Adult hypoglycaemia, insulinoma vs other | A (0.651) | Glucose, insulin, C-peptide, proinsulin, BOHB, sulfonylurea screen, insulin antibodies, glucagon response. Covers insulin and C-peptide only. Missing: proinsulin, BOHB. Glucose is on the device, but the sample is defined by a laboratory-method glucose | Venous plasma. C-peptide: capillary plausible (validated outside hypoglycaemia). Insulin: not known | Timed: during spontaneous or fast-induced hypoglycaemia; samples kept only if glucose <60 mg/dL (row 1 dossier) | One diagnostic episode, several draws within one fast; home: 1-3 self-captured episodes (judgement) | Home Low: one-off, unsafe to self-sample during hypoglycaemia, needs laboratory glucose. POC Medium: a fast result could end a supervised fast sooner, but proinsulin and BOHB still go to the laboratory | No |
| 2 | Factitious or exogenous insulin | B (0.568) | Insulin, C-peptide, glucose, proinsulin; analogue-detecting assay. Glucose on the device. Insulin assay analogue cross-reactivity is decisive (0-264% across 16 assays, row 1 dossier) | Venous. Capillary insulin not known | Timed: at hypoglycaemia | Once; home: not appropriate (judgement) | Home None: self-collection breaks chain of custody in suspected factitious use. POC Low-Medium: emergency-department critical sample, only if the assay's analogue detection is known | No |
| 3 | Sulfonylurea or meglitinide hypoglycaemia | C (0.492) | Insulin, C-peptide, glucose plus drug screen. Missing: drug screen (the deciding test) | Venous; drug screen on plasma or urine | Timed: at hypoglycaemia | Once | Home None. POC Low: the pattern looks the same as insulinoma without the screen | No |
| 4 | Congenital hyperinsulinism, infant | B (0.530) | Glucose, BOHB, free fatty acids, glucagon response, high-sensitivity insulin; C-peptide and proinsulin if suspected. Missing: BOHB and FFA (the reliable markers); insulin is supportive only | Venous or heel-prick, small volume. Capillary: not known in infants. Needs low-range insulin (>1.25 uU/mL) | Timed: critical sample at glucose <50 mg/dL, inpatient | Once at diagnosis; follow-up uses glucose and BOHB (row 26) | Home None. POC Low: NICU; BOHB is the more useful rapid test | No |
| 5 | Hypoglycaemia after bariatric surgery | B (0.532), weak-evidence flag | Insulin (with or without C-peptide) and glucose at nadir. Glucose on the device (CGM context helps). No accepted insulin threshold | Venous. C-peptide capillary plausible; insulin not known | Timed: at a symptomatic nadir, or during a mixed-meal test in clinic | 1-2 diagnostic samples; home: 3-6 episodes captured in a diagnostic window (judgement) | Home Medium: episodes happen at home and recur, but without a threshold the insulin result adds little to glucose. POC Low | No in practice. Borderline only in an unproven home-capture protocol |
| 6 | Diabetes classification, random C-peptide | A (0.655) | C-peptide plus concurrent glucose (≥4 mmol/L); eGFR context; antibodies come first. Covers C-peptide. Glucose on the device | Plasma or serum. Capillary plausible: transdermal capillary C-peptide was 100%/100% at the 200 pmol/L venous threshold (Besser 2024) | Random (non-fasting); >3 years from diagnosis; not within 2 weeks of a hyperglycaemic emergency | About once (repeat if 200-600 pmol/L or low glucose); home: once (judgement) | Home Medium for collection (single random draw, capillary validated) but fails on frequency. POC Medium-High: the result is available at the visit where the decision is made | No |
| 7 | MODY genetic-test triage | B (0.560) | C-peptide (blood) or urinary C-peptide:creatinine ratio (UCPCR), with antibodies, age and BMI. Covers blood C-peptide. Missing: antibodies; UCPCR is a urine test (not covered) | Blood or urine. Capillary post-meal C-peptide plausible, but not validated as a UCPCR substitute | Post-meal (UCPCR at 2 h after the largest meal); >2-5 years duration | Once; home: once | Home Medium: post-meal home sampling is already practised with UCPCR. POC Medium | No |
| 8 | Residual beta-cell function, trial endpoint | D (0.374) | Stimulated C-peptide (MMTT AUC); glucose. Covers C-peptide. Glucose on the device | MMTT venous in trials. Home DBS validated against the MMTT (Willemsen 2018: r=0.91, Bland-Altman agreement; Hendriks 2025: stimulated DBS slope predicted 12-month MMTT AUC) | Clinic MMTT; home version uses fasting plus 60-90 min after a standard meal | MMTT 2-4/yr in trials (judgement); home DBS: median 24 cards over 6.9 months (Willemsen 2018), 6.5 card pairs over 12 months (Hendriks 2025) | Home High (the best-validated home C-peptide use). POC Low | Yes in the home research version. Research-only in care |
| 9 | Type 3c diabetes, C-peptide | D (0.358) | Fasting or MMTT C-peptide; glucose; exocrine tests. Glucose on the device | Venous. Capillary C-peptide plausible | Fasting or stimulated | Once | Home Low. POC Low-Medium | No |
| 10 | Islet or pancreas graft function | B (0.556) | Basal and stimulated C-peptide, glucose, creatinine (C-peptide/glucose/creatinine ratio), HbA1c. Covers C-peptide. Missing: creatinine (glucose on the device) | Venous. Capillary C-peptide plausible; not validated in graft recipients | Fasting (protocolised); MMTT for stimulated values | International survey: fasting C-peptide recommended every 1-3 months (PMID 35019897, search excerpt of table) = 4-12/yr; CIT protocol: C-peptide/glucose/creatinine ratio monthly (CIT document, search excerpt); CITR data at day 28, day 75, 6 and 12 months, then annually. Home: monthly fasting (judgement) | Home Medium-High: frequent fasting draws for early graft-dysfunction detection, which the survey names as the unmet need. POC Medium: transplant-clinic visits | Yes (first year: 4-12; later 1-4). Small population |
| 11 | Bariatric remission score | C (0.413) | C-peptide inside a score with age, BMI, duration. Covers C-peptide | Venous. Capillary C-peptide plausible | Fasting, preoperative | Once | Home Low. POC Low | No |
| 12 | Severe or syndromic IR, type B | B (0.506) | Fasting insulin (JDS >30 uU/mL), anti-insulin-receptor antibodies, genetics. Covers insulin. Missing: antibodies | Venous. Capillary insulin not known; very high values need assay range checks (hook effect [recall]) | Fasting | Once (diagnostic) | Home Low. POC Low | No |
| 13 | Stroke with prediabetes: pioglitazone (IRIS HOMA-IR >3.0) | C (0.492) | Fasting insulin plus fasting glucose. Glucose on the device (HOMA needs it). IRIS used central laboratories because insulin is not standardised | Venous, central laboratory. Capillary insulin not known | Fasting; at least 14 days after the event | Once | Home Low: a home fasting draw is easy, but it is once and the threshold is assay-bound. POC Low-Medium | No |
| 14 | Suspected MASLD without T2D | C (0.469), weak-evidence flag | HOMA-IR (fasting insulin or C-peptide plus glucose). Glucose on the device | Venous. Capillary not known for insulin | Fasting | Once at diagnosis, maybe at follow-up | Home Low. POC Low | No |
| 15 | PCOS IR assessment | Not scored | Fasting insulin or HOMA-IR. Guideline says not in routine care | Venous | Fasting | 0 recommended | Home None. POC None | No |
| 16 | Paediatric obesity | Not scored | Fasting insulin. Endocrine Society 2017 recommends against (strong) | Venous | Fasting | 0 recommended | Home None. POC None | No |
| 17 | Prediction, monitoring, screening (HOMA-IR, TyG) | Not scored (Unsupported) | HOMA-IR needs glucose; TyG needs no insulin at all. Missing: triglycerides (glucose on the device) | Venous | Fasting | 0 recommended; a consumer monitoring model could imply 4-12/yr (judgement) | Home Low (no evidence; technically easy). POC Low | No on evidence. It would pass only in an unsupported consumer model |
| 18 | Research: IR-targeted trial enrolment and endpoints | Not scored (research) | HOMA-IR, OGTT insulin, clamp. Glucose on the device | Venous; decentralised capillary sampling plausible for fasting insulin (not validated) | Fasting or post-load at trial visits | Trial visits 2-6/yr (judgement); decentralised: 4-12 (judgement) | Home Medium (decentralised trials). POC Low | Borderline (protocol-dependent) |
| 19 | CF-related diabetes, insulin indices | Not scored (research) | OGTT glucose (the clinical test); insulin indices research only | Venous, OGTT in clinic | Post-load | Annual OGTT; insulin not used | Home None. POC Low | No |
| 20 | Insulin autoimmune syndrome | B (0.525), weak-evidence flag | Total insulin (very high), insulin autoantibodies, PEG precipitation, C-peptide. Missing: antibodies, PEG | Venous. Very high insulin needs a dilution protocol | Timed or any time (antibody-bound insulin persists) | Once (diagnostic); follow-up during remission 1-3/yr (judgement) | Home None. POC Low | No |
| 21 | Non-islet-cell tumour hypoglycaemia | B (0.516), weak-evidence flag | Insulin and C-peptide (suppressed), glucose, IGF-II/IGF-I. Missing: IGF-II (glucose on the device) | Venous | Timed: at hypoglycaemia | Once | Home None. POC Low-Medium (critical sample in hospital) | No |
| 22 | Selective arterial calcium stimulation with hepatic venous sampling | C (0.455) | Hepatic venous insulin gradient | Hepatic vein, angiography suite; capillary not applicable | Timed series during the procedure | One procedure (many samples within it) | Home None. POC Low (an intra-procedural rapid insulin assay is conceivable, not studied here) | No |
| 23 | Insulinoma with postprandial symptoms | C (0.439) | Insulin and glucose during an OGTT or meal test. Glucose on the device | Venous, in clinic | Post-load or mixed-meal, timed | Once | Home Low. POC Low | No |
| 24 | Child >2 years with new hyperinsulinaemic hypoglycaemia | B (0.551) | As row 4 and row 1. Missing: BOHB (glucose on the device) | Venous | Timed: at hypoglycaemia | Once | Home None. POC Low | No |
| 25 | Infant spurious insulin from antibodies | C (0.422), weak-evidence flag | Insulin, C-peptide, PEG precipitation of maternal and infant samples. Missing: PEG | Venous, infant | Any time | Once | Home None. POC None | No |
| 26 | Cure or diazoxide-response fasts (negative entry) | Not scored | Glucose and BOHB, not insulin | n/a | Fasting test | 0 insulin tests | Home None. POC None | n/a |
| 27 | TPIAT: beta-cell reserve before, graft after | D (0.295), weak-evidence flag | MMTT C-peptide, glucose. Glucose on the device | Venous. Capillary C-peptide plausible | Stimulated (MMTT); fasting for follow-up | Before surgery once; after, 2-4/yr (judgement) | Home Medium for post-operative follow-up. POC Low | No (borderline) |
| 28 | C-peptide interpretation in CKD (a limit, not a use) | C (0.440) | Serum C-peptide plus eGFR; UCPCR. Missing: creatinine | n/a | n/a | n/a | n/a: a limit on every capillary C-peptide use (falsely high with low eGFR) | n/a |
| 29 | Teplizumab Stage 3 eligibility (C-peptide ≥0.2 pmol/mL) | B (0.531) | Peak stimulated C-peptide on MMTT; antibodies. Covers C-peptide. Missing: antibodies. The label allows "an alternative method for peak C-peptide" if no MMTT is available | MMTT venous. Capillary post-meal peak plausible, but not validated against the label threshold | Stimulated; within 8 weeks of Stage 3 diagnosis | Once at eligibility. PROTECT measured the primary endpoint at week 78 (Ramos 2023) | Home Low-Medium (one-time, regulatory threshold). POC Medium | No for eligibility. Follow-up monitoring is a new candidate (section 3) |
| 30 | Stage 2 T1D teplizumab candidates (negative entry) | Not scored | Selection is by autoantibodies and OGTT glucose; C-peptide not needed | n/a | OGTT | 0 for selection | Home None for selection. See candidate N3 | No |
| 31 | Reclassification and insulin de-escalation | A (0.613) | Random C-peptide plus concurrent glucose; antibodies; ketone monitoring during step-down (pathway 1 plan: weekly glucose and ketone contact for 4 weeks). Missing: BOHB (glucose on the device) | Plasma. Capillary plausible (Besser 2024) | Random; ≥3 years; glucose ≥4 mmol/L; eGFR floor | Once before withdrawal (Holt and ADA "measure before stopping insulin"); home: 3-5 during a monitored step-down (judgement; no source supports serial C-peptide) | Home Medium. POC Medium-High (same-visit decision) | No (borderline only in an unvalidated serial protocol) |
| 32 | Ketosis-prone diabetes after DKA | B (0.542) | Fasting C-peptide (>0.33 nmol/L) or glucagon-stimulated C-peptide (>0.5 nmol/L), antibodies. Missing: antibodies; glucagon stimulation is a clinic protocol | Venous. Capillary fasting C-peptide plausible | Fasting, after resolution, not within about 2 weeks of the episode | 1-3 in the first year (judgement) | Home Medium. POC Medium | No (borderline) |
| 33 | Youth >2 years, suspected non-T1D | C (0.470) | Home post-meal UCPCR, or fasting or post-meal C-peptide. Covers blood C-peptide. UCPCR is urine (not covered) | Urine or blood. Capillary post-meal C-peptide plausible, not validated against UCPCR cutoffs | Post-meal (2 h) | Once | Home Medium: an established home-sampling habit. POC Medium | No |
| 34 | Neonatal diabetes (negative entry) | Not scored | Age triggers genetics; no C-peptide needed | n/a | n/a | 0 | Home None. POC None | n/a |
| 35 | Pregnancy: first-trimester HOMA-IR for GDM | C (0.492) | Fasting insulin plus glucose. Glucose on the device | Venous | Fasting, first trimester | Once (unsupported) | Home Low. POC Low | No |
| 36 | Children with obesity and prediabetes | Not scored (not evaluated) | Fasting insulin or HOMA-IR; glucose-based tests preferred | Venous | Fasting | 0 recommended | Home None. POC None | No |
| 37 | Postoperative IR (research) | Not scored (research) | HOMA2-IR on postoperative day 1. Glucose on the device | Venous, inpatient | Fasting, timed post-surgery | 1-2 per trial | Home None. POC Low | No |
| 38 | PCOS with hidden FPLD2 (research) | Not scored (research) | Insulin and C-peptide during an oral glucose challenge; LMNA genetics. Glucose on the device; protocol is in clinic | Venous | Post-load in clinic | Once | Home None. POC Low | No |
| 39 | Acromegaly treatment outcome | Not scored (research) | Fasting insulin or HOMA-IR as an outcome | Venous | Fasting | 1-2 (judgement) | Home Low. POC Low | No |
| 40 | Alpelisib hyperglycaemia | Not scored (unsupported) | Glucose; insulin is mechanistic only | n/a | n/a | 0 | Home None. POC None | No |
| 41 | ICU and preterm glycaemic control (model-derived sensitivity) | Not scored (research) | Glucose and insulin dose; no insulin assay is used | n/a | Hourly or more | 0 assays now; if an assay were added to models, many per day (untested, judgement) | Home None. POC Low (research only) | n/a |
| 42 | Metabolic syndrome | Not scored (unsupported) | None | n/a | n/a | 0 | None / None | No |
| 43 | Adult antipsychotic monitoring | Not scored (unsupported) | None (glucose, lipids, weight) | n/a | n/a | 0 | None / None | No |
| 44 | HIV metabolic disease | Not scored (not evaluated) | None found | n/a | n/a | 0 | None / None | No |
| 45 | Prior gestational diabetes | C (0.402), weak-evidence flag | OGTT and A1C are the tests; fasting HOMA-IR research only | Venous | Fasting | 0 recommended | Home Low. POC Low | No |
| 46 | Fulminant T1D at onset | C (0.425), weak-evidence flag | Fasting C-peptide (<0.10 nmol/L) and stimulated (<0.17 nmol/L), or urinary C-peptide. Covers serum C-peptide; urine not covered | Venous, acute setting. Capillary plausible, but needs a low detection limit | Fasting and stimulated, at onset | Once | Home None. POC Medium (an acute same-day result supports the diagnosis) | No |
| 47 | Slowly progressive T1D (SPIDDM) | B (0.543) | Fasting C-peptide <0.6 ng/mL defines progression. Covers C-peptide | Venous. Capillary fasting C-peptide plausible | Fasting | 1-2/yr while monitoring progression (judgement) | Home Medium (a fasting home sample to track decline). POC Medium | No (borderline) |
| 48 | Reactive (idiopathic postprandial) hypoglycaemia | Not ranked (incomplete) | Glucose with symptoms decides; insulin collected but not a criterion | Venous, OGTT or MMTT in clinic | Post-load or mixed-meal | Once | Home Low. POC Low | No |
| 49 | Autoantibody-positive relatives: progression risk | D (0.398) | OGTT glucose plus C-peptide (Index60 needs 5-9 timed samples). Glucose on the device | Venous OGTT. Capillary C-peptide plausible; not validated in stage 1-2 | Post-load, timed | OGTT every 6-12 months in research (consensus, PMID 38912694); children in stage 2: glucose measures every 3 months. Home: post-meal C-peptide every 1-3 months (judgement) | Home Medium. POC Low-Medium | No now; plausible 4-12/yr in a home research version |
| 50 | Children on second-generation antipsychotics (CAMESA) | C (0.468), weak-evidence flag | Fasting insulin (≤100 pmol/L; assay-specific); glucose. Glucose on the device | Venous | Fasting | Baseline and 3 months for olanzapine, then periodic: 2-3 in year one, 1/yr after (row 50) | Home Low-Medium (a fasting draw for needle-averse children). POC Medium (psychiatry clinic) | No |

Count (judgement): no row meets the threshold in routine clinical practice today. One row meets it in routine care for a small group: row 10, graft monitoring in the first year. Two meet it only in research or home-research versions: row 8 (home DBS endpoints) and row 18 (decentralised trials, protocol-dependent). Seven are borderline (rows 5, 17, 27, 31, 32, 47, 49): each would reach 5-10/yr only under a monitoring protocol that no guideline currently states.

## 1a. Grouped view (added 2026-10-25, user)

The same rows, grouped on four axes. Every frequency is the column (d) value above, a judgement unless section 1 names a source.

- **Frequency:** one-time (once, or once per episode), occasional (about 1-4 a year, or reaching 5 only under a protocol no guideline states), frequent (5 or more a year, the user's threshold).
- **Analyte:** C-peptide, insulin, or both. Glucose is on the device for all of them and is not listed as a gap.
- **Timing:** four types, not two. Fasting, post-meal or post-load, random (non-fasting), and timed at hypoglycaemia.
- **Setting:** home, or clinic (point-of-care or central laboratory).

### Frequent and occasional uses

| Use | Frequency (tests/yr) | Analyte | Timing | Best setting | Status |
|---|---|---|---|---|---|
| Row 10, islet or pancreas graft, first year | Frequent (4-12) | C-peptide (plus creatinine) | Fasting | Home or clinic | Routine care; small population |
| Row 8 and N1, residual beta-cell function after diagnosis | Frequent (6.5 pairs a year up to weekly) | C-peptide | Post-meal and fasting; only the post-meal slope predicted the 12-month MMTT (Hendriks 2025, abstract) | Home | Research; no care decision tied to it |
| N2, response after teplizumab or another disease-modifying drug | Frequent (4-12, judgement) | C-peptide | Post-meal (ITAD: fasting and post-meal) | Home | Trial endpoint |
| Row 18 and N6, decentralised trial sampling | Frequent (protocol) | C-peptide; insulin only in IR-drug trials | Both | Home | Research; small market (see N6) |
| Row 49 and N3, stage 1-2 type 1 diabetes | Occasional now (OGTT 1-2); 4-12 in an untested home version | C-peptide | Post-load or post-meal | Home | Research; untested at home |
| N7, stem-cell islet trials | Occasional (about 4) | C-peptide | Post-meal (clinic MMTT) | Clinic today | Investigational |
| Row 31 and N4, insulin de-escalation follow-up | Occasional (3-5, judgement) | C-peptide | Random | Home or clinic | Serial testing unsupported |
| Row 27, TPIAT follow-up | Occasional (2-4) | C-peptide | Fasting or post-meal | Home | Weak evidence |
| Row 32, ketosis-prone diabetes | Occasional (1-3 in year one) | C-peptide | Fasting | Home or clinic | Tier B |
| Row 47, slowly progressive type 1 diabetes | Occasional (1-2) | C-peptide | Fasting | Home | Tier B |
| Row 5 and N5, recurrent hypoglycaemia capture | Occasional (3-6 episodes) | Insulin and C-peptide | Timed at symptoms | Home | Unsupported; glucose accuracy decides |
| Row 50, children on antipsychotics | Occasional (2-3 in year one, then 1) | Insulin | Fasting | Clinic | Weak evidence |
| Row 20 and N8, insulin autoimmune or type B follow-up | Occasional (1-4) | Insulin | Fasting or any time | Clinic | Rare; unsupported |
| Row 17 and N10, consumer HOMA-IR tracking | Would be frequent (4-12) | Insulin | Fasting | Home | Unsupported; conflicts with rows 15 and 16 |

### One-time uses (by analyte and timing)

- Random C-peptide: rows 6 and 31 (the first check), both tier A, clinic point-of-care fit.
- Post-meal C-peptide: rows 7 and 33. Stimulated C-peptide: rows 9, 29, 46. Fasting C-peptide: row 11.
- Fasting insulin: rows 12, 13, 14, 35, 39.
- Post-load insulin: rows 23, 38, 48.
- Insulin and C-peptide timed at hypoglycaemia: rows 1, 2, 3, 4, 21, 24, 25. Procedure samples: row 22.
- Not recommended or no insulin test: rows 15, 16, 19, 26, 30, 34, 36, 37, 40-45. Row 28 is a limit (kidney function), not a use.

### What the grouping shows (judgement)

1. **Frequent uses: 4, and 1 in care.** Row 10 is in routine care; rows 8 and 18 and candidate N2 are research or trial uses. Against a bar of 5-10 frequent uses, the review finds about a third to a half of that, and most of it is research.
2. **Every frequent use is C-peptide.** Insulin has no frequent use with evidence behind it; it appears only in occasional rows that are weak or unsupported (5, 17, 20, 50) and in IR-drug trials (row 18).
3. **Timing splits.** Fasting serves graft monitoring (row 10). Post-meal serves beta-cell tracking (N1, N2), where it predicted better than fasting in the one cohort that compared them (abstract level).
4. **Setting splits.** The frequent uses are home uses. The tier A uses (rows 1, 6, 31) are one-time clinic decisions, which suit a point-of-care version, not a home test.
5. **Where 5-10 could come from.** The occasional rows above (49, 31, 32, 47, 27, 5, and N7 if a stem-cell product is approved) are the candidates. Each needs a monitoring schedule and a decision that uses the repeat result (section 4, point 5); none has that today. This is the "what would make it viable" list for the project goal (D-30).

## 2. Ranked shortlist (evidence tier combined with home fit and frequency)

The ranking rule is a judgement, not a computation. Rows that meet the frequency threshold come first. Within that, evidence tier, then home fit. Tier-A rows that fail on frequency are listed separately, because they suit POC, not home.

**Home version**
1. **Row 10, islet or pancreas graft monitoring** (tier B). Meets the threshold (4-12/yr in year one), uses fasting C-peptide, home fit Medium-High. Limits: needs creatinine for the ratio (glucose is on the device); the population is small (hundreds per year in the US [judgement]); the kidney graft changes C-peptide clearance.
2. **Candidate N1/N2, residual beta-cell monitoring after T1D diagnosis or on disease-modifying drugs** (row 8 basis, tier D as a routine use). This has the strongest capillary evidence: home DBS feasibility and agreement in two cohorts, and home DBS as a primary trial endpoint in ITAD. Meets the threshold in research use. It is not a care decision today.
3. **Row 18 and candidate N6, decentralised trial sampling** (research). Meets the threshold depending on the protocol. The buyer is a sponsor, not a patient. Small market with existing competition (mailed dried blood spot cards); at most a validation route, not a commercial market (see N6).
4. **Row 49 and candidate N3, stage 1-2 T1D monitoring** (tier D). The consensus schedule already calls for 2-4 glucose checks a year, and OGTT C-peptide is an option. A home C-peptide version is plausible but untested.
5. **Row 5 and candidate N5, post-bariatric or recurrent hypoglycaemia home capture** (tier B, weak-evidence flag). Events happen at home, but there is no insulin threshold, and laboratory-grade glucose is the limiting factor.
6. **Rows 31, 32, 47 (with 27), insulin de-escalation and C-peptide decline follow-up** (tiers A, B, B, D). Borderline frequency. A serial-testing schedule is not supported by any source read.

**POC version** (single-visit decisions where same-visit results matter; frequency fails, so the case is workflow, not repeat testing)
1. Row 6 and row 31 (tier A): random C-peptide at the diabetes clinic visit, decided at that visit. The best POC evidence match, with the device's glucose read from the same sample.
2. Row 1 (tier A) and row 21: emergency-department or supervised-fast critical samples. A rapid result could shorten a fast, but proinsulin, BOHB and laboratory glucose are still needed.
3. Row 29 (tier B): teplizumab eligibility within 8 weeks of diagnosis, if an "alternative method for peak C-peptide" were validated.
4. Rows 10, 46, 7, 50: Medium POC fit for clinic visits.

Rows 2, 3, 4, 20, 22, 24, 25 fit neither version. They need analytes Metsulin lacks (proinsulin, BOHB, drug screen, antibodies, PEG), a timed in-hospital sample, or a chain of custody. The IR rows (13-17, 35-45, 50) fail on frequency, on evidence, or both. Row 17, the only one that would generate frequent tests (consumer IR monitoring), is unsupported by evidence.

## 3. Candidate uses not in the 50 rows (all candidate ideas; none is a verified use)

| ID | Candidate | Plausible tests/yr | Evidence status (read level) |
|---|---|---|---|
| N1 | Tracking residual beta-cell function after Stage 3 T1D diagnosis (honeymoon) in routine care | Home DBS: about 6.5 card pairs per year (Hendriks 2025) up to weekly (Willemsen 2018) | Research feasibility only. The stimulated (post-meal) DBS slope over 6 months predicted 12-month MMTT C-peptide; the fasting slope did not. No care decision is tied to the result. Abstract level |
| N2 | Monitoring response after teplizumab or other disease-modifying drugs | 4-12 (judgement) | PROTECT primary endpoint: stimulated C-peptide at week 78 (Ramos 2023; per-protocol analysis Herold 2026). ITAD uses frequent home DBS fasting and post-prandial C-peptide as the primary endpoint (Marcovecchio 2020, protocol). Label monitoring requirements were not re-read here; the project has the label read for eligibility only (row 29). Trial-endpoint use, not a care decision. Abstract level |
| N3 | Stage 2 (and high-risk stage 1) T1D monitoring | Children in stage 2: glucose measures every 3 months; adults: HbA1c every 6 months plus one other modality; OGTT with stimulated C-peptide is an option (PMID 38912694, full-text excerpts). Home C-peptide: 4-12 (judgement) | Consensus monitoring exists, but C-peptide is optional and OGTT-based. The consensus says only glucose methods (meter, CGM) can be self-managed at home. Expert opinion ([E] grades in the excerpts) |
| N4 | Follow-up after insulin dose de-escalation (row 31 extension) | 3-5 in year one (judgement) | No source supports serial C-peptide; the rule is one check before withdrawal. Ketone monitoring (not covered) is the safety test in the pathway 1 plan. Unsupported |
| N5 | Recurrent hypoglycaemia home capture (post-bariatric, suspected insulinoma between visits, reactive) | 3-6 episodes in a diagnostic window (judgement) | No study of home insulin or C-peptide capture found. Diagnosis rests on laboratory or CGM-confirmed glucose. Unsupported |
| N6 | Decentralised trial sampling (beta-cell preservation, beta-cell replacement, IR-targeted drugs) | Weekly to quarterly (protocol) | C-peptide microsampling agreement exists (section 5). Insulin capillary validation not found. Research use. At most a validation route (validation data and first reference customers), not a market to build on (judgement, 2026-10-25): the market is small (for illustration only, about 3,500 participants in open trials × about 12 home tests each ≈ 40,000 tests spread over several years; the test count per person is an assumption); mailed dried blood spot cards with central-lab assay already do this job cheaply, and trials batch their samples, so an immediate home result adds little; the published precedents are small, academic and European (ITAD, 45 children; INNODIA home study, 292 people; `usecases/scoring/home-cpeptide-precedents.md`); these trials need C-peptide and glucose (both on the device), not insulin. Size (registry count 2026-10-25, `usecases/scoring/t1d-preservation-trials.md`): 72 type 1 diabetes preservation trials since 2021 with a C-peptide outcome, about 6,400 participants (3,529 in 36 trials still recruiting or not yet recruiting); only 4 of 72 use home or remote sampling (3 dried blood spot, 1 home urine), none of them industry-sponsored; 10 have 5 or more C-peptide time points a year. Registry records only; counts depend on the search rules |
| N7 | Stem-cell-derived (for example iPSC-derived) or encapsulated islet recipients. **Investigational, not approved:** no stem-cell-derived islet product is FDA-approved (user, 2026-10-25); row 10 covers only deceased-donor pancreas and islet transplants and does not include these | About 4 a year in current trials: where stated, C-peptide is a clinic mixed-meal test on venous blood about every 3 months; no trial uses home, capillary or dried-blood-spot sampling (registry check 2026-10-25, `usecases/scoring/stem-cell-islet-trials.md`: 14 ClinicalTrials.gov records, about 251 participants across 12 trials). Fails the 5-10 a year threshold today; a home role would be between-visit fasting or random C-peptide, which no protocol asks for yet | Trial use only today. C-peptide is the main readout of graft function in these trials, so frequent remote sampling would serve sponsors first; if a product is approved, the monitored population could grow well beyond today's graft recipients (judgement). Academic work in this area includes the Delibasi laboratory (iPSC-derived islets; per the user, 2026-10-25). Needs creatinine for the CIT ratio alongside C-peptide and glucose (both on the device) |
| N8 | Type B insulin resistance or insulin autoimmune syndrome remission follow-up | 2-4 (judgement) | Insulin falls as remission occurs [recall]; not searched. Rare. Unsupported here |
| N9 | Checkpoint-inhibitor or other drug-induced insulin-deficient diabetes at onset | Once [recall] | Fails frequency; not searched |
| N10 | Consumer fasting-insulin or HOMA-IR tracking (lifestyle, GLP-1 response) | 4-12 (judgement) | This is row 17 (unsupported) and conflicts with PCOS and paediatric obesity guidance (rows 15, 16). It would meet the frequency threshold with no evidence of clinical utility; listed so it is not mistaken for a supported use |

## 4. What would have to be true for the top home candidates

Applies to rows 10, 8 (N1, N2), 49 (N3) and N6, and to POC rows 6 and 31.

1. **Capillary-versus-venous agreement at the decision thresholds.** For C-peptide, agreement has been shown at the 200 pmol/L threshold (Besser 2024, transdermal plasma, n=91) and across the range for DBS and volumetric microsampling (Jones 2018; Willemsen 2018). Still needed:
   - Low-end performance at 80 pmol/L (Holt), <0.1 nmol/L fasting (Igls, fulminant T1D) and 0.2 pmol/mL peak (teplizumab). An older DBS method's lowest value corresponded to serum 0.44 nmol/L (Johansson 2010), which is too high for T1D and graft decisions.
   - High-end performance at 600 pmol/L.
   - Haematocrit effects for spots.
   - Harmonisation to a reference procedure (Missouri programme, TaMADOR-type LC-MS/MS; pathway 1 plan).
   For insulin, no capillary or DBS validation was found, so every insulin use starts at zero. Analogue cross-reactivity must be stated per assay (0-264% across 16 immunoassays, row 1 dossier), and insulin results are not interpretable in insulin-treated people.
2. **Stability in transit.**
   - DBS C-peptide fell 11.6% after 48 h at room temperature; volumetric microsampling fell 0.1% (Jones 2018).
   - DBS C-peptide was stable for six months (Johansson 2010).
   - C-peptide in EDTA whole blood was reported stable for 24 h, while unspun serum lost 22-74% (pathway 1 plan, from a gap search).
   - Insulin stability in capillary or dried matrices was not found. Haemolysis degrading insulin is [recall].
   - A home device must specify the matrix, the anticoagulant and the maximum time to analysis.
   - If the result is read on the device rather than mailed, transit drops out, but on-device precision at low concentrations becomes the question.
3. **Sampling timing at home.**
   - A fasting state must be verified.
   - A standard meal is needed for post-meal values (Willemsen 2018 used standardised breakfasts).
   - A concurrent glucose is needed (adjustment for home glucose reduced variance in both DBS cohorts); Metsulin measures glucose from the same sample, so the open point is that channel's accuracy at each use's thresholds, not whether glucose is measured.
   - Hypoglycaemia capture would need laboratory-grade glucose, so it is not a realistic home use.
   - Renal function must be known (row 28).
   - Within-person biological variation of random C-peptide in insulin-treated adults is not published (pathway 1 plan), so a change that counts as meaningful between two home results cannot be stated yet.
4. **Regulatory class.**
   - C-peptide test systems are FDA Class I and 510(k)-exempt (21 CFR 862.1135, per the pathway 1 plan). The insulin test system classification was not checked here.
   - Home self-collection devices and home-use (over-the-counter) tests need their own authorisation [recall, not verified].
   - A POC version used outside a full laboratory needs a CLIA waiver or a moderate-complexity certificate at the site [recall, not verified].
   - A device whose result drives a regulated decision (teplizumab eligibility, insulin withdrawal) would carry a higher burden than a research-endpoint device (judgement).
5. **A decision that uses the repeat result.** Except for graft monitoring, where the survey names early detection of dysfunction, no source read ties a serial C-peptide value to an action. Without that, frequent home testing serves research and trials, not care.

## 5. Sources for this file (PMID and DOI from PubMed records unless stated)

| Source | Identifiers | Read level | Used for |
|---|---|---|---|
| Hendriks 2025, home DBS C-peptide in new-onset T1D (INNODIA, n=292) | https://doi.org/10.2337/dc25-0214 (PMID 40402094) | Abstract | Home frequency (6.5 card pairs/12 months); stimulated slope predicts 12-month MMTT |
| Willemsen 2018, frequent home DBS C-peptide, n=32 children | https://doi.org/10.1210/jc.2018-00500 (PMID 29860430) | Abstract | r=0.91 against plasma; 24 cards over 6.9 months; glucose adjustment needed |
| Besser 2024, transdermal capillary C-peptide, n=91 | https://doi.org/10.2337/dc23-1379 (PMID 38087932) | Abstract | 100%/100% at the venous 200 pmol/L threshold; 3.3% sampling failures |
| Jones 2018, DBS and volumetric microsampling for C-peptide | https://doi.org/10.1177/1932296818763464 (PMID 29521111) | Abstract | Agreement; 48-h stability (DBS -11.6%, VAMS -0.1%) |
| Johansson 2010, C-peptide in DBS, healthy adults | https://doi.org/10.3109/00365513.2010.501113 (PMID 20602576) | Abstract | Lowest detectable value = serum 0.44 nmol/L; stable 6 months |
| Marcovecchio 2020, ITAD protocol | https://doi.org/10.12688/wellcomeopenres.15697.1 (PMID 32399500) | Abstract | Home DBS C-peptide as primary trial endpoint |
| Phillip 2024, consensus monitoring of IAb+ pre-stage 3 T1D | https://doi.org/10.2337/dci24-0042 (PMID 38912694) | Full text, keyword-window excerpts via a fetch tool (PMC11381572); the PubMed full-text call returned empty | Monitoring intervals; OGTT C-peptide optional; home methods limited to glucose |
| Ramos 2023, PROTECT teplizumab | https://doi.org/10.1056/NEJMoa2308743 (PMID 37861217); NCT03875729 https://clinicaltrials.gov/study/NCT03875729 | Abstract | Week-78 stimulated C-peptide endpoint |
| Herold 2026, PROTECT per-protocol analysis | https://doi.org/10.1007/s00125-026-06849-5 (PMID 42720752) | Abstract | Same endpoint; insulin dose and time in range |
| Int. survey of monitoring in pancreas and islet transplantation, 2022 | https://doi.org/10.1097/TP.0000000000004058 (PMID 35019897) | Abstract; table seen only as a web-search excerpt of PMC9271126 | Fasting C-peptide "recommended every 1-3 months" (consensus opinion) |
| CITR 11th Allograft Report 2022 | https://www.citregistry.org/system/files/11th_CITR_Network_Report_Allograft_2022_0.pdf (no PMID/DOI) | Web-search excerpt | Follow-up at day 28, day 75, months 6 and 12, then annually |
| CIT metabolic testing document | https://www.isletstudy.org/citdocs/metabolic%20testing.pdf (no PMID/DOI) | Web-search excerpt | C-peptide/glucose/creatinine ratio monthly; MMTT every 3 months (protocol) |
| Project files | `usecases-verified.md`; `usecases/scoring/ranking.md`; `usecases/scoring/dossiers/row-01.md`, `row-06.md`, `row-07.md`, `row-31.md`; `usecases/scoring/pathways/pathway-1-plan.md` | Read in full | All row content, tiers, thresholds, assay and stability notes cited "per project file" |

Search results seen as excerpts but not used for any claim: CIT-08 long-term outcomes (PMC9767903; PMID and DOI not retrieved, look-up budget spent); CITR C-peptide predictive-value report (PMC10148684; identifiers not retrieved); Mikovic 2024 short fast (https://doi.org/10.1007/s12020-024-03759-7, PMID 38451386, abstract; capillary glucose was used only for monitoring during the fast, venous samples for insulin); Simmons 2016 DBS islet autoantibodies (https://doi.org/10.1371/journal.pone.0166213, PMID 27846247, abstract; antibodies are not a Metsulin analyte).

## 6. Search log (15 look-ups, the maximum)

| # | Tool | Query or IDs | Result |
|---|---|---|---|
| 1 | PubMed search | dried blood spot C-peptide validation | 2 hits (40402094, 20602576) |
| 2 | PubMed search | consensus guidance monitoring islet autoantibody-positive pre-stage 3 type 1 diabetes | 6 hits; 38912694 used |
| 3 | PubMed metadata | 40402094, 20602576, 38912694 | Identifiers and abstracts |
| 4 | PubMed full text | PMC11381572 | Empty full text (abstract only) |
| 5 | Web fetch | pmc.ncbi.nlm.nih.gov/articles/PMC11381572 | Excerpts with monitoring intervals |
| 6 | PubMed search | (dried blood spot OR capillary OR microsampling) AND insulin AND C-peptide AND (agreement OR comparison) AND venous | 7 hits |
| 7 | PubMed search | teplizumab newly diagnosed PROTECT C-peptide week 78 | 2 hits |
| 8 | PubMed metadata | 38451386, 38087932, 29860430, 29521111, 37861217, 42720752 | Identifiers and abstracts |
| 9 | PubMed search | dried blood spot insulin measurement (hypoglycemia OR validation OR immunoassay OR mass spectrometry) | 21 hits; none validated insulin in DBS among the 8 checked |
| 10 | PubMed search | Collaborative Islet Transplant Registry follow-up C-peptide schedule ... | 0 hits |
| 11 | PubMed metadata | 40767977, 38792494, 38367516, 37999718, 32479742, 32399500, 27846247, 25411707 | Only 32399500 used |
| 12 | PubMed search | (finger-prick OR capillary blood) insulin concentration venous plasma comparison | 9 hits; none a capillary insulin assay validation (titles and abstracts of 3 checked) |
| 13 | Web search | islet transplant follow-up C-peptide schedule (CITR, survey, MMTT) | Survey table excerpt, CITR report, CIT document |
| 14 | PubMed search | International Survey of Clinical Monitoring Practices in Pancreas and Islet Transplantation | 35019897 |
| 15 | PubMed metadata | 35019897, 27885969, 21929838, 17397609 | 35019897 identifiers; the others were not relevant |

Not searched (budget spent): the teplizumab label's monitoring section, TrialNet protocol documents, the regulatory classification of insulin test systems, post-bariatric episode frequency, capillary insulin stability. Absence statements in this file ("not found", "not known") are search-limited, not proven absence.
