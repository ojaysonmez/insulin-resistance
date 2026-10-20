# Watchlist (draft, not running)

> Paths: this file lives in `update-watch/`. The deliverables (`merged-conclusion.md`, `usecases-verified.md`) are in the project root; reviews are in `reviews/`; reports in `analysis/` and `usecases/`. Other files named here without a folder are in `update-watch/`.

Used by the weekly watch in `UPDATE-PLAN.md`. Edit this file, not the agent prompts, to change what is monitored. Draft 2026-10-19; items come from the project's current deliverables. Search strings are deliberately short (long conjunctions broke in earlier runs). Date-limit each PubMed query by entry date to the window of the run (2 days with 1 day of overlap in the daily pilot, 8 days in a weekly run). Record the count and how many records were screened. The machine-readable copy of section 4 is `queries.json`; keep the two in step (the script `tools/watch_fetch.py` reads the JSON file).

## 0. Objective and signal types (D-31, 2026-10-19)
The watch exists to catch a new fact that changes the viability of a use case in `usecases-verified.md`, or that reveals a new candidate use. Since decision D-30 the project's goal is to find and score the most viable uses and what would make the others viable, so the watch is aimed at each use's path to viability (the missing piece recorded in the scoring) and not at re-checking the clinical-utility conclusion for its own sake. Every kept item names the signal type and the row or pathway it affects.

| Signal | What it is | Class |
|---|---|---|
| S1 Guideline, label or regulatory change | A guideline, consensus statement, drug label or regulatory decision that names an insulin or C-peptide test (new recommendation, threshold or eligibility criterion) for a use | review; urgent if it contradicts a row's status |
| S2 Missing piece addressed | A study, trial or registry result that supplies a row's missing piece: external validation of a score, a trial of measurement-guided care, an incremental-value study, accuracy data, an agreed criterion | review |
| S3 Assay or standardisation milestone | A reference material or method listing, harmonisation result, or biological-variation data (for example EuBIVAS insulin values) | review |
| S4 New candidate use | A use of insulin, C-peptide or insulin-resistance measurement not yet in the list, especially post-meal or stimulated, with a guideline or trial source | candidate for the scoring queue (the main session decides whether to add a row, after a skeptic review) |
| S5 Integrity | Retraction or correction of a cited paper | urgent |

Anything else is logged and dropped (section 6). Queries Q1 to Q3 look for S2 on the unlock conditions of the insulin-resistance uses; Q4 for S1; Q5 and Q6 for S3; Q7 to Q13 for S1 or S2 on the rows they name; Q14 to Q17 for S2 and S4 on the closest-to-viable rows (48, 49, 9, 5).

## 1. Retraction and correction check
All PMIDs and DOIs in `merged-conclusion.md` and `usecases-verified.md`. Method: PubMed record title and first author match; Crossref `works/{doi}` field `updated-by` (and `update-to`). Known notices already seen: corrections on EASL-EASD-EASO 2024 (PMIDs 38852583, 38869512), Holt 2021 (34590174), Palmer 2004 (14693724), AACE 2022 (35963508), ERAS bariatric (34984504); DiaPep277 (24757230) retracted and cited only as a do-not-cite note. Flag any new notice.
Highest priority (load-bearing): IRIS 26886418; Spence 2019 30734043; Hu 2024 38191206; Liu 2026 42569452; Xu 2026 42702103; WHI 25944628; ATTICA 41178693; LAMP 42145088; PLIS 34531293; EuBIVAS 38987271; ARIC 29618016; Rohlfing 2025 40802520; Rosli 2022 35622611; Zhou 2022 35177563; Isokuortti 28660493; Gutenberg 34380182.

## 2. Registry watch (status, results, enrolment)
| ID | What | Why it matters |
|---|---|---|
| NCT07710274 | PRISM-I, HOMA-IR 2.5 or more entry and outcome | IR-enriched pilot |
| CTRI/2026/09/117733 | HOMA-IR above 3.8 (men) or 3.46 (women) decides metformin vs voglibose | Only registered trial where an IR value decides treatment |
| IRCT20170812035642N11 | Diet by metabolic profile | IR-stratified |
| ISRCTN74144960 | MET-HFpEF, IR one of three entry routes | HFpEF |
| ISRCTN11215387 | ITT-IR policy trial, Wakayama | Closest to IR-guided care; unpublished |
| NCT07412028 | Hidden severe genetic IR in PCOS (ANDROLIPO / AP-HP) | Severe IR in PCOS |
| NCT05760339 | Perioperative IR, HOMA2-IR day 1 | Research endpoint |
| NCT06856291 | TRIM-IR, observational | Context |
| NCT03708419 | PERSON | Completed; watch for follow-up |
| NCT01101438 | MA.32 | Follow-up analyses |
| NCT02519543 | TRIO-BD | Psychiatry |
New-trial searches (ClinicalTrials.gov, WHO ICTRP): "insulin resistance" with randomized and stratified or selected; "HOMA-IR" eligibility; "insulin-guided" or "IR-guided". Any new randomized trial in which an insulin or IR value decides treatment is class **review**. Stale-record rule: flag a tracked trial whose registered completion date has passed by more than 6 months while its status is still recruiting or active, because the registry will not show that it is probably finished (NCT05760339 at baseline).

## 3. Documents and labels (new version, erratum or changed text on insulin, C-peptide or IR)
ADA Standards of Care (living updates; sections 2, 3, 9, 14), ADA/EASD consensus (adult T1D classification 2021; precision medicine 2023; 2026 T2D consensus, not yet read), AACE (2022; 2026 algorithm, not yet read), EASL-EASD-EASO MASLD (2024), AASLD (2023), International PCOS guideline (2023), Endocrine Society (2017 paediatric obesity, 2009 hypoglycaemia, 2016 lipodystrophy), Pediatric Endocrine Society and International Hyperinsulinism guideline (2023), ISPAD (classification, CFRD, monogenic), JDS criteria (IR syndromes 2022, fulminant and slowly progressive T1D), Igls consensus (2018; Igls 2.0), ENETS (2016), KDIGO (diabetes in CKD), ESC and ACC/AHA prevention guidelines, AHA cardio-kidney-metabolic advisory, AAP obesity (2023), FDA Tzield label (rev 06/2026) and EMA record, JCTLM database (insulin reference method or material listing).
Highest-value changes: any recommendation that names an insulin or HOMA-IR measurement or threshold (class **review**); a JCTLM listing for insulin (changes the measurement section); a new label criterion for C-peptide (changes use-case rows 8, 29, 30).

## 4. PubMed queries (last 8 days, short strings)
| # | Query | Looking for | Triggers |
|---|---|---|---|
| Q1 | "HOMA-IR" AND ("C-statistic" OR "reclassification" OR "decision curve") | Incremental value over standard predictors | Bottom line 2 |
| Q2 | "triglyceride-glucose" AND ("C-statistic" OR "reclassification" OR "decision curve") | TyG incremental value | Bottom line 2 |
| Q3 | "insulin resistance" AND (randomized OR trial) AND (HOMA OR stratified OR interaction) | IR-stratified or interaction analyses | Bottom lines 1-2 |
| Q4 | ("fasting insulin" OR "HOMA-IR") AND (guideline[ti] OR consensus[ti] OR "position statement"[ti]) | New recommendations | Bottom line 1 |
| Q5 | insulin AND (harmonization OR commutability OR "reference measurement" OR "reference material" OR "reference method") | Assay standardisation | Measurement section |
| Q6 | ("biological variation" OR EuBIVAS) AND (insulin OR "C-peptide") | Variability data (EuBIVAS insulin values still missing) | Measurement section |
| Q7 | "C-peptide" AND (classification OR teplizumab OR "mixed meal") | C-peptide uses | Use-case rows 6-10, 29-33, 46-47 |
| Q8 | pioglitazone AND "insulin resistance" | IRIS follow-up | Row 13 |
| Q9 | MASLD AND ("insulin resistance" OR HOMA-IR) AND (guideline OR consensus OR trial) | MASLD recommendations or trials | Row 14 |
| Q10 | PCOS AND "insulin resistance" AND metformin | PCOS | Row 15 |
| Q11 | insulin AND hypoglycaemia AND (guideline OR consensus) | Hypoglycaemia work-up | Rows 1-5 |
| Q12 | "congenital hyperinsulinism" OR "hyperinsulinaemic hypoglycaemia" OR "hyperinsulinemic hypoglycemia" | Congenital and acquired hyperinsulinism | Rows 4, 24-26 |
| Q14 | ("postprandial hypoglycemia" OR "reactive hypoglycemia") AND ("mixed meal" OR "meal test") | Reactive hypoglycaemia work-up | Row 48 |
| Q15 | "C-peptide" AND "oral glucose tolerance" AND "type 1 diabetes" AND (progression OR "risk score") | Type 1 risk staging by OGTT C-peptide | Row 49 |
| Q16 | ("type 3c diabetes" OR "pancreatogenic diabetes" OR "diabetes of the exocrine pancreas") AND ("C-peptide" OR classification) | Type 3c classification | Row 9 |
| Q17 | ("post-bariatric hypoglycemia" OR "postbariatric hypoglycemia") AND (diagnosis OR consensus OR guideline) | Post-bariatric hypoglycaemia criteria | Row 5 |
| Q13 | "insulin resistance" AND ("Mendelian randomization" OR trial) AND (cancer OR dementia OR depression) | Oncology and psychiatry signals | Steelman section |
If a query returns zero hits, rerun a shorter variant before logging a negative; log both strings. Notes from the dry run of 2026-10-19: do not use `randomized[pt]` or other publication-type tags for new records (types are added days after entry; use free-text words); do not use the bare word `standardization` (PubMed maps it to `standard`); the bare term `hyperinsulinism` explodes to insulin-resistance papers; Q4 is expected to return zero most weeks, which is normal for guidelines; if a query returns more than about 60 hits, rewrite the string instead of screening the top 25.

## 5. Triggers that need a full review
| New item | Claims affected | Class |
|---|---|---|
| Randomized trial of IR-measurement-guided care vs usual care, or an IR-stratified trial with hard outcomes | Bottom lines 1 and 2 | review |
| Pre-specified incremental-value study of HOMA-IR or TyG over PCE, SCORE2 or PREVENT with calibration and decision curve, external validation | Bottom line 2 | review |
| Guideline recommending routine IR measurement, or naming an assay and threshold | Bottom line 1; guideline section | review |
| JCTLM-listed insulin reference method or certified reference material | Measurement section | review |
| EuBIVAS insulin biological-variation values published or retrieved | Measurement section | review |
| Retraction or correction of a load-bearing paper | Any statement citing it | urgent |
| Result posted for a tracked trial | The row's claim | review |
| New label or guideline criterion involving C-peptide | Use-case rows 8, 29, 30 and others | review |
| New use of insulin or C-peptide measurement with a guideline source | Use-case list | minor or review |

## 6. Log only, no PENDING entry (added 2026-10-19 after the dry run)
These are recorded in the run log with PMID and a one-line reason but do not become entries in `PENDING.md`, because the dry run showed they only produce items the first reviewer rejects:
- A single paper on C-peptide or insulin assay standardisation or commutability that is not a JCTLM listing, an IFCC or CLSI standard, or EuBIVAS insulin data.
- A TyG, TyG-BMI, CRP-TyG or similar surrogate study whose comparator is not PCE, SCORE2 or PREVENT, whatever its net-reclassification result.
- A cohort or prediction study of HOMA-IR or TyG for an outcome outside the deliverables' scope.
A paper moves from log-only to an entry if it contradicts a stated fact in the deliverables or adds a new use of insulin or C-peptide measurement with a guideline source.
