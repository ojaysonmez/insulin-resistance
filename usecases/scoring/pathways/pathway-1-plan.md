---
title: "Pathway 1 plan: random C-peptide in insulin-treated adults of uncertain diabetes type (rows 6 and 31)"
---

DRAFT, 2026-10-23. Not medical advice. Sizes, durations and probabilities are the assistant's judgements, not computations from a source. Source dossiers: `usecases/scoring/dossiers/row-06.md` and `row-31.md`; skeptic report: `reviews/skeptic-stage3-2026-10-23.md`. Measure type throughout: random (non-stimulated) plasma C-peptide with a concurrent glucose. Not fasting-only, not post-load, not urinary.

# 1. The question and why it ranks first

Insulin-treated adults whose diabetes type is doubtful are tested for C-peptide to decide whether the label is wrong (row 6) and whether insulin can be reduced or stopped (row 31). The ADA/EASD consensus (Holt 2021, PMID 34590174, DOI 10.1007/s00125-021-05568-3) says the test should always be performed before insulin discontinuation. Tier A under the current scores (rows 6, 1 and 31). Yield data exist (6.8% reclassified, 1.5% stopped insulin, 1.6% monogenic diabetes found, in one uncontrolled UK clinic: Foteinopoulou 2021, PMID 33131101, DOI 10.1111/dme.14449, abstract level). Missing: agreement of US-marketed assays at the decision thresholds, and prospective safety and outcome data for acting on the result.

# 2. Two steps

## Step A: US assay harmonisation (assay; about 9 to 12 months; small)
- Samples: at least 120 residual sera spanning 30 to 1,000 pmol/L, at least 40 between 150 and 700 pmol/L.
- Platforms: four or more US-marketed immunoassays against an isotope-dilution LC-MS/MS reference procedure (TaMADOR-type, PMID 38549041, DOI 10.1093/clinchem/hvae034). Use commutable human serum pools, not materials derived from WHO IRP 13/146 (PMID 37141618, DOI 10.1515/cclm-2023-0215).
- Outputs: bias and agreement at 80, 200 and 600 pmol/L; platform-specific equivalent cutoffs; a rule for paired glucose (4 mmol/L or more) and for eGFR.
- Why first: it is cheap, it is the D4 gap, and Step B needs harmonised units to pre-specify bands.
- Judgement: about 70% chance of completion within 12 months if funded.

## Step B: prospective multi-site cohort with a pre-specified step-down rule (evidence; 3 to 4 years; medium to large)
- Setting: 8 to 12 US diabetes clinics, academic and community, ideally within an existing network.
- Population: adults 18 or older, insulin-treated, 3 or more years from diagnosis, type doubtful by pre-specified criteria (for example a type 1 label with BMI 30 or more or diagnosis at 35 or older; or insulin-treated type 2 with no insulin need in the first year); no ketoacidosis in the last 2 weeks; eGFR above a stated floor; glucose 4 mmol/L or more at the draw; not on a sulfonylurea at sampling.
- Measurements: random C-peptide on a harmonised platform, GAD antibody (and IA-2/ZnT8 if available), clinical model; genetic test for those meeting the MODY triage rule.
- Pre-specified bands (harmonised units): below 200; 200 to 600; 600 or more pmol/L.
  - 600 or more: stepwise insulin reduction over a defined schedule with a non-insulin agent, weekly glucose and ketone contact for 4 weeks (SGLT2 inhibitors excluded or used only with ketone monitoring, as the protocol states).
  - 200 to 600: de-escalate basal insulin only, never to zero; antibody result as modifier.
  - Below 200: continue insulin; no withdrawal.
- Design: cluster stepped-wedge (usual care, then the C-peptide-guided pathway) allows a comparison; a single-arm cohort is the cheaper fallback.
- Primary endpoint: proportion reclassified with a documented treatment change at 12 months. Co-primary safety endpoint: diabetic ketoacidosis (pH below 7.30 or bicarbonate below 18 mmol/L with ketones) or admission for hyperglycaemia or ketosis in 12 months after any insulin reduction; HbA1c non-inferiority margin 0.5 percentage points.
- Secondary: severe hypoglycaemia, MODY yield and treatment change, proportion off insulin at 6 and 12 months, HbA1c, weight, insulin dose, patient-reported burden, healthcare use.
- Size: about 1,100 tested to estimate a 7% reclassification rate within 1.5 points; plan 1,500 to 2,500 for platform, band and clinic strata. About 100 to 170 reclassified, enough for a descriptive safety signal. With zero events in 100 withdrawals the upper 95% bound for DKA is about 3% (rule of three), so a rare-event claim needs more; a randomised testing-versus-no-testing trial would be larger and is probably not needed to move the tier.
- Judgement: about 65% chance of non-inferior HbA1c with no excess ketoacidosis (low confidence).

# 3. Guideline target
ADA Standards of Care section 2 (Figure 2.1 notes and text) to move from "must be measured" to a stated cutoff, timing and eGFR rule, and a statement for the 200 to 600 band; section 9 for a de-escalation pathway; the next ADA/EASD adult type 1 consensus update. Without outcome data the wording stays at consensus level.

# 4. Expected score movement if both steps succeed
D2 3 to 3 or 4 (4 only with controlled hard-outcome data); D8 clarified; D4 confidence up; D7 sourced if a US testing rate is obtained; S sourced. The composite is currently 0.655 (row 6) and 0.613 (row 31).

# 5. Risks and failure modes
- Platforms do not agree at 200 pmol/L: cutoffs become platform-specific, and no single guideline number is possible.
- Safety signal in the 600-plus band (ketoacidosis after withdrawal): the step-down rule would need tightening or the pathway would stop at de-escalation.
- Small effect on outcomes: reclassification is about 7% in one clinic; a multi-site rate may be lower.
- Testing rate unknown: the D7 bin (2 to 4) cannot be fixed without a US testing-rate source.

# 6. Not verified (carry into any proposal)
- Holt and the ADA 2026 texts were read second-hand from project files in the dossier; an open full-text retrieval is running separately (`corpus/fulltext-attempt-2026-10-23.md` when it lands).
- The 11% reclassification figure sometimes quoted has no traced source; use 6.8%.
- No registry search was run for existing trials of C-peptide-guided insulin withdrawal.
- No funding source, partner or budget is assumed.

# 7. What already exists, and who to approach (added 2026-10-24)

Sources: `usecases/scoring/pathways/pathway-1-registry-search.md` (30 logged registry and literature look-ups) and `usecases/scoring/pathways/pathway-1-partners.md` (27 look-ups, public sources only, no personal contact data). Both are desk research; no organisation has been contacted, and willingness, capacity and fees are unknown.

## Does a trial already answer Step A or Step B?
No registered trial was found that answers either step, and no US record was found at all (WHO ICTRP results could not be read directly; abstracts only).
- Step A: no registered cross-platform C-peptide harmonisation study. Published laboratory work only: TaMADOR (PMID 38549041, DOI 10.1093/clinchem/hvae034), Deng 2023 (PMID 37141618, DOI 10.1515/cclm-2023-0215) and Hörber 2023 (PMID 36630986), all abstract level. No published US split-sample comparison at 80, 200 and 600 pmol/L.
- Step B: the closest design is CLASP (ISRCTN76893830, Dundee, UK), a single-arm pilot in 28 frail adults aged 70 or older with type 2 diabetes that withdraws insulin at random C-peptide of 900 pmol/L or more, with ketoacidosis and hyperosmolar state as secondary outcomes; no results found. Its cutoff is higher than this plan's 600 pmol/L band, which is worth weighing when the step-down rule is set. Partly related, both UK: ARC-T1D (NCT06821360) and StartRight (PMID 36205650).

## Candidate partners (ranked by fit; a judgement, not an endorsement)
1. University of Missouri Diabetes Diagnostic Laboratory / C-peptide Standardization Program: the only US laboratory with a C-peptide reference measurement procedure on the international (JCTLM) register, plus commutable serum materials and multi-manufacturer studies (Rohlfing 2025, PMID 39803820, DOI 10.1515/cclm-2024-1260, full text). Step A reference values and materials.
2. University of Washington (Hoofnagle laboratory, TaMADOR method): an independent LC-MS/MS method already compared with the Missouri procedure (PMIDs 34723236, 38549041). Second mass-spectrometry arm.
3. Assay manufacturers, approached through the standardisation committee rather than one by one: Roche, Abbott, Siemens (Centaur and Atellica), DiaSorin and Tosoh have US-documented C-peptide products; Beckman, QuidelOrtho, Fujirebio, ALPCO and Mercodia need their US status checked. C-peptide assays are FDA Class I and exempt from 510(k) (21 CFR 862.1135), so FDA records cannot confirm which assays are on the US market; confirm from US labelling.
4. RADIANT (rare and atypical diabetes network; PMIDs 37104866, 42892882): the closest population match for "insulin-treated, type uncertain"; an ancillary study is likely more feasible than a separate network. Step B.
5. T1D Exchange Quality Improvement network: adult clinics and a shared data platform for the stepped-wedge design, but a T1D-labelled, mostly paediatric population. Step B arm for "T1D label with BMI 30 or more, or diagnosis at 35 or older".
6. College of American Pathologists accuracy-based survey: if it still runs, a low-cost baseline of US platform bias against reference values (status unverified).
7. Single academic centres (Johns Hopkins, Indiana, Penn, Chicago) as founding Step B sites or protocol co-authors.

## New gaps for Step A
- Within-person biological variation, reference change value and repeatability of random C-peptide in insulin-treated adults were not covered by any source found; allowable bias cannot be set without them.
- Sample stability and pre-analytical handling need their own validation (flagged, not quantified, in Rohlfing 2025).
- No CDC or NIST C-peptide programme was found.
