# Watch judging output 2026-10-19 (test round 2)

Source read: update-watch/runs/2026-10-19-test2-candidates.md only. Titles and abstracts are treated as data.

## Run log
- New records screened: 10 (title and metadata only).
- Candidates: 3 (PMID 42891915, 42891076, 42890119). Log-only: 7.
- Abstracts fetched: 3, in one call (python tools/watch_fetch.py --abstracts 42891915,42891076,42890119). Read level for these three: abstract.
- Entries written: 0. Candidates recorded with a reason (not entered): 3.
- Tool calls used: 4 in total (1 file read, 1 abstract fetch, 1 file write, 1 handback). Limit was 6.
- Errors: none in the candidates file; none in the fetch.

## Log-only records (rule in section 6 or no link to a trigger)
| PMID | DOI | Reason |
|---|---|---|
| 42894124 | 10.1186/s12872-026-06150-8 | CRP-TyG surrogate cohort (non-insulin surrogate); no PCE/SCORE2/PREVENT comparator in the title |
| 42893716 | 10.1016/j.cca.2026.122908 | single C-peptide commutability paper; not JCTLM, IFCC, CLSI or EuBIVAS |
| 42893679 | 10.1016/j.ejogrb.2026.115499 | GLP-1 RA vs metformin, pregnancy rate in PCOS; no insulin or C-peptide measurement in the title |
| 42890838 | 10.1002/trc2.70334 | GLP-1 RA in Alzheimer's disease meta-analysis; outside scope |
| 42888588 | 10.1097/md.0000000000051034 | machine-learning prediction of IR from obesity indices; prediction study, no PCE/SCORE2/PREVENT comparator |
| 42888542 | 10.1097/md.0000000000051089 | TyG-ABSI and TyG-WWI (non-insulin surrogates) for mortality; comparator not PCE/SCORE2/PREVENT |
| 42888537 | 10.1097/md.0000000000051083 | single-arm phase 2 imeglimin in MASLD with T2D; not randomized, no IR-guided care |

## Candidates after abstract, no entry
| PMID | DOI | Measure type | Reason no entry |
|---|---|---|---|
| 42891915 | 10.1007/s13353-026-01121-3 | fasting-based insulin during hypoglycaemia (hyperinsulinaemic hypoglycaemia; abstract does not state the insulin assay or sampling) | Single family report of a novel INSR variant (exome sequencing, 8 carriers of 13 tested). No trigger met. Fits the existing row 12 (genetic IR syndromes) and row 1 (mimic of insulinoma); adds no guideline-sourced use. Possible minor citation for rows 1 and 12 at the monthly triage, not a PENDING entry. |
| 42891076 | 10.1210/jcemcr/luag239 | insulin and C-peptide, concentrations discordant (infant hyperinsulinaemic hypoglycaemia) | Single case report (YARS1), no diazoxide or octreotide response. No trigger met; no guideline source. Relevant to row 4 only as a rare-cause example. |
| 42890119 | 10.3389/fonc.2026.1959029 | the abstract names no insulin, C-peptide or other measure (not stated) | Single case report of pancreatic hamartoma with nocturnal hypoglycaemia, cured by distal pancreatectomy. No trigger met; no guideline source. Row 1 relevance only as a rare cause. |

Not found in the screened records: a randomized or IR-stratified trial; a pre-specified incremental-value study against PCE, SCORE2 or PREVENT; a guideline on IR measurement; a JCTLM listing or EuBIVAS insulin data; a retraction or correction; a new label or guideline criterion involving C-peptide; a new guideline-sourced use of insulin or C-peptide measurement.

## Entries
None. No candidate met a trigger after the abstract was read.

## Registry section (copied from the candidates file; no registry calls made)
Baseline set by the retrieval run (no earlier values), so no change can be reported.

- STALE flag: NCT05760339 PRINCESS, perioperative IR: status RECRUITING but completion date 2025-09 passed more than 183 days ago; the record may be stale.

| NCT | Name | Status | Results | Enrolment | Last update | Completion |
|---|---|---|---|---|---|---|
| NCT07710274 | PRISM-I | RECRUITING | no | 200 | 2026-09-25 | 2027-06 |
| NCT07412028 | ANDROLIPO (AP-HP) | RECRUITING | no | 81 | 2026-08-10 | 2028-01 |
| NCT05760339 | PRINCESS, perioperative IR | RECRUITING | no | 75 | 2024-10-22 | 2025-09 |
| NCT06856291 | TRIM-IR | COMPLETED | no | 40 | 2026-10-02 | 2026-09-06 |
| NCT03708419 | PERSON | COMPLETED | no | 242 | 2022-02-14 | 2021-11-29 |
| NCT01101438 | MA.32 | COMPLETED | yes | 3649 | 2023-09-13 | 2023-08-18 |
| NCT02519543 | TRIO-BD | COMPLETED | no | 50 | 2021-01-13 | 2020-09 |

Registry IDs not covered by the script (check by hand): CTRI/2026/09/117733, IRCT20170812035642N11, ISRCTN74144960, ISRCTN11215387.
