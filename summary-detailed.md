# Is measuring insulin resistance clinically useful? Plain-language summary (detailed version)

Detailed version with the full trace table. Written on 2026-10-19 before the project goal was reframed (decision D-30), so it reads as an evidence review. The one-page brief in `summary.md` is the starting point; use this file when you need the evidence and its sources.

Status: written by the summary editor role from the project files on 2026-10-19 (no search, no new evidence), then spot-checked by the main session: 8 of 8 sampled claims matched their source files, and one outdated statement (about retractions) was corrected and marked below. Not yet reviewed by a skeptic. This is a reading aid for `merged-conclusion.md` and `usecases-verified.md`; if they differ, those two files win. This is not medical advice.

How it was made:
- Where two files differ, the later skeptic-reviewed wording was followed.
- The glossary labels are plain-language wording added by the editor; their usage matches the files.

## Read this first
- Specialty reviews have not been done for cardiology, hepatology, reproductive medicine, nephrology, oncology or psychiatry [HANDOFF: Next step]. Several files also show thin coverage in these areas: the liver, PCOS, oncology and psychiatry evidence rests on guidelines read in part, abstracts or small trials [merged-conclusion: Added by the steelman run; Open gaps 1, 5].
- The percentages below are judgements of how likely a verdict is to survive further checking. They are not calculations [merged-conclusion: Bottom line 1; Bottom line 2].
- About 20 to 30 important papers were read at abstract level only [HANDOFF: Waiting on the user]. The files also say that most rows in the treatment-interaction table, and many use-case rows, rest on abstracts or titles [merged-conclusion: Trials and interaction; usecases-verified: top note].
- Scope: the verdicts cover fasting-based measures (fasting insulin, HOMA-IR) and non-insulin surrogates (TyG, TG/HDL-C). Post-load and mixed-meal measures were weighed only through a few trials and use cases. C-peptide was weighed only for niche uses [merged-conclusion: Bottom line, scope note].
- "Not found" means not found in the records that were screened [merged-conclusion: How far the searcher's negatives can be trusted].

## 1. The answer
Routine measurement of fasting insulin, HOMA-IR or TyG/TG-HDL-C has no established clinical utility today. This applies in primary care, prediabetes, type 2 diabetes, PCOS, fatty liver disease (MASLD) and obesity. Confidence is about 80-85%, a judgement of how likely the verdict is to hold up [merged-conclusion: Bottom line 1].

Every use-case row about insulin resistance is limited, research-only or unsupported. None is established [usecases-verified: Summary by kind, notes]. Insulin and C-peptide do have established roles for other questions. These are hypoglycaemia work-up, diabetes classification, transplant graft assessment and one drug-eligibility criterion [merged-conclusion: Bottom line 3; usecases-verified: Summary by kind, notes].

The weaker claim is that routine measurement has been "shown not to add value". Confidence in that claim is only about 45-50%, because no adequately powered outcome test exists [merged-conclusion: Bottom line 2].

## 2. Main findings
- No guideline read requires fasting insulin, HOMA-IR or an OGTT-derived estimate, or ties one to a change in treatment [merged-conclusion: What is well supported].
- The PCOS guideline (2023) says insulin assays are not recommended in routine care. The stated reason is assay inaccuracy, not proof of no benefit [merged-conclusion: What is well supported, PCOS]. The Endocrine Society (2017) recommends against measuring insulin when evaluating children for obesity. It is a strong recommendation of moderate quality. It is one guideline, and the 2023 American Academy of Pediatrics (AAP) guideline could not be retrieved [usecases-verified: row 16].
- The European liver guideline (2024) says HOMA-IR or OGTT-derived estimates "may be considered" in suspected MASLD without type 2 diabetes. This is weak, consensus-based and level of evidence 3. It is not linked to any change in work-up or therapy [merged-conclusion: What is well supported, MASLD].
- A single fasting insulin or HOMA-IR cannot reliably classify a person near a cutoff or detect individual change. Within-person variation is about 25-30%, and assays disagree. This is the strongest measurement conclusion, and it is established for fasting measures [merged-conclusion: Added by chemist runs, Net]. For post-load indices, reproducibility is mixed, and use at a cutoff was not tested [merged-conclusion: Added by chemist runs, Net].
- Added prediction value is thin for fasting insulin and HOMA-IR. For TyG the results conflict (for example ATTICA against Liu 2026). The ATTICA gain carries heavy qualifiers, and TyG uses triglycerides and glucose, not insulin [merged-conclusion: What is well supported, incremental prediction; ATTICA].
- Association with disease is real but modest. HOMA-IR is linked to incident type 2 diabetes and non-fatal cardiovascular events, but not to fatal events [merged-conclusion: What is well supported, Association is real but modest].
- The one trial that selected patients by HOMA-IR above 3.0 (IRIS, after stroke) found less stroke or heart attack with pioglitazone (9.0% vs 11.8%, HR 0.76). It had no comparison group chosen without the IR value, so it cannot show that testing is needed. Glycaemic category may be a substitute selector [merged-conclusion: What is well supported, IRIS]. ADA and AACE guideline wording names "insulin resistance" as a condition but names no assay or threshold [merged-conclusion: Bottom line 3].
- No randomized trial comparing insulin-resistance-guided care with usual care was found. This is the best-supported "not found" in the project [merged-conclusion: Trials and interaction]. Treatment-interaction results are mostly abstract-level and often point in opposite directions. The oncology trials are chance-compatible by their authors' own statements [merged-conclusion: Trials and interaction; Added by the steelman run, Oncology].
- Insulin and C-peptide are established for secretion questions: hypoglycaemia, diabetes classification in insulin-treated people, MODY triage, graft function (Igls) and teplizumab eligibility. The use-case list has 49 rows: 11 established, 16 limited, 11 research-only, 11 unsupported (counts updated 2026-10-19 after two rows were added; the rest of this summary was written when the list had 47 rows). Most "unsupported" rows mean no use was found, not that a use was tested and rejected [usecases-verified: Summary by kind, notes].

## 3. Use cases by patient type

| Patient type and question | Test (measure type) | Status | Notes |
|---|---|---|---|
| **Insulin-resistance uses** | | | |
| Adults, routine risk prediction or screening | Fasting HOMA-IR, TyG | Unsupported | Whether monitoring has support was tested in none of the sources read [usecases-verified: row 17] |
| PCOS, routine care | Fasting insulin, HOMA-IR | Unsupported | Guideline: insulin assays not recommended routinely [usecases-verified: row 15] |
| Children with obesity (also prediabetes or T2D) | Fasting insulin | Unsupported | Guideline recommends against; row 36 is by extension [usecases-verified: rows 16, 36] |
| Suspected MASLD, no T2D | HOMA-IR or OGTT-derived estimate | Limited | Weak "may be considered" [usecases-verified: row 14] |
| Stroke/TIA with prediabetes or IR | HOMA-IR above 3.0 (trial entry criterion) | Limited | No guideline names an assay [usecases-verified: row 13] |
| Suspected severe or genetic IR syndromes | Fasting insulin above 30 µU/mL (Japanese criteria) | Limited | Expert criteria, no accuracy data [usecases-verified: row 12] |
| Trial enrolment or endpoints; postoperative IR; PCOS genetic IR; acromegaly; ICU model-derived sensitivity; prior GDM; first-trimester GDM prediction | HOMA-IR, OGTT insulin, derived indices | Research-only | GDM rows are title-level [usecases-verified: rows 18, 35, 37-39, 41, 45] |
| Metabolic syndrome; antipsychotic or HIV monitoring; alpelisib | None found | Unsupported | No use found in the sources read [usecases-verified: rows 40, 42-44] |
| **Insulin and C-peptide for other questions** | | | |
| Adult hypoglycaemia: insulinoma, factitious insulin, sulfonylurea | Insulin, C-peptide at hypoglycaemia (drug screen separates sulfonylurea) | Established | Thresholds second-hand via ENETS [usecases-verified: rows 1-3] |
| Infant or child with persistent hypoglycaemia; child over 2 years | Insulin, C-peptide in a critical sample | Established | In infants insulin is supportive, not required [usecases-verified: rows 4, 24] |
| Insulinoma with negative imaging | Hepatic venous insulin gradient | Established (specialist, second-line) | [usecases-verified: row 22] |
| Post-bariatric hypoglycaemia; postprandial-only insulinoma; insulin autoimmune syndrome; NICTH; infant with antibody artefact | Insulin, C-peptide | Limited | [usecases-verified: rows 5, 20, 21, 23, 25] |
| Insulin-treated person with doubtful diabetes type; MODY triage | Random C-peptide (concurrent glucose); UCPCR | Established | Narrower than first drafted; two consensus sources [usecases-verified: rows 6, 7, 31] |
| Type 3c, ketosis-prone, paediatric non-T1D, fulminant and slowly progressive T1D | C-peptide | Limited | Japanese rows are national expert criteria [usecases-verified: rows 9, 32, 33, 46, 47] |
| Islet or pancreas graft function | C-peptide within Igls criteria | Established (consensus) | TPIAT reserve is limited [usecases-verified: rows 10, 27] |
| Recent Stage 3 T1D, ages 8-17: teplizumab | Peak stimulated C-peptide at least 0.2 pmol/mL | Established (regulatory) | Accelerated approval on a surrogate; ADA 2026 predates it [usecases-verified: row 29] |
| T1D trial endpoints; kidney disease; cystic fibrosis insulin indices | Stimulated C-peptide; UCPCR; OGTT insulin | Research-only | Kidney disease is a caution on other rows [usecases-verified: rows 8, 19, 28] |
| Bariatric remission scores | C-peptide as one input | Limited | No incremental C-peptide analysis [usecases-verified: row 11] |
| Stage 2 T1D; neonatal diabetes; HI cure fasts | None needed | Unsupported (negative entries) | [usecases-verified: rows 26, 30, 34] |

## 4. Main uncertainties and studies that would settle them
- Does adding HOMA-IR or TyG improve risk prediction? Needed: a prespecified study over PCE or SCORE2 in an external, diverse cohort. It should report change in C-statistic, reclassification (category-based and category-free), calibration and decision curves. The same question for post-load measures and C-peptide has had only a few searches [merged-conclusion: Open gaps 2].
- Does measuring change outcomes? Needed: a trial of measurement-guided care [merged-conclusion: Added by the steelman run, last bullet].
- Does the HOMA-IR value, or glycaemic category, identify who benefits from pioglitazone after stroke? Needed: a trial across all HOMA strata with a second randomization to "measure and treat if above 3.0" against "treat by glycaemic category". It would settle one niche only. It needs a sample several times IRIS's size and has no obvious sponsor [merged-conclusion: Added by the steelman run, last bullet].
- Do baseline measures change treatment effect on hard outcomes? Needed: adequately sized, prespecified interaction tests, stated per measure. The only prespecified test found (DIETFITS) is null. It used post-glucose insulin and a weight-loss outcome [merged-conclusion: Open gaps 3; Bottom line 2].
- Can cutoffs be trusted across laboratories? Needed: assay-harmonised, clamp-anchored, ethnicity-specific cutoffs, and a study of how often people cross a cutoff on repeat testing [merged-conclusion: Open gaps 4].
- Some "not found" results came from narrow or unscreened searches. Pregnancy, dementia, heart failure with preserved ejection fraction and PCOS were not properly tested [merged-conclusion: Added by the steelman run, Not tested by anyone; Open gaps 1].

## 5. How reliable is this
The project's skeptics checked well over 100 PMIDs against PubMed and found no fabricated citations [merged-conclusion: Provenance]. *Added by the main session, not by the editor:* a later automated check of all 128 PMIDs in the two main documents, with fresh lookups on 2026-10-19, found every PMID in PubMed, one retracted paper (a type 1 diabetes drug trial, DiaPep277, which the use-case list cites only as a "do not cite" note) and 8 corrections or errata, none of which changes a claim [CHANGELOG: full run of the citation checker, 2026-10-19]. The sentence in `merged-conclusion.md` that Crossref retraction checks found none is therefore out of date and is on the list to be corrected after a skeptic review. The work is not a systematic review, and the two report sets share tools, so their agreement is not fully independent [merged-conclusion: Provenance].

Read at full-text level by a skeptic:
- The key guideline passages: ADA 3.13, AACE R 9.4, Endocrine Society Rec 1.7, the Japan Diabetes Society (JDS) criteria, EASL, PCOS, the teplizumab label and the ADA 2026 classification section [skeptic-usecases: Part 1 items 1-9; 2.4].
- ATTICA, PERSON, the MA.32 insulin analysis and the presurgical metformin follow-up [skeptic-steelman: How I checked].

Not read in full: TriMaster, the Mendelian randomization paper, TRIO-BD, the depression pioglitazone trial, the NAFLD cohort and the C-peptide score papers [merged-conclusion: Open gaps 6].

Abstract-level or title-level rows in the use-case list have lower confidence [usecases-verified: top note]. Some guidelines were checked only by keyword search or in part. Several were not read at all (ISPAD, AAP 2023, OPTN Policy 11, ESC 2021, AHA 2023, AACE 2026) [merged-conclusion: What is well supported, Limits of "no recommendation found"; Open gaps 5].

One inconsistency remains in the use-case file. Its conflicts section still lists some items as open that the skeptic review resolved. The editor followed the skeptic review [usecases-verified: section 5 intro; skeptic-usecases: 2.6].

## What this means in practice
This describes the evidence, not individual advice.

For a clinician:
- The guidelines read do not require routine insulin or HOMA-IR testing. The PCOS guideline advises against routine insulin assays. The Endocrine Society advises against insulin testing in paediatric obesity evaluation [merged-conclusion: What is well supported; usecases-verified: rows 15, 16].
- Near a cutoff, a single result is unreliable. Both the result and the cutoff depend on the laboratory's assay [merged-conclusion: Added by chemist runs, Net; Measurement].
- Insulin and C-peptide have established roles in hypoglycaemia work-up and in classifying insulin-treated diabetes [usecases-verified: rows 1-7, 31]. Insulin therapy makes insulin- and C-peptide-based indices uninterpretable. Kidney disease raises C-peptide [merged-conclusion: Added by chemist runs; usecases-verified: row 28].

For a patient asking about the test:
- The evidence shows no proof that routine measurement improves outcomes [merged-conclusion: Bottom line 1; Trials and interaction].
- Results can differ a lot between repeat tests and between laboratories [merged-conclusion: Added by chemist runs].
- The tests do have clear uses for specific questions, such as hypoglycaemia or deciding the diabetes type [usecases-verified: Summary by kind, notes].

## Glossary
- **Fasting insulin:** insulin level after fasting. It is a fasting-based measure [merged-conclusion: Bottom line scope note].
- **HOMA-IR:** an index calculated from fasting insulin and glucose. HOMA-IR, QUICKI and FIRI are monotone transforms of one another [merged-conclusion: Added by chemist runs, measurement; skeptic-steelman: problem 2].
- **TyG:** an index from triglycerides and glucose. It is not an insulin measure [merged-conclusion: What is well supported, ATTICA].
- **Post-load or mixed-meal measures:** insulin after a glucose drink or meal, such as OGTT insulin or Matsuda [merged-conclusion: Bottom line scope note].
- **C-peptide:** a by-product of insulin made by the pancreas, used to judge the body's own insulin production [usecases-verified: rows 6, 29].
- **Incremental value:** whether a test improves prediction beyond what is already known. It is measured as change in C-statistic (delta C) and reclassification (NRI) [merged-conclusion: Open gaps 2].
- **Clamp:** the reference laboratory method for insulin sensitivity, against which surrogates are tested [merged-conclusion: Surrogates are modest].

## Trace table

| Section | Sentence / block | Source |
|---|---|---|
| Read this first | Specialty reviews not done | HANDOFF: Next step |
| Read this first | Percentages are judgements | merged-conclusion: Bottom line 1, 2 |
| Read this first | 20-30 papers abstract-only | HANDOFF: Waiting on the user; merged-conclusion: Trials and interaction; usecases-verified: top note |
| Read this first | Scope of verdicts | merged-conclusion: Bottom line, scope note |
| Read this first | "Not found" meaning | merged-conclusion: How far the searcher's negatives can be trusted |
| 1 | Routine measurement: no utility, 80-85% | merged-conclusion: Bottom line 1 |
| 1 | IR rows limited/research/unsupported; other uses established | usecases-verified: Summary by kind, notes; merged-conclusion: Bottom line 3 |
| 1 | "Shown not to add value" 45-50% | merged-conclusion: Bottom line 2 |
| 2 | Bullet 1 | merged-conclusion: What is well supported |
| 2 | Bullet 2 | merged-conclusion: What is well supported (PCOS); usecases-verified: row 16 |
| 2 | Bullet 3 | merged-conclusion: What is well supported (MASLD) |
| 2 | Bullet 4 | merged-conclusion: Added by chemist runs, Net |
| 2 | Bullet 5 | merged-conclusion: What is well supported (incremental prediction, ATTICA) |
| 2 | Bullet 6 | merged-conclusion: What is well supported (Association is real but modest) |
| 2 | Bullet 7 | merged-conclusion: What is well supported (IRIS); Bottom line 3 |
| 2 | Bullet 8 | merged-conclusion: Trials and interaction; Added by the steelman run (Oncology) |
| 2 | Bullet 9 | usecases-verified: Summary by kind, notes |
| 3 | Each table row | usecases-verified: rows as cited in that row |
| 4 | Each bullet | merged-conclusion: Open gaps 1-4, 6; Added by the steelman run, last bullet and Not tested by anyone; Bottom line 2 |
| 5 | Verification statements | merged-conclusion: Provenance; Open gaps 5, 6; What is well supported (Limits of "no recommendation found"); skeptic-usecases: Part 1 items 1-9, 2.4, 2.6; skeptic-steelman: How I checked; usecases-verified: top note, section 5 intro |
| 5 | Citation check with fresh lookups (added by the main session) | CHANGELOG: full run of the citation checker, 2026-10-19 |
| Practice | Clinician and patient points | merged-conclusion: What is well supported; Added by chemist runs; Bottom line 1; Trials and interaction; usecases-verified: rows 1-7, 15, 16, 28, 31, Summary by kind notes |
| Glossary | Definitions | merged-conclusion: scope note, chemist runs, ATTICA, Open gaps 2, Surrogates are modest; usecases-verified: rows 6, 29; skeptic-steelman: problem 2 |
