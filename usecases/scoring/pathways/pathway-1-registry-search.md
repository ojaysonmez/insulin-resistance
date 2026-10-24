---
title: "Pathway 1 registry and literature search: C-peptide-guided insulin withdrawal, reclassification with treatment change, and C-peptide assay harmonisation"
---

Search run 2026-10-24 by the evidence-searcher subagent for `usecases/scoring/pathways/pathway-1-plan.md` (rows 6 and 31 of `usecases-verified.md`). Retrieval only. Not medical advice. Statements about relevance are screening judgements, not appraisals. The budget was 30 searches or look-ups; all 30 were used (log below). Measure types are named per record: random (non-fasting) plasma C-peptide, fasting C-peptide, stimulated (MMTT/glucagon) C-peptide, capillary or home C-peptide, UCPCR (urinary C-peptide:creatinine ratio).

Scope questions:
- (a) C-peptide used to guide insulin withdrawal, de-escalation or switching in adults.
- (b) C-peptide used to reclassify diabetes type, with a treatment-change outcome.
- (c) C-peptide assay harmonisation: cross-platform comparison against an isotope-dilution LC-MS/MS reference, or commutable materials.

# 1. Search log

"Screened" means titles (and summaries where the tool returned them) were read for relevance. Where a source returned more hits than were displayed, only the displayed page was screened; that is stated.

| # | Date | Source / tool | Search string or look-up | Hits (total) | Screened | Relevant kept |
|---|---|---|---|---|---|---|
| 1 | 2026-10-24 | ClinicalTrials.gov (Clinical_Trials MCP, search_trials) | condition `diabetes`; advanced `"C-peptide" AND (withdrawal OR discontinuation OR de-escalation OR "stopping insulin" OR deintensification)` | 81 | 50 (first page) | 0 new (free-text hits were drug trials measuring C-peptide as an endpoint) |
| 2 | 2026-10-24 | ClinicalTrials.gov | condition `diabetes`; advanced `"C-peptide" AND (classification OR reclassification OR misclassification OR "diabetes type")` | 123 | 50 (first page) | NCT07828626, NCT03737799, NCT03607604 |
| 3 | 2026-10-24 | ClinicalTrials.gov | advanced `"C-peptide" AND (assay OR standardization OR harmonization OR "mass spectrometry")` | 170 | 30 (first page) | 0 |
| 4 | 2026-10-24 | ClinicalTrials.gov get_trial_details | NCT07828626 | 1 | 1 | yes |
| 5 | 2026-10-24 | ClinicalTrials.gov get_trial_details | NCT03737799 | 1 | 1 | yes |
| 6 | 2026-10-24 | ClinicalTrials.gov | advanced `AREA[BriefTitle]("C-peptide" OR "C peptide") AND AREA[OfficialTitle](insulin OR classification OR type OR testing)` | 8 | 8 | NCT04005261; NCT02614170 (assay-adjacent, peripheral) |
| 7 | 2026-10-24 | ClinicalTrials.gov get_trial_details | NCT04005261 | 1 | 1 | yes (peripheral) |
| 8 | 2026-10-24 | ClinicalTrials.gov | condition `diabetes`; advanced `AREA[BriefTitle]("insulin withdrawal" OR "stopping insulin" OR "insulin discontinuation" OR "insulin cessation" OR "insulin de-escalation" OR "deintensification" OR "de-intensification" OR "deprescribing")` | 7 | 7 | NCT04945070 (fasting C-peptide used as eligibility only) |
| 9 | 2026-10-24 | ISRCTN API | `https://www.isrctn.com/api/query/format/default?q=C-peptide%20insulin&limit=100` | 122 | 100 (first 100 returned) | ISRCTN76893830 (CLASP), ISRCTN18000901 (iDiabetes); ISRCTN15312527 and ISRCTN18189469 noted, not kept |
| 10 | 2026-10-24 | ISRCTN API | `q=C-peptide diabetes classification` | 3 | 3 | ISRCTN63815121 (title only; LADA early-insulin RCT, not a C-peptide-guided design) not kept |
| 11 | 2026-10-24 | ISRCTN API record | ISRCTN76893830 | 1 | 1 | yes |
| 12 | 2026-10-24 | ISRCTN API record | ISRCTN18000901 | 1 | 1 | yes (peripheral) |
| 13 | 2026-10-24 | Amass TrialCore (ClinicalTrials.gov + WHO ICTRP registries) | `C-peptide guided insulin withdrawal or discontinuation in adults with insulin-treated diabetes` | 25 returned (no total given) | 25 | JPRN-UMIN000010563 (title only, peripheral); otherwise repeats |
| 14 | 2026-10-24 | Amass TrialCore | `C-peptide testing to reclassify diabetes type (type 1, type 2, MODY, LADA) and change treatment` | 25 returned | 25 | NCT06821360 (ARC-T1D); DRKS00038674, NL-OMON47436 noted as peripheral |
| 15 | 2026-10-24 | Amass TrialCore | `C-peptide immunoassay comparison standardization isotope dilution mass spectrometry reference` | 15 returned | 15 | 0 (no registered C-peptide harmonisation study) |
| 16 | 2026-10-24 | ClinicalTrials.gov get_trial_details | NCT06821360 | 1 | 1 | yes |
| 17 | 2026-10-24 | PubMed (search_articles) | `"C-peptide"[Title/Abstract] AND insulin[Title/Abstract] AND (withdraw*[...] OR discontinu*[...] ...)` with 7 wildcards | 0 (query refused: "too many wildcards (max: 5)") | 0 | failed search; rerun as #18 |
| 18 | 2026-10-24 | PubMed | `"C-peptide"[Title/Abstract] AND insulin[Title/Abstract] AND (withdrawal[Title/Abstract] OR discontinuation[Title/Abstract] OR cessation[Title/Abstract] OR "stopping insulin"[Title/Abstract] OR "stop insulin"[Title/Abstract] OR de-escalation[Title/Abstract] OR deintensification[Title/Abstract] OR simplification[Title/Abstract] OR misclassification[Title/Abstract] OR reclassification[Title/Abstract]) AND ("2019"[dp] : "2026"[dp])` | 125 | 60 (first page, relevance sort) | 33131101, 36205650, 41395661, 39226586, 32947641 |
| 19 | 2026-10-24 | PubMed | `"C-peptide"[Title/Abstract] AND (harmoni*[Title/Abstract] OR standardi*[Title/Abstract] OR commutab*[Title/Abstract] OR "reference measurement procedure"[Title/Abstract] OR "isotope dilution"[Title/Abstract] OR "mass spectrometry"[Title/Abstract]) AND (immunoassay*[Title/Abstract] OR assay*[Title/Abstract] OR method comparison[Title/Abstract])` (date_from 2019 passed to the tool but the result list included pre-2019 records, so the date filter appears not to have applied) | 111 | 40 (first page) | 40781799, 36630986, 35734440, 40093566, 34723236, 35676794 |
| 20 | 2026-10-24 | PubMed E-utilities esummary | PMIDs from #18 and #19, plus 38549041 and 37141618 (cited in the plan) | 79 records | 79 | identifiers verified (PMID, DOI, year, journal) |
| 21 | 2026-10-24 | PubMed E-utilities efetch (abstracts) | 36205650, 41395661, 40781799, 36630986, 38549041, 37141618, 33131101, 39226586, 35676794 | 9 | 9 | abstracts read |
| 22 | 2026-10-24 | PubMed | `"C-peptide"[Title/Abstract] AND ("type 1 diabetes"[Title/Abstract] OR "insulin-treated"[Title/Abstract]) AND (misdiagnos*[Title/Abstract] OR reclassif*[Title/Abstract] OR misclassif*[Title/Abstract] OR "non-type 1"[Title/Abstract] OR capillary[Title/Abstract]) AND ("2019"[dp] : "2026"[dp])` | 55 | 50 (first page) | 42118608 (PRISM), 36923852, 35313393, 38087932, 30802485 |
| 23 | 2026-10-24 | ClinicalTrials.gov | advanced `AREA[BriefTitle]("C-peptide" OR "C peptide" OR "UCPCR") AND (assay OR immunoassay OR "point of care" OR capillary OR "dried blood" OR home OR remote OR urinary)` | 4 | 4 | 0 new |
| 24 | 2026-10-24 | WHO ICTRP direct (`https://trialsearch.who.int/?SearchAll=C-peptide%20insulin%20withdrawal`) | reachability | HTTP 200, page shell only (scripted page; no result rows parsed) | 0 | not usable; ICTRP content covered only through Amass TrialCore (#13-15) |
| 25 | 2026-10-24 | EU CTIS public API (`https://euclinicaltrials.eu/ctis-public-api/search`, containAll `C-peptide insulin`) | first attempt (reachability) | HTTP 200 | 0 | see #27 |
| 26 | 2026-10-24 | EU CTR (`https://www.clinicaltrialsregister.eu/ctr-search/search?query=C-peptide+AND+insulin+AND+withdrawal`) | first attempt (reachability) | 21 | 0 | see #28 |
| 27 | 2026-10-24 | EU CTIS public API | containAll `C-peptide insulin` (parsed) | 2 | 2 | 0 |
| 28 | 2026-10-24 | EU CTR | `C-peptide AND insulin AND withdrawal` (parsed, first page) | 21 | 20 | EudraCT 2015-005740-34 (title only; insulin regimen de-escalation, C-peptide use unknown) |
| 29 | 2026-10-24 | PubMed E-utilities esummary | PMIDs from #22, plus 34590174 (Holt 2021) | 44 records | 44 | identifiers verified |
| 30 | 2026-10-24 | PubMed E-utilities efetch (abstracts) | 42118608, 36923852, 35313393 | 3 | 3 | abstracts read |

Not searched within the budget: bioRxiv/medRxiv (the available tool has no keyword search, only date and category browsing), Consensus, Europe PMC full text, ANZCTR and ChiCTR directly (reached only through Amass TrialCore).

# 2. Relevant registry records

Read level for registry records: the full registry entry as returned by the tool (ClinicalTrials.gov API v2 record or ISRCTN XML record), unless stated otherwise. Registry status is as the registry reports it on 2026-10-24 and may be out of date.

| Field | ISRCTN76893830 (CLASP pilot) | NCT06821360 (ARC-T1D) | NCT07828626 (BRIGHT) | NCT03737799 (StartRight) | ISRCTN18000901 (iDiabetes) | NCT04005261 | NCT04945070 (IDEAL) |
|---|---|---|---|---|---|---|---|
| Link | https://www.isrctn.com/ISRCTN76893830 | https://clinicaltrials.gov/study/NCT06821360 | https://clinicaltrials.gov/study/NCT07828626 | https://clinicaltrials.gov/study/NCT03737799 | https://www.isrctn.com/ISRCTN18000901 | https://clinicaltrials.gov/study/NCT04005261 | https://clinicaltrials.gov/study/NCT04945070 |
| Title | Safety and feasibility of insulin simplification or cessation in frail older adults with type 2 diabetes: a pilot study of CLASP (using C-peptide to clarify, simplify and personalise type 2 diabetes management in frail older adults) | Evaluating the practicalities and potential benefits of using remote C-peptide testing in clinical practice to confirm established type 1 diabetes | Understanding the impact of endogenous insulin secretion on clinical outcomes in type 1 diabetes and the optimal approach to C-peptide measurement for outcome prediction | Getting the right classification and treatment from diagnosis in adults with diabetes | The iDiabetes Platform: enhanced phenotyping of patients with diabetes for precision diagnosis, prognosis and treatment | C-peptide concentrations in type 2 diabetes treated with insulin | Insulin therapy de-intensification with iGlarLixi |
| Question | (a) | (b) | (b) peripheral; (c) partly (capillary vs plasma) | (b) | (b) peripheral | (a)/(b) peripheral | (a) peripheral |
| Sponsor | University of Dundee (PI E. Pearson); funders NHS Tayside Charitable Foundation, Chief Scientist Office Scotland | Royal Devon and Exeter NHS Foundation Trust; NIHR Exeter CRF, NIHR | Royal Devon and Exeter NHS Foundation Trust; Univ. Exeter, Univ. Birmingham | Royal Devon and Exeter NHS Foundation Trust; NIHR, Diabetes UK, Univ. Exeter | University of Dundee (PI E. Pearson); Chief Scientist Office, Tayside Health Fund | Goztepe Training and Research Hospital | Institute for Clinical and Experimental Medicine (IKEM), Prague |
| Country | UK (Scotland) | UK (England) | UK (England, 4 sites) | UK | UK (Scotland) | Turkey | Czech Republic |
| Design | Single-arm observational pilot cohort with protocolised insulin withdrawal plus semaglutide; qualitative interviews | Observational, single clinic, mailed home capillary kit | Observational, two arms (cohort extension; 200 with MMTT vs home sampling) | Prospective observational cohort | Cluster RCT of GP practices (3 arms) | Cross-sectional | Open-label RCT, MDI vs iGlarLixi |
| Status | Recruitment 2024-12-13 to 2025-12-31; overall end 2025-12-31 (status field not parsed; no results found in PubMed searches #18 and #22) | Enrolling by invitation | Recruiting | Unknown (completion 2024-12-31 listed) | Recruitment end 2026-08-21; end 2027-12-31 | Completed | Unknown on registry; results published (PMID 41395661) |
| Enrolment | 28 (target) | 1,000 (estimated; 1,500 invited) | 700 | 1,815 | 22,500 (target) | 249 | 96 planned; 90 analysed per paper |
| Start / completion | 2024-12-13 / 2025-12-31 | 2024-12-03 / 2025-12 | 2025-10-31 / 2027-06-30 | 2016-08-01 / 2024-12-31 | 2024-10-30 / 2027-12-31 | 2018-11-01 / 2019-03-01 | 2021-07 / 2023 (registry) |
| Population | Age 70 or older, frail (care home, community-nurse insulin, or Clinical Frailty Score 5 or more), T2D over 3 years, on insulin, HbA1c below 70 mmol/mol, BMI 25 (as written in the registry) | Adults with a type 1 diabetes code or rapid insulin progression, duration over 3 years, one hospital service | Insulin-treated adults from StartRight (arm 1); adults with T1D and known C-peptide (arm 2) | Adults diagnosed within 12 months, aged 18 to 50 at diagnosis, plus a cohort over 50 | All adults with diabetes in Tayside GP practices | T2D on insulin at least 6 months | T2D on MDI, HbA1c 9% or less, total daily insulin 0.8 IU/kg or less |
| Intervention | Gradual insulin withdrawal with substitution by oral or injectable semaglutide; FreeStyle Libre 3 CGM | Home finger-prick C-peptide 1-5 h after a meal with self-recorded glucose | MMTT and home capillary post-meal C-peptide; CGM 14 days | None (biomarkers measured; results reported to clinicians for antibodies, per PMID 36205650) | Platform recommendations; "iDiabetesPlus" adds tests including "insulin production and resistance" (assay and cutoff not stated in the registry summary) | None | Switch to iGlarLixi |
| C-peptide measure and cutoff | Random C-peptide 900 pmol/L or more with paired serum glucose above 3.9 mmol/L (entry criterion) | Capillary post-meal C-peptide; "high C-peptide suggestive of non-type 1" (cutoff not stated) | Plasma and capillary 90-min MMTT and home post-meal; arm 2 requires positive antibodies if C-peptide over 600 pmol/L | Non-fasting serum C-peptide and UCPCR; outcome defined by post-meal C-peptide below 600 pmol/L and below 200 pmol/L | Not stated | Fasting C-peptide (bands "adequate, borderline, insufficient"; cutoffs not stated) | Fasting C-peptide above lower limit of normal (eligibility only) |
| Primary outcome | Percentage of patients stopping insulin | Proportion of samples returned within 4 weeks | Association of home capillary vs plasma MMTT C-peptide; C-peptide vs outcomes | Diabetes type defined by insulin requirement at 3 years | Hierarchical composite (death, hospitalisation, eGFR decline, HbA1c) by win ratio | Proportion in each fasting C-peptide band | HbA1c change at 24 weeks |
| Safety outcomes (ketoacidosis) | Secondary: hospital admission with HHS; DKA or severe hypoglycaemia or ambulance call-out; CGM time below range | None registered | Hypoglycaemia questionnaires, CGM | Secondary: ketoacidosis (self-report confirmed from notes) | Severe hypoglycaemia (paramedic call-out); no DKA outcome listed | None | Not read on registry; paper reports hypoglycaemia and CGM metrics (abstract level) |
| Fills Step A? | No | No | No (single-region capillary vs plasma comparison, not cross-platform) | No | No | No | No |
| Fills Step B? | Partly: closest design to the 600-plus band step-down rule, but frail older T2D only, cutoff 900 pmol/L, n=28, single arm, UK | Partly: yield of reclassification candidates; no treatment-change outcome registered | No | Partly: treatment-change data at diagnosis (not the long-duration population) | No | No | No |

Peripheral records noted but not tabulated (title or summary level only): JPRN-UMIN000010563 and JPRN-UMIN000010575 (Juntendo University, ultrasensitive C-peptide assay utility in insulin-dependent patients; completed; dates not given); NCT03607604 (UCPCR to identify MODY, UAE, status unknown, n=778); NCT02614170 (Fujirebio Diagnostics, reference specimens for C-peptide and insulin in healthy people, completed 2016, n=328); DRKS00038674 (late-onset type 1 diabetes record review, Germany, completed); EudraCT 2015-005740-34 (dapagliflozin plus saxagliptin to revert basal-bolus insulin to basal-supported oral therapy in T2D; title only, unknown whether C-peptide is used to select patients); ISRCTN15312527 (non-autoimmune insulin-deficient diabetes in young people in sub-Saharan Africa; title only).

# 3. Relevant papers (2019 onward unless cited in the plan)

All PMIDs and DOIs below were checked against the PubMed esummary record on 2026-10-24 (searches #20 and #29). No full texts were read in this run.

| Identifier | Design (one line) | Population, size | Outcome relevant here | Question | Read level |
|---|---|---|---|---|---|
| Foteinopoulou 2021, https://doi.org/10.1111/dme.14449, PMID 33131101 | Single-centre uncontrolled clinic audit | Clinician-diagnosed T1D at least 3 years, Edinburgh; 859 tested | Random C-peptide 200 pmol/L or more prompted work-up; 6.8% reclassified, 1.5% stopped insulin, 1.6% monogenic; cost per person tested | (a), (b) | Abstract |
| Eason 2022 (StartRight), https://doi.org/10.2337/dc22-0623, PMID 36205650 | Prospective cohort (StartRight) | Adults with clinically diagnosed T1D under 12 months; 722 | Antibody-negative group: 22.6% (37/164) discontinued insulin at median 24 months with similar HbA1c; progression by UCPCR. Antibody result, not C-peptide, was the trigger | (b) | Abstract |
| Luk 2026 (PRISM), https://doi.org/10.2337/dc26-0114, PMID 42118608 | Single-centre 3-year RCT of biomarker-guided classification and treatment vs usual care | Young-onset non-type 1 diabetes, Hong Kong; 884 | C-peptide (with antibodies and genetics) used to classify; primary composite complications not reduced (OR 0.908); insulin-withdrawal results not stated in the abstract | (b) | Abstract |
| Novodvorský 2026 (IDEAL), https://doi.org/10.1111/dom.70362, PMID 41395661 | Open-label RCT, 5 centres | T2D on MDI; 90 analysed | De-escalation to iGlarLixi non-inferior on HbA1c; fasting C-peptide above lower limit of normal used for eligibility only | (a) peripheral | Abstract |
| Thewjitcharoen 2023, https://doi.org/10.1016/j.heliyon.2023.e14262, PMID 36923852 | Cross-sectional, single centre | Clinically diagnosed adult T1D at least 3 years, Thailand; 73 | Preserved C-peptide (random or stimulated) in 11.0%; treatment change not reported in abstract | (b) | Abstract |
| Laspe 2023, https://doi.org/10.4093/dmj.2021.0322, PMID 35313393 | Retrospective comparison, single centre | Insulin-treated "ambiguous type", Germany; 115 | Characterisation only; no treatment-change outcome in abstract | (b) peripheral | Abstract |
| Costa 2025, https://doi.org/10.1089/dia.2024.0246, PMID 39226586 | Retrospective inpatient cohort | Adults admitted with hyperglycaemic emergency, Mayo Clinic; 187 | Inpatient C-peptide did not predict later insulin discontinuation (inpatient setting, not the pathway population) | (a) peripheral | Abstract |
| Moradian 2024 (TaMADOR), https://doi.org/10.1093/clinchem/hvae034, PMID 38549041 | Interlaboratory LC-MS/MS comparison | 3 laboratories; leftover samples and reference materials | Inter-lab imprecision for C-peptide; slope 1.044 vs University of Missouri reference method | (c) | Abstract |
| Deng 2023, https://doi.org/10.1515/cclm-2023-0215, PMID 37141618 | Commutability study | 74 individual sera, 12 processed materials; ID-LC-MS/MS vs 6 immunoassays, China | Frozen human serum pools commutable on most assays; WHO ISR 13/146-derived materials not commutable on over half | (c) | Abstract |
| Hörber 2023, https://doi.org/10.1055/a-1998-6889, PMID 36630986 | Method comparison of 5 immunoassays (no MS reference) | Serum samples across the clinical range, Germany | Mean bias up to 36.6% between platforms (Roche vs Siemens ADVIA Centaur) | (c) | Abstract (open-access full text exists, PMC9998184; not read) |
| Schleicher 2025, https://doi.org/10.1177/19322968251362848, PMID 40781799 | Commentary | Not applicable | States that C-peptide standardisation is not implemented, relative to ADA/EASD 0.2 and 0.6 nmol/L cutoffs | (c) | Abstract |
| Maddaloni 2022, https://doi.org/10.1111/dom.14785, PMID 35676794 | Narrative review | Not applicable | Notes standardisation gap and limited utility evidence in T2D | (a), (c) context | Abstract |
| Holt 2021 (ADA/EASD adult T1D consensus), https://doi.org/10.1007/s00125-021-05568-3, PMID 34590174 | Consensus report | Not applicable | Identifier verified only; content not re-read in this run (the plan cites it second-hand) | context | Title only (this run) |
| LC-MS/MS method papers: https://doi.org/10.1016/j.jmsacl.2022.06.003 (PMID 35734440); https://doi.org/10.1016/j.jmsacl.2025.02.001 (PMID 40093566); https://doi.org/10.1016/j.jmsacl.2020.12.001 (PMID 34723236) | Single-laboratory method development | Not applicable | Candidate reference or comparison methods | (c) | Title only |
| Little and colleagues review, https://doi.org/10.1016/j.biotechadv.2019.02.015, PMID 30802485 | Review of immunoassay harmonisation for diabetes biomarkers | Not applicable | Background on C-peptide standardisation programme | (c) | Title only |
| Transdermal sampling, https://doi.org/10.2337/dc23-1379, PMID 38087932 | Sampling-method comparison | Children and adults with T1D | Alternative sampling to venous; not cross-platform | (c) peripheral | Title only |

# 4. Negative results (searched, nothing found)

- No registered randomised or controlled trial in which a C-peptide result, by protocol, triggers insulin withdrawal or de-escalation in adults of uncertain type (ClinicalTrials.gov #1, #8; ISRCTN #9, #10; Amass TrialCore #13; EU CTR #28; EU CTIS #27). The only protocolised C-peptide-triggered withdrawal study found is the single-arm CLASP pilot (ISRCTN76893830).
- No registered US study of C-peptide-guided insulin withdrawal or reclassification (all relevant records are UK, plus one each in Turkey, Czech Republic, Hong Kong).
- No registered study of cross-platform C-peptide harmonisation against an isotope-dilution LC-MS/MS reference (ClinicalTrials.gov #3, #23; Amass TrialCore #15). Harmonisation evidence exists only as published laboratory studies (Section 3), none of them a multi-platform US-marketed panel at the 80, 200 and 600 pmol/L decision points.
- PubMed searches #18 and #22 returned no protocol paper or results paper for CLASP, ARC-T1D or BRIGHT.

# 5. What this means for Step A and Step B

Does any trial already answer the question? No, from what was retrieved.
- Step A (US assay harmonisation): no registered or published study does what Step A specifies. TaMADOR (PMID 38549041) supplies an LC-MS/MS method and a reference-method comparison but no immunoassay panel. Deng 2023 (PMID 37141618) supports the choice of frozen human serum pools as commutable material, but used Chinese-market assays. Hörber 2023 (PMID 36630986) shows inter-platform bias on five European-market analysers without an MS reference. Read level for all three is abstract only.
- Step B (prospective cohort with a pre-specified step-down rule): CLASP (ISRCTN76893830) is the nearest registered design: random C-peptide with paired glucose, protocolised withdrawal, a DKA and HHS safety outcome, and CGM. It differs from Step B in population (frail, 70 or older, T2D only), cutoff (900 pmol/L, not 600), size (28) and absence of a comparator. Its results were not found. ARC-T1D (NCT06821360) measures feasibility and yield of remote testing in a type 1 clinic but registers no treatment-change or safety outcome. StartRight (PMID 36205650) reports insulin cessation after an antibody result in recent-onset diabetes, not after a C-peptide result in long-duration diabetes. PRISM (PMID 42118608) is a randomised biomarker-guided-care trial but in young-onset non-type 1 diabetes with a complications endpoint.

Potential collaborators (from registry sponsor and investigator fields; no contact made):
- University of Dundee / NHS Tayside (E. Pearson): CLASP and iDiabetes.
- University of Exeter / Royal Devon University Healthcare NHS Foundation Trust (A. Jones and the StartRight group): ARC-T1D, BRIGHT, StartRight; capillary C-peptide method.
- TaMADOR consortium (Univ. Washington, Cedars-Sinai, Pacific Northwest National Laboratory) and the University of Missouri reference laboratory (R. Little, K. Kabytaev), with NIDDK involvement listed in the author affiliations of PMID 38549041: candidate reference-procedure partners for Step A.
- Tübingen / DZD laboratory group (A. Peter, S. Hörber) and the National Center for Clinical Laboratories, Beijing: published cross-platform and commutability work.
- Chinese University of Hong Kong (PRISM investigators): randomised biomarker-guided classification experience.

Gaps that remain:
- No US-marketed immunoassay panel compared against an ID-LC-MS/MS reference at 80, 200 and 600 pmol/L.
- No controlled or multi-site prospective data on outcomes and ketoacidosis after insulin withdrawal triggered by random C-peptide in long-duration, insulin-treated adults of uncertain type.
- No evidence retrieved for the 200 to 600 pmol/L band (de-escalation without withdrawal).
- No eGFR-specific rule tested prospectively (BRIGHT excludes eGFR below 30; CLASP excludes eGFR 30 or below).

Uncertainties: registry statuses may be stale (StartRight "unknown", IDEAL "unknown" although published). CLASP's ISRCTN status field was not parsed; its recruitment end date has passed. ICTRP direct search was not usable; ICTRP coverage depends on Amass TrialCore. Only the first page of the larger free-text searches (#1, #2, #3, #18, #19, #22) was screened.

# 6. Could not retrieve

- WHO ICTRP direct results (scripted page; no rows parsed).
- Full texts of any paper (not attempted within the 30-call budget), including Hörber 2023 (open access, PMC9998184) and TaMADOR (PMC12052497).
- Holt 2021 consensus text (identifier verified only).
- CLASP results or protocol paper; ARC-T1D and BRIGHT outputs.
- Details of EudraCT 2015-005740-34 beyond its title.
- bioRxiv/medRxiv keyword search (tool does not support it).
