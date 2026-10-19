# Evidence set: clinical utility of insulin resistance (IR) measurement

**Role:** evidence searcher (retrieval and documentation only; no interpretation or grading beyond one line of study design per item)
**Run date:** 2026-10-18 (all counts and "latest" statements are as of this date)
**Scope:** fasting insulin, HOMA-IR, OGTT insulin, C-peptide, TyG, TG/HDL-C across prediabetes, T2D, PCOS, MASLD, obesity and cardiovascular risk. Coverage and reimbursement are out of scope.
**Status:** current version includes Round 2 additions and corrections (section 12, 2026-10-19). Where section 12 contradicts sections 6 or 9, section 12 is right.
**Independence:** no file in `ir-team/` other than the role file was opened. (A sibling file exists in `new-roles/`; it was not read.)

---

## 0. How to read this document

### 0.1 Read levels (stated for every item)

| Code | Meaning |
|---|---|
| **FT-scan** | Full text retrieved (NCBI PMC XML/HTML or Europe PMC) and the passages that mention insulin/HOMA/C-peptide/TyG/measurement were read in context. **Not** read end to end. Text files were scanned with regular expressions; synonyms outside the pattern could be missed. |
| **FT-ret** | Full text retrieved but only abstract and a few passages read. |
| **Abs** | PubMed abstract only (verified against the PubMed record). |
| **Title** | PubMed/Europe PMC record (title, journal, DOI) only. |
| **Reg** | Registry record fields read (ClinicalTrials.gov API v2, ISRCTN API). |
| **Reg-list** | Only the registry search-result row seen (title, status, size). |
| **Snip** | Search-tool snippet only (Consensus/Amass); identifier then verified in PubMed. |

### 0.2 Identifier verification

Every PMID and DOI in the tables below was pulled back from the PubMed record (NCBI E-utilities `esummary`/`efetch`, 2026-10-18) and the title matched to the intended article. NCT numbers listed as **Reg** were opened in the ClinicalTrials.gov API v2; ISRCTN11215387 was opened in the ISRCTN API. Registry IDs marked **Reg-list** were seen only in a search-result row (ICTRP or Amass), not on the primary registry page. No citation is listed that was not retrieved.

### 0.3 Tools and access

| Source | Used how | Notes |
|---|---|---|
| PubMed | NCBI E-utilities (`esearch`, `esummary`, `efetch`) via script; also the PubMed MCP tool for early searches | Exact counts and query translations logged (Appendix A). PubMed's automatic term mapping widens some strings; the translation is in the raw log for the first MCP searches (Appendix B). |
| Consensus | MCP `search` | Free tier returns 3 papers per query and no PMIDs/DOIs; used only for discovery, every hit re-verified in PubMed. |
| Amass BiomedCore / TrialCore | MCP | BiomedCore for semantic discovery (PMIDs provided, re-verified). TrialCore includes WHO ICTRP-sourced registries. RegulatoryCore not used (no regulatory question in scope). |
| ClinicalTrials.gov | API v2 (`/api/v2/studies`) | Counts and records logged. |
| WHO ICTRP | Portal `trialsearch.who.int/AdvSearch.aspx` driven through the in-app browser | **The portal defaults to "Recruiting" only.** My first batch (10 searches) was run with that default; all were re-run with status = ALL. Only the status = ALL results are reported (rows marked "A-" in Appendix B). Portal has no public query API. |
| Europe PMC | REST search (`SRC:PPR` for preprints) | Used as the preprint index. The bioRxiv/medRxiv MCP tool has no keyword search (date/category only), so it was not used for retrieval. |
| Publisher sites | `curl`, WebFetch, browser | OUP (ESC) and AHA returned 403/Cloudflare; no attempt was made to bypass the bot checks. |

---

## 1. Retrieval summary by question group

| Group | What was retrieved | Retrieval status |
|---|---|---|
| **1. RCTs / pragmatic trials of IR-guided or IR-stratified care** | No trial found that randomises participants to IR measurement versus no measurement (testing-strategy trial). Found: trials that randomise **within** IR strata or IR-phenotype (PERSON, Gardner 2016 pilot); an enrichment RCT that required HOMA-IR > 3.0 for entry (IRIS); a cluster-randomised "intention to treat insulin resistance" policy trial (ISRCTN11215387, publication not found); several registered phenotype-guided trials with no results (PLIS NCT01947595, PRISM-I NCT07710274). | Registry records read; two key publications FT-scanned. |
| **2. Incremental value / reclassification** | 4 cohort analyses reporting ΔC / NRI / IDI for TyG, HOMA-IR or insulin in primary prevention or diabetes prediction (WHI, Hu 2024, Barzegar 2020, Liu 2026 + 5-cohort pooled ΔC), plus ATTICA TyG vs SCORE2, plus several TyG-added-to-model studies in coronary/ACS cohorts, and 10+ association meta-analyses. | Hu 2024, Barzegar 2020, Liu 2026 FT-scanned; others abstract. WHI full text not open access. |
| **3. Treatment × baseline IR interaction** | LAMP post hoc (liraglutide × HOMA-IR ≥ 2.5, stroke), IRIS and two IRIS secondary analyses, DPP, GRADE (three papers), DIETFITS (INS-30), LIRA-ADD2SGLT2i (HOMA-IR tertiles), SPRINT post hoc, PIVENS adipose-IR paper. | Several FT-scanned; others abstract. No interaction analysis found in the large CV outcome trials searched (see §9 negatives). |
| **4. Guidelines** | 16 guideline/consensus documents or sections with full text retrieved and scanned; wording quoted in §5.1. Four relevant documents not retrievable (ESC 2021, AHA 2023 CKM advisory, AACE 2026 T2D algorithm, ADA/EASD 2026 T2D consensus), plus two lower-priority ones (§5.2). | See §5 and §10. |
| **5. Assay standardisation / cutoffs** | ADA Insulin Standardization Workgroup papers (2007, 2007, 2009, 2010), LC-MS/MS reference procedure papers, C-peptide harmonisation papers, pre-analytical/interference papers, HOMA-IR cutoff systematic reviews, clamp-validated cutoff studies. | Staten 2010 FT-scanned; others abstract. Clin Chem papers are not open access. |

---

## 2. Group 1 — trials of IR-guided or IR-stratified care

### 2.1 Publications

| Identifier | Design (one line) | Population, size | Outcome | Read |
|---|---|---|---|---|
| PMID 26886418, doi:10.1056/NEJMoa1506930 (Kernan 2016, NEJM). Registry NCT00091949 | Double-blind placebo-controlled RCT of pioglitazone; **entry required HOMA-IR > 3.0** (index "chosen because it identifies the highest quartile among populations without diabetes"); 13 prespecified subgroups tested for interaction (Figure 2 not machine-readable) | 3876 non-diabetic patients with recent ischaemic stroke/TIA | Fatal/non-fatal stroke or MI | FT-scan (PMC4887756) |
| PMID 25458644, doi:10.1016/j.ahj.2014.07.016 (Viscoli 2014) | IRIS rationale and design | as above | as above | Abs |
| PMID 29084736, doi:10.1161/CIRCULATIONAHA.117.030458 (Yaghi 2018) | Planned secondary analysis of IRIS using updated stroke definitions | IRIS | Stroke outcomes | Abs |
| PMID 30734043, doi:10.1001/jamaneurol.2019.0079 (Spence 2019) | Post hoc analysis of IRIS in participants with prediabetes and in good adherers. Abstract states "insulin resistance is not commonly measured in clinical practice" | IRIS subset | Stroke/MI, new diabetes | FT-scan (PMC6515584) |
| PMID 42145088, doi:10.1161/STROKEAHA.125.056010 (Lu 2026, Stroke). Registry NCT03948347 | Post hoc analysis of open-label RCT LAMP; treatment-by-IR interaction in Cox models, HOMA-IR cut 2.5; authors label analyses exploratory; HOMA-IR from multi-centre local assays without central standardisation (their limitation section) | 510 of 636 (T2D, minor stroke/high-risk TIA, China); 348 (68.2 %) classed IR | 90-day recurrent stroke; composite vascular events | FT-scan (PMC13281981) |
| PMID 26638192, doi:10.1002/oby.21331 (Gardner 2016) | Pilot RCT 2×2: low-fat vs low-carbohydrate diet **within** insulin-AUC median-split strata | 61 adults BMI 28–40 | 6-month weight change | Abs (FT retrieved, PMC5898445, not scanned) |
| PMID 29466592, doi:10.1001/jama.2018.0245 (Gardner 2018, DIETFITS). Registry NCT01826591 | RCT low-fat vs low-carbohydrate diet; prespecified test of interaction with INS-30 (30-min insulin after glucose) and genotype pattern | 609 adults BMI 28–40 | 12-month weight change | FT-scan (PMC5839290, methods passages) |
| PMID 36811468, doi:10.1016/j.ajcnut.2022.12.014 (Soto-Mota 2023) | Secondary reanalysis of DIETFITS (insulin-secretion quintiles × glycaemic-load reduction) | DIETFITS | Weight change | Abs |
| PMID 41436888, doi:10.1038/s41366-025-01989-x (Follis 2026) | Secondary analysis of DIETFITS (DXA-estimated visceral fat; effect modification by sex and insulin-resistance strata) | 449 with DXA | Visceral fat loss | Abs |
| PMID 36599304, doi:10.1016/j.cmet.2022.12.002 (Trouwborst 2023, Cell Metab). Registry NCT03708419 | Parallel RCT: participants classified by OGTT-derived **muscle IR vs liver IR**, then randomised to phenotype-matched or mismatched diet (12 weeks) | 242, BMI 25–40, age 40–75 | Cardiometabolic health (registered primary: disposition index) | Abs (not open access) |
| PMID 34277687, doi:10.3389/fnut.2021.694568 (Gijbels 2021) | PERSON design paper | 240 planned | Disposition index | Abs |
| PMID 41536020, doi:10.1002/oby.70116 (Morwani-Mangnani 2026) | Secondary analysis of PERSON (MetaboHealth score × IR metabotype) | 242 | Cardiometabolic and body-composition outcomes | Abs (FT retrieved, PMC12933231, not scanned) |
| PMID 35839545, doi:10.1016/j.clnu.2022.06.032 (Aldubayan 2022, PREVENTOMICS) | Double-blind RCT, biomarker-guided (metabolomic + genetic clusters) vs standard diet; not IR-specific | 100 randomised, 82 completers | 10-week weight/health outcomes | Abs |
| PMID 40497454, doi:10.1210/clinem/dgaf350 (Stafford 2025, JCEM) | DPP data: k-means prediabetes subgroups from 22 biomarkers, differential intervention effects | 3145 DPP participants | Incident diabetes by subgroup × arm | Abs |
| PMID 39643008, doi:10.1016/j.diabres.2024.111939 (Rong 2025) | Systematic review/meta-analysis of lifestyle RCTs by prediabetes phenotype (i-IFG, i-IGT, IFG+IGT; not insulin-based) | RCTs to Dec 2023 | Diabetes incidence, insulin sensitivity | Abs |
| PMID 36432409, doi:10.3390/nu14224721 (Kabisch 2022) | Replication analysis of prediction model for non-response to lifestyle intervention (RCT data) | 131 with prediabetes | Conversion to normal glucose regulation | Abs |

### 2.2 Registered trials (records read)

| Registry ID | Design | Population / size | Status on 2026-10-18 | Read |
|---|---|---|---|---|
| **ISRCTN11215387** ("ITT-IR"; Wakayama Rosai Hospital, Japan) | Cluster-randomised open parallel trial of an "intention to treat insulin resistance" policy (self-monitoring, visceral-fat follow-up, diet advice, preferential non-insulinotropic drugs) vs conventional diabetes care; one of seven physicians applied the policy. Record does not describe an IR laboratory measurement as the allocation trigger | Early-stage diabetes, adults 16–90 y; size fields in record: 604 and 757 (field labels not shown in XML) | Start 2016-04-05, overall end 2021-06-30; Amass TrialCore lists hasResults = true but the ISRCTN XML showed no results document; **no publication found** (PubMed, Europe PMC) | Reg (ISRCTN API) |
| NCT03708419 (PERSON, Maastricht) | RCT, phenotype-matched diet | 242 actual | Completed 2021-11; no results posted | Reg |
| NCT01947595 (PLIS, Tübingen) | Randomised multicentre; intensified vs conventional lifestyle in prediabetes "non-responders", with intensive phenotyping | 1145 actual | Completed; no results posted | Reg |
| NCT07710274 (PRISM-I, NUHS Singapore) | Randomised parallel pilot of "precision lifestyle" (CGM, smart ring); inclusion requires metabolic syndrome and IR; primary outcome HOMA-IR | 200 est. | Recruiting; start 2026-09-17 | Reg |
| NCT03804411 (Almazov, Russia) | RCT to find predictors of response to SGLT2i/DPP-4i/GLP-1RA/SU and build a personalised-selection algorithm | 800 est. | Unknown status; last update 2020 | Reg |
| NCT07606872 (Snouda Metabolic Score) | Single-group validation; IR is one of five scored domains; personalised 24-week protocol | 150 est. | Enrolling by invitation | Reg |
| NCT00091949 (IRIS) | see PMID 26886418 | 3876 | Completed; results posted | Reg |
| NCT03948347 (LAMP) | Open-label RCT liraglutide in T2D with minor stroke/TIA | 1708 est. | Status unknown (last update 2023-02) | Reg |
| NCT07412028 (AP-HP) | Diagnostic case-control: severe genetic IR syndromes among "classic" PCOS; fasting/OGTT insulin and C-peptide primary outcomes | 81 est. | Recruiting | Reg |
| NCT03388697 (UTMB) | Validation of Quantose IR (insulin + nonglycaemic biomarkers) in pregnancy; primary outcome gestational diabetes | 100 actual | Completed | Reg |
| ACTRN12624000306516 (Deakin) | Randomised crossover comparison of mixed-meal challenge vs fasting sample vs OGTT against clamp for IR detection | 255 actual | Recruiting | Reg-list (Amass + ICTRP) |

**Not found** (strings in Appendix A/B): a registered or published randomised trial whose arms are "IR measured / IR not measured" or "treatment chosen by HOMA-IR / fasting insulin vs usual care" with clinical outcomes.

---

## 3. Group 2 — incremental-value and reclassification studies

### 3.1 Primary studies reporting discrimination/reclassification

| Identifier | Design | Population, n | Exposure added to what | Reported metrics (as printed) | Read |
|---|---|---|---|---|---|
| PMID 25944628, doi:10.1161/CIRCOUTCOMES.114.001563 (Schmiegelow 2015, WHI) | Prospective cohort | 15,288 women, no CVD/AF/diabetes; 894 CVD events in 10 y | Fasting insulin, HOMA-IR, TG/HDL-C, impaired fasting glucose added to traditional risk factors | Abstract: HR per doubling attenuated and non-significant after adjusting for HDL-C; "did not improve CVD risk discrimination and reclassification" | Abs (not open access) |
| PMID 38191206, doi:10.1136/bmjdrc-2023-003680 (Hu 2024) | Cohort, 10-y diabetes prediction models | 5578 (94.7 % men), 943 incident diabetes | HOMA-IR + HOMA-β (model 3) and + FPG + HOMA (model 4) vs baseline model 1 (age, sex, BMI, smoking, dyslipidaemia, hypertension, HbA1c) | AUROC model 1 0.79; model 2 (+FPG) 0.84; model 4 0.84. NRI/IDI vs model 1: model 2 0.61 / 0.09; **model 3 (HOMA) 0.13 (0.05–0.22) / 0.04 (0.03–0.05)**; model 4 0.67 / 0.09 | FT-scan (PMC10806829) |
| PMID 32993633, doi:10.1186/s12933-020-01121-5 (Barzegar 2020, TLGS) | Cohort, 16 y | 7521 Iranians ≥ 30 y | TyG added to Framingham-variable model | Table 4 as printed (table title reads "Population 60 years (n = 6175)"; the comparison symbol was lost in extraction): C-index 0.789 (FRS) and 0.771 (FRS + TyG); IDI 0.001 (−0.004 to 0.007). The text sentence says the C-index "did not change"; table values reproduced verbatim, direction not interpreted | FT-scan (PMC7526412) |
| PMID 42569452, doi:10.3389/fcvm.2026.1804411 (Liu 2026) | Cohort (CHNS) + meta-analysis of incremental C-index | CHNS adults 45–80 y; 5 cohorts pooled | TyG added to Framingham Risk Score | C-index 0.731 → 0.732 (P = 0.559); pooled ΔC 0.0004 (−0.0092 to 0.0100); excluding Barzegar 2020: 0.0051 (0.0007–0.0094); GRADE "very low" (authors) | FT-scan (PMC13449919) |
| PMID 41178693, doi:10.1111/dom.70270 (Mavraganis 2026, ATTICA) | Derivation + external validation cohorts | 1677 derivation; 1237 validation | TyG ≥ 8.46 added to SCORE2 | NRI 0.668 / 0.469; Δ Harrell's C 0.054 / 0.044 (abstract) | Abs |
| PMID 36434636, doi:10.1186/s12933-022-01694-3 (Liu 2022) | 10-y cohort | 6095 non-diabetic, Eastern China | TyG added to traditional factors | Abstract: significant improvement in discrimination and reclassification for CVD and CHD | Abs |
| PMID 35999546, doi:10.1186/s12933-022-01599-1 (Tai 2022) | Post hoc of ACCORD (NCT00000620) | 5695 with T2D | Cumulative TyG added to conventional model | Abstract: improved C-statistic, NRI, IDI | Abs |
| PMID 36093151, doi:10.3389/fcvm.2022.957626 (Pang 2022) | Retrospective cohort | 515 NSTE-ACS after PCI | TyG added to GRACE | AUC 0.798 → 0.849; NRI 0.718; IDI 0.086; decision-curve analysis reported | Abs |
| PMID 35906587, doi:10.1186/s12933-022-01576-8 (Wu 2022) | Retrospective cohort | 526 premature CAD | TyG added to risk model | C-statistic 0.715 → 0.719 (P = 0.007); NRI 0.101 (P = 0.362); IDI 0.011 | Abs |
| PMID 42559066, doi:10.3389/fcvm.2026.1863508 (Sun 2026) | Retrospective cohort | 890 new CAD | TyG, METS-IR, TyG-BMI, TG/HDL-C; incremental AUC/C/NRI/IDI | METS-IR highest incremental value (C 0.779; IDI 0.082; NRI 0.356) | Abs |
| PMID 19700136, doi:10.1016/j.cardfail.2009.03.001 (Kalogeropoulos 2009, Health ABC) | Prospective cohort | 2386 elderly without diabetes; 185 incident HF | OGTT, fasting insulin, HbA1c, HOMA-IR, HOMA-B added to fasting glucose | Abstract: none improved HF prediction | Abs |
| PMID 24098646, doi:10.1371/journal.pone.0074410 (Venkataraman 2013) | Derivation (clamp) + independent cohort | 253 men (clamp); longitudinal cohort | Predicted ISI (fasting insulin + TG + WHR) vs HOMA-IR | AUC for incident CVD 0.74 vs 0.61; for diabetes 0.77 vs 0.76 | Abs |
| PMID 18689695, doi:10.2337/dc08-0368 (Balkau 2008, DESIR) | Cohort; clinical, biological and genetic diabetes risk scores | 3817 (1863 men, 1954 women) | Not verified whether insulin was included | – | Abs |
| PMID 17533210, doi:10.1001/archinte.167.10.1068 (Wilson 2007) | Cohort; diabetes prediction models | 160 incident T2D | Not verified whether insulin was included | – | Abs |

### 3.2 Association meta-analyses and reviews (no incremental-value metrics unless stated)

| Identifier | Design | Size | Read |
|---|---|---|---|
| PMID 23300589, doi:10.1371/journal.pone.0052036 (Gast 2012) | Meta-analysis: glucose, insulin, HOMA-IR vs incident CVD in adults without diabetes; text states the HOMA-IR addition to prediction models was not tested | 65 studies, 516,325 participants | FT-scan (PMC3532497) |
| PMID 28811358, doi:10.1042/BSR20170947 (Zhang 2017) | Meta-analysis, fasting insulin/HOMA-IR vs CV and all-cause mortality | 7 articles, 26,976 | FT-ret (PMC6448479) |
| PMID 33812373, doi:10.1186/s12933-021-01268-9 (Ding 2021) | Meta-analysis, TyG vs ASCVD | cohort studies | FT-ret (PMC8019501) |
| PMID 35778731, doi:10.1186/s12933-022-01546-0 (Liu 2022) | Meta-analysis, TyG vs CVD and mortality (general population) | – | FT-ret (PMC9250255) |
| PMID 39180024, doi:10.1186/s12933-024-02392-y (Nayak 2024) | Umbrella review of TyG meta-analyses | – | FT-ret (PMC11344391) |
| PMID 36181637, doi:10.1007/s40292-022-00542-5 (González-González 2022) | Systematic review/meta-analysis, HOMA-IR vs T2D, MACE, hypertension, dyslipidaemia, NASH, cancer | – | Abs |
| PMID 34953633, doi:10.1016/j.numecd.2021.11.005 (Chen 2022) | Meta-analysis, TG/HDL-C vs CV events | – | Abs |
| PMID 37415168, doi:10.1186/s12933-023-01906-4 (Liang 2023) | Meta-analysis, TyG and CAD risk/severity/prognosis | – | Abs |
| PMID 39844258, doi:10.1186/s12933-025-02584-0 (Rao 2025) | Meta-analysis, TyG-BMI vs CVD | – | Abs |
| PMID 40760488, doi:10.1186/s12933-025-02890-7 (Xu 2025) | Meta-analysis, TyG vs MACE by diabetes status in CHD | – | Abs |
| PMID 36521498, doi:10.1016/S2666-7568(22)00247-1 (Lopez-Jaramillo 2023) | Pooled cohorts, five countries, TyG vs mortality and CVD | – | Abs |

### 3.3 Diagnostic-accuracy and clamp-validation items (used in Group 5 as well)

| Identifier | Design | Size | Read |
|---|---|---|---|
| PMID 27907900, doi:10.1093/humrep/dew243 (Cassar 2016) | Meta-analysis of clamp studies in PCOS | clamp studies | Abs |
| PMID 32256572, doi:10.1155/2020/4678526 (Sánchez-García 2020) | Systematic review, TyG diagnostic accuracy for IR | – | Abs |
| PMID 40560922, doi:10.1371/journal.pone.0326179 (Cabanillas-Lazo 2025) | Systematic review, TyG and TG/HDL accuracy for IR in children/adolescents | – | Abs |
| PMID 26155920, doi:10.1038/ijo.2015.125 (ter Horst 2015) | Clamp-derived cutoffs; fasting insulin to identify IR in obesity | 112 non-obese, 100 obese men | Abs |
| PMID 10480510, doi:10.2337/diacare.22.9.1462 (Matsuda 1999) | OGTT insulin-sensitivity indices vs euglycaemic clamp | – | Abs |

Registered diagnostic/validation studies: NCT03388697, NCT04623320 (13C-glucose breath test vs clamp, T1D), NCT06766617, NCT07260201 (TyG/TGI-BMI vs HOMA-IR), ACTRN12624000306516 (Reg-list). Results not posted/published as far as retrieved.

---

## 4. Group 3 — treatment-by-baseline-IR interaction in trials

| Identifier | Design | Population, n | IR measure and result location | Read |
|---|---|---|---|---|
| PMID 42145088 (LAMP post hoc) | see §2.1 | 510 | HOMA-IR ≥ 2.5; abstract: P for interaction 0.02 for stroke recurrence and composite vascular events; stroke recurrence 5.8 % vs 18.1 % (HOMA-IR ≥ 2.5), no benefit < 2.5 | FT-scan |
| PMID 26886418 (IRIS) | see §2.1 | 3876 | Entry criterion only; subgroup figure not extractable from text | FT-scan |
| PMID 30734043 (IRIS prediabetes post hoc) | see §2.1 | IRIS subset | – | FT-scan |
| PMID 29466592 (DIETFITS) | see §2.1 | 609 | INS-30 × diet interaction reported in abstract: P = 0.47 | FT-scan |
| PMID 16046308, doi:10.2337/diabetes.54.8.2404 (Kitabchi 2005, DPP) | RCT secondary analysis: baseline and changes in insulin sensitivity/secretion vs diabetes hazard, by arm (placebo n = 1082, metformin 1073, lifestyle 1079) | 3234 | Insulin sensitivity measures from DPP baseline; abstract: hazard negatively associated with baseline insulin sensitivity (HR 0.62–0.94 per SD by arm) | FT-scan (PMC1360738, partial) |
| PMID 11832527, doi:10.1056/NEJMoa012512 (Knowler 2002, DPP) | Primary DPP RCT | 3234 | – | Abs |
| PMID 38285957, doi:10.2337/dc23-1782 (Garvey 2024, GRADE) | RCT secondary analysis: baseline factors (including insulin sensitivity/secretion indices) and differential effectiveness of four add-ons to metformin | 5047 | Treatment-by-factor interaction tests with FDR control (methods) | FT-scan (PMC10973909, methods) |
| PMID 38190619, doi:10.2337/dc23-1059 (Utzschneider 2024, GRADE) | Time-varying HOMA2-%S and C-peptide response vs HbA1c, by arm | glimepiride 1254, liraglutide 1262, sitagliptin 1268 | Abstract: heterogeneity P = 0.009 (HOMA2-%S) for initial HbA1c reduction in sitagliptin vs other arms | Abs |
| PMID 39998948, doi:10.2337/dc24-2419 (Utzschneider 2025, GRADE) | Model-based β-cell parameters by arm | 4712 at baseline | – | Abs |
| PMID 34132018, doi:10.1111/dom.14464 (Blonde 2021, LIRA-ADD2SGLT2i post hoc) | Post hoc, HbA1c/BMI/duration/**HOMA-IR tertile**/SGLT2i duration | 303 | Abstract: no significant HOMA-IR interaction (P > 0.05) | Abs |
| PMID 41293821, doi:10.1161/HYPERTENSIONAHA.125.24666 (Fan 2026, SPRINT post hoc) | Post hoc: IR and intensive BP control on cognitive outcomes | 7427 of 9361 | – | Abs |
| PMID 22532269, doi:10.1002/hep.25805 (Bell 2012, PIVENS) | RCT secondary analysis: adipose-tissue IR (Adipo-IR) vs histology | PIVENS participants | – | Abs |
| PMID 20427778, doi:10.1056/NEJMoa0907929 (Sanyal 2010, PIVENS) | RCT pioglitazone / vitamin E / placebo in non-diabetic NASH | 247 | – | Abs |
| PMID 21428766, doi:10.1056/NEJMoa1010949 (DeFronzo 2011, ACT NOW) | RCT pioglitazone vs placebo in IGT | 602 | – | Abs |
| PMID 31058962, doi:10.1210/jc.2019-00361 (Vaccaro 2019, TOSCA.IT) | RECPAM subgroups by pretreatment CV risk, pioglitazone vs sulfonylurea | 2820 | Not an IR measure | Abs |
| PMID 21747052, doi:10.1161/CIRCULATIONAHA.111.025767 (Qi 2011, POUNDS LOST) | Genotype × diet interaction on HOMA-IR/insulin change | 738 | IR is the outcome, not the modifier | Abs |

Also retrieved at Title level only (not read): PMID 40368575 (tirzepatide, JACC 2025), PMID 40550133 (tirzepatide post hoc, Ann Intern Med 2025), PMID 26525880 (DPP genetic burden × lifestyle/metformin on insulin sensitivity), PMID 33334808 (GRADE baseline characteristics and insulin sensitivity/β-cell function).

---

## 5. Group 4 — guideline full texts

### 5.1 Retrieved and scanned (wording copied from the retrieved text)

| Guideline | Identifier, access | Passage(s) relevant to IR measurement | Read |
|---|---|---|---|
| International evidence-based PCOS guideline 2023 | PMID 37580314, doi:10.1210/clinem/dgad463 (also 37580037, 37589624, 37580861); PMC10505534 | Rec **1.9.12 (PP)** and **3.1.10 (PP)**: "Insulin resistance is a pathophysiological factor in PCOS; however, clinically available insulin assays are of limited clinical relevance and are not recommended in routine care" (3.1.10: "should not be used in routine care"). Text also: "routinely available measures of insulin resistance are inaccurate and clinical measurement is not currently recommended" | FT-scan |
| EASL-EASD-EASO MASLD guideline 2024 | PMID 38852583 (Obes Facts), doi:10.1159/000539371; also 38851997 (J Hepatol), 38869512 (Diabetologia exec. summary, PMC11519095); PMC11299976 | "Assessment of insulin resistance (e.g. using HOMA-IR or estimates derived from the OGTT) may be considered to clarify metabolic dysfunction in adults with (suspected) MASLD and without an established diagnosis of type 2 diabetes (LoE 3, weak recommendation…)". Work-up table lists fasting plasma insulin and/or C-peptide and HOMA-IR under "Type 2 diabetes or insulin resistance". Text: "interpretation of HOMA-IR and Adipo-IR requires standardised measurement of insulin and/or C-peptide concentrations" | FT-scan |
| AASLD practice guidance NAFLD 2023 | PMID 36727674, doi:10.1097/HEP.0000000000000323; PMC10735173 | Strict scan (HOMA, fasting insulin, insulin level/test/assay, C-peptide, TyG, "assess/measure insulin resistance") found **no** recommendation text; IR appears as pathophysiology/comorbidity background | FT-scan |
| ADA Standards of Care 2026, §3 Prevention | PMID 41358891, doi:10.2337/dc26-S003; PMC12690170 | Rec **3.13**: "In people with a history of stroke and evidence of insulin resistance and prediabetes, pioglitazone may be considered to lower the risk of stroke or myocardial infarction…" (grade letters as flattened in PMC text: "A" after the recommendation, "C" after the lower-dose sentence). Text describes IRIS entry as "HOMA of insulin resistance index of ≥3.0" | FT-scan |
| ADA Standards 2026, §2 Diagnosis/Classification | PMID 41358893, doi:10.2337/dc26-S002; PMC12690183. 2025 edition: PMID 39651986, doi:10.2337/dc25-S002; PMC11635041 | C-peptide: "only indicated in people receiving insulin treatment" for classification. Risk-based testing lists "individuals with polycystic ovary syndrome" and "other clinical conditions associated with insulin resistance (e.g., severe obesity, acanthosis nigricans, metabolic dysfunction-associated steatotic liver disease)" as triggers for diabetes testing. 2025 text on cystic-fibrosis-related diabetes: "CGM or HOMA of β-cell function… may be more sensitive than OGTT to detect risk for progression to CFRD; however, evidence linking these results to long-term outcomes is lacking, and these tests are not recommended for screen[ing]" (sentence cut at the extraction limit). No recommendation to measure IR | FT-scan |
| ADA Standards 2026, §4 Comprehensive evaluation | PMID 41358897; PMC12690184 | MASLD definition uses cardiometabolic risk factors "as surrogates for insulin resistance"; 0 hits for HOMA/fasting insulin/C-peptide | FT-scan |
| ADA Standards 2026, §8 Obesity; §10 CVD; §14 Children | PMIDs 41358882; 41358899; 41358890 | §8 and §10: 0 hits for the strict IR terms; §14: IR mentioned in type 1/type 2 phenotype discussion only | FT-scan |
| 2026 AHA/ACC/ADA/ASN CKM guideline | PMID 42265997, doi:10.1016/j.jacc.2026.03.056; PMC13399222 | Strict scan: 0 hits. IR appears as pathophysiology; "High triglycerides and low HDL-C are markers of insulin resistance" | FT-scan |
| 2019 ACC/AHA primary prevention guideline | PMID 30879355, doi:10.1161/CIR.0000000000000678; PMC7734661 | Strict scan: 0 hits; "metabolic syndrome" listed as a risk-enhancer | FT-scan |
| Endocrine Society pediatric obesity guideline 2017 | PMID 28359099, doi:10.1210/jc.2016-2573; PMC6283429 | Rec **1.7**: "We recommend against measuring insulin concentrations when evaluating children or adolescents for obesity (1\|⊕⊕⊕○)". Text cites lack of standardised insulin assays, poor reproducibility, 2.5-fold range of proposed cutoffs | FT-scan |
| Endocrine Society PCOS guideline 2013 | PMID 24151290, doi:10.1210/jc.2013-2350; PMC5399492 | Strict scan found no recommendation to measure insulin/HOMA | FT-scan |
| NASPGHAN paediatric NAFLD guideline 2017 | PMID 28107283, doi:10.1097/MPG.0000000000001482; PMC5413933 | One mention (HOMA-IR in metformin trial discussion) | FT-scan |
| Japan Diabetes Society, IR syndrome criteria 2022 | PMID 35463863, doi:10.1007/s13340-022-00570-5; PMC8980125 | Fasting serum insulin "30 μU/mL" as major sign for genetic IR syndrome and type B IR syndrome (severe syndromes) | FT-scan |
| Lancet Commission, clinical obesity definition 2025 | PMID 39824205, doi:10.1016/S2213-8587(24)00316-4; PMC11870235 | 0 hits for insulin/HOMA/clamp terms | FT-scan |
| ADA/EASD second international consensus report on precision diabetes medicine 2023 | PMID 37794253, doi:10.1038/s41591-023-02502-5; PMC10735053 | HOMA-IR and C-peptide listed among nonglycaemic measures used to subclassify T2D; CVD-prediction review statement: "high predictive utility for N-terminal pro b-type natriuretic peptide (high evidence), troponin T and triglyceride-glucose (moderate evidence)" | FT-scan |

### 5.2 Guidelines identified but full text not retrieved

| Document | Identifier | Why |
|---|---|---|
| 2021 ESC guidelines on CVD prevention | PMID 34458905, doi:10.1093/eurheartj/ehab484 | No PMC copy; OUP/ESC returned 403 and a Cloudflare check; not bypassed |
| AHA presidential advisory, CKM health 2023 | PMID 37807924, doi:10.1161/CIR.0000000000001184 | No PMC copy; AHA site 403 |
| AACE consensus, T2D algorithm 2026 | PMID 41842862, doi:10.1016/j.eprac.2026.01.006 | No PMC copy; publisher 403 |
| ADA/EASD consensus, management of T2D 2026 | PMID 42825450 (Diabetes Care), 42825923 (Diabetologia) | No PMC copy; publisher 403 |
| 2018 AHA/ACC cholesterol guideline | PMID 30423393 | No PMC copy; not fetched at publisher |
| EASL-EASD-EASO NAFLD 2016 | PMID 27062661 | Superseded by 2024; no PMC copy |

---

## 6. Group 5 — assay standardisation, cutoffs and variability

| Identifier | Design | Content | Read |
|---|---|---|---|
| PMID 17272483, doi:10.1373/clinchem.2006.082214 (Marcovina 2007) | ADA Workgroup comparison of 12 commercial insulin methods | Abstract: within-assay CV 3.7–39.0 %; among-assay CV 12–66 % (median 24 %); a common reference preparation did not change among-assay CV | Abs |
| PMID 17363420, doi:10.1373/clinchem.2006.077784 (Manley 2007) | Comparison of 11 insulin assays on 150 serum samples (99 fasting/51 postprandial), all calibrated to IRP 66/304 | Abstract: insulin values from different assays "varied by a factor of 2"; mean CV 3 % automated vs 5 % manual; one assay gave lower values in heparinised plasma than serum | Abs |
| PMID 19325009, doi:10.1373/clinchem.2008.118380 (Miller 2009) | 10 methods vs ID-LC-MS/MS on 39 single-donor sera | Abstract: 4 of 10 methods had ≥ 95 % of results within 32 % of IDMS; bias > 15.5 % for 7 of 10 | Abs |
| PMID 20040676, doi:10.2337/dc09-1206 (Staten 2010) | ADA commentary by the Insulin Standardization Workgroup | Text: lack of standardised insulin assays prevents comparing studies; a reference measurement procedure (ID-MS) exists; clinical guidelines for insulin-based indices require outcome evidence first | FT-scan (PMC2797975) |
| PMID 17586588, doi:10.1373/clinchem.2007.088393 (Rodríguez-Cabaleiro 2007) | Pilot ID-LC-MS/MS reference procedure vs 4 immunoassays, 80 samples | Precision/accuracy of reference procedure | Abs |
| PMID 38549041, doi:10.1093/clinchem/hvae034 (Moradian 2024) | Interlaboratory comparison of antibody-free LC-MS/MS for insulin and C-peptide (TaMADOR) | – | Abs |
| PMID 30802485, doi:10.1016/j.biotechadv.2019.02.015 (Hörber 2020) | Review: harmonisation of immunoassays for diabetes biomarkers (HbA1c, C-peptide, insulin) | – | Abs |
| PMID 36630986, doi:10.1055/a-1998-6889 (Hörber 2023) | Comparison of five C-peptide immunoassays | – | Abs |
| PMID 28646033, doi:10.1373/clinchem.2016.269274 (Little 2017) | Review: reference measurement system for C-peptide | – | Abs |
| PMID 37141618, doi:10.1515/cclm-2023-0215 (Deng 2023); PMID 36843403, doi:10.3343/alm.2023.43.4.345 (Deng 2023) | EQA material commutability for C-peptide; ID-LC-MS/MS C-peptide reference method (China) | – | Abs / Title |
| PMID 37409980, doi:10.1515/cclm-2023-0339 (Nkuna 2023) | Stability of C-peptide and insulin under storage conditions | – | Title |
| PMID 24486652, doi:10.1016/j.clinbiochem.2014.01.026 (Garinet 2014) | Hemolysis/haemoglobin interference on one insulin immunoassay | – | Title |
| PMID 10633871 (Chevenne 1999) | Review: insulin assays and reference values | – | Title |
| PMID 15161807, doi:10.2337/diacare.27.6.1487 (Wallace 2004) | HOMA modelling review | – | Title |
| PMID 35939943, doi:10.1016/j.dsx.2022.102581 (Tahapary 2022) | Review of HOMA-IR and TyG cutoffs | Abstract: "high degree of variability in determining threshold levels of HOMA-IR" | Abs |
| PMID 27984205, doi:10.1515/jpem-2016-0242 (van der Aa 2017) | Systematic review, definitions of IR in children | 103 articles, 146 definitions, 14 methods | Abs |
| PMID 31522316, doi:10.1007/s00431-019-03464-y (Arellano-Ruiz 2019) | Systematic review/MA, HOMA cutoffs vs metabolic syndrome in youth | 6 studies, 8732 | Abs |
| PMID 26559605, doi:10.1016/j.rpped.2015.08.006 (Andrade 2016) | Systematic review, HOMA-IR cutoffs in adolescents (Portuguese) | – | Title |
| PMID 40917357, doi:10.3389/fendo.2025.1646258 (Ballena-Caicedo 2025) | Systematic review/MA, global prevalence of IR by HOMA-IR | 87 studies, 235,148; pooled 26.53 % | Abs |
| PMID 36468919, doi:10.20945/2359-3997000000533 (da Silva 2023) | Hyperglycaemic-clamp-validated HOMA-IR cutoffs in adolescents | n = 80 | Snip (Consensus) + PubMed verification |
| PMID 38715798, doi:10.3389/fendo.2024.1343641 (Malagón-Soriano 2024) | Surrogate IR indices vs Matsuda, cutoffs | 93 young men | Abs |
| PMID 38190491, doi:10.1089/met.2023.0181 (Nakamura 2024) | IR estimate vs steady-state plasma glucose; HOMA-IR comparison | 52 | Snip + PubMed verification |
| PMID 16804799, doi:10.1055/s-2006-924233 (Radikova 2006) | Proposed cutoffs for insulin-sensitivity indices | – | Title |
| PMID 17957034, doi:10.1152/ajpendo.00645.2007 (Muniyappa 2008) | Review of insulin-sensitivity methods | – | Abs |

Registry items touching cutoffs/standardisation: NCT03244449 (Reg-list), NCT07260201 (Reg-list), NCT06358989 (Reg-list), NCT04623320 (Reg-list). No registered insulin-assay standardisation study was found (ICTRP A-I9: 9 records, none an assay study).

---

## 7. Trial-registry searches (summary; strings in Appendix A and B)

| Registry | Searches | Result |
|---|---|---|
| ClinicalTrials.gov API v2 | 20 queries (R1a–RO1), 2026-10-18 | Totals 1–1743 per query; noisy relevance ranking. Relevant records in §2.2. Searches for baseline-IR subgroup interventional trials returned 1 record (NCT02437084, statin-induced diabetes, not a treatment-effect-by-IR design). |
| WHO ICTRP (portal, status ALL) | 9 searches with status ALL (A-I1…A-I10 except A-I8); 10 earlier searches with the default Recruiting filter are logged but not used | Condition "insulin resistance" × title "stratified/guided/tailored/targeted": 8 records, none an IR-guided outcome trial. × "cardiovascular events/outcomes/mortality/stroke/MI": 10 records for 8 trials (includes EUCTR2008-005546-23-DE, the EU registration of IRIS). × "prediction/diagnostic/screening…": 11 trials (e.g. NCT03388697, NCT07321288). TyG: 111 records/110 trials, almost all observational. |
| Amass TrialCore (ICTRP-sourced + CT.gov) | 2 queries | Found ISRCTN11215387 and ACTRN12624000306516. |
| `global_trial_search` MCP (CT.gov, ChiCTR, ISRCTN, ANZCTR…) | 1 query | 9 hits, none relevant. |

---

## 8. Preprints (unreviewed; title level only)

Found through Europe PMC `SRC:PPR` (medRxiv, bioRxiv, Research Square, Preprints.org). Not peer reviewed. Not opened beyond title.

- PPR1265251, doi:10.64898/2026.05.02.26352290 (medRxiv, 2026) — Heterogeneity of insulin resistance surrogates in thousands of non-diabetic adults.
- PPR1266531, doi:10.64898/2026.04.02.26350088 (medRxiv, 2026) — Beyond the TyG index: composite metrics and atrial-fibrillation risk prediction.
- PPR1126601, doi:10.1101/2025.11.25.25340964 (medRxiv, 2025) — TG/HDL-C ratio for assessing IR in healthy Kazakh adults.
- PPR1246440, doi:10.21203/rs.3.rs-9907316/v1 (Research Square, 2026) — Prediabetes subtype stratification by β-cell function, hyperglycaemic clamp.
- PPR1296908, doi:10.21203/rs.3.rs-9719269/v1 (Research Square, 2026) — Incremental predictive value of TyG and derivatives for hypertension and…

---

## 9. Negative and null search results (so absence ≠ not searched)

Exact strings are in Appendix A (labelled). Zero-result or non-yielding searches:

| Label | Target | Result |
|---|---|---|
| Q1a | RCT, IR-guided/HOMA-IR-guided (tiab) | 0 PubMed records |
| Q1b | pragmatic/cluster RCT with IR testing | 1 irrelevant record |
| Q1h–Q1j, E1–E3 | publication of ITT-IR trial (ISRCTN11215387) | not found in PubMed or Europe PMC |
| R3a (CT.gov) | interventional trials with "baseline insulin resistance/HOMA-IR" × subgroup/effect modification | 1 record (NCT02437084), not a treatment-by-IR design |
| Q2a, Q2a-loose | TyG + NRI/C-statistic + systematic review/MA | 1 record each, irrelevant (no meta-analysis of TyG incremental value other than the one embedded in PMID 42569452) |
| Q2h, Q2i, Q2i-loose | PCOS IR diagnostic validation vs clamp (strict); prediabetes progression prediction MA | 0 |
| Q2e | fasting insulin + CHD + Emerging Risk Factors | 1 irrelevant record |
| Q3d, Q3e | DPP baseline-insulin treatment-response strings; Look AHEAD × insulin/HOMA | 0 and 2 irrelevant |
| Q3f | ACCORD/ORIGIN/EMPA-REG/LEADER/SUSTAIN/SURPASS/SURMOUNT/STEP × HOMA-IR × interaction | 269 records, top 10 not about treatment-by-IR interaction; **not exhaustively screened** |
| Q5b | IFCC working group on insulin standardisation | 0 (string too narrow) |
| Q5h, Q5w | HOMA-IR/QUICKI/Matsuda vs clamp validation systematic review | 0 |
| Q5q | HOMA-IR "different insulin assays" | **Malformed (OR precedence)**, 41,789 irrelevant records; ignore |
| Q4b | ADA 2025 sections | **Malformed (OR precedence)**, 3.7 M records; the 2025 section 2 was found through Q4a/other strings |
| I9 (ICTRP, status ALL) | assay standardisation/cutoff titles | 9 records, none an assay-standardisation study |
| Bio/medRxiv MCP | – | not usable for keyword retrieval |

Not found by any search: (a) a randomised trial of IR **measurement** as the intervention; (b) a published decision-curve analysis of HOMA-IR or fasting insulin for treatment decisions in prediabetes/T2D/PCOS/MASLD; (c) an incremental-value (ΔC/NRI) study of HOMA-IR over Pooled Cohort Equations, SCORE2 or QRISK in primary prevention (WHI used traditional risk factors; ATTICA used SCORE2 with TyG, not insulin); (d) an interaction analysis of baseline HOMA-IR in the pivotal GLP-1RA/SGLT2i cardiovascular or weight-loss trials (only LIRA-ADD2SGLT2i HOMA-IR tertiles and LAMP); (e) a guideline recommending routine insulin/HOMA-IR measurement outside the conditional EASL MASLD statement and the Japanese severe-IR-syndrome criteria.

---

## 10. What could not be retrieved

1. Full text of the ESC 2021 prevention guideline, AHA 2023 CKM advisory, AACE 2026 T2D algorithm, ADA/EASD 2026 T2D consensus, and the 2018 AHA/ACC cholesterol guideline (publisher blocks; see §5.2).
2. Full text of WHI (Schmiegelow 2015), PERSON (Cell Metab 2023), IRIS Circulation 2018, HOMA-IR meta-analysis (PMID 36181637), and the ADA/Clin Chem standardisation papers (2007, 2007, 2009): abstracts only.
3. The IRIS Figure 2 (13 subgroup forest plot) — not extractable from text.
4. A publication or results for ISRCTN11215387 (ITT-IR); results flag is true in the record but no document was located.
5. Results/publications for NCT01947595 (PLIS) were not searched for separately.
6. ICTRP portal export: counts and first result pages only (up to 11 rows read per search); further pages not paged.
7. Amass RegulatoryCore: not searched (no regulatory question).
8. Consensus: three papers per query only.

## 11. Search gaps (honest list)

- **PubMed term mapping and phrase-search limits.** Many strings used `[tiab]` phrases or long OR blocks; some returned 0 because of over-specific phrases (Q1a, Q2a, Q2h, Q2i, Q5b, Q5h). Looser versions were run for some (Q2a-loose, Q2h-loose, Q2i-loose) but not for all.
- **Only the top 8–12 records per query were displayed and read** for large-count searches (e.g. Q2b 64, Q2c 112, Q3f 269, Q3i 145, Q2p 227, TyG ICTRP 111). Records beyond the top page were not screened. The TyG and "insulin resistance surrogates" literature (> 1000 PubMed records) is not exhaustively covered; coverage is by meta-analysis and by incremental-value-specific strings.
- **No Embase, Cochrane CENTRAL, Scopus or Web of Science.** Citation chasing from reference lists was not done.
- **PCOS and MASLD incremental-value or testing-strategy literature** was searched with fewer strings than CV and diabetes; PCOS diagnostic criteria papers (Rotterdam, AE-PCOS) were not retrieved because they do not address IR measurement (lookup of Rotterdam 2004 by citation failed).
- **OGTT insulin / C-peptide:** only a handful of strings (Q2t, Q2u, Q5i, Q5z, Q5x); no dedicated pass on 2-h insulin or C-peptide as predictors.
- **Obesity-specific guidelines** beyond the Lancet 2025 commission and Endocrine Society paediatric guideline (e.g. adult obesity guidelines, NICE, WHO) were not retrieved.
- **Regional guidelines** (NICE, KDIGO, ISPAD, IDF, JDS beyond the IR-syndrome criteria, Chinese/Indian guidelines) were not searched.
- **ICTRP:** keyword engine, no field for outcome measure; strings were title/condition/intervention only. First batch used the Recruiting default (fixed).
- **ClinicalTrials.gov:** relevance ranking weak; `query.term` strings returned many unrelated hits.
- **Date limits:** no start-date filter in most searches; new items after 2026-10-18 not covered.


---


---

## 12. Round 2 additions (2026-10-19)

Added after a structured exchange with the clinical chemist. Sections 1–11 above are unchanged except where this section says an earlier claim was wrong. **Corrections to earlier sections:** (a) section 9 negatives for HOMA/QUICKI/Matsuda vs clamp, IFCC-linked insulin standardization, and TyG incremental value were wrong or incomplete (see 12.2); (b) section 6: Staten 2010 calls ID-MS "a reference measurement procedure for insulin" in the ADA workgroup's usage, but Rohlfing 2025, Moradian 2024 and Liu 2025 say no JCTLM-listed insulin reference measurement procedure exists (JCTLM database not queried directly); (c) PMID 21617108 is the Diabetes Care version of Sacks 2011 (doi:10.2337/dc11-9998); doi:10.1373/clinchem.2010.161596 is PMID 21617152.

### 12.1 New items by request

#### Request 1 — biological variation
- **Carobene 2022**, PMID 33554550, doi:10.1515/cclm-2020-1490 (CCLM letter, "Biological variation of serum insulin: updated estimates from EuBIVAS and meta-analysis"). Read level: **Title only**; PubMed has no abstract, Crossref has no abstract, no open-access copy found. The CVI/CVG/RCV values were not retrieved.
- González-Lao 2019, PMID 30389455, doi:10.1016/j.cca.2018.10.031 (Abs): systematic review of BV data for diabetes-related analytes (47 publications; C-peptide publications all BIVAC grade C; global estimates produced for insulin and C-peptide; numbers not in abstract).
- Mooy 1996, PMID 8721775, doi:10.1007/BF00418345 (Abs): two 75-g OGTTs, SDdif of fasting insulin 23–32 pmol/L and of 2-h insulin 190–304 pmol/L, by glucose-tolerance category; Schousboe 2002, PMID 12564620, doi:10.1080/003655102764654358 (Abs): duplicate OGTTs, CV of insulin and HOMA.
- No C-peptide EuBIVAS paper found.

#### Request 2 — post-2019 comparability
- **Rohlfing 2025**, PMID 40802520, doi:10.1515/cclm-2025-0552 (FT): 12 insulin immunoassays from 9 manufacturers on 40 sera vs an IDMS method; ICC > 0.99 within assay; differences vs LC-MS −298.2 to +302.6 pmol/L; only one assay in full agreement.
- Rosli 2022, PMID 35622611, doi:10.1002/jcla.24521 (FT): 7 kits, RSD 1.7–23.2 %.
- Deng 2023, PMID 36750430 (serum-pool commutability, Abs); Tohidi 2017, PMID 28150502 (8 assays, factor 1.8, Abs); Loh 2017, PMID 27665422 (Title); Rohlfing 2025 C-peptide, PMID 39803820, doi:10.1515/cclm-2024-1260 (FT); Schleicher 2025, PMID 40781799 (Abs); Cosma 2019, PMID 30978327 (Abs); Larsen 2017, PMID 27989491 (Abs).
- Not found: CAP or other EQA survey data for insulin.

#### Request 3 — reproducibility of OGTT-derived indices and TyG
- Hudak 2021, PMID 34679116 (Abs): 89 persons, two OGTTs; CV OGIS 6.5 ± 5.1 %, revised QUICKI 2.8 ± 2.1 %. Hani 2024, PMID 39726936 (Abs): 257 children. Gordon 2011, PMID 21945562 (Abs): OGIS CV 7.8 %, Stumvoll ISI 14.4 %. Also PMIDs 18713820, 28482366, 20879960, 36788467, 33972923, 35894085 (Abs).
- **Not found:** any TyG test-retest or biological-variation study (10 strings, see log). Jeong 2021 (PMID 34724122) is a validity study, not repeatability.

#### Request 4 — cross-reactivity
- Li 2025, PMID 39030378 (Atellica 92–121 % for five analogues, Abs); Heurtault 2014, PMID 24150210 (16 assays, 0–264 %, Abs); Violin 2023, PMID 37598742 (Abs); Dayaldasani 2015, PMID 25172526 (Abs); Oh 2018, PMID 30027696 (Lumipulse, Abs, proinsulin value truncated); older single-platform studies (PMIDs 16690737, 20392753, 21239867; Titles for 14709671, 21410416, 39086570).
- **Not retrieved:** proinsulin cross-reactivity percentages on named current platforms (only Lumipulse tested it, and the value was not in the abstract text I could read).

#### Request 5 — reference procedure and JCTLM
- Rohlfing 2025 (FT, PMC12452087): "There is still no JCTLM-listed reference method for insulin, nor are there any JCTLM-listed certified primary or secondary reference materials available."
- Moradian 2024, PMID 38549041 (FT, PMC12052497): "Accuracy was not assessed for insulin measurements, because there is no reference measurement procedure available"; the same paper states the University of Missouri C-peptide reference method is JCTLM-listed.
- Rohlfing C-peptide 2025 (FT): the Missouri LC-MS C-peptide reference measurement procedure "is now listed with the JCTLM".
- Candidate insulin RMP and CRM papers: Liu 2025, PMID 40353876 (Abs, "candidate reference measurement procedure"); Ma 2024, PMID 38556594; Wang 2022, PMID 35201368; Luo 2025, PMID 40270241 (Abs).
- Sacks/NACB 2011, PMID 21617108 (Diabetes Care version; FT via PMC3114322): graded GPP recommendation that a standardized insulin assay should be developed; text says the ADA workgroup called for traceability to an ID-LC-MS/MS reference.
- Not done: direct query of the JCTLM database (script-driven site, not queryable here); a web search found no insulin RMP entry but did not settle it.
- **Resolution of the conflict in my original report:** Staten 2010 says ID-MS is "a reference measurement procedure for insulin" in the ADA workgroup's usage; three later sources (2024, 2025, 2025) say no insulin RMP is JCTLM-listed or available. The sources describe different things (a workgroup's measurement procedure vs a listed, internationally recognised RMP). I relayed both and did not rule between them.

#### Request 6 — guidelines and pre-analytics
- Sacks 2011 NACB/ADA (PMID 21617108, FT; companion PMID 21617152): states insulin assays are poorly harmonized; routine insulin measurements for PCOS are not recommended (cited to ACOG); C-peptide interlab CVs > 10 % within-run and 18 % between-run (15 labs, 9 methods).
- Sacks 2023 update (PMIDs 37471273, 37473453 and executive summaries 37471272, 37562009): **abstract only**; full text behind a browser check that I did not bypass.
- Hemolysis: PMIDs 26121452, 20080083, 27231209, 27817149, 22372347, 41371327, 42351586, 36635939, 24486652 (Abs/Title). Tubes and time: Vogeser 2005 PMID 15885238, Déchelotte 2016 PMID 27693646, Mubiru 2025 PMID 40587435, Nkuna 2023 PMID 37409980, Oddoze 2012 PMID 22285385. Reference intervals: PMIDs 27989491, 41857869, 39529982, 32588601, 25740418, 24530467, 17332147.
- No guideline specific to insulin pre-analytics found.

### 12.1b What changed
- About 60 new identifiers, mostly in Group 5 (assay comparability, reference procedure, BV, cross-reactivity, pre-analytics) where the original had about 25.
- The original's Group 5 "variability" gap (biological variation, repeatability) is now partly filled: EuBIVAS letter identified (values not read), OGTT-index CVs from three papers, no TyG repeatability found.
- The original statement that an ID-MS reference procedure exists is now qualified (see Request 5).
- New guideline-level source for insulin standardization: Sacks 2011/2023.


**Late note (message received after the report was written):** the chemist confirmed by reading the full text that Moradian 2024 says "Accuracy was not assessed for insulin measurements, because there is no reference measurement procedure available" and that Staten 2010 (PMC2797975) carries the quote I sent. The chemist reads the two as consistent: an ID-MS procedure used by the ADA workgroup, but no internationally recognised or JCTLM-listed insulin RMP with a network. JCTLM database status remains unverified by both of us. This was not counted as an outgoing message of mine.

### 12.2 Negative claims from the original report re-tested with broader strings

| Original negative | Broader string(s) used now | Result |
|---|---|---|
| Q5h/Q5w: no systematic review of HOMA/QUICKI/Matsuda vs clamp | `HOMA clamp validation systematic review` (2); `HOMA-IR euglycemic clamp meta-analysis` (3) | **Original was wrong.** Found Otten 2014, PMID 24891021, doi:10.1007/s00125-014-3285-x (meta-analysis of surrogate indices vs clamp, Abs) and Renklint 2024, PMID 39013634 (insulin-secretion surrogates, Abs). |
| Q5b: no IFCC-linked insulin standardization paper (0) | `insulin standardization IFCC` (26), `insulin assay standardization` (19,038; top 25 read) | **Original was wrong in effect.** Found Robbins 1996 ADA Task Force, PMID 8549870, doi:10.2337/diab.45.2.242 (Abs) and 2020s papers listed above. |
| Q2a: no TyG incremental-value study except the Liu 2026 pooled analysis | `TyG index incremental value` (177, top 25 read); `triglyceride glucose reclassification` (297, top 25 read) | **Partly wrong.** New: Song 2022, PMID 36151571 (TyG added to CAC score, 5775 adults, Abs); Huang 2024, PMID 39465316 (no incremental value beyond coronary CTA, 3528 patients, Abs); several TyG-related index papers from the CKM/CHARLS cohorts not opened. |
| Q2h: PCOS IR diagnostic accuracy vs clamp (0) | `insulin resistance polycystic ovary diagnostic accuracy` (54, top 25 read) | Still nothing on accuracy vs clamp beyond PMID 27907900 (original). |
| Q5r/Q5y: no consensus on IR measurement in laboratory medicine | `insulin measurement recommendations laboratory` (373, top 25 read) | **Partly wrong.** Sacks 2011/2023 laboratory guidelines found (above). |
| "No TyG repeatability data" (not claimed before) | 10 strings | Still none. |
| ICTRP no-count results (two) and CT.gov registry negatives | not re-run in Round 2 (browser pane not used) | Untested here. |

Also: in my original report, the section 9 statement "(c) incremental-value study over Pooled Cohort Equations, SCORE2 or QRISK" was not re-tested in this round.


### Appendix C — Round 2 search log (2026-10-19)

Source for every line: PubMed via NCBI E-utilities `esearch`, date 2026-10-19, strings as typed (PubMed automatic term mapping applies). Count is PubMed's total; where stated above I read the top 25–40 records of large sets and all records of sets under about 40. Web and tool searches: web search "JCTLM database reference measurement procedure insulin serum listed" (no insulin RMP entry found); Crossref API for doi:10.1515/cclm-2020-1490 (title only, no abstract); WebFetch of the CAP 2022 accuracy-based survey document failed (host not resolved); PMC pages for PMIDs 37471273 and 37473453 returned a browser check and were not opened.

```
[R2-1a] PubMed(E-utilities) 2026-10-19 | count=5915 | insulin biological variation
[R2-1b] PubMed(E-utilities) 2026-10-19 | count=2 | EuBIVAS insulin
[R2-1c] PubMed(E-utilities) 2026-10-19 | count=268 | biological variation C-peptide
[R2-1d] PubMed(E-utilities) 2026-10-19 | count=0 | biological variation insulin glucose HbA1c EuBIVAS healthy
[R2-1e] PubMed(E-utilities) 2026-10-19 | count=4 | within-subject biological variation insulin reference change value
[R2-1f] PubMed(E-utilities) 2026-10-19 | count=0 | EFLM biological variation database insulin
[R2-2a] PubMed(E-utilities) 2026-10-19 | count=871 | insulin immunoassay comparison
[R2-2b] PubMed(E-utilities) 2026-10-19 | count=1 | Rosli insulin assay comparison
[R2-2c] PubMed(E-utilities) 2026-10-19 | count=165 | insulin assays harmonization
[R2-2d] PubMed(E-utilities) 2026-10-19 | count=2 | insulin immunoassays external quality assessment
[R2-2e] PubMed(E-utilities) 2026-10-19 | count=76 | C-peptide immunoassay comparison
[R2-2f] PubMed(E-utilities) 2026-10-19 | count=1213 | C-peptide assays standardization
[R2-2g] PubMed(E-utilities) 2026-10-19 | count=133 | insulin measurement platforms comparability 2020:2026[dp]
[R2-2h] PubMed(E-utilities) 2026-10-19 | count=66 | College of American Pathologists survey insulin
[R2-2i] PubMed(E-utilities) 2026-10-19 | count=39 | insulin assay method comparison mass spectrometry immunoassay
[R2-3a] PubMed(E-utilities) 2026-10-19 | count=74 | reproducibility Matsuda index
[R2-3b] PubMed(E-utilities) 2026-10-19 | count=413 | reproducibility oral glucose tolerance test insulin
[R2-3c] PubMed(E-utilities) 2026-10-19 | count=459 | reproducibility insulin sensitivity indices
[R2-3d] PubMed(E-utilities) 2026-10-19 | count=341 | triglyceride glucose index repeatability
[R2-3e] PubMed(E-utilities) 2026-10-19 | count=6 | OGIS reproducibility
[R2-3f] PubMed(E-utilities) 2026-10-19 | count=31 | test-retest reliability OGTT insulin sensitivity children
[R2-3g] PubMed(E-utilities) 2026-10-19 | count=0 | within-subject variability insulin sensitivity index Matsuda
[R2-4a] PubMed(E-utilities) 2026-10-19 | count=395 | proinsulin cross-reactivity insulin assay
[R2-4b] PubMed(E-utilities) 2026-10-19 | count=51 | insulin analogue cross-reactivity immunoassay
[R2-4c] PubMed(E-utilities) 2026-10-19 | count=206 | insulin analog detection immunoassays
[R2-4d] PubMed(E-utilities) 2026-10-19 | count=4 | insulin glargine detemir cross-reactivity assay
[R2-5a] PubMed(E-utilities) 2026-10-19 | count=2 | JCTLM insulin
[R2-5b] PubMed(E-utilities) 2026-10-19 | count=4458 | insulin reference measurement procedure
[R2-5c] PubMed(E-utilities) 2026-10-19 | count=46 | insulin reference method isotope dilution
[R2-5d] PubMed(E-utilities) 2026-10-19 | count=26 | insulin standardization IFCC
[R2-6a] PubMed(E-utilities) 2026-10-19 | count=292 | insulin hemolysis
[R2-6b] PubMed(E-utilities) 2026-10-19 | count=4 | C-peptide hemolysis stability
[R2-6c] PubMed(E-utilities) 2026-10-19 | count=12 | insulin sample stability serum separation
[R2-6d] PubMed(E-utilities) 2026-10-19 | count=72 | insulin preanalytical
[R2-6e] PubMed(E-utilities) 2026-10-19 | count=95 | C-peptide reference intervals
[R2-6f] PubMed(E-utilities) 2026-10-19 | count=935 | insulin reference intervals adults
[R2-6g] PubMed(E-utilities) 2026-10-19 | count=37 | C-peptide guideline
[R2-6h] PubMed(E-utilities) 2026-10-19 | count=6 | C-peptide consensus statement measurement
[R2-6i] PubMed(E-utilities) 2026-10-19 | count=3 | C-peptide recommendations preanalytical
[R2-6j] PubMed(E-utilities) 2026-10-19 | count=373 | insulin measurement recommendations laboratory
[R2-6k] PubMed(E-utilities) 2026-10-19 | count=2 | Call for Standardization of C-Peptide Measurement
[R2-6l] PubMed(E-utilities) 2026-10-19 | count=0 | C-peptide interlaboratory international comparison
[R2-6m] PubMed(E-utilities) 2026-10-19 | count=0 | guidelines insulin measurement serum plasma sample handling
[R2-4e] PubMed(E-utilities) 2026-10-19 | count=532 | proinsulin cross-reactivity
[R2-4f] PubMed(E-utilities) 2026-10-19 | count=220 | proinsulin interference insulin immunoassay
[R2-4g] PubMed(E-utilities) 2026-10-19 | count=9 | insulin assay specificity proinsulin split products
[R2-4h] PubMed(E-utilities) 2026-10-19 | count=0 | insulin assay cross-reactivity Roche Elecsys Abbott Architect Siemens Beckman
[R2-1g] PubMed(E-utilities) 2026-10-19 | count=13 | C-peptide intraindividual variation
[R2-1h] PubMed(E-utilities) 2026-10-19 | count=5 | C-peptide within-subject coefficient of variation
[R2-1i] PubMed(E-utilities) 2026-10-19 | count=28 | European Biological Variation Study EuBIVAS
[R2-1j] PubMed(E-utilities) 2026-10-19 | count=947 | biological variation fasting insulin
[R2-1k] PubMed(E-utilities) 2026-10-19 | count=51752 | insulin index of individuality
[R2-3h] PubMed(E-utilities) 2026-10-19 | count=33 | TyG index reproducibility
[R2-3i] PubMed(E-utilities) 2026-10-19 | count=8 | triglyceride glucose index within-person variability
[R2-3j] PubMed(E-utilities) 2026-10-19 | count=0 | triglyceride-glucose index reliability test-retest
[R2-3k] PubMed(E-utilities) 2026-10-19 | count=678 | triglyceride glucose biological variation
[R2-3l] PubMed(E-utilities) 2026-10-19 | count=9 | HOMA-IR reproducibility repeated measurements
[R2-3m] PubMed(E-utilities) 2026-10-19 | count=2 | Matsuda index coefficient of variation repeated OGTT
[R2-3n] PubMed(E-utilities) 2026-10-19 | count=413 | oral glucose tolerance test insulin reproducibility
[R2-N1] PubMed(E-utilities) 2026-10-19 | count=2 | HOMA clamp validation systematic review
[R2-N2] PubMed(E-utilities) 2026-10-19 | count=3 | HOMA-IR euglycemic clamp meta-analysis
[R2-N3] PubMed(E-utilities) 2026-10-19 | count=177 | TyG index incremental value
[R2-N4] PubMed(E-utilities) 2026-10-19 | count=297 | triglyceride glucose reclassification
[R2-N5] PubMed(E-utilities) 2026-10-19 | count=54 | insulin resistance polycystic ovary diagnostic accuracy
[R2-N6] PubMed(E-utilities) 2026-10-19 | count=1705 | HOMA-IR assay variability
[R2-N7] PubMed(E-utilities) 2026-10-19 | count=19038 | insulin assay standardization

```


---

## Appendix A — Scripted search log (every query string, source, date, result count)

Sources: `PubMed(E-utilities)` = `esearch` against PubMed; `ClinicalTrials.gov API v2` = parameters as JSON; `EuropePMC REST` = Europe PMC search. Labels Q1–Q5 map to question groups 1–5; R = registry; P/E = preprints/Europe PMC. Counts are as returned on 2026-10-18. Entries Q5q and Q4b are malformed (see section 9). Entries repeated after a failed run were de-duplicated.

```
[Q1a] PubMed(E-utilities) 2026-10-18 | count=0 | ("insulin resistance"[tiab] OR "HOMA-IR"[tiab] OR "fasting insulin"[tiab]) AND (stratified[tiab] OR guided[tiab] OR tailored[tiab] OR targeted[tiab]) AND randomized controlled trial[pt] AND ("insulin resistance-guided"[tiab] OR "HOMA-IR-guided"[tiab] OR "insulin-guided"[tiab] OR "guided by insulin"[tiab] OR "based on insulin resistance"[tiab])
[Q1b] PubMed(E-utilities) 2026-10-18 | count=1 | ("insulin resistance"[tiab] OR HOMA-IR[tiab]) AND ("pragmatic trial"[tiab] OR "cluster randomized"[tiab] OR "cluster-randomised"[tiab]) AND (testing[tiab] OR screening[tiab] OR measurement[tiab])
[Q1c] PubMed(E-utilities) 2026-10-18 | count=7 | ("insulin resistance"[tiab] OR HOMA-IR[tiab] OR "insulin resistant"[tiab]) AND (randomized[tiab]) AND ("cardiovascular events"[tiab] OR "stroke"[tiab] OR "myocardial infarction"[tiab] OR "incident diabetes"[tiab]) AND (inclusion[tiab] OR enrolled[tiab] OR eligible[tiab]) AND (pioglitazone[tiab] OR metformin[tiab] OR "GLP-1"[tiab])
[Q1d] PubMed(E-utilities) 2026-10-18 | count=16 | ("precision nutrition"[tiab] OR "personalized nutrition"[tiab] OR "personalised nutrition"[tiab]) AND ("insulin resistance"[tiab] OR "insulin sensitivity"[tiab]) AND randomized controlled trial[pt]
[Q1e] PubMed(E-utilities) 2026-10-18 | count=10 | ("insulin secretion"[tiab] OR "insulin resistance"[tiab] OR "insulin dynamics"[tiab]) AND ("low-carbohydrate"[tiab] OR "low carbohydrate"[tiab]) AND ("effect modification"[tiab] OR interaction[tiab] OR modifies[tiab] OR "whom"[tiab]) AND randomized[tiab]
[Q1f] PubMed(E-utilities) 2026-10-18 | count=26 | "metformin"[tiab] AND ("polycystic ovary syndrome"[tiab] OR PCOS[tiab]) AND ("insulin resistance"[tiab] OR HOMA-IR[tiab]) AND (baseline[tiab] AND (predict*[tiab] OR modif*[tiab] OR response[tiab])) AND (randomized[tiab] OR "systematic review"[pt] OR meta-analysis[pt])
[Q1g] PubMed(E-utilities) 2026-10-18 | count=15 | ("diabetes prevention"[tiab] OR "prediabetes"[tiab]) AND ("insulin resistance"[tiab] OR "insulin sensitivity"[tiab] OR "fasting insulin"[tiab]) AND (metformin[tiab] OR lifestyle[tiab]) AND (subgroup[tiab] OR "effect modification"[tiab] OR heterogeneity[tiab] OR "treatment response"[tiab]) AND (randomized[tiab] OR "Diabetes Prevention Program"[tiab])
[Q2a] PubMed(E-utilities) 2026-10-18 | count=1 | ("triglyceride-glucose"[tiab] OR "TyG index"[tiab]) AND ("net reclassification"[tiab] OR "C-statistic"[tiab] OR "C-index"[tiab] OR "integrated discrimination"[tiab] OR "incremental value"[tiab] OR "added value"[tiab]) AND (systematic review[pt] OR meta-analysis[pt])
[Q2b] PubMed(E-utilities) 2026-10-18 | count=64 | ("HOMA-IR"[tiab] OR "fasting insulin"[tiab] OR "insulin resistance"[tiab]) AND ("net reclassification"[tiab] OR "integrated discrimination"[tiab] OR "delta C"[tiab] OR "change in C"[tiab] OR "incremental value"[tiab]) AND ("cardiovascular disease"[tiab] OR "coronary heart disease"[tiab] OR "cardiovascular events"[tiab]) AND (cohort[tiab] OR prospective[tiab])
[Q2c] PubMed(E-utilities) 2026-10-18 | count=112 | ("HOMA-IR"[tiab] OR "fasting insulin"[tiab] OR "insulin resistance"[tiab]) AND ("decision curve"[tiab] OR "net benefit"[tiab]) AND (diabetes[tiab] OR cardiovascular[tiab] OR "fatty liver"[tiab])
[Q2d] PubMed(E-utilities) 2026-10-18 | count=21 | ("HOMA-IR"[tiab] OR "fasting insulin"[tiab] OR "insulin"[ti]) AND ("incident diabetes"[tiab] OR "type 2 diabetes"[ti]) AND (prediction[tiab] OR "risk score"[tiab] OR "risk model"[tiab]) AND (discrimination[tiab] OR "area under"[tiab] OR calibration[tiab]) AND ("fasting glucose"[tiab] OR HbA1c[tiab] OR "glycated hemoglobin"[tiab])
[Q2e] PubMed(E-utilities) 2026-10-18 | count=1 | "fasting insulin"[tiab] AND ("coronary heart disease"[tiab]) AND ("risk prediction"[tiab] OR "risk factor"[tiab]) AND "Emerging Risk Factors"[tiab]
[Q2f] PubMed(E-utilities) 2026-10-18 | count=3 | ("triglyceride-glucose"[tiab] OR "TyG"[tiab] OR "TG/HDL"[tiab] OR "triglyceride to HDL"[tiab] OR "triglyceride/HDL"[tiab]) AND ("type 2 diabetes"[tiab] OR "incident diabetes"[tiab]) AND ("C-statistic"[tiab] OR "AUC"[tiab] OR "area under"[tiab] OR "reclassification"[tiab]) AND (systematic review[pt] OR meta-analysis[pt])
[Q2g] PubMed(E-utilities) 2026-10-18 | count=5 | ("HOMA-IR"[tiab] OR "insulin resistance"[tiab] OR "TyG"[tiab]) AND ("fatty liver"[tiab] OR MASLD[tiab] OR NAFLD[tiab]) AND ("diagnostic accuracy"[tiab] OR AUROC[tiab] OR "sensitivity and specificity"[tiab]) AND (meta-analysis[pt] OR systematic review[pt])
[Q2h] PubMed(E-utilities) 2026-10-18 | count=0 | ("HOMA-IR"[tiab] OR "insulin resistance"[tiab]) AND ("polycystic ovary"[tiab] OR PCOS[tiab]) AND ("diagnostic"[tiab] OR "cutoff"[tiab] OR "cut-off"[tiab] OR "ROC"[tiab]) AND (clamp[tiab]) AND (validation[tiab] OR accuracy[tiab])
[Q2i] PubMed(E-utilities) 2026-10-18 | count=0 | "insulin resistance"[tiab] AND ("prediabetes"[tiab]) AND ("risk prediction"[tiab] OR "progression to diabetes"[tiab]) AND ("HOMA-IR"[tiab] OR "fasting insulin"[tiab]) AND (systematic review[pt] OR meta-analysis[pt])
[Q2a-loose] PubMed(E-utilities) 2026-10-18 | count=1 | triglyceride glucose index AND (incremental OR reclassification OR discrimination) AND (cardiovascular) AND (meta-analysis[pt] OR systematic review[pt])
[Q2a2] PubMed(E-utilities) 2026-10-18 | count=5 | triglyceride glucose index AND Framingham risk score AND (C-index OR C-statistic OR NRI OR IDI)
[Q2h-loose] PubMed(E-utilities) 2026-10-18 | count=167 | (HOMA-IR OR "insulin resistance") AND (polycystic ovary syndrome) AND (euglycemic clamp) AND (cut-off OR cutoff OR diagnostic OR accuracy)
[Q2i-loose] PubMed(E-utilities) 2026-10-18 | count=0 | (HOMA-IR OR "fasting insulin") AND prediabetes AND (progression OR incident diabetes) AND (prediction OR predictive value) AND (meta-analysis[pt] OR systematic review[pt])
[Q2j] PubMed(E-utilities) 2026-10-18 | count=296 | "insulin resistance" AND "polycystic ovary syndrome" AND (systematic review[pt] OR meta-analysis[pt]) AND (diagnosis OR measurement OR assessment OR HOMA)
[Q2k] PubMed(E-utilities) 2026-10-18 | count=33 | (HOMA-IR OR "insulin resistance") AND (NAFLD OR MASLD OR "fatty liver") AND (fibrosis OR cardiovascular OR outcomes) AND (prognostic OR prognosis) AND (meta-analysis[pt])
[Q2l] PubMed(E-utilities) 2026-10-18 | count=3 | (fasting insulin OR HOMA-IR) AND (risk prediction OR prognostic model) AND (children OR adolescents OR youth) AND (type 2 diabetes OR metabolic syndrome) AND (systematic review[pt] OR meta-analysis[pt])
[Q3a] PubMed(E-utilities) 2026-10-18 | count=20 | (baseline insulin resistance OR baseline HOMA-IR OR baseline insulin sensitivity) AND (subgroup OR interaction OR effect modification OR heterogeneity of treatment effect) AND (semaglutide OR tirzepatide OR liraglutide OR dulaglutide) AND (randomized)
[Q3b] PubMed(E-utilities) 2026-10-18 | count=14 | (baseline HOMA-IR OR baseline insulin resistance) AND (SGLT2 OR empagliflozin OR dapagliflozin OR canagliflozin) AND (post hoc OR subgroup OR interaction) AND (randomized)
[Q3c] PubMed(E-utilities) 2026-10-18 | count=29 | (baseline HOMA-IR OR insulin resistance) AND (pioglitazone) AND (NASH OR NAFLD OR MASH OR stroke OR prediabetes) AND (interaction OR subgroup OR responders OR post hoc)
[Q3d] PubMed(E-utilities) 2026-10-18 | count=0 | Diabetes Prevention Program AND (insulin sensitivity OR insulin resistance OR HOMA-IR OR fasting insulin) AND (metformin OR lifestyle) AND (treatment response OR heterogeneity OR differential OR predict)
[Q3e] PubMed(E-utilities) 2026-10-18 | count=2 | Look AHEAD AND (HOMA-IR OR insulin resistance OR fasting insulin) AND (cardiovascular OR weight loss) AND (baseline OR interaction OR subgroup)
[Q3f] PubMed(E-utilities) 2026-10-18 | count=269 | (ACCORD OR ORIGIN OR EMPA-REG OR LEADER OR SUSTAIN OR SURPASS OR SURMOUNT OR STEP) AND (HOMA-IR OR "insulin resistance") AND (baseline) AND (interaction OR subgroup OR heterogeneity OR "treatment effect")
[Q3g] PubMed(E-utilities) 2026-10-18 | count=12 | (resmetirom OR semaglutide OR lanifibranor OR pioglitazone OR vitamin E) AND (MASH OR NASH) AND (baseline HOMA-IR OR baseline insulin resistance) AND (response OR subgroup OR interaction)
[Q3h] PubMed(E-utilities) 2026-10-18 | count=17 | (metformin OR lifestyle) AND (polycystic ovary syndrome) AND (baseline HOMA-IR OR baseline insulin resistance OR baseline hyperinsulinemia) AND (response OR predictor OR subgroup) AND (randomized controlled trial[pt])
[Q3i] PubMed(E-utilities) 2026-10-18 | count=145 | (baseline HOMA-IR OR baseline insulin resistance OR baseline fasting insulin) AND (bariatric OR "weight loss" OR "anti-obesity") AND (predict* OR modif*) AND (randomized controlled trial[pt])
[Q3j] PubMed(E-utilities) 2026-10-18 | count=23 | (Mendelian randomization OR "heterogeneity of treatment effect") AND (insulin resistance) AND (treatment) AND (trial)
[Q5a] PubMed(E-utilities) 2026-10-18 | count=8733 | insulin AND (immunoassay OR assay) AND (standardization OR harmonization OR harmonisation) AND (comparability OR "between-method" OR "inter-assay" OR "method comparison")
[Q5b] PubMed(E-utilities) 2026-10-18 | count=0 | insulin assay AND (International Federation of Clinical Chemistry OR IFCC) AND (working group) AND (standardization OR harmonization OR "reference measurement procedure" OR "isotope dilution")
[Q5c] PubMed(E-utilities) 2026-10-18 | count=31 | insulin AND ("reference measurement procedure" OR "isotope dilution mass spectrometry" OR "LC-MS/MS") AND (immunoassay) AND (harmonization OR standardization OR traceability)
[Q5d] PubMed(E-utilities) 2026-10-18 | count=19 | HOMA-IR AND (cutoff OR cut-off OR threshold OR "reference range" OR "reference interval") AND (population-specific OR healthy OR validation) AND (euglycemic clamp OR "hyperinsulinemic")
[Q5e] PubMed(E-utilities) 2026-10-18 | count=2406 | HOMA-IR AND (variability OR "within-subject" OR "intra-individual" OR "biological variation" OR reproducibility)
[Q5f] PubMed(E-utilities) 2026-10-18 | count=21 | insulin AND (hemolysis OR "pre-analytical" OR preanalytical OR "sample handling") AND (immunoassay) AND (stability OR interference)
[Q5g] PubMed(E-utilities) 2026-10-18 | count=1902 | (insulin immunoassay) AND (proinsulin OR "cross-reactivity" OR "insulin analogs") AND (specificity)
[Q5h] PubMed(E-utilities) 2026-10-18 | count=0 | HOMA-IR AND (clamp) AND (correlation) AND (validity OR accuracy OR "diagnostic performance") AND (systematic review[pt] OR meta-analysis[pt])
[Q5i] PubMed(E-utilities) 2026-10-18 | count=982 | C-peptide AND (assay OR immunoassay) AND (standardization OR harmonization OR "reference") AND (clinical)
[Q5j] PubMed(E-utilities) 2026-10-18 | count=10 | "triglyceride-glucose" AND (cutoff OR threshold OR "optimal cut") AND (clamp OR "insulin resistance") AND (diagnostic OR validation) AND (meta-analysis[pt] OR systematic review[pt])
[Q5k] PubMed(E-utilities) 2026-10-18 | count=2 | Standardization of insulin immunoassays AND American Diabetes Association Workgroup
[Q5l] PubMed(E-utilities) 2026-10-18 | count=2 | Manley AND insulin AND immunoassay AND (variability OR comparison) AND Clin Chem[ta]
[Q5m] PubMed(E-utilities) 2026-10-18 | count=3 | Miller WG AND insulin AND standardization
[Q5n] PubMed(E-utilities) 2026-10-18 | count=1 | Wallace TM AND "Use and abuse of HOMA modeling"
[Q5o] PubMed(E-utilities) 2026-10-18 | count=14 | insulin AND (assay) AND (NIST OR "WHO international standard" OR "IRP 66/304" OR "first international reference")
[Q5p] PubMed(E-utilities) 2026-10-18 | count=2 | Harmonization AND insulin AND (External Quality Assessment OR proficiency testing) AND (laboratories)
[Q5q] PubMed(E-utilities) 2026-10-18 | count=41789 | HOMA-IR AND "different insulin assays" OR "insulin assay dependent" OR "assay-specific"
[Q5r] PubMed(E-utilities) 2026-10-18 | count=60 | "insulin resistance" AND (consensus OR statement) AND (laboratory medicine OR "clinical chemistry") AND measurement
[Q4a] PubMed(E-utilities) 2026-10-18 | count=152 | "Standards of Care in Diabetes" AND 2026 AND American Diabetes Association
[Q4b] PubMed(E-utilities) 2026-10-18 | count=3731630 | "Standards of Care in Diabetes" AND 2025 AND "Diagnosis and Classification" OR "Prevention or Delay of Diabetes"
[Q4c] PubMed(E-utilities) 2026-10-18 | count=22 | Recommendations from the 2023 international evidence-based guideline for the assessment and management of polycystic ovary syndrome
[Q4d] PubMed(E-utilities) 2026-10-18 | count=19 | EASL-EASD-EASO Clinical Practice Guidelines on the management of metabolic dysfunction-associated steatotic liver disease
[Q4e] PubMed(E-utilities) 2026-10-18 | count=5 | AASLD Practice Guidance on the clinical assessment and management of nonalcoholic fatty liver disease
[Q4f] PubMed(E-utilities) 2026-10-18 | count=21548 | AACE consensus statement insulin resistance OR dysglycemia-based chronic disease OR prediabetes
[Q4g] PubMed(E-utilities) 2026-10-18 | count=68 | 2021 ESC Guidelines on cardiovascular disease prevention in clinical practice
[Q4h] PubMed(E-utilities) 2026-10-18 | count=56 | 2019 ACC/AHA Guideline on the Primary Prevention of Cardiovascular Disease
[Q4i] PubMed(E-utilities) 2026-10-18 | count=58 | Endocrine Society clinical practice guideline AND (insulin resistance OR prediabetes OR "polycystic ovary" OR obesity) AND (guideline[pt] OR practice guideline[pt])
[Q4j] PubMed(E-utilities) 2026-10-18 | count=9 | precision medicine in diabetes consensus report ADA EASD
[Q4k] PubMed(E-utilities) 2026-10-18 | count=20 | Cardiovascular-Kidney-Metabolic Health presidential advisory American Heart Association
[Q4l] PubMed(E-utilities) 2026-10-18 | count=3 | Clinical obesity Lancet Diabetes Endocrinol Commission definition and diagnostic criteria
[Q4m] PubMed(E-utilities) 2026-10-18 | count=2 | (practice guideline[pt] OR guideline[pt]) AND ("insulin resistance"[ti]) AND (2018:2026[dp])
[Q4n] PubMed(E-utilities) 2026-10-18 | count=2 | (practice guideline[pt] OR guideline[pt] OR consensus development conference[pt]) AND ("HOMA-IR"[tiab] OR "fasting insulin"[tiab]) AND (not recommended OR "should not" OR "routine measurement" OR "no role")
[Q4o] PubMed(E-utilities) 2026-10-18 | count=245 | Clinical Practice Guideline pediatric OR children AND "insulin resistance" AND (screening OR testing) AND recommendations
[R1a] ClinicalTrials.gov API v2 2026-10-18 | totalCount=464 | {"query.term": "(\"insulin resistance\" OR HOMA-IR OR \"fasting insulin\") AND (guided OR stratified OR tailored OR personalized OR \"based on insulin\")", "filter.advanced": "AREA[StudyType]INTERVENTIONAL"}
[R1b] ClinicalTrials.gov API v2 2026-10-18 | totalCount=457 | {"query.cond": "insulin resistance", "query.intr": "testing OR screening OR stratified OR guided", "filter.advanced": "AREA[StudyType]INTERVENTIONAL"}
[R1c] ClinicalTrials.gov API v2 2026-10-18 | totalCount=1743 | {"query.term": "\"HOMA-IR\" AND (\"insulin resistance-guided\" OR \"stratified by HOMA\" OR \"HOMA-IR >\" OR \"HOMA-IR \u2265\") AND randomized"}
[R1d] ClinicalTrials.gov API v2 2026-10-18 | totalCount=290 | {"query.cond": "Insulin Resistance", "filter.advanced": "AREA[StudyType]INTERVENTIONAL AND AREA[Phase]PHASE3"}
[R1e] ClinicalTrials.gov API v2 2026-10-18 | totalCount=21 | {"query.cond": "Insulin Resistance", "query.term": "cardiovascular events OR stroke OR myocardial infarction OR mortality", "filter.advanced": "AREA[StudyType]INTERVENTIONAL AND AREA[EnrollmentCount]RANGE[1000,MAX]"}
[R1f] ClinicalTrials.gov API v2 2026-10-18 | totalCount=304 | {"query.term": "precision nutrition OR personalized nutrition insulin resistance phenotype", "filter.advanced": "AREA[StudyType]INTERVENTIONAL"}
[R1g] ClinicalTrials.gov API v2 2026-10-18 | totalCount=13 | {"query.cond": "Insulin Resistance", "query.term": "biomarker-guided OR phenotype-guided OR \"insulin resistance phenotype\"", "filter.advanced": "AREA[StudyType]INTERVENTIONAL"}
[R1h] ClinicalTrials.gov API v2 2026-10-18 | totalCount=23 | {"query.cond": "Prediabetes", "query.term": "insulin resistance AND (stratif* OR subgroup OR phenotype)", "filter.advanced": "AREA[StudyType]INTERVENTIONAL"}
[R2a] ClinicalTrials.gov API v2 2026-10-18 | totalCount=52 | {"query.term": "\"triglyceride-glucose\" OR \"TyG index\" OR \"TyG\"", "filter.advanced": "AREA[StudyType]INTERVENTIONAL"}
[R2b] ClinicalTrials.gov API v2 2026-10-18 | totalCount=58 | {"query.term": "\"triglyceride-glucose\" OR \"TyG index\"", "filter.advanced": "AREA[StudyType]OBSERVATIONAL"}
[R2c] ClinicalTrials.gov API v2 2026-10-18 | totalCount=59 | {"query.term": "(HOMA-IR OR \"insulin resistance\") AND (\"risk prediction\" OR \"prediction model\" OR \"reclassification\" OR \"incremental\")", "filter.advanced": "AREA[StudyType]OBSERVATIONAL"}
[R3a] ClinicalTrials.gov API v2 2026-10-18 | totalCount=1 | {"query.term": "(\"baseline insulin resistance\" OR \"baseline HOMA-IR\") AND (subgroup OR \"effect modification\" OR \"treatment response\")", "filter.advanced": "AREA[StudyType]INTERVENTIONAL"}
[R3b] ClinicalTrials.gov API v2 2026-10-18 | totalCount=355 | {"query.cond": "Prediabetes OR Type 2 Diabetes", "query.term": "insulin resistance guided OR \"insulin sensitivity\" stratified metformin OR pioglitazone OR GLP-1 randomized response prediction"}
[R5a] ClinicalTrials.gov API v2 2026-10-18 | totalCount=416 | {"query.term": "insulin assay standardization OR insulin harmonization OR HOMA-IR cutoff validation OR \"reference interval\" insulin"}
[R5b] ClinicalTrials.gov API v2 2026-10-18 | totalCount=3 | {"query.term": "HOMA-IR cutoff OR \"HOMA-IR threshold\" OR \"insulin resistance diagnostic\"", "filter.advanced": "AREA[StudyType]OBSERVATIONAL"}
[R5c] ClinicalTrials.gov API v2 2026-10-18 | totalCount=8 | {"query.cond": "Insulin Resistance", "query.term": "clamp validation OR \"euglycemic clamp\" surrogate index OR \"surrogate marker\" diagnostic accuracy"}
[RP1] ClinicalTrials.gov API v2 2026-10-18 | totalCount=9 | {"query.cond": "Polycystic Ovary Syndrome", "query.term": "(HOMA-IR OR \"insulin resistance\") AND (stratified OR guided OR phenotype OR \"insulin resistant\")", "filter.advanced": "AREA[StudyType]INTERVENTIONAL AND AREA[Phase](PHASE3 OR PHASE4)"}
[RM1] ClinicalTrials.gov API v2 2026-10-18 | totalCount=34 | {"query.cond": "MASH OR NASH OR MASLD OR NAFLD", "query.term": "HOMA-IR AND (stratified OR subgroup OR guided OR biomarker)", "filter.advanced": "AREA[StudyType]INTERVENTIONAL AND AREA[Phase](PHASE2 OR PHASE3 OR PHASE4)"}
[RC1] ClinicalTrials.gov API v2 2026-10-18 | totalCount=1 | {"query.cond": "Cardiovascular Diseases", "query.term": "insulin resistance AND (pioglitazone OR metformin OR GLP-1 OR SGLT2) AND (HOMA-IR OR \"insulin resistant\")", "filter.advanced": "AREA[StudyType]INTERVENTIONAL AND AREA[EnrollmentCount]RANGE[500,MAX]"}
[RO1] ClinicalTrials.gov API v2 2026-10-18 | totalCount=11 | {"query.cond": "Obesity", "query.term": "(HOMA-IR OR \"insulin resistance\") AND (stratified OR guided OR phenotype-based OR \"insulin resistant\" OR responders) AND (semaglutide OR tirzepatide OR liraglutide OR metformin)", "filter.advanced": "AREA[StudyType]INTERVENTIONAL AND AREA[Phase](PHASE2 OR PHASE3 OR PHASE4)"}
[Q1h] PubMed(E-utilities) 2026-10-18 | count=400 | "intention to treat for insulin resistance" OR "ITT-IR" OR ("insulin resistance" AND Wakayama AND cardiovascular AND diabetes AND cluster)
[Q1i] PubMed(E-utilities) 2026-10-18 | count=0 | Kohro OR Nakamura OR Wakayama AND "insulin resistance" AND "early stages of diabetes" AND cardiovascular events
[Q1j] PubMed(E-utilities) 2026-10-18 | count=0 | "insulin resistance" AND "non-insulinotropic" AND (cardiovascular OR diabetes) AND (randomized OR cluster)
[Q2m] PubMed(E-utilities) 2026-10-18 | count=18 | insulin resistance AND incident cardiovascular events AND adults without diabetes AND (meta-analysis[pt] OR systematic review[pt])
[Q2n] PubMed(E-utilities) 2026-10-18 | count=83 | (fasting insulin OR hyperinsulinemia OR HOMA-IR) AND coronary heart disease AND (meta-analysis[pt])
[Q2o] PubMed(E-utilities) 2026-10-18 | count=50 | triglyceride glucose index AND cardiovascular AND (meta-analysis[pt]) AND (prospective OR cohort)
[Q2p] PubMed(E-utilities) 2026-10-18 | count=227 | Barzegar OR Tehran Lipid and Glucose Study AND triglyceride glucose AND cardiovascular
[Q2q] PubMed(E-utilities) 2026-10-18 | count=31 | "triglyceride-glucose" AND (UK Biobank OR "Framingham" OR "ARIC" OR "MESA" OR "Rotterdam Study") AND (cardiovascular OR "coronary") AND (reclassification OR discrimination OR "C-index")
[Q2r] PubMed(E-utilities) 2026-10-18 | count=124 | (insulin resistance OR HOMA-IR OR fasting insulin) AND (identification OR diagnosing OR "predict insulin resistance") AND (routine clinical measurements OR "clinical variables") AND (clamp OR "insulin sensitivity")
[Q2s] PubMed(E-utilities) 2026-10-18 | count=4 | HOMA-IR AND (predict OR prediction OR prognosis) AND (type 2 diabetes) AND (prediabetes) AND (cohort) AND (hazard OR "odds ratio") AND (independent of fasting glucose OR "beyond fasting glucose" OR "after adjustment for fasting glucose")
[Q2t] PubMed(E-utilities) 2026-10-18 | count=41 | oral glucose tolerance test AND insulin AND (post-load OR "2-hour insulin" OR "insulin response") AND (predict OR prediction) AND (diabetes OR cardiovascular) AND (incremental OR reclassification OR "additional")
[Q2u] PubMed(E-utilities) 2026-10-18 | count=75 | C-peptide AND (insulin resistance OR HOMA) AND (cardiovascular OR mortality OR diabetes) AND (cohort) AND (prediction OR incremental OR reclassification)
[Q2v] PubMed(E-utilities) 2026-10-18 | count=8 | (triglyceride/HDL OR "TG/HDL-C" OR "triglyceride to high-density lipoprotein") AND (insulin resistance) AND (cardiovascular) AND (meta-analysis[pt] OR systematic review[pt])
[Q3k] PubMed(E-utilities) 2026-10-18 | count=39 | Diabetes Prevention Program Research Group[corporate author] AND (insulin sensitivity OR insulin resistance OR HOMA OR "fasting insulin") AND (metformin OR lifestyle)
[Q3l] PubMed(E-utilities) 2026-10-18 | count=15 | Glycemia Reduction Approaches in Diabetes GRADE AND (insulin sensitivity OR insulin resistance OR HOMA OR beta-cell function) AND (response OR differential OR baseline)
[Q3m] PubMed(E-utilities) 2026-10-18 | count=43 | TODAY study AND (insulin sensitivity OR insulin resistance OR HOMA) AND (treatment failure OR metformin OR rosiglitazone)
[Q3n] PubMed(E-utilities) 2026-10-18 | count=78 | Pregnancy in Polycystic Ovary Syndrome AND (insulin resistance OR HOMA-IR OR metformin) AND (clomiphene OR letrozole) AND (baseline OR predictors OR response)
[Q3o] PubMed(E-utilities) 2026-10-18 | count=21 | IRIS AND pioglitazone AND (HOMA-IR OR insulin resistance) AND (stroke OR myocardial infarction) AND (Kernan OR Viscoli OR Inzucchi OR Furie)
[Q3p] PubMed(E-utilities) 2026-10-18 | count=3 | pioglitazone AND (insulin resistance) AND (prediabetes OR nondiabetic) AND (stroke) AND (post hoc OR secondary analysis) AND (IRIS)
[Q3q] PubMed(E-utilities) 2026-10-18 | count=11 | Look AHEAD AND (insulin OR HOMA OR insulin sensitivity) AND (outcome OR response OR predictor)
[Q3r] PubMed(E-utilities) 2026-10-18 | count=58 | (TODAY OR RISE OR "Restoring Insulin Secretion") AND (insulin sensitivity OR clamp) AND (metformin OR liraglutide OR glargine) AND (randomized)
[Q3s] PubMed(E-utilities) 2026-10-18 | count=8 | (metabolic surgery OR bariatric OR sleeve OR bypass) AND (baseline insulin resistance OR HOMA-IR OR fasting insulin) AND (predict OR predictor) AND (diabetes remission) AND (randomized controlled trial[pt] OR meta-analysis[pt])
[Q3t] PubMed(E-utilities) 2026-10-18 | count=11 | (SURPASS OR SURMOUNT OR STEP OR SUSTAIN) AND (HOMA-IR) AND (baseline) AND (post hoc OR subgroup)
[Q3u] PubMed(E-utilities) 2026-10-18 | count=15 | (statin OR rosuvastatin OR atorvastatin) AND (baseline insulin resistance OR HOMA-IR) AND (new-onset diabetes) AND (randomized OR post hoc OR JUPITER)
[P1] EuropePMC REST 2026-10-18 | hitCount=133 | SRC:PPR AND ("insulin resistance" OR "HOMA-IR" OR "fasting insulin") AND (reclassification OR "C-statistic" OR "incremental value" OR "risk prediction")
[P2] EuropePMC REST 2026-10-18 | hitCount=125 | SRC:PPR AND ("insulin resistance" OR "HOMA-IR") AND (randomized OR trial) AND (guided OR stratified OR "treatment effect modification" OR "heterogeneity of treatment effect")
[P3] EuropePMC REST 2026-10-18 | hitCount=57 | SRC:PPR AND ("triglyceride-glucose" OR "TyG") AND (reclassification OR "C-index" OR "incremental")
[P4] EuropePMC REST 2026-10-18 | hitCount=54 | SRC:PPR AND (insulin AND (assay OR immunoassay) AND (harmonization OR standardization OR "traceability"))
[P5] EuropePMC REST 2026-10-18 | hitCount=68 | SRC:PPR AND ("HOMA-IR") AND (cutoff OR threshold OR "reference interval")
[Q5s] PubMed(E-utilities) 2026-10-18 | count=6 | HOMA-IR AND (cutoff OR cut-off OR "cut-off points") AND (insulin resistance) AND (population OR ethnic OR ethnicity) AND (systematic review[pt] OR meta-analysis[pt])
[Q5t] PubMed(E-utilities) 2026-10-18 | count=45 | "HOMA-IR" AND (reference values OR percentiles OR "normal range") AND (NHANES OR "general population" OR "healthy adults") AND (insulin assay OR immunoassay)
[Q5u] PubMed(E-utilities) 2026-10-18 | count=5 | HOMA-IR AND (adolescents OR children) AND (cutoff OR cut-off) AND (systematic review[pt] OR meta-analysis[pt])
[Q5v] PubMed(E-utilities) 2026-10-18 | count=21228 | insulin AND (assay OR immunoassay) AND (HOMA OR "insulin resistance") AND (differences OR discrepancy OR "between assays" OR "method-dependent")
[Q5w] PubMed(E-utilities) 2026-10-18 | count=0 | quantitative insulin sensitivity check index OR QUICKI OR Matsuda AND (clamp) AND (validation OR accuracy) AND (systematic review[pt] OR meta-analysis[pt])
[Q5x] PubMed(E-utilities) 2026-10-18 | count=56 | "mixed meal" OR "oral glucose tolerance test" AND "insulin sensitivity" AND clamp AND (validation OR agreement) AND (index OR Matsuda OR "oral minimal model")
[Q5y] PubMed(E-utilities) 2026-10-18 | count=120 | insulin resistance AND (measurement OR assessment) AND (clinical practice) AND (review OR consensus OR position statement) AND (limitations OR "not recommended" OR "lack of standardization")
[Q5z] PubMed(E-utilities) 2026-10-18 | count=2 | Clinical Chemistry AND insulin AND "C-peptide" AND harmonization AND "reference measurement"
[Q5aa] PubMed(E-utilities) 2026-10-18 | count=0 | "threshold value for identifying insulin resistance (HOMA-IR) in an admixed adolescent population"[ti]
[Q5ab] PubMed(E-utilities) 2026-10-18 | count=0 | "Insulin Resistance Is Better Estimated by Using Fasting Glucose, Lipid Profile, and Body Fat Percent Than by HOMA-IR"[ti]
[Q5ac] PubMed(E-utilities) 2026-10-18 | count=0 | "Surrogate indices of insulin resistance using the Matsuda index as reference in adult men"[ti]
[Q5aa] PubMed(E-utilities) 2026-10-18 | count=1 | threshold value identifying insulin resistance HOMA-IR admixed adolescent population hyperglycemic clamp
[Q5ab] PubMed(E-utilities) 2026-10-18 | count=1 | Insulin Resistance Is Better Estimated Fasting Glucose Lipid Profile Body Fat Percent Than HOMA-IR Japanese
[E1] EuropePMC REST 2026-10-18 | hitCount=8 | "intention to treat for insulin resistance" OR "ITT-IR" OR ISRCTN11215387
[E2] EuropePMC REST 2026-10-18 | hitCount=7 | "Wakayama Rosai" AND "insulin resistance" AND cardiovascular
[E3] EuropePMC REST 2026-10-18 | hitCount=0 | (ISRCTN11215387) OR (NCT07606872 AND Snouda)
```


---

## Appendix B — Searches run through MCP tools, the browser pane and web fetches (2026-10-18)

### B.1 PubMed MCP `search_articles` (early searches; counts are PubMed `total_count`)

| # | Query string | Count |
|---|---|---|
| B1 | `(insulin resistance OR HOMA-IR OR "fasting insulin") AND (randomized controlled trial[Publication Type]) AND (insulin-guided OR "insulin resistance-guided" OR "stratified by insulin" OR "personalized" OR "insulin secretion pattern")` | 171 |
| B2 | `(HOMA-IR OR "fasting insulin" OR "triglyceride-glucose index") AND ("net reclassification" OR "C-statistic" OR "C statistic" OR "incremental value" OR "integrated discrimination") AND (cardiovascular OR diabetes)` | 192 |
| B3 | `(baseline insulin resistance OR baseline HOMA-IR OR "baseline insulin") AND (treatment effect modification OR interaction OR "differential response") AND (randomized trial) AND (lifestyle OR metformin OR pioglitazone OR GLP-1)` | 159 |
| B4 | `(insulin assay standardization OR insulin harmonization OR "insulin immunoassay" comparison) AND (HOMA-IR cutoff OR reference interval)` | 39 |
| B5 | `(guideline OR consensus statement) AND ("insulin resistance") AND (measurement OR testing OR "fasting insulin" OR HOMA) AND (recommend*)` | 64 |
| B6 | `Gardner Association of weight loss with low-fat vs low-carbohydrate diets with genotype pattern or insulin secretion DIETFITS` | 3 |
| B7 | `Pioglitazone after ischemic stroke or transient ischemic attack Kernan IRIS insulin resistance` | 78 |
| B8 | `Diabetes Prevention Program baseline insulin resistance OR insulin sensitivity AND metformin OR lifestyle intervention diabetes incidence heterogeneity` | 6975 (non-specific) |
| B9 | `"insulin resistance" AND ("targeted" OR "tailored" OR "guided") AND (randomized) AND (outcome OR "cardiovascular events" OR "incident diabetes") AND ("HOMA-IR" OR "insulin sensitivity") AND (screening OR "test-and-treat" OR "testing strategy")` | 7 |
| B10 | `Viscoli pioglitazone insulin resistance IRIS trial HOMA-IR subgroup stroke myocardial infarction` | 0 |
| B11 | `triglyceride-glucose index incremental prediction cardiovascular disease risk C-statistic Framingham OR pooled cohort equations` | 1073 |
| B12 | `HOMA-IR incident cardiovascular disease prospective cohort meta-analysis systematic review` | 3 |
| B13 | `"fasting insulin" AND "diabetes" AND (prediction OR risk score) AND (reclassification OR "area under the curve" OR "added value") AND ("Systematic Review"[Publication Type] OR "Meta-Analysis"[Publication Type])` | 6 |

`lookup_article_by_citation` batch: Kernan NEJM 2016;374:1321 (→ PMID 26886418); Knowler NEJM 2002;346:393 (→ 11832527); DeFronzo NEJM 2011;364:1104 (→ 21428766); Sanyal NEJM 2010;362:1675 (→ 20427778); Matthews Diabetologia 1985;28:412 (→ 3899825, the original HOMA paper; not otherwise used); Rotterdam consensus Fertil Steril 2004;81:19 → not found.

### B.2 Consensus (3 results per call)

| # | Query | Notes |
|---|---|---|
| C1 | `triglyceride-glucose index added predictive value over conventional risk factors for cardiovascular events net reclassification improvement` | Liu 2026 (42569452); Wang 2020 (TyG in diabetes + ACS) and Qiu 2025 (TyG-WWI) seen as snippets only, not listed in tables |
| C2 | `HOMA-IR or fasting insulin improves prediction of incident type 2 diabetes beyond glucose and BMI C-statistic` | Hu 2024 (38191206); Bello-Chavolla 2018 (METS-IR) and Xing 2025 seen as snippets only |
| C3 | `randomized trial insulin resistance-guided treatment allocation versus usual care` | Nothing relevant (exercise/metformin RCTs with HOMA-IR as outcome) |
| C4 | `treatment effect heterogeneity by baseline insulin resistance HOMA-IR in randomized trials of glucose-lowering or weight-loss therapy` (medical_mode) | Utzschneider 2024 (38190619) and two non-specific papers |
| C5 | `clinical practice guideline recommendation against routine measurement of fasting insulin or HOMA-IR` | Wallace 2004; Nakamura 2024; Assani 2025 (snippet only) |
| C6 | `HOMA-IR cutoff validation against euglycemic clamp and between-assay insulin variability` | da Silva 2023 (36468919); Kardus 2024 (snippet only); Malagón-Soriano 2024 (38715798) |

### B.3 Amass BiomedCore / TrialCore and `global_trial_search`

| # | Tool and query | Filters | Result |
|---|---|---|---|
| A1 | BiomedCore: `randomized trial of insulin resistance-guided or HOMA-IR-stratified treatment` | publicationTypes = Randomized Controlled Trial; limit 15 | Mostly HOMA-IR-as-outcome RCTs; IRIS design paper (25458644); POUNDS LOST (21747052) |
| A2 | BiomedCore: `does adding fasting insulin or HOMA-IR to conventional cardiovascular risk score improve prediction C-statistic reclassification` | limit 10 | WHI (25944628), Gast 2012, Zhang 2017, Kalogeropoulos 2009, Venkataraman 2013 |
| A3 | BiomedCore: `triglyceride-glucose index added to risk model improves C-statistic net reclassification cardiovascular events cohort` | minPublicationDate 2018-01-01; limit 10 | Liu 2026, Mavraganis 2026, Liu 2022, Pang 2022, Wu 2022, Tai 2022, Sun 2026 |
| A4 | BiomedCore: `post hoc analysis randomized trial treatment benefit differs by baseline insulin resistance HOMA-IR interaction` | publicationTypes = RCT; limit 12 | LIRA-ADD2SGLT2i post hoc (34132018); others irrelevant |
| T1 | TrialCore: `insulin resistance guided OR stratified by HOMA-IR randomized treatment` | studyType = INTERVENTIONAL; limit 12 | No IR-guided outcome trial |
| T2 | TrialCore: `EUCTR OR ChiCTR OR JPRN OR CTRI insulin resistance HOMA-IR stratified OR guided randomised cardiovascular OR diabetes prevention outcome` | INTERVENTIONAL; minStartDate 2015-01-01; limit 10 | ISRCTN11215387; ACTRN12624000306516 |
| G1 | `global_trial_search`: `insulin resistance HOMA-IR stratified OR guided randomized` | size 15 | 9 total, none relevant |
| T3 | TrialCore `get_amass_trialcore_record` for ISRCTN11215387 | – | Tool argument error; ISRCTN API used instead |

### B.4 WHO ICTRP portal (in-app browser, form `AdvSearch.aspx`)

Initial attempts: (a) a script-set search returned the whole database (286,359 records; fields not applied because of the portal's watermark handling); (b) a scripted form POST returned the portal's error page. Fixed by firing the focus event before setting the text fields. **The default "Recruiting" status filter was discovered after searches I1–I10; searches were re-run with status = ALL below.**

Default Recruiting filter (not used for conclusions): I1 cond=`insulin resistance`, title=`stratified OR guided OR tailored OR targeted` → 2; I2 cond=`insulin resistance`, title=`cardiovascular` → 9 records/8 trials; I3 title=`HOMA-IR OR insulin resistance-guided OR insulin sensitivity-guided` → 2; I4 title=`prediction OR predictive OR risk score OR reclassification OR diagnostic` → 1; I5 title=`triglyceride glucose OR TyG` → 13; I6 cond=`prediabetes`, title=`insulin resistance` → 6; I7 cond=`polycystic ovary syndrome`, title=`insulin resistance OR HOMA-IR` → 30/29; I8 cond=`fatty liver OR steatotic OR NAFLD OR NASH`, title=`insulin resistance OR HOMA-IR` → 23; I9 title=`cut-off OR cutoff OR threshold OR reference range OR standardization OR harmonization OR screening` → 0; I10 intervention=`measurement OR testing OR HOMA-IR OR fasting insulin OR OGTT OR diagnostic` → 19.

Status = ALL (used):

| # | Condition | Title / intervention text | Records / trials |
|---|---|---|---|
| A-I1 | `insulin resistance` | title `stratified OR guided OR tailored OR targeted` | 8 / 8 |
| A-I2 | `insulin resistance` | title `cardiovascular events OR cardiovascular outcomes OR mortality OR stroke OR myocardial infarction` | 10 / 8 |
| A-I3 | `insulin resistance` | title `HOMA-IR OR insulin resistance-guided OR insulin sensitivity-guided` | 8 / 8 |
| A-I4 | `insulin resistance` | title `prediction OR predictive OR risk score OR reclassification OR diagnostic OR screening` | 11 / 11 |
| A-I5 | (none) | title `triglyceride glucose OR TyG` | 111 / 110 |
| A-I6 | `prediabetes` | title `insulin resistance OR HOMA-IR OR insulin sensitivity` | 55 / 55 |
| A-I7 | `polycystic ovary syndrome` | title `insulin resistance guided OR HOMA-IR stratified OR insulin resistant OR phenotype` | 19 / 19 |
| A-I9 | `insulin resistance` | title `cut-off OR cutoff OR threshold OR reference OR standardization OR harmonization OR validation` | 9 / 8 |
| A-I10 | `insulin resistance` | intervention `HOMA-IR OR fasting insulin OR OGTT OR clamp OR measurement OR testing OR diagnostic` | 80 / 78 |

(The liver search I8 was not re-run with status ALL.) Only the first result page (up to 11 rows) of each search was read.

### B.5 Web, API and full-text retrieval

- WebFetch of `trialsearch.who.int` (portal description); ISRCTN API `https://www.isrctn.com/api/query/format/default?q=ISRCTN11215387` (read).
- ClinicalTrials.gov API v2 single-record reads: NCT07710274, NCT01947595, NCT03804411, NCT05105321, NCT03708419, NCT03948347, NCT07606872, NCT03388697, NCT00091949, NCT04501406, NCT07412028.
- Full texts pulled (NCBI PMC XML/HTML or Europe PMC): PMIDs 37580314, 38852583, 38869512, 36727674, 39651986, 41358893, 41358891, 41358897, 41358882, 41358899, 41358890, 42265997, 30879355, 35463863, 28107283, 24151290, 39824205, 37794253, 28359099, 26886418, 30734043, 38285957, 16046308, 42145088, 29466592, 41536020, 26638192, 23300589, 28811358, 39180024, 33812373, 35778731, 20040676, 32993633, 38191206, 42569452.
- Blocked (403/Cloudflare, not bypassed): academic.oup.com (ESC 2021), ahajournals.org (AHA 2023), escardio.org PDF, diabetesjournals.org (ADA/EASD 2026), endocrinepractice.org (AACE 2026).
- Europe PMC REST preprint and ITT-IR searches (P1–P5, E1–E3) are in Appendix A.
