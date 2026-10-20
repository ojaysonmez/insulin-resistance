# Judging output 2026-10-19 (test3), window 2026-10-17 to 2026-10-19

## Run log
- New records: 10. Candidates: 4. Log-only: 6.
- Abstracts fetched: 4 (PMIDs 42891915, 42891076, 42890119, 42888588), one call to tools/watch_fetch.py.
- Entries written: 0 (no candidate met a trigger after the abstract was read).
- Tool calls used: 5 (read candidates file, abstract fetch, write, fix-up edit with sed; the final hand-back is not counted). A PostToolUse hook reported a missing tools/deliverable_reminder.py after the write; the file was written and the hook was not investigated.
- Assumptions: the ML IR-prediction title was unclear, so it was treated as a candidate. Read level for all four is abstract only.

## Log-only list (title and metadata only)
| PMID | DOI | Reason |
|---|---|---|
| 42894124 | 10.1186/s12872-026-06150-8 | CRP-TyG surrogate study, comparator not PCE/SCORE2/PREVENT (section 6 rule 2) |
| 42893716 | 10.1016/j.cca.2026.122908 | Single C-peptide control-material commutability paper; not JCTLM, IFCC/CLSI or EuBIVAS (section 6 rule 1) |
| 42893679 | 10.1016/j.ejogrb.2026.115499 | GLP-1 RA vs metformin on pregnancy rates in PCOS; treatment meta-analysis, no insulin/C-peptide measurement |
| 42890838 | 10.1002/trc2.70334 | GLP-1 RA in Alzheimer disease/MCI meta-analysis; outside scope |
| 42888542 | 10.1097/md.0000000000051089 | TyG-ABSI/TyG-WWI mortality cohort; outcome outside deliverables, no PCE/SCORE2/PREVENT comparator (section 6 rules 2, 3) |
| 42888537 | 10.1097/md.0000000000051083 | Single-arm phase 2 of imeglimin in MASLD with T2D; drug efficacy, not a measurement use |


## Candidates read at abstract level, no entry written
| PMID | DOI | Measure type | Decision and reason |
|---|---|---|---|
| 42891915 | 10.1007/s13353-026-01121-3 | Unspecified (hyperinsulinaemic hypoglycaemia reported; no assay or threshold given in abstract) | No entry. Single-family INSR variant report (n=13 tested). Relevant to use-case row 12 (genetic IR syndromes) and row 1 (mimics insulinoma) as a possible citation, but no guideline source and no contradiction of a stated fact. Impact none; optional minor citation for row 12. |
| 42891076 | 10.1210/jcemcr/luag239 | C-peptide and insulin, timing unspecified (abstract notes discordance between insulin and C-peptide) | No entry. Single case of YARS1-related congenital hyperinsulinism (row 4); no guideline source. Impact none. Abstract is short and may be truncated, so details of the discordance are not found in the screened records. |
| 42890119 | 10.3389/fonc.2026.1959029 | Unspecified (nocturnal hypoglycaemia; no insulin or C-peptide values in abstract) | No entry. Case report of pancreatic hamartoma with islet cells causing hypoglycaemia (row 1/22 area). No guideline source. Impact none. |
| 42888588 | 10.1097/md.0000000000051034 | Fasting-based (HOMA-IR in NHANES 2015-2018) as the outcome label; BMI/WHtR as predictors | No entry. Cross-sectional prediction of HOMA-IR >= 75th percentile in 3562 non-diabetic adults, no external validation, no hard outcome and no PCE/SCORE2/PREVENT comparison. Does not meet the incremental-value trigger. Impact none. |

Triggers checked and not found in the screened records: randomized IR-guided trial, pre-specified incremental-value study over PCE/SCORE2/PREVENT, guideline recommending routine IR measurement, JCTLM insulin reference listing, EuBIVAS insulin data, retraction or correction, new C-peptide label or guideline criterion, new guideline-sourced use of insulin or C-peptide measurement.

## Registry section (copied from the candidates file)
Baseline set by this run (no earlier values), so no change can be reported.
- STALE: NCT05760339 PRINCESS, perioperative IR: status RECRUITING but completion date 2025-09 passed more than 183 days ago; the record may be stale.

| NCT | Name | Status | Results | Enrolment | Last update | Completion |
|---|---|---|---|---|---|---|
| NCT07710274 | PRISM-I | RECRUITING | no | 200 | 2026-09-25 | 2027-06 |
| NCT07412028 | ANDROLIPO (AP-HP) | RECRUITING | no | 81 | 2026-08-10 | 2028-01 |
| NCT05760339 | PRINCESS, perioperative IR | RECRUITING | no | 75 | 2024-10-22 | 2025-09 |
| NCT06856291 | TRIM-IR | COMPLETED | no | 40 | 2026-10-02 | 2026-09-06 |
| NCT03708419 | PERSON | COMPLETED | no | 242 | 2022-02-14 | 2021-11-29 |
| NCT01101438 | MA.32 | COMPLETED | yes | 3649 | 2023-09-13 | 2023-08-18 |
| NCT02519543 | TRIO-BD | COMPLETED | no | 50 | 2021-01-13 | 2020-09 |

No posted-result change is reportable (baseline run). MA.32 already shows results "yes" at baseline; whether that was previously known is not found in the screened records.

Registry IDs not covered by the script (check by hand): CTRI/2026/09/117733, IRCT20170812035642N11, ISRCTN74144960, ISRCTN11215387.

## Errors
(none)
