# Dossier, row 7: C-peptide or UCPCR triage before MODY genetic testing

Stage 3 (D-32). Written 2026-10-23. Reads: `usecases-verified.md` row 7, `usecases/scoring/ranking.md`, V1-V5 JSON entries for row 7, `usecases/scoring-rubric.md`. No deliverable or score file edited. Confidence figures are judgements. Measure type: serum C-peptide (random, fasting or post-meal) and post-meal urinary C-peptide:creatinine ratio (UCPCR). Classification use (no insulin-resistance index involved).

Current scores (from V1-V5): D1 2, D2 3, D8 3, D3 2, D4 2, D5 2, D6 3, D7 3 (bin 2 or 3, low), S 1 (V4) vs 2 (V5). Ranking: rank 4, tier B, composite 0.576.

## 1. The decision and who makes it
Decision: which antibody-negative, young-onset or atypical diabetes patients get a monogenic (GCK, HNF1A, HNF4A, etc.) gene panel. The result changes the order of testing; it does not by itself set the diagnosis. Decision makers: pediatric or adult endocrinologists and diabetes genetics/precision-diabetes clinics (specialist outpatient). Primary care and pediatricians suspect it and refer. Downstream effect: sulfonylurea instead of insulin for HNF1A/4A, no treatment for GCK, cascade testing of relatives.

## 2. Evidence table
| PMID | DOI | Design | n | Finding | Read level (this session) |
|---|---|---|---|---|---|
| 37794142 | 10.1038/s43856-023-00369-8 | Systematic review plus expert opinion (PMDI 2023) | 100 studies (Q1) | Four who-to-test recommendations; abstract does not name C-peptide | Abstract (metadata re-fetched); full text per project file only |
| 40640995 | 10.5694/mja2.52717 | ANZ joint-society consensus 2025 (adults) | consensus | Test if onset <30 y without markers of T1D/T2D, or high probability by validated tool; more than 80% undiagnosed or misdiagnosed | Abstract; full text per project file only |
| 36537518 | 10.1111/pedi.13426 | ISPAD 2022 guideline | consensus | Monogenic diabetes in children; no abstract in PubMed record; C-peptide wording unread | Title/metadata only here; full text (stripped lists) per project file |
| 21270186 | 10.2337/dc10-1293 | Case-control, UK adults, diabetes >=5 y, no renal impairment | HNF1A 54, HNF4A 23, GCK 20, T1D 69, T2D 54 | Post-meal UCPCR >=0.2 nmol/mmol: HNF1A/4A MODY vs T1D 97% sens, 96% spec, AUC 0.98; vs T2D AUC 0.64 | Abstract |
| 23289766 | 10.1111/pedi.12008 | Cross-sectional, UK pediatric | 264 (T1D 160, T2D 41, MODY 63) | UCPCR >=0.7 after >2 y separates non-T1D (MODY+T2D) from T1D (100%/97%, AUC 0.997); MODY vs T2D AUC 0.57 | Abstract |
| 25792383 | 10.1159/000375410 | Single-centre, Turkey | MODY 27, T1D 42 | UCPCR >=0.22: 96.3%/85.7%; fasting C-peptide 0.62 ng/mL: 93%/90% | Abstract |
| 32052124 | 10.1007/s00431-020-03606-7 | Single-centre, Egypt | T1D 50, T2D 30 | UCPCR >=0.28: 97%/88% (T2D vs T1D, not MODY) | Abstract |
| 41086125 | 10.2337/dc25-1029 | Prediction-model development plus external validation (Exeter calculator update) | 594 MODY + 597 non-MODY; recalibration n=1,299; validation n=1,025 | Early-insulin-treated: AUC 0.98 with C-peptide + antibodies vs 0.80 clinical only; at >=5% probability, positive genetic-test rate 16-19%; stated valid for White European, diagnosed <=35 y | Abstract |
| 34362814 | 10.2337/dc21-0491 | ProDiGY, exome sequencing, multiethnic US youth with presumed T2D | 3,333 | 2.8% (93) carry LP/P MODY variant; 89% would change management; MODY group had LOWER fasting C-peptide (3.0 vs 4.7 ng/mL); no clinical criterion reliably separated groups | Abstract |
| 36868256 | 10.1016/S2213-8587(23)00025-6 | SEARCH incidence 2002-18 | 18,169 T1D; 5,293 T2D | Denominator for D7 only | Abstract |

PMIDs 37794142, 40640995, 41086125 etc. have DOIs matched to their PubMed records in this session. No PMID without DOI in this table. V1 cites ADA 2026 Standards, PMID 41358893, DOI 10.2337/dc26-s002; not re-verified here.

## 3. Established vs not, by measure type
Established (reasonably):
- Post-meal UCPCR (2 h after largest meal, boric acid) separates HNF1A/4A MODY from long-duration T1D in UK adults (PMID 21270186) and non-T1D from T1D in UK children after >2 y (PMID 23289766). Small case-control cohorts, single country.
- Serum C-peptide plus islet antibodies, combined with clinical features, discriminates monogenic diabetes in early-insulin-treated people, externally validated in a UK cohort (PMID 41086125). C-peptide effect is not separated from antibodies.
- Consensus bodies accept "antibody-negative, young onset" as an indication; ANZ adds validated probability tools.
Not established:
- Any benefit of C-peptide or UCPCR over antibodies plus age/BMI in a prospective pathway (yield, treatment change).
- Use in the T2D-phenotype branch: UCPCR cannot separate MODY from T2D (AUC 0.64 and 0.57). In ProDiGY, youth with MODY had lower fasting C-peptide than other presumed-T2D youth, so a "preserved C-peptide" rule does not apply there and the direction is untested as a triage rule.
- Fasting vs random vs post-meal serum thresholds for MODY triage: only a single-centre fasting cut-off (0.62 ng/mL, PMID 25792383).
- US multiethnic validation: none found (searches below).
- The "PPV 20%" in row 7: not traceable to any abstract read here. See section 4.

## 4. Three weakest points in the current scores
1. D2 = 3 and the row's "PPV 20% (quoted)". The figure has no retrievable source in this session. Nearest verified numbers are the 16-19% positive-test rate at >=5% calculator probability (PMID 41086125) and the 2.8% ProDiGY prevalence. If 20% came from a different pathway, the pathway definition is missing. What would change it: locating the primary source; if none, D2 should be 2 (observational accuracy, no pathway outcome) per clarification 8 logic. Judgement: 55% chance D2 should fall to 2 if source cannot be found.
2. D8 = 3 and D1 = 2 rest on the C-peptide-plus-antibody pair, not C-peptide alone (PMID 41086125), in White European, UK data. Anchor 19 requires data on reclassification given alternatives; none isolates C-peptide's added yield over antibodies. What would change it: a head-to-head in one cohort of antibodies + age/BMI vs + C-peptide/UCPCR, reporting net reclassification and yield. D8 could be 2.
3. D7 = 3 and S 1 vs 2 (V4 vs V5 disagree). D7 chain rests on unsourced 5-10% shares (V1 itself says bin 2 or 3). S depends on whether C-peptide is the only triage available. What would change it: a sourced US count of antibody-negative youth/young adults with non-obese, non-T2D-typical diabetes (SEARCH or T1D Exchange plus Kaiser data) and ProDiGY-style yield per stratum.
Also note D3 = 2: ADA does not name C-peptide in the MODY recommendation (per V1). ISPAD wording unread. Reading ISPAD 2022 full text could move D3 to 2 (confirmed) or 3 only if it recommends the test.

## 5. Viability pathway
- Design: prospective, consecutive, multi-centre diagnostic-yield study with a pre-specified pathway. Enrol US youth and young adults (age 6-35) with diabetes >2 y (stratify <3 y vs >=3 y), antibody-negative (GAD, IA-2, ZnT8), not obese or with family history. All receive serum C-peptide (random with paired glucose, and 2 h post-meal), post-meal UCPCR (home kit), and a full MODY gene panel (reference standard, not only test-positives, to avoid verification bias). Prespecified comparison: antibodies + age/BMI + family history (and the Exeter calculator) vs the same plus C-peptide/UCPCR.
- Population: US multiethnic (non-Hispanic Black, Hispanic, Asian, American Indian, White), because the Exeter calculator is validated for White Europeans only and ProDiGY shows presumed-T2D prevalence in a multiethnic group.
- Targets: PPV for a pathogenic variant of at least 20-25% in the test-positive group (versus the 2.8% base rate in presumed T2D and 16-19% for the calculator at 5%); sensitivity at least 90% for HNF1A/4A/GCK; net gain in true positives per 100 genes panels ordered, with lower CI above clinical-only pathway. These targets are my judgement, not guideline values.
- Added yield: report incremental AUC/net reclassification over antibodies + age/BMI, and fraction of panels avoided in test-negative patients; also treatment change (sulfonylurea switch) at 12 months.
- Assay availability: serum C-peptide is a standard US lab test (harmonisation across platforms is the open item). UCPCR: US commercial send-out availability not verified here; the cited studies used a UK reference lab. Need a US lab-validated UCPCR (CLIA) with boric-acid collection and a cut-off per assay, or restrict to serum C-peptide.
- Guideline target: ADA Standards of Care MODY recommendation (2.29b, per V1) to name biomarker-assisted selection; ISPAD update; endorsement by a US precision-diabetes body.
- Rough size and time: with an expected 10-15% pathogenic rate in the selected group, about 1,000-1,500 participants for adequate precision on PPV and incremental yield (confidence low); 3-4 sites in a SEARCH/ProDiGY-type network; 12 months enrolment plus 12 months follow-up, about 3 years including sequencing and analysis. Cost order: low millions USD (judgement).

## 6. Risks
- Pathway fails to beat antibodies + age/BMI + calculator (probability of no added yield: judged about 40%).
- C-peptide is unsuitable in the T2D-like branch (ProDiGY shows lower, not higher, values; UCPCR AUC 0.57-0.64).
- Early disease (<2-3 y) false low values; renal impairment distorts UCPCR; recent hypoglycemia, stress or exogenous insulin-related timing effects on serum values; sample handling errors in home urine kits.
- Falling gene-panel prices and wider direct genetic testing (including reflex or population sequencing) may make triage unnecessary; this would remove the use. Counterweight: payer rules are out of scope here.
- Ancestry bias in the calculator and thresholds; MODY genes beyond HNF1A/4A/GCK may have different C-peptide behaviour.

## 7. Assumptions and unverified items
- Read level this session: abstract or metadata only for all papers; full text of PMDI 2023, ANZ 2025 and ISPAD 2022 taken from project-file statements, not re-read.
- "PPV 20%" and "fails in first ~3 years": not found in the abstracts read. The pediatric paper (PMID 23289766) states validity after >2 y duration, and PMID 21270186 studied >=5 y. The "~3 y" wording in the row should be checked against full text of PMDI/ANZ.
- ADA 2026 rec 2.29b wording and PMID 41358893 taken from V1, not re-checked.
- D7 shares (adult 20-34 band, 5-10% non-obese antibody-negative) are V1 assumptions.
- US UCPCR commercial availability: unverified.
- Sample size, PPV targets and timeline in section 5 are judgements.
- Searches run (PubMed): "MODY United States youth antibody-negative C-peptide genetic testing yield multiethnic" 0 hits; "SEARCH for Diabetes in Youth maturity-onset diabetes of the young prevalence autoantibody-negative" 0 hits; "ProDiGY monogenic diabetes youth presumed type 2 diabetes prevalence" 1 hit (PMID 34362814). Metadata look-up of 9 PMIDs (all matched DOI). Look-ups used: 4 of 8. Not searched: ClinicalTrials.gov for an active MODY-triage trial, Exeter calculator original paper, US UCPCR laboratory availability.
