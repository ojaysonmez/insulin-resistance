---
title: "Pathway 1 Step A gap search: C-peptide biological variation, analytical variation, pre-analytical stability and performance specifications"
---

DRAFT, 2026-10-24. Subagent report for Pathway 1 Step A (`usecases/scoring/pathways/pathway-1-plan.md` sections 2 and 7; gaps from `usecases/scoring/pathways/pathway-1-partners.md` section 6). Not medical advice. Desk research only: 24 logged look-ups (limit 25). Measure type: C-peptide (plasma or serum unless marked urine). Section 5 is a derivation from published inputs with the standard EFLM formulas; it is not a finding, and the confidence statements are judgements, not computations.

Read levels: **FT** = full text read (for PMC papers here this means a keyword search of the full text with `tools/pmc_text.py`, not a cover-to-cover read); **Abs** = abstract only; **Rec** = PubMed record or title only, with numbers taken from a database page that cites the paper; **Web** = web page read directly.

# 1. Bottom line

1. **No within-person biological variation (CVi), reference change value or test-retest data were found for random (non-fasting) plasma C-peptide in insulin-treated adults or in any diabetes population.** This is the population and sample type Step A is about. The gap noted in `pathway-1-partners.md` is confirmed, not closed.
2. Every published CVi for C-peptide comes from small groups of **healthy** adults, mostly **fasting**, mostly measured on **RIA or older immunoassays** (1990 to 2008). The figures run from 9.3% to 28.4%. The EFLM Biological Variation Database lists 5 datasets and gives **no meta-analysed estimate** for C-peptide (Web). A 2018 EFLM systematic review graded every C-peptide publication BIVAC C (González-Lao 2018, Abs).
3. The only repeatability figures from people with diabetes are for **fasting and 2-h post-meal serum C-peptide in type 2 diabetes**: a 38% and a 27% coefficient of variation on repeat sampling (Bowman 2012, n = 77, Abs). These read as total within-person variation, analytical variation included, and come from a pre-2012 Exeter assay. Whether patients were insulin-treated, and what the sampling interval was, could not be confirmed from the abstract.
4. Current immunoassays are precise within a laboratory: CVa is about 1.4% to 10% (Abs). Agreement **between** methods is poor. Measured inter-method bias is 20% to 52%, and the inter-system CV is 24.5%. This is several times larger than any bias limit that biological variation would justify (section 5).
5. Pre-analytical handling matters, and in the same direction across studies. **K2/K3-EDTA whole blood is the most robust option at room temperature for up to 24 h.** Uncentrifuged serum at room temperature loses 22% to 74% over 24 to 48 h. Freeze-thaw (up to 4 to 6 cycles) and long-term storage at -80 °C look acceptable. One study disagrees on separated serum versus plasma in the fridge (section 4).
6. No C-peptide analytical performance specification set from clinical outcomes was found, and none from ADA, IFCC or EFLM. The only published desirable specification is the biological-variation one in the Ricós/Westgard 2014 table: CVa 8.3%, bias 7.1%, total error 20.8% (Web). It is built on healthy-subject CVi data of grade C quality.

# 2. Biological variation and repeatability

| Source | Population, state, n | Sample, assay | CVi (%) | CVg (%) | II (CVi/CVg) | Other figures | Read level | Notes |
|---|---|---|---|---|---|---|---|---|
| Ricós 1990, https://doi.org/10.1177/000456329002700412, PMID 2403234 | Healthy, n not seen | Serum; 1990-era RIA or ELISA (MeSH) | 9.3 (7.9 to 11.1) | 13.3 (9.5 to 21.1) | 0.70 (derived) | none | Rec; numbers from the EFLM BVD page | Older assay generation |
| Widjaja 1999, https://pubmed.ncbi.nlm.nih.gov/10102917/ (PubMed record has no DOI) | 12 healthy adults aged about 23, overnight fast, 12 consecutive days | Plasma per EFLM; RIA (MeSH) | 24 (EFLM CI 21.3 to 27.4) | 26.0 (18.0 to 43.9) per EFLM | 0.9 (paper) | Mean 0.39 nmol/L | Abs | Best BIVAC coding of the 5 EFLM datasets; RIA era |
| Lacher 2005 (NHANES III), https://doi.org/10.1373/clinchem.2004.039354, PMID 15590751 | US NHANES III participants, "healthy" per EFLM | Plasma; method not seen | 28.4 (27.2 to 29.6) | 65.7 (separate dataset, no CI) | not derivable (CVI and CVG from different datasets) | none | Rec; numbers from the EFLM BVD page | Fasting status unknown; population survey, so not steady-state healthy |
| Dittadi 2008, https://doi.org/10.1515/CCLM.2008.285, PMID 18844505 | Healthy, n not seen | Serum; three methods compared (IRMA and luminescent per MeSH) | 23.8 | 33.1 | 0.72 (derived) | Not seen | Rec (letter, no abstract); numbers from EFLM | Which of the three methods the EFLM figure refers to is unknown |
| Ricós/Westgard desirable specifications table, 2014 edition, https://www.westgard.com/clia-and-quality-regulation-requirements/quality-requirements/biodatabase1.html (also reproduced in a Bio-Rad 2024 table) | Pooled from 3 papers | Serum | 16.6 | 23.2 | 0.72 | Desirable CVa 8.3, bias 7.1, TE 20.8 | Web (excerpt) | Pre-BIVAC pooled values; the source papers are not named on the page |
| González-Lao 2018, https://doi.org/10.1016/j.cca.2018.10.031, PMID 30389455 | Systematic review | various | Not seen | Not seen | none | All C-peptide publications graded BIVAC C | Abs | The abstract says global estimates were made for all analytes except pyruvate, lactate and fructosamine, so a C-peptide figure may exist in the paywalled text. The EFLM BVD page says "No Meta-Analysis Calculation Found". **Unresolved.** |
| Bowman 2012, https://doi.org/10.1111/j.1464-5491.2011.03428.x, PMID 21883437 | 77 adults with type 2 diabetes (Exeter); insulin use not stated in the abstract | Serum C-peptide versus urine CPCR; Exeter routine assay (not stated in the abstract) | Fasting serum CV 38 (95% CI 26 to 59); 2-h post-meal serum CV 27 (20 to 34) | none | none | Urine CPCR: fasting 28 (21 to 35), post-meal 26 (18 to 33) | Abs | **The only diabetes repeatability data found.** Looks like total within-person CV (biological plus analytical). Interval between repeats not seen |
| McDonald 2009, https://doi.org/10.1373/clinchem.2009.129312, PMID 19713273 | 21 healthy volunteers | Urine CPCR; Roche ECLIA | none | none | none | CV for first-void fasting CPCR 52%, second-void 33% | Abs | Urine only |
| Greenbaum 2008, https://doi.org/10.2337/dc07-2451, PMID 18628574 | Type 1 diabetes up to 4 years' duration, TrialNet (148) and ECPT (118) | Stimulated (MMTT or glucagon) serum C-peptide, repeated 3 to 10 days apart | none | none | none | Peak C-peptide R² = 0.96 for repeat MMTT | FT (keyword search) and Abs | Stimulated, not random; no CV reported in the text searched |
| Vollenbrock 2022, https://doi.org/10.1111/dme.15012, PMID 36398450 | 535 adults with type 1 diabetes longer than 5 years | Fasting serum, ultrasensitive assay; year 0 versus year 1 | none | none | none | Small fall over 1 year (effect size -0.16) | Abs | Long-term drift, not short-term CVi |
| Hope 2017, https://doi.org/10.1007/s00125-017-4449-2, PMID 28983693 | Insulin-treated type 2 diabetes (n = 256) | Random non-fasting C-peptide | none | none | none | The authors call random C-peptide "practical, stable and inexpensive"; no repeatability figure in the abstract | Abs | Does not fill the gap |

Diet and time of sampling: C-peptide was among 6 of 77 analytes raised significantly by a standard breakfast or lunch in 20 healthy adults (Plumelle 2013, https://doi.org/10.1016/j.clinbiochem.2013.11.002, PMID 24240063, Abs). For a random-sample rule, the time since the last meal and the concurrent glucose are therefore part of the within-person variance, not noise to be ignored.

# 3. Analytical variation (CVa) and between-method agreement

| Source | Platform(s) | Within-lab imprecision | Between-lab or between-method | Read level | Assay-generation note |
|---|---|---|---|---|---|
| Little 2008, https://doi.org/10.1373/clinchem.2007.101287, PMID 18420730 | 15 labs, 9 routine methods, against the Missouri MS reference | Within-run under 2% to over 10%; between-run under 2% to over 18% | Disagreement largest at higher concentrations; recalibration with 8 sera removed significant differences | Abs | 2007-era methods; many since replaced |
| Hörber 2023, https://doi.org/10.1055/a-1998-6889, PMID 36630986 | Abbott Alinity i, DiaSorin Liaison XL, Roche Cobas e411, Siemens ADVIA Centaur XPT, Immulite 2000 XPi | not given | Mean bias up to 36.6% (Roche versus Centaur); Abbott, DiaSorin and Immulite within 2.3% to 4.2% of each other | Abs | Current platforms; German samples |
| Zhou 2022, https://doi.org/10.3343/alm.2022.42.4.428, PMID 35177563 | 94 Chinese labs, 5 serum pools | Mean intra-lab CV 2.3%; intra-system 6.7% | Inter-lab CV 16.4%; inter-system 24.5%, falling to 5.7% after recalibration with 2 pools | Abs | Current Chinese market mix |
| Cho 2024, https://doi.org/10.3343/alm.2024.0072, PMID 39175364 | ID-UPLC-MS/MS versus Roche ECLIA, 138 sera | MS intra- and inter-run under 5% | ECLIA +51.8% mean bias against MS (slope 1.564) | Abs | Current; Korea |
| Rohlfing 2025, https://doi.org/10.1515/cclm-2024-1260, PMID 39803820 | Anonymised current assays versus the Missouri RMP | not extracted | 95% limits of agreement width averaged 1.1 nmol/L before and 0.38 nmol/L after recalibration | FT (keyword search) | Current; the authors say biological variability, allowable error and universal thresholds "still need to be thoroughly studied" |
| Moradian 2024 (TaMADOR), https://doi.org/10.1093/clinchem/hvae034, PMID 38549041 | 3 LC-MS/MS laboratories | 2.7% to 3.7% CV at verification | Median interlaboratory imprecision 13.4% (single results), 10.8% (averaged replicates); slope 1.044 against Missouri RMP | Abs | Antibody-free LC-MS/MS |
| Deng 2023 (Ann Lab Med), https://doi.org/10.3343/alm.2023.43.4.345, PMID 36843403 | ID-LC-MS/MS | Total CV 1.3% to 2.2% | 6 immunoassays agreed far better after recalibration | Abs | Candidate reference-type method |
| Grothoff 2025, https://doi.org/10.1016/j.jmsacl.2025.02.001, PMID 40093566 | MRM LC-MS (Glu-C digest) | Inter-day under 9.6%, intra-day under 8.9% | r² 0.95 against reference method | Abs | Research method |
| Cabaleiro 2006, https://doi.org/10.1373/clinchem.2005.062505, PMID 16613996 | ID-LC/MS/MS | Total CV up to 2.9% | 3 immunoassays lacked intercomparability and trueness | Abs | Older immunoassays |
| Cosma 2019, https://doi.org/10.1016/j.cca.2019.04.057, PMID 30978327 | Mindray CL-2000i | Repeatability 1.35% to 1.7%; intermediate 1.4% to 2.6% | Similar to Tosoh AIA-CL2400 | Abs | Current, non-US |
| Oh 2018, https://doi.org/10.3343/alm.2018.38.6.530, PMID 30027696 | Fujirebio Lumipulse G1200 versus Roche E170, 200 insulin-treated patients | Within-lab 2.89% to 3.35% | Mean difference 0.2 nmol/L; no proinsulin cross-reactivity | Abs | Current or recent |
| El Kenz 2004, https://pubmed.ncbi.nlm.nih.gov/15074471/ (record has no DOI) | Siemens ADVIA Centaur | Total CV 6% to 10%; day-to-day 4.4% to 6.6% | +20% proportional bias against RIA | Abs | Older Centaur generation |
| de Leur 2022, https://doi.org/10.1111/dme.14785, PMID 34989030 | Mercodia ultrasensitive ELISA and Beckman IRMA | About 40% CV near the detection limit; LoQ 9.7 and 3.8 pmol/L | none | Abs | Relevant only below about 10 pmol/L, well below the 80 pmol/L level |
| Yu 2026, https://doi.org/10.1016/j.cca.2026.122908, PMID 42893716 | Alinity i, cobas e801, DxI 800, Atellica IM 1600 | not given | Pooled human serum more commutable than commercial controls; used 7.1% as the allowable error (the Ricós desirable **bias**) | Abs | Current US-marketed platform families, Korean samples |

Interference: hemolysis lowered C-peptide on the Abbott Alinity at hemoglobin concentrations within a 0.3 to 20 g/L band across analytes (Karin 2023, https://doi.org/10.1515/cclm-2022-0924, PMID 36635939, Abs). Hemolysis lowered C-peptide with dose and time on a Chinese routine platform (Wu 2016, https://doi.org/10.1002/jcla.22008, PMID 27231209, Abs). Older reports describing C-peptide as unaffected are cited there. Step A needs a hemolysis-index cutoff for each platform.

# 4. Pre-analytical stability

| Source | Design | Main result for C-peptide | Read level |
|---|---|---|---|
| McDonald 2012, https://doi.org/10.1371/journal.pone.0042084, PMID 22860060 | 3 platforms; tube, time to centrifugation, temperature | Stable 24 h at room temperature in K-EDTA (whole blood or spun) and in spun serum gel; **uncentrifuged serum gel fell to 78% at 24 h**; stable after 6 freeze-thaw cycles | Abs |
| Nkuna 2023, https://doi.org/10.1515/cclm-2023-0339, PMID 37409980 | 10 healthy adults, fasting and non-fasting; SST and K2-EDTA; Roche Cobas e602 | Separated serum at 2 to 8 °C for 7 days: -5% (serum) versus -13% (plasma). Delayed centrifugation at room temperature for 48 h: -46% (plasma), -74% (serum). Limit used: desirable total error from biological variation | Abs |
| Mubiru 2025, https://doi.org/10.1371/journal.pone.0312065, PMID 40587435 | 8 healthy adults (Uganda), random samples | K2-EDTA above 90% of baseline under all conditions to 24 h; **uncentrifuged plain serum at room temperature fell to 51%**; iced or spun serum above 90% | Abs |
| Oddoze 2012, https://doi.org/10.1016/j.clinbiochem.2012.01.012, PMID 22285385 | 81 analytes, 10 subjects | C-peptide affected by delay, tube type or temperature (no figure in the abstract) | Abs |
| Zhang 1998, https://pubmed.ncbi.nlm.nih.gov/9625060/ (record has no DOI) | Serum-clot contact at 32 °C | Separate serum within 6 h | Abs; older assay |
| Duschean 2026, https://doi.org/10.1080/17576180.2026.2690265, PMID 42495793 | Tasso+ SST capillary microsampling, 11 fasted healthy people | No consequential loss with 72 h delayed centrifugation at 4 °C | Abs |
| Jones 2018, https://doi.org/10.1177/1932296818763464, PMID 29521111 | Dried blood spot and VAMS | 48 h at room temperature: -11.6% (DBS), -0.1% (VAMS) | Abs |
| Retnakaran 2019, https://doi.org/10.1111/dom.13617, PMID 30565366 | Serum frozen at -80 °C for more than 5 years, then remeasured | CCC 0.91 (0.84 to 0.95) against the fresh result | Abs |
| Tjernvoll 2025, https://doi.org/10.1080/00365513.2025.2487989, PMID 40243258 | Pooled serum, 4 freeze-thaw cycles at -80 °C | Stable against a biological-variation-based allowable bias | Abs |
| Deng 2023 (CCLM), https://doi.org/10.1515/cclm-2023-0215, PMID 37141618 | Frozen human serum pools (EQA material) | Stable at 4 and -20 °C for 16 days or more, -80 °C for 1 year or more, room temperature only 12 h | Abs |
| McDonald 2009, https://doi.org/10.1373/clinchem.2009.129312, PMID 19713273 | Urine CPCR, 21 healthy | Unchanged 24 h at room temperature and 72 h at 4 °C without preservative; 72 h at room temperature in boric acid; 7 freeze-thaw cycles; **82% to 84% after 90 days at -20 °C** | Abs |
| Hagedorn 2026, https://doi.org/10.1016/j.jcte.2026.100438, PMID 42011319 | Urine CPCR, 18 non-diabetic, Tosoh | No preservative at room temperature: -16% at 48 h, -21% at 72 h; boric acid -16% at 72 h; sodium carbonate stable; cold packs after refrigeration acceptable | Abs |

What disagrees: the effect of boric acid on urine at 72 h (stable in McDonald 2009 on Roche; -16% in Hagedorn 2026 on Tosoh), and separated serum versus plasma in the fridge (serum better in Nkuna 2023). All stability studies used healthy volunteers, and most had 8 to 21 subjects. None studied insulin-treated patients, whose samples have low C-peptide and high exogenous insulin, and a proteolysis effect at low concentration has not been shown to be the same.

# 5. Derivation (not a finding): what limits follow from the CVi and CVa found

Standard EFLM/Fraser formulas (biological-variation model; minimum, desirable and optimum are factors of 0.75, 0.5 and 0.25 on CVi for imprecision and 0.375, 0.25 and 0.125 on the combined variation for bias):
- desirable CVa ≤ 0.5 × CVi
- desirable bias ≤ 0.25 × √(CVi² + CVg²)
- desirable TEa = 1.65 × (0.5 × CVi) + 0.25 × √(CVi² + CVg²)
- RCV (two-sided 95%) = √2 × 1.96 × √(CVa² + CVi²); log-normal (asymmetric) version shown where noted

| Input set (healthy subjects unless stated) | Desirable CVa | Desirable bias | Desirable TEa | Desirable bias in pmol/L at 80 / 200 / 600 | Minimum bias (pmol/L at 80 / 200 / 600) | RCV 95%, CVa 5% (symmetric; log-normal up/down) |
|---|---|---|---|---|---|---|
| Ricós 1990: CVi 9.3, CVg 13.3 | 4.7% | 4.1% | 11.7% | 3 / 8 / 24 | 6.1%: 5 / 12 / 37 | 29%; +34% / -25% |
| Ricós/Westgard 2014: CVi 16.6, CVg 23.2 | 8.3% | 7.1% | 20.8% | 6 / 14 / 43 | 10.7%: 9 / 21 / 64 | 48%; +61% / -38% |
| Widjaja 1999 (RIA): CVi 24.0, CVg 26.0 | 12.0% | 8.8% | 28.6% | 7 / 18 / 53 | 13.3%: 11 / 27 / 80 | 68%; +95% / -49% |
| Dittadi 2008: CVi 23.8, CVg 33.1 | 11.9% | 10.2% | 29.8% | 8 / 20 / 61 | 15.3%: 12 / 31 / 92 | 67%; +94% / -49% |
| Bowman 2012, T2D fasting serum, total CV 38 (no CVg) | n/a | n/a | n/a | n/a | n/a | 105%; +177% / -64% |
| Bowman 2012, T2D 2-h post-meal, total CV 27 | n/a | n/a | n/a | n/a | n/a | 75%; +109% / -52% |

How often a patient would cross a band edge on a repeat sample (derivation; log-normal, the person's true mean taken as fixed, no bias):

| Total within-person CV (CVi with CVa 5%) | Mean 700, result below 600 | Mean 800, result below 600 | Mean 250, result below 200 | Mean 160, result 200 or more |
|---|---|---|---|---|
| 10.6% (Ricós 1990) | 7% | 0% | 2% | 2% |
| 17.3% (Ricós/Westgard 2014) | 18% | 5% | 10% | 10% |
| 24.5% (Widjaja 1999) | 26% | 12% | 18% | 18% |
| 38% (Bowman 2012, T2D fasting) | 34% | 22% | 27% | 27% |

Single-result guard bands at a one-sided 95% level (same assumptions): to be confident that a person's mean is at least 600 pmol/L, one result would need to be about 710 (CVi 9.3) to 800 (CVi 16.6) to 890 (CVi 24) pmol/L, or about 1,100 pmol/L with Bowman's 38%. To be confident that the mean is below 200 pmol/L, the result would need to be at most about 170, 150, 135 or 110 pmol/L. CLASP's 900 pmol/L withdrawal cutoff (from `pathway-1-plan.md` section 7) falls inside this range.

Reading the derivation:
- The measured inter-method biases (20% to 52%; inter-system CV 24.5%) are 3 to 7 times the desirable bias (7.1%) and above even the minimum bias under every input set. So **harmonisation (Step A) is a necessary precondition** whatever CVi is finally used.
- The width of the CVi range (9% to 28%) changes the desirable bias at 600 pmol/L from about 24 to about 61 pmol/L, and the repeat-crossing rate near a band edge from single digits to about one in three. **The choice of CVi, not the formula, decides the answer.** None of the input sets describes the target population or sample type.
- Biological-variation specifications assume a stable patient (steady state). Random C-peptide in insulin-treated adults depends on the time since the last meal, the glucose level, renal function and possibly current insulin dose. A specification for a **fixed decision threshold** would ideally come from the clinical-outcome model (misclassification rate at 200 and 600 pmol/L), and none exists.
- A judgement, not a computation: until Step A measures CVi itself, the Ricós/Westgard desirable bias of **7.1% (about 6, 14 and 43 pmol/L at 80, 200 and 600 pmol/L)** is a defensible interim target for harmonisation, and a minimum target of **about 11% (9, 21 and 64 pmol/L)** is a fallback. This is not a validated specification.

# 6. What Step A would need to measure itself

1. **Within-person variation of random C-peptide in the target population.** About 30 to 40 insulin-treated adults with doubtful type, spread across the 80 to 1,000 pmol/L range. Take 4 or 5 random draws over 2 to 6 weeks with concurrent plasma glucose, time since last meal, insulin dose, eGFR and hemolysis index. Run all samples from one person in duplicate in a single run, on at least one immunoassay and the LC-MS/MS comparator. Use nested ANOVA (BIVAC-compliant design) to give CVi, CVa and CVg with confidence intervals, the index of individuality, the RCV, and the observed proportion crossing 200 and 600 pmol/L between draws. Report by glucose stratum (4 mmol/L or more against below 4) and by eGFR.
2. **Imprecision at the decision levels** (CLSI EP05/EP15-type) at about 80, 200 and 600 pmol/L on each platform. Check against the derived limits (section 5).
3. **Pre-analytical validation on patient samples, not only healthy volunteers.** K2-EDTA against serum gel; centrifugation at 0, 4, 24 and 48 h at room temperature and 4 °C; one to four freeze-thaw cycles; -20 °C against -80 °C storage for the residual-sera bank. Acceptance limit: the bias limit chosen from point 1 (or 7.1% in the interim). The 120 residual sera proposed in `pathway-1-plan.md` have unknown handling histories. Either document tube type and time to separation, or collect fresh samples prospectively.
4. **Hemolysis and other interference thresholds** for each platform. Cross-reactivity with proinsulin and split products at high proinsulin:C-peptide ratios, which is relevant to insulin-deficient patients.
5. **Commutability of the harmonisation materials** (pooled human serum, as in Yu 2026 and Deng 2023) before they are used to set platform-equivalent cutoffs.
6. Optional: whether a paired urine CPCR, posted from home, meets the same limits. Its within-person CV in type 2 diabetes was 26% to 28% (Bowman 2012), and it has its own stability limits (section 4).

# 7. Still unknown

- CVi, CVg, RCV and repeatability of **random** C-peptide in **insulin-treated adults** or any diabetes group: not found. The Bowman 2012 figures are the closest, covering fasting and 2-h meal samples in type 2 diabetes (abstract only, assay and insulin status not seen).
- Whether the González-Lao 2018 meta-analysis contains a global C-peptide CVi. The paper is paywalled, and the EFLM BVD page reports none.
- The assays behind the Ricós 1990, Dittadi 2008 and Lacher 2005 estimates, and their subject numbers: not read. Those figures come from the EFLM page.
- How CVi depends on concentration, glucose, eGFR and the time since a meal.
- Any outcome-based or consensus (ADA, IFCC, EFLM APS) analytical performance specification for C-peptide: none found. No CDC or NIST programme was found here either (consistent with `pathway-1-partners.md`).
- Stability in samples from insulin-treated patients, and in samples with low C-peptide (about 80 pmol/L or less).
- Whether the Hörber 2023 platform biases apply to US-labelled versions of the same analysers.

# 8. Search log (24 look-ups; limit 25)

| # | Tool | String or identifiers | Hits | Screened / used |
|---|---|---|---|---|
| 1 | PubMed search | C-peptide[Title] AND ("biological variation" OR "within-subject" OR "intra-individual" OR reproducibility OR repeatability) | 87 | First 25 retrieved; 20 screened in #4 |
| 2 | PubMed search | C-peptide[Title] AND (stability OR "pre-analytical" OR preanalytical OR "sample handling" OR EDTA) | 78 | First 25 retrieved; 20 screened in #5, 6 in #6 |
| 3 | PubMed search | "urine C-peptide" AND creatinine AND (stability OR validation OR boric) | 7 | 7 screened (#5, #6) |
| 4 | PubMed metadata | 23 PMIDs from #1 | 20 returned | 7 used; 29860430, 29404672 and 28731212 not returned, not screened |
| 5 | PubMed metadata | 26 PMIDs from #2 and #3 | 20 returned | 5 used |
| 6 | PubMed metadata | 28811070, 27083170, 24623023, 24353253, 21883437, 21843301 | 6 | 1 used (21883437); 27083170 seen (review) |
| 7 | PubMed search | (C-peptide OR "C peptide") AND ("biological variation" OR "biological variability" OR "reference change value" OR "index of individuality") | 11 | 11 screened in #8 |
| 8 | PubMed metadata | 10 PMIDs from #7 | 10 | 6 used |
| 9 | Web search | biologicalvariation.eu C-peptide; EFLM BVD C-peptide CVI; C-peptide CVI desirable bias | 10 results | EFLM page found |
| 10 | Web fetch | biologicalvariation.eu/api/search/by_analyte?query=C-peptide | 1 page | 5 datasets, no meta-analysis |
| 11 | PubMed search | Title phrases "Quality goals for hormone testing" / NHANES III BV / McDonald TJ C-peptide stability / "International comparison of C-peptide" | 6 | Only the McDonald clause ran; 22860060 and 19713273 used |
| 12 | PubMed search | ("random C-peptide" OR "non-fasting C-peptide" OR "nonfasting C-peptide") AND (repeat OR reproducib* OR variability OR "test-retest" OR agreement) | 8 | 8 screened in #13; none gave repeatability figures |
| 13 | PubMed metadata | 22860060, 19713273 and 8 PMIDs from #12 | 10 | 3 used |
| 14 | PubMed search | C-peptide[Title] AND (standardization/standardisation/harmonization/comparability[Title] OR inter-laboratory OR interlaboratory OR proficiency) | 13 | 13 screened |
| 15 | Web search | González-Lao 2018 C-peptide CVI; C-peptide allowable total error; CVI 9.3 CVG 13.3 | 10 results | Westgard and Bio-Rad tables (Ricós 2014 values) |
| 16 | PubMed metadata | 10 PMIDs from #14 | 10 | 6 used |
| 17 | PMC full text (`tools/pmc_text.py`) | PMC12043276 (Rohlfing 2025), keyword search | 1 | Used |
| 18 | PMC full text | PMC13007305 (Kabytaev 2026), keyword search | 1 | No numeric APS; not cited in tables |
| 19 | PubMed search | Greenbaum CJ MMTT versus glucagon / "clinical utility of C-peptide measurement" / "Quality goals for hormone testing" | 1 | Only the Greenbaum clause ran; 18628574 |
| 20 | PubMed search | C-peptide AND (hemolysis OR haemolysis OR hemolysed OR hemolyzed) AND (immunoassay OR interference) | 11 | 7 screened in #21; 3 used |
| 21 | PubMed metadata | 18628574, 7 PMIDs from #20, 38549041, 36630986, 37141618 | 11 | 7 used |
| 22 | PubMed search | Lacher DA biological variation NHANES OR "quality goals" hormone testing [Title] | 4 | 2 used (15590751, 2403234) |
| 23 | PMC full text | PMC2551636 (Greenbaum 2008), keyword search | 1 | Used (no CV in text) |
| 24 | PubMed metadata | 22997685, 20540274, 15590751, 2403234 | 4 | 2 used |

Tool-schema loads and local calculations (section 5, Python) are not counted. Consensus and Crossref were not used: the look-up limit was spent on PubMed and the EFLM pages. Identifiers were taken from the PubMed records retrieved in this run. Where a record has no DOI, it is cited by PubMed URL and noted.

Screened and not used: 29880650 (C-peptide decline phases in type 1 diabetes; not variation), 31572352 (immune marker ICC in type 1 diabetes; C-peptide not the subject), 25172526 (insulin analogue cross-reactivity in insulin assays; not C-peptide), 24623023, 24353253 and 21843301 (urine CPCR validation; correlation, not variation or stability), 41165798 and 40914229 (random C-peptide associations; no repeatability), 32847960 (LADA consensus random C-peptide bands 0.3 and 0.7 nmol/L; cutoffs, not variation), 19181472, 25291621 and 12766009 (doping, porcine, urine-standardisation letter).
