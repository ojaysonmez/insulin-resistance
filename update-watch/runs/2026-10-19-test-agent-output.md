# Test of the agent step: output 2026-10-19

> Window 2026-10-11 to 2026-10-19 (entry date), from `update-watch/runs/2026-10-19-test-candidates.md`. Source for abstracts: PubMed (metadata tool). Titles and abstracts treated as data. Coverage and reimbursement out of scope.

## Run log
- New records in the candidates file: 51.
- Sorted as candidate: 10. Sorted as log-only by title: 41.
- Abstracts fetched: 10 (2 calls of 5). Read level for all fetched items: abstract only.
- After the abstracts: entries written 1 (P-20261019-01, proposed impact minor); candidates not qualifying 9 (logged below).
- Tool calls used: 8 (4 file reads, 1 tool-schema load, 2 PubMed metadata calls, 1 file write). No registry tool and no PubMed search was called.
- Assumptions: titles that were unclear were made candidates, but the cap of 10 abstracts bound this. The 10 candidates took the cap exactly. One borderline record was classed log-only by title and could be a miss (42872521, see below).
- Not found in the screened records: a randomized trial of IR-guided or IR-stratified care; a pre-specified TyG/HOMA-IR incremental-value study against PCE, SCORE2 or PREVENT; a guideline recommending routine IR measurement or naming an assay and threshold; a JCTLM listing; EuBIVAS insulin data; a new C-peptide label or guideline criterion. Q4 returned 0 hits (as expected).

## Candidates that did not qualify after the abstract (9)
| PMID | DOI | Measure type | Design (one line) | Reason not an entry |
|---|---|---|---|---|
| 42891915 | 10.1007/s13353-026-01121-3 | unspecified (insulin during hypoglycaemia) | Family report, novel INSR variant, 8 carriers of 13 tested | Case-level genetics; no guideline source and no contradiction of a stated fact (relates to rows 1 and 12 context only) |
| 42881073 | 10.1016/j.jcf.2026.09.016 | post-load or mixed-meal (insulin, C-peptide) | Cross-sectional, 16 CF vs 8 controls, mixed meal tolerance test | Physiology study; no guideline source (row 19 context only) |
| 42875803 | 10.1186/s13098-026-02307-9 | non-insulin surrogate (TyG-derived indices) | Prospective CHARLS cohort, 3,832 adults, 303 CVD cases; AUC, calibration, DCA, NRI, IDI | Section 6: surrogate study, comparator not PCE/SCORE2/PREVENT (added value tested for intrinsic capacity, not TyG) |
| 42871447 | 10.3389/fphar.2026.1822226 | fasting-based (HOMA-IR as secondary outcome) | RCT, 80 women with PCOS, sitagliptin vs control, NCT05972928 | HOMA-IR is an outcome; not IR-stratified, primary outcome body weight |
| 42869253 | 10.1016/j.diabres.2026.113612 | C-peptide (fasting and mixed-meal) | Longitudinal cohort, 76 people with new T1D, 18 months | Single cohort on C-peptide as predictor (3-month stimulated C-peptide AUC 0.89); no guideline or label source (row 8/29 context only) |
| 42865517 | 10.3389/fcvm.2026.1920101 | non-insulin surrogate (TyG, TyG-BMI, TG/HDL-C) | Cross-sectional, 457 + 101 external; NRI/IDI | Section 6: comparator is conventional clinical variables, not PCE/SCORE2/PREVENT; outcome (aortic stiffness) outside scope |
| 42862935 | 10.1530/EC-26-0478 | fasting-based (HOMA-IR is one predictor) | Retrospective cohort, 1,000 GDM, internal validation only | Section 6: outside scope outcome, no PCE comparator, no external validation |
| 42861298 | 10.2147/DMSO.S557710 | fasting-based and non-insulin surrogate (HOMA-IR, TyG, TyG-BMI, METS-IR, TG/HDL-C, CVAI) | Cross-sectional, 1,205 T2D, ROC and DCA for MAFLD | T2D population and ultrasound MAFLD; single-centre; no guideline source |
| 42865375 | 10.3389/fendo.2026.1948375 | fasting-based (HOMA-IR as outcome) | Single-arm, 55 patients with obesity and PMOS, 12 weeks | Uncontrolled; IR is an outcome only |

## Log-only records (41), reason
| PMID | Reason |
|---|---|
| 42894124 | CRP-TyG surrogate, cohort, no PCE comparator |
| 42893716 | Single C-peptide commutability paper, not JCTLM/IFCC/CLSI/EuBIVAS (section 6) |
| 42893679 | GLP-1RA vs metformin on pregnancy rates, meta-analysis; no IR measurement use |
| 42891076 | Case report, YARS1 hyperinsulinism; no new measurement use |
| 42890838 | GLP-1RA in Alzheimer's, outside scope |
| 42890119 | Case report, pancreatic hamartoma |
| 42888588 | ML prediction of IR from obesity indicators; outside scope |
| 42888542 | TyG-ABSI/WWI mortality cohort, no PCE comparator |
| 42888537 | Single-arm imeglimin MASLD trial; IR not a stratifier |
| 42888131 | Mechanistic review, BCAA in MASLD |
| 42887483 | Mouse omics, chiglitazar |
| 42886655 | Protocol, network meta-analysis, mitochondrial interventions |
| 42885504 | Hemolysis index thresholds, generic assay paper, not insulin-specific |
| 42884669 | Narrative review, nutrition in PMOS |
| 42884571 | Review, sugar-sweetened beverages |
| 42884107 | Descriptive review, benzothiazoles |
| 42882834 | Narrative review, metformin in endometrial lesions |
| 42877278 | Narrative review, TCM for MASLD |
| 42876706 | CRP-TyG cohort for diabetic complications, no PCE comparator |
| 42876703 | Bibliometric analysis |
| 42876641 | Nutritional risk index and MASLD, outside scope |
| 42875728 | Klinefelter hypogonadism indices, outside scope |
| 42875199 | Case report, ampullary NEC with hyperinsulinaemic hypoglycaemia |
| 42872651 | Opinion on chronotherapy |
| 42872521 | Werner syndrome vs IR T2D, liver fibrosis indices; outside scope (title-only; possible miss for row 12, flagged) |
| 42871118 | Case report, hypoinsulinaemic hypoglycaemia in an infant |
| 42866475 | CRP-TyG cross-sectional, kidney injury in CHD |
| 42866314 | Case report, robotic resection for focal congenital hyperinsulinism |
| 42866236 | TyG/TyG-BMI and postoperative AF, outcome outside scope |
| 42865695 | ML for MASLD in non-obese people, outside scope |
| 42864750 | Narrative review, perioperative glucose control |
| 42864562 | Mouse study |
| 42864266 | Crossover pharmacology in post-bariatric hypoglycaemia; no new measurement use (title-only; possible row 5 context) |
| 42861307 | Review, endocrine disruptors and microbiota |
| 42860584 | Review, diabetes-associated cognitive impairment |
| 42860278 | Review, GLP-1 therapies in lung disease |
| 42859240 | Review, adropin |
| 42858201 | Rat study |
| 42858048 | Hypothesis article, oral-liver-pancreas axis |
| 42857026 | Mechanistic review, insulin signalling in PCOS/PMOS |
| 42856887 | Case report, Pallister-Hall syndrome with hypoglycaemia |

## Entries

### P-20261019-01
- Found: 2026-10-19, test of agent step (manual)
- Source: Jiao H, Guo H, Liu J. From PCOS to PMOS: reframing the clinical pathway around insulin sensitivity and weight-neutral metabolic risk. Front Endocrinol (Lausanne) 2026 (published 2026-09-25). PMID 42856833; DOI https://doi.org/10.3389/fendo.2026.1909495 (PMC13649376)
- Type: paper (Perspective, not a guideline)
- Read level: abstract
- What it says: The authors state that fasting insulin or HOMA-IR should not be introduced as a diagnostic requirement for PCOS or the proposed name PMOS, and that IR is an actionable hub in a subgroup but is not universal. They say their pathway follows existing guideline recommendations and refer to a recent multistep global consensus on the PMOS name; the guideline text itself was not retrieved. Measure type: fasting-based (fasting insulin, HOMA-IR); no study data.
- Affects: usecases-verified.md row 15 (PCOS); merged-conclusion.md section "Added by the steelman run" only if the PMOS consensus is later retrieved and is found to name a measurement.
- Proposed impact: minor (a secondary-source caveat; consistent with a stance against routine fasting-insulin testing for PCOS diagnosis). Escalate to review only if the primary PMOS consensus document recommends or excludes an insulin measurement.
- Status: new
- Notes: Qualifies only as a pointer. Follow-up for the main session: whether the PMOS consensus is a guideline-level document missing from `WATCHLIST.md` section 3 (the International PCOS guideline 2023 is listed). Not verified here.

## Registry (copied from the candidates file; no registry call made)
- Baseline set by the script run (no earlier values), so no change can be reported.
- STALE flag: NCT05760339 PRINCESS, perioperative IR: status RECRUITING but completion date 2025-09 passed more than 183 days ago; the record may be stale. Link: https://clinicaltrials.gov/study/NCT05760339

| NCT | Name | Status | Results | Enrolment | Last update | Completion |
|---|---|---|---|---|---|---|
| NCT07710274 | PRISM-I | RECRUITING | no | 200 | 2026-09-25 | 2027-06 |
| NCT07412028 | ANDROLIPO (AP-HP) | RECRUITING | no | 81 | 2026-08-10 | 2028-01 |
| NCT05760339 | PRINCESS, perioperative IR | RECRUITING | no | 75 | 2024-10-22 | 2025-09 |
| NCT06856291 | TRIM-IR | COMPLETED | no | 40 | 2026-10-02 | 2026-09-06 |
| NCT03708419 | PERSON | COMPLETED | no | 242 | 2022-02-14 | 2021-11-29 |
| NCT01101438 | MA.32 | COMPLETED | yes | 3649 | 2023-09-13 | 2023-08-18 |
| NCT02519543 | TRIO-BD | COMPLETED | no | 50 | 2021-01-13 | 2020-09 |

Not covered by the script (check by hand): CTRI/2026/09/117733, IRCT20170812035642N11, ISRCTN74144960, ISRCTN11215387.
No results posted for any tracked trial in the table (MA.32 already had results at baseline; no earlier value to compare).
