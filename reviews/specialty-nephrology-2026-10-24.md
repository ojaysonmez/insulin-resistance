# Specialty review: nephrology (2026-10-24)

Reviewer role: specialty reviewer (nephrology), subagent run. Inputs read: `merged-conclusion.md` (whole file, including the scope note), the kidney-related rows of `usecases-verified.md` (rows 1, 2, 7, 10, 11, 27, 28, 33 and the status notes that mention renal failure, KDIGO and OPTN), `reviews/scope-audit.md` (sections 1-3 and the matrix), and, for already-corrected claims, the kidney- and eGDR-related passages of `reviews/skeptic-merged.md`, `reviews/skeptic-steelman.md` and the OPTN passage of `reviews/skeptic-usecases.md`. No other specialty report was read. No deliverable, score or claims file was edited.

Search budget: 20 look-ups (PubMed connector, Parallel web search/fetch), all used; each tool call counts as one look-up, including metadata and full-text fetches. Local text scanning of fetched documents did not count.

Measure tags used below: FASTING (fasting insulin, HOMA-IR, QUICKI), POSTLOAD (OGTT- or meal-derived insulin indices), SURROGATE (TyG, TG/HDL-C, eGDR: no insulin assay), CPEPTIDE, CLAMP. Confidence figures are judgements, not computations.

Assumptions recorded:
- A1. "Kidney-related rows" taken as rows 1, 2 (renal failure caveats in hypoglycaemia work-up), 7 and 33 (UCPCR and renal impairment), 10 and 27 (graft function), 11 (CKD caveat), 28 (C-peptide in CKD).
- A2. The "OPTN C-peptide criterion" is read as the kidney-pancreas waiting-time qualifying criterion (Policy 11.3.B) and the pancreas/kidney-pancreas registration criteria (Policy 11.2), current and historical.
- A3. "SGLT2 subgroup analyses by IR surrogates" covers SGLT2 inhibitor kidney-outcome trials (CREDENCE, DAPA-CKD, EMPA-KIDNEY) with any HOMA-IR, TyG or eGDR subgroup.
- A4. Where a PubMed record gave no DOI or a field was empty, that is stated.

## 1. Documents checked, with read levels

| Document | Identifiers (verified on PubMed or at source) | Read level |
|---|---|---|
| KDIGO 2022 Clinical Practice Guideline for Diabetes Management in CKD | PMID 36272764, https://doi.org/10.1016/j.kint.2022.06.008 (PubMed abstract field empty). Kidney Int 2022;102(5S):S1-S127. PDF at kdigo.org | Full PDF text obtained (595,638 characters, through the last reference, page S127) and term-scanned for 20 terms; plus targeted excerpt extraction. Not read end to end. |
| ADA-KDIGO consensus report, Diabetes management in CKD, 2022 | PMID 36189689, https://doi.org/10.2337/dci22-0027 (PMC9870667) | Abstract only |
| 2026 AHA/ACC/ADA/ASN CKM guideline | PMID 42265997, https://doi.org/10.1016/j.jacc.2026.03.056 (PMC13399222) | PubMed record only (title, abstract); not re-scanned (the team already regex-scanned it) |
| International consensus on post-transplantation diabetes mellitus (Sharif 2024) | PMID 38171510, https://doi.org/10.1093/ndt/gfad258 (PMC11024828) | PMC full text obtained (47,910 characters) and term-scanned; the eight opinion-statement headings and the passages around every hit read |
| OPTN Policies effective 2026-10-01 (HRSA), Policy 11.2 and 11.3 | https://www.hrsa.gov/sites/default/files/hrsa/optn/optn_policies.pdf | Targeted excerpt extraction of sections 11.1-11.3.D (verbatim policy text returned); not read end to end |
| UNOS news, "Removing BMI and C-peptide from kidney/pancreas waiting time criteria", 2019-07-11 | https://unos.org/news/removing-bmi-and-cpeptide-from-kidney-pancreas-waiting-time-criteria | Search excerpt only |
| HRSA/OPTN Kidney-Pancreas Allocation System FAQ (2014 system) | https://www.hrsa.gov/optn/professionals/resources/kidney-pancreas/kidney-pancreas-allocation-system-frequently-asked-questions | Search excerpt only |
| OMB/OPTN Adult Kidney-Pancreas Candidate Registration form instructions | https://omb.report/icr/202506-0915-004/doc/159331301.pdf | Search excerpt only |
| Ebert 2024, FIDELITY by eGDR | PMID 38151465, https://doi.org/10.2337/dc23-1420 (PMC10909685) | Abstract |
| Jia 2014, surrogate indices vs clamp with and without CKD (ULSAM) | PMID 24476695, https://doi.org/10.1038/ki.2014.1 | Abstract |
| de Boer 2016, glucose and insulin homeostasis in moderate-severe CKD | PMID 26823551, https://doi.org/10.1681/ASN.2015070756 (PMC5004653) | Abstract |
| Huber 2020, tubular secretory clearance and whole-body insulin clearance | PMID 32785690, https://doi.org/10.1210/clinem/dgaa522 | Abstract (end section) |
| van Baar 2022, whole-body insulin clearance in T2D with normal kidney function | PMID 35221224, https://doi.org/10.1016/j.jdiacomp.2022.108166 | Abstract (end section) |
| Hung 2011, IR indices vs clamp in African American haemodialysis patients | PMID 21441124, https://doi.org/10.2215/CJN.08070910 | Abstract |
| King-Morris 2015, IR indices vs clamp in peritoneal dialysis | PMID 26526047, https://doi.org/10.3747/pdi.2013.00296 | Abstract |
| Kobayashi 2000 (first author not checked), clamp before and after HD/CAPD | PMID 10607769, https://doi.org/10.1093/ndt/15.1.65 | Abstract |
| D'Elia 2019, glucose/C-peptide ratio by renal function | PMID 30794834, https://doi.org/10.1016/j.diabres.2019.02.015 | Abstract (already in row 28) |
| Zhou 2022, UCPCR by renal function in T2D | PMID 36465621, https://doi.org/10.3389/fendo.2022.1052794 | Abstract (already in row 28) |
| Besser 2011, UCPCR for HNF1A/HNF4A MODY | PMID 21270186, https://doi.org/10.2337/dc10-1293 | Abstract (first part) |
| Gurram 2021, pretransplant C-peptide and SPK outcomes | PMID 34599533, https://doi.org/10.1111/ctr.14498 | Abstract |
| Rohan 2018, type 1 vs type 2 diabetes pancreas transplant outcomes | PMID 30501589, https://doi.org/10.6002/ect.2017.0296 | Abstract |
| Williamson 2025, C-peptide trajectory after pancreas transplant | PMID 40190934, https://doi.org/10.7759/cureus.80103 | Abstract (partial) |
| Fragoso 2015, HOMA-IR and CV morbidity/ESRD in diabetic CKD | PMID 26066409, https://doi.org/10.1016/j.jdiacomp.2015.05.010 | Abstract |
| TyG and incident CKD meta-analyses: Zhang 2025; Wang 2025; Ren 2023; 40562097 (2025) | PMID 41162198, https://doi.org/10.1080/0886022X.2025.2572356; PMID 40623418, https://doi.org/10.1055/a-2634-0157; PMID 37088649, https://doi.org/10.1016/j.numecd.2023.03.026; PMID 40562097, https://doi.org/10.1016/j.clnesp.2025.06.028 | Abstracts |
| Tuo 2025, TyG and outcomes in CKD patients (meta-analysis) | PMID 39915738, https://doi.org/10.1186/s12882-025-03984-w | Abstract |

Identifier note: PMID 36243226, which I first queried as KDIGO 2022 from memory, is a proton whole-lung irradiation paper. The correct KDIGO 2022 PMID is 36272764. This PMID does not occur anywhere in the repository (grep), so nothing needs correcting; it is recorded so no later run reuses it.

## 2. Claims checked and verdicts

| # | Claim (location) | Measure type | Source checked | Verdict | Reason |
|---|---|---|---|---|---|
| C1 | Bottom line 1: no established utility for routine fasting insulin, HOMA-IR or TyG/TG-HDL-C; risk tools in use take no IR input; the 2026 CKM guideline (AHA/ACC/ADA/ASN) does not recommend measuring them (merged L10) | FASTING, SURROGATE | KDIGO 2022 full-text term scan; PTDM consensus 2024 full-text term scan; ADA-KDIGO 2022 abstract | **Holds; nephrology adds support** | KDIGO 2022 (595,638 characters scanned): "C-peptide" 0 hits; "fasting insulin" 0; "HOMA" 0 true hits (5 substring hits are inside author names such as "Thomas"); "TyG", "triglyceride-glucose", "eGDR", "glucose disposal", "insulin clearance", "hyperinsulin", "metabolic syndrome" 0; "insulin resistance" 2 hits, both in reference titles (refs 303, 304); "insulin sensitivity" 3 hits, all narrative (sodium intake, physical activity, a reference title). The one sentence on insulin levels is about drugs, not a test: "Risk of hypoglycemia is high in patients with advanced CKD who are treated by glucose-lowering agents that raise blood insulin levels (exogenous insulin, sulfonylureas, meglitinides)." The PTDM consensus recommends OGTT-based glucose screening (Opinion Statement 1, starting on the waiting list), with "HOMA" 0 hits and fasting insulin only as an endpoint in trial tables. Scan-level negative, not a reading. |
| C2 | "Documents not read in full: ... NICE, KDIGO and ISPAD (Set B)" (merged L24; open gap 5) | n/a | KDIGO 2022 PDF | **Needs update** | KDIGO 2022 is now full-text term-scanned (whole document, references included), not read end to end. Move it from "not read" to "full text term-scanned, no insulin, HOMA-IR, C-peptide or TyG measurement found". |
| C3 | "eGDR-based analyses (FIDELITY, FINEARTS-HF) use clinical variables ... The FIDELITY eGDR formula was not checked." (merged L88) | SURROGATE (eGDR) | Ebert 2024, PMID 38151465, abstract | **Needs correction (now checked)** | The abstract says eGDR was "calculated using waist circumference, hypertension status, and glycated hemoglobin for 12,964 patients"; median 4.1 mg/kg/min. Below-median eGDR carried more cardiovascular events but "was not associated with kidney outcomes". No heterogeneity of finerenone's effect: cardiovascular HR 0.81 (0.72-0.92) below median vs 0.92 (0.79-1.06), P interaction 0.23; kidney HR 0.84 (0.68-1.02) vs 0.70 (0.58-0.85), P interaction 0.28. The evidence searcher's report already had this; the merged file did not carry it. In a CKD trial, the surrogate predicted no kidney outcome. |
| C4 | "Insulin therapy and analogue cross-reactivity make insulin- and C-peptide-based indices uninterpretable" (merged L48) | FASTING, CPEPTIDE | de Boer 2016; Huber 2020; van Baar 2022 (abstracts) | **Missing caveat** | Reduced kidney function is a third interpretive limit. In nondiabetic CKD (mean eGFR 37.6), clamp insulin sensitivity was lower (3.9 vs 5.0 mg/min per µU/mL) and insulin clearance was lower (876 vs 998 mL/min); clearance correlated with sensitivity (r = 0.72) (PMID 26823551). A high fasting insulin or HOMA-IR in CKD therefore mixes lower clearance with lower sensitivity. The kidney's share of whole-body insulin clearance appears modest outside advanced CKD (each 20% lower eGFR: 13 mL/min lower clearance, PMID 32785690; no association with GFR when kidney function is normal, PMID 35221224), so the distortion is larger for C-peptide (row 28) than for insulin. No study found quantifies the error in HOMA-IR by eGFR stage. |
| C5 | Surrogate validity: "HOMA-IR versus clamp: r about -0.82 and category agreement kappa 0.63" (merged L34) | FASTING, POSTLOAD, CLAMP | Jia 2014; Hung 2011; King-Morris 2015 (abstracts) | **Missing caveat (population)** | The general-population figures do not establish validity in kidney disease, but the CKD data do not overturn them. In 1,074 Swedish men aged 70 (495 with eGFR <60, median 46), "all ISIs provided satisfactory (weighted κ over 0.6)" agreement with the clamp, OGTT-derived indices agreed better than fasting ones, and all discriminated clamp-defined IR (GDR <4 mg/kg/min) (PMID 24476695). In dialysis the data are tiny and conflict: haemodialysis, n=12, HOMA-IR and QUICKI "reasonable alternatives" (PMID 21441124); peritoneal dialysis, n=10, "HOMA-IR and QUICKI failed to have strong predictive value" (PMID 26526047). Dialysis itself changes clamp GDR (6.5 to 9.7 mg/kg/min after starting HD, n=10; PMID 10607769), so one value before dialysis does not carry over. |
| C6 | "Association is real but modest" (merged L32) | FASTING, SURROGATE | Jia 2014; Fragoso 2015; TyG meta-analyses; Tuo 2025 | **Holds; add the CKD evidence, which is association only** | TyG and incident CKD: pooled RR 1.44 (1.33-1.56; 12 cohorts, n=58,838; PMID 41162198); 1.52 (PMID 40623418); 1.47 (PMID 37088649); 1.67 (PMID 40562097). Within CKD, TyG and all-cause mortality HR 1.22 (1.13-1.31; 12 studies, n=26,530; PMID 39915738). None of these abstracts reports incremental value over eGFR, UACR or a kidney-failure risk equation. HOMA-IR in CKD: one cohort of 119 (PMID 26066409; ESRD OR 1.034 with a reported CI of 1.005-1.650, asymmetric as printed). Against: in ULSAM, "Neither HEGC nor ISIs independently predicted mortality" over 10 years, with or without CKD (PMID 24476695), and in FIDELITY eGDR did not predict kidney outcomes (C3). |
| C7 | Use-case row 28 (C-peptide in CKD): research-only; "falsely elevated in renal impairment; correction methods 'poorly validated'"; UCPCR ≤1.13 nmol/g, AUC 0.978, n=85; "No guideline on CKD adjustment retrieved. KDIGO 2022 abstract blank." | CPEPTIDE | Zhou 2022 and D'Elia 2019 abstracts (re-read); KDIGO 2022 full-text scan | **Holds; one caveat to add; KDIGO negative now stronger** | KDIGO 2022 contains no C-peptide statement at all (0 hits in full text), so "no guideline" is now a full-text scan negative for KDIGO, not just an abstract negative. Caveats from the Zhou abstract: single centre, n=85; fasting serum C-peptide "was uncorrelated with 24hUCP" when eGFR was 60 or lower; the reference standard for "severe insulin deficiency" is not given in the abstract; cutoff derived and tested in the same sample. D'Elia: lower glucose/C-peptide ratios when eGFR was 49 or lower, which the authors link to hypoglycaemia risk with secretagogues; this is an association in 87 clinic patients, not a validated dosing tool. The "about half of C-peptide is cleared by the kidney" figure was not re-verified here. |
| C8 | Rows 7 and 33 (UCPCR for MODY and paediatric reclassification): "renal impairment" as a limit | CPEPTIDE | Besser 2011 abstract | **Holds** | The UCPCR derivation cohort was explicitly "without renal impairment" (PMID 21270186), so the published UCPCR cutoffs have not been validated in CKD. |
| C9 | Row 10 (Igls graft function): "kidney dysfunction raises it" | CPEPTIDE | D'Elia, Zhou (direction only) | **Holds (direction); missing nephrology caveat** | Most whole-pancreas grafts are implanted with a kidney (simultaneous pancreas-kidney). Kidney-graft dysfunction or rejection will change serum C-peptide independently of beta-cell graft function; no source here quantifies this ([recall] for the clinical point; the direction is sourced). Igls numeric thresholds should not be read without the concurrent eGFR. |
| C10 | Skeptic-usecases note: OPTN kidney-pancreas waiting time once required insulin plus C-peptide ≤2 ng/mL (or >2 with BMI at or below the maximum); removed 2019-07-11; "needs a primary read" (reviews/skeptic-usecases.md; merged open gap 5 "OPTN Policy 11 text" unread) | CPEPTIDE | OPTN Policies effective 2026-10-01 (excerpts); UNOS news 2019; HRSA FAQ; OMB form | **Holds, now primary-sourced; still a withdrawn use** | Current Policy 11.2.B: each kidney-pancreas candidate "must be diagnosed with diabetes or have pancreatic exocrine insufficiency with renal insufficiency". Current 11.3.B (age 18 or older): waiting time starts when the candidate is registered for kidney-pancreas, qualifies for kidney waiting time under Policy 8, and "is on insulin". No C-peptide criterion. UNOS (2019-07-11): BMI and C-peptide removed from kidney-pancreas waiting-time criteria; "C-peptide will no longer be factored into waiting time eligibility, it will continue to be a required field for data collection." The OMB registration form still asks for the candidate's C-peptide value in ng/mL. The HRSA FAQ gives the 2014 criteria (on insulin with C-peptide ≤2 ng/mL, or >2 ng/mL with BMI at or below the maximum allowable). Islet registration (11.2.C) uses insulin dependence or HbA1c above 6.5%, not C-peptide. Status: a **withdrawn regulatory use; registry data field only**. Read level: policy excerpts plus secondary excerpts. |
| C11 | "No randomized trial comparing IR-measurement-guided care with usual care was found" (merged L60) | FASTING, SURROGATE | Nephrology search (S10, S11 below) | **Holds within this search; search-limited** | No CKD, dialysis or transplant trial allocating care by an IR value turned up. Registries (ClinicalTrials.gov, ICTRP) were not searched for CKD-specific trials within this budget. |
| C12 | Merged L105 lists heart-failure trials stratified by eGDR as existing (FINEARTS-HF) under "not tested by anyone" | SURROGATE | Ebert 2024 | **Missing item** | FIDELITY (CKD with T2D, n=12,964) belongs next to FINEARTS-HF as a large eGDR-stratified post hoc analysis with a null interaction for both cardiovascular and kidney outcomes. |
| C13 | IRIS / ADA 3.13 / AACE R 9.4 pioglitazone-for-IR niche (merged L15, L33) | FASTING | KDIGO 2022 scan | **Holds; caveat for CKD** | KDIGO 2022 lists thiazolidinediones only as options in a drug-choice figure and in evidence tables (11 hits, all tables or figure labels); it gives no IR-based selection rule. Whether IRIS enrolled or excluded people with reduced eGFR was not checked here. Applying the HOMA-IR >3.0 entry rule to people with CKD extrapolates both the trial population and the assay's validity (C4, C5). |

Confidence figures, from the nephrology side (judgements):
- Bottom line 1 (no routine utility, 80-85%): for CKD, dialysis and kidney-transplant settings I would put it at about 85% or higher. KDIGO 2022 and the 2024 PTDM consensus contain no insulin, HOMA-IR, C-peptide or TyG measurement recommendation (scan-level), reduced kidney function adds a clearance bias to fasting insulin and C-peptide, and the only large CKD trial analysis (FIDELITY eGDR) is null for effect modification.
- Bottom line 2 ("shown not to add value", about 40% fasting, about 30% TyG): unchanged. The ULSAM null (neither clamp nor surrogates predicted mortality) is a prognostic null, not an incremental-value test, and the TyG-CKD meta-analyses are association-only. Neither moves the figure.

## 3. Missed evidence (new, sourced)

1. **KDIGO 2022 full text has no IR or C-peptide measurement** (C1, C2). This closes the KDIGO item in the "documents not read" list at scan level and supports row 28's "no guideline" at full-text-scan level. FASTING, SURROGATE, CPEPTIDE.
2. **International PTDM consensus 2024** (PMID 38171510, DOI 10.1093/ndt/gfad258, PMC full text term-scanned): Opinion Statement 1 is "Perform an oral glucose tolerance test for diagnosis and screening; start on the waiting list". The OGTT recommended here is glucose-based; insulin and HOMA-IR are not recommended (HOMA 0 hits; "fasting insulin" 3 hits, all endpoints in tables of prevention or treatment trials). The consensus states GRADE recommendations would be "flawed" because of the evidence base, so these are opinion statements. This is a nephrology guideline-level negative for IR measurement in transplant candidates and recipients, and it shows that the measured post-load quantity is glucose, not insulin (relevant to the scope note's handling of post-load measures).
3. **FIDELITY eGDR analysis** (PMID 38151465): see C3 and C12. SURROGATE.
4. **CKD-specific validity of surrogates** (PMID 24476695 against PMIDs 21441124 and 26526047): see C5. Moderate CKD: fasting and OGTT-derived indices acceptable against the clamp (weighted kappa >0.6; OGTT-derived better). Dialysis: n=10-12, conflicting. FASTING, POSTLOAD, CLAMP.
5. **Insulin clearance in CKD** (PMIDs 26823551, 32785690, 35221224): see C4. FASTING.
6. **OPTN Policy 11 primary text** (C10): C-peptide was a kidney-pancreas waiting-time criterion from 2014 to 2019 and is now a required data-collection field only. CPEPTIDE.
7. **Pretransplant C-peptide and SPK outcomes** (CPEPTIDE, retrospective, conflicting):
   - Gurram 2021 (PMID 34599533; 46 C-peptide ≥2.0 ng/mL vs 46 matched <0.5 ng/mL): 5-year pancreas graft survival 60% vs 86% (P = 0.03); pancreas graft failure attributed to insulin resistance 13% vs 0% (P = 0.026); weight gain >5 kg 72% vs 26%. "Insulin resistance" here is a clinical attribution of graft failure, not a measured index.
   - Rohan 2018 (PMID 30501589; 112 of 214 transplants with pretransplant C-peptide, 63 type 1, 49 type 2): no difference in rejection, graft loss or death; more pancreatitis and BK nephropathy in type 2.
   - Williamson 2025 (PMID 40190934): small series that "question[s] the predictive value of pre-transplant C-peptide levels".
   - Net: after the OPTN criterion was removed, pretransplant C-peptide is at most a centre-level selection input with conflicting retrospective evidence. Suggested status: limited or research-only. This is a secretion/classification use and should be kept apart from IR measurement.
8. **TyG and kidney outcomes** (C6): four meta-analyses of incident CKD and one of outcomes in CKD, all association-level; no incremental-value or decision analysis over eGFR, UACR or a kidney-failure risk equation found in these abstracts. SURROGATE.
9. **Dialysis changes insulin sensitivity** (PMID 10607769): clamp GDR rose after starting HD or CAPD (n=19 non-diabetic ESRD). This adds to the measurement argument (C5): a value is specific to the dialysis state.

Searched and nothing relevant found:
- SGLT2 inhibitor kidney trials (CREDENCE, DAPA-CKD, EMPA-KIDNEY) with HOMA-IR, TyG or eGDR subgroups: 2 records, neither relevant (S10).
- Finerenone: one record only (FIDELITY eGDR) for IR, eGDR or TyG terms (S3); no FIDELIO or FIGARO HOMA-IR analysis found.

## 4. Overreach risks

1. **Carrying general-population cutoffs into CKD.** HOMA-IR thresholds (IRIS >3.0, MAFLD ≥2.5, JDS fasting insulin >30 µU/mL) were not derived in CKD. Fasting insulin and C-peptide rise with lower clearance (C4), and validity in dialysis rests on two studies of 10-12 patients (C5). Any sentence that applies these thresholds to "patients with diabetes" should exclude or flag eGFR below about 60 and dialysis.
2. **Treating TyG-CKD association meta-analyses as utility.** Pooled RRs of 1.4-1.7 are association. Without incremental value over eGFR and UACR (which CKD staging and PREVENT already use), they say nothing about measuring TyG. The same applies to the steelman-type argument that TyG "may serve as" a CKD risk tool.
3. **Reading eGDR nulls as evidence about insulin-based IR.** FIDELITY and FINEARTS-HF used waist, hypertension and HbA1c. HbA1c reliability falls in advanced CKD (KDIGO 2022 chapter 2 discusses it; the specific wording was not extracted here, [recall] for detail), so eGDR in CKD carries an extra measurement problem.
4. **Citing the OPTN C-peptide ≤2 ng/mL rule as current.** It was removed on 2019-07-11. Current policy needs diabetes plus insulin use for kidney-pancreas waiting time.
5. **Calling C-peptide graft-function use "IR measurement".** Rows 10 and 27 and the SPK selection literature are secretion uses; "graft failure due to insulin resistance" in Gurram 2021 is a clinical label, not an assay.
6. **Row 28 figure "about half of C-peptide is cleared by the kidney".** Not re-verified here; keep it attributed to its source (Jones and Hattersley 2013, keyword windows) rather than stating it as fact.

## 5. Suggested changes (exact sentences; not applied)

S-1. In `merged-conclusion.md`, "What is well supported", limits of "no recommendation found" (L24), replace "and NICE, KDIGO and ISPAD (Set B)." with:
> "NICE and ISPAD (Set B). KDIGO 2022 (PMID 36272764, DOI 10.1016/j.kint.2022.06.008) was later term-scanned in full text (whole PDF, references included; not read end to end) by the nephrology reviewer: no recommendation to measure fasting insulin, HOMA-IR, C-peptide, TyG or eGDR was found (`reviews/specialty-nephrology-2026-10-24.md`)."

S-2. In `merged-conclusion.md` L88, replace "The FIDELITY eGDR formula was not checked." with:
> "In FIDELITY (PMID 38151465, DOI 10.2337/dc23-1420, abstract; type 2 diabetes with CKD, n=12,964), eGDR was computed from waist circumference, hypertension status and HbA1c; below-median eGDR was associated with more cardiovascular events but not with kidney outcomes, and finerenone's effect did not differ by eGDR (cardiovascular P interaction 0.23, kidney 0.28). eGDR is a non-insulin surrogate."

S-3. In `merged-conclusion.md` L48, after "...LAMP excluded insulin users for this reason.", add:
> "Reduced kidney function is a further limit: in nondiabetic CKD (mean eGFR 37.6), both clamp-measured insulin sensitivity and insulin clearance were lower than in controls (PMID 26823551, DOI 10.1681/ASN.2015070756, abstract), so a high fasting insulin or HOMA-IR in CKD mixes lower clearance with lower sensitivity; C-peptide is affected more (use-case row 28). No study found quantifies the resulting error in HOMA-IR by eGFR stage."

S-4. In `merged-conclusion.md` L34 ("Surrogates are modest."), add:
> "In CKD the evidence is thin: in 495 older Swedish men with eGFR below 60 (median 46), fasting and OGTT-derived indices agreed acceptably with the clamp (weighted kappa above 0.6, OGTT-derived better; PMID 24476695, DOI 10.1038/ki.2014.1, abstract), while in dialysis two studies of 12 and 10 patients disagree on HOMA-IR (PMIDs 21441124 and 26526047, abstracts)."

S-5. In `merged-conclusion.md` L105, after "for example FINEARTS-HF", add:
> "and FIDELITY in CKD with type 2 diabetes (PMID 38151465; null interaction for cardiovascular and kidney outcomes)".

S-6. In `usecases-verified.md` row 28, replace "No guideline on CKD adjustment retrieved. KDIGO 2022 abstract blank." with:
> "No guideline on CKD adjustment retrieved; the KDIGO 2022 full text (PMID 36272764) contains no C-peptide statement (term scan of the whole PDF, nephrology review 2026-10-24). In Zhou 2022 (n=85, single centre), fasting serum C-peptide was uncorrelated with 24-hour urinary C-peptide at eGFR 60 or lower, and the UCPCR cutoff was derived and tested in the same sample."

S-7. In `usecases-verified.md` row 10, append to the notes:
> "Most whole-pancreas grafts are placed with a kidney; kidney-graft function changes serum C-peptide independently of beta-cell function, so read C-peptide with the concurrent eGFR (direction sourced in row 28; size not quantified)."

S-8. New row or note in `usecases-verified.md` (after skeptic review), for pretransplant C-peptide:
> "Kidney-pancreas candidates (adults): pretransplant C-peptide | CPEPTIDE | Formerly an OPTN kidney-pancreas waiting-time criterion (on insulin with C-peptide ≤2 ng/mL, or >2 ng/mL with BMI at or below a maximum; 2014 system); removed 2019-07-11; current OPTN Policy 11.3.B requires kidney waiting-time qualification and insulin use only (OPTN Policies effective 2026-10-01, excerpts read); C-peptide remains a required data field | Secretion/classification | Withdrawn regulatory use; centre-level selection is limited (retrospective, conflicting: PMID 34599533, DOI 10.1111/ctr.14498; PMID 30501589, DOI 10.6002/ect.2017.0296; abstracts)."

S-9. In `merged-conclusion.md` "What is well supported", first bullet, add a nephrology sub-bullet:
> "Kidney disease and transplantation: KDIGO 2022 (full-text term scan) and the 2024 international PTDM consensus (PMID 38171510, DOI 10.1093/ndt/gfad258, full-text term scan) recommend no insulin, HOMA-IR or C-peptide measurement; the PTDM consensus recommends OGTT glucose screening from the waiting list onward, a glucose test, not an insulin-based index."

S-10. In open gap 5, replace "and the OPTN Policy 11 text" with:
> "(the OPTN Policy 11 text has now been read at excerpt level by the nephrology reviewer; no C-peptide criterion remains)".

## 6. Open questions

1. Is there a study quantifying the bias in HOMA-IR or fasting insulin by eGFR stage against the clamp, for example in CRIC or ULSAM full text? Not found in 20 look-ups. Jia 2014 (PMID 24476695) full text may contain stratified agreement tables; it was not read.
2. Do the TyG-CKD meta-analyses or their primary cohorts report incremental value over eGFR plus UACR or KFRE (delta C, NRI, decision curve)? Not searched specifically (budget).
3. Did FIDELITY, CREDENCE, DAPA-CKD or EMPA-KIDNEY collect fasting insulin? None found; FIDELITY used eGDR because, presumably, no insulin assay was available (not stated in the abstract).
4. Did IRIS exclude reduced eGFR, and are there IRIS or PROactive subgroups by eGFR? Not checked.
5. Should Igls criteria for SPK recipients be read with eGFR adjustment? The Igls documents (rows 10 and 27) were not re-read for kidney wording.
6. The ADA-KDIGO 2022 consensus (PMC9870667) and the KDIGO 2024 CKD evaluation guideline were not read; the 2026 CKM guideline was not re-scanned for kidney-specific IR wording.

## 7. Search log

| # | Tool / database | Query or target | Results | Used |
|---|---|---|---|---|
| L1 | PubMed metadata | PMIDs 36243226, 36189689, 30794834, 36465621, 42265997 | 5 records; 36243226 is not KDIGO (proton irradiation) | ADA-KDIGO, D'Elia, Zhou, CKM records |
| L2 | PubMed search | `(HOMA-IR OR "insulin resistance") AND ("chronic kidney disease" OR hemodialysis) AND (clamp) AND (validity OR validation OR accuracy OR comparison)` | 10 | 24476695, 21441124, 26526047, 10607769, 28150400 (context) |
| L3 | PubMed search | `finerenone (FIDELITY OR FIDELIO OR FIGARO) ("glucose disposal rate" OR "insulin resistance" OR "triglyceride-glucose")` | 1 | 38151465 |
| L4 | PubMed metadata | 36272764, 38151465 and the 10 L2 records | 12 | KDIGO PMID/DOI verified (abstract empty) |
| L5 | Parallel web search | OPTN Policy 11 C-peptide; removal 2019; C-peptide 2 ng/mL BMI 30 (3 queries) | 10 pages | HRSA policy PDF, HRSA FAQ, UNOS 2019 news, OMB form, SRTR 2012, OBM Transplantation 2022 (not used) |
| L6 | Parallel web fetch (excerpts) | KDIGO 2022 PDF, objective: insulin resistance, C-peptide, HOMA, insulin clearance | 1 document, excerpts | hypoglycaemia and insulin-level passages |
| L7 | PubMed search | `"C-peptide" AND ("chronic kidney disease" OR "renal function" OR "renal impairment" OR eGFR) AND (clearance OR "beta-cell function" OR interpretation OR "urinary C-peptide")` | 79 (top 20 retrieved) | 21270186; rest animal, off-topic or case reports |
| L8 | Parallel web fetch (excerpts) | OPTN Policies effective 2026-10-01, sections 11.2-11.3 | 1 document, excerpts | Policy 11.2.B, 11.2.C, 11.3.B verbatim |
| L9 | PubMed metadata | 13 records from L7 | 13 | titles and abstracts screened; 25411603 (liraglutide switching in renal impairment, n=21) not used |
| L10 | PubMed search | `(dapagliflozin OR empagliflozin OR canagliflozin OR "SGLT2 inhibitor") AND (CREDENCE OR "DAPA-CKD" OR "EMPA-KIDNEY" OR "chronic kidney disease") AND ("insulin resistance" OR "HOMA-IR" OR "triglyceride-glucose" OR "glucose disposal rate") AND (subgroup OR "post hoc" OR interaction OR modif)` | 2 | none relevant (negative) |
| L11 | PubMed search | `"insulin clearance" AND ("chronic kidney disease" OR "kidney function" OR eGFR) AND (HOMA OR "fasting insulin" OR "insulin sensitivity")` | 6 | 26823551, 32785690, 35221224 |
| L12 | PubMed search | `(HOMA-IR OR "insulin resistance" OR "triglyceride-glucose") AND (hemodialysis OR "peritoneal dialysis" OR "end-stage renal disease" OR "chronic kidney disease") AND (mortality OR "cardiovascular events" OR "kidney failure" OR progression) AND (cohort OR "meta-analysis")` | 190 (top 20 retrieved, titles screened) | none used directly; mostly reviews, CKM papers and off-topic |
| L13 | PubMed search | `("post-transplant diabetes" OR "posttransplantation diabetes" OR PTDM) AND (consensus OR guideline) AND (kidney transplant)` | 26 (top 10) | 38171510 |
| L14 | PubMed metadata | 21 records from L10-L13 | 21 | as above |
| L15 | PubMed full text | PMC11024828 (PTDM consensus) | 1 full text | term scan |
| L16 | PubMed search | `("simultaneous pancreas-kidney" OR "pancreas transplant") AND ("type 2 diabetes") AND ("C-peptide") AND (outcomes OR survival)` | 16 (top 10) | 34599533, 30501589, 40190934 |
| L17 | PubMed search | `("HOMA-IR" OR "homeostasis model assessment") AND (hemodialysis OR haemodialysis OR "end-stage renal disease") AND (mortality OR "cardiovascular death")` | 51 (top 15) | 26066409 only; the Shinohara 2002 HD mortality cohort [recall] was not in the top 15 and was not retrieved |
| L18 | PubMed search | `("triglyceride-glucose index" OR "TyG index") AND ("chronic kidney disease" OR "kidney function decline" OR "end-stage kidney disease") AND ("meta-analysis"[Publication Type] OR "systematic review"[Title])` | 9 | 41162198, 40623418, 37088649, 40562097, 39915738 |
| L19 | PubMed metadata | 21 records from L16-L18 | 21 | as above |
| L20 | Parallel web fetch (full content) | KDIGO 2022 PDF | 1 document, 595,638 characters | term scan (C1) |

Terms scanned in KDIGO 2022 (L20), with hits: insulin resistance 2 (references only); insulin sensitivity 3 (narrative); HOMA 5 (all false positives inside names); C-peptide 0; "C peptide" 1 (false positive, "insulinotropic peptide"); fasting insulin 0; insulin clearance 0; triglyceride-glucose 0; TyG 0; glucose disposal 0; eGDR 0; hyperinsulin 0; insulin concentration 0; "insulin level" 1 (drug sentence quoted in C1); metabolic syndrome 0; pioglitazone 2 (table and reference); thiazolidinedione 11 (tables and figure).

Terms scanned in the PTDM consensus (L15): HOMA 0; C-peptide 1 (trial table); fasting insulin 3 (trial tables); insulin resistance 3 (mechanism narrative, trial table); insulin sensitivity 6 (trial tables); TyG 0; triglyceride 1.

## 8. Could not retrieve or did not read

- KDIGO 2022: obtained in full but term-scanned, not read end to end; a statement phrased without the scanned terms could be missed.
- ADA-KDIGO 2022 consensus (PMC9870667): abstract only; full text not read.
- KDIGO 2024 CKD evaluation and management guideline: not searched (budget).
- 2026 CKM guideline: not re-scanned; relies on the team's regex scan.
- OPTN Policy 11: excerpt extraction only. The 2018 OPTN board report and the public-comment proposal were not read; the 2014 criteria rest on the HRSA FAQ excerpt and an SRTR 2012 article excerpt (maximum allowable BMI initially 28 kg/m2, per that excerpt).
- Igls 2018 and 2021 documents: not re-read for kidney-function wording.
- Full texts not read: Jia 2014 (no PMC), de Boer 2016 (PMC5004653 available, not fetched), Ebert 2024 (PMC10909685 available, not fetched), Hung 2011, King-Morris 2015, all TyG meta-analyses, Gurram 2021, Rohan 2018.
- Not searched: ClinicalTrials.gov or ICTRP for CKD trials using HOMA-IR, fasting insulin or TyG as entry or stratification criteria; Embase; NICE CKD guidance; incremental value of TyG over KFRE, eGFR or UACR; IRIS eligibility by eGFR.
- Shinohara 2002 (HOMA-IR and CV mortality in non-diabetic haemodialysis) [recall]: not retrieved, so not cited.
