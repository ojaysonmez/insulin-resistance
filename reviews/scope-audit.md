# Scope audit: do the IR conclusions over-generalise across measure types?

Method: local files only (merged-conclusion.md, usecases-verified.md, analysis/*.md, reviews/steelman.md, reviews/skeptic-merged.md). No searches, no citation checks. Line numbers refer to the files as read on 2026-10-19.

Measure tags: CLAMP, FASTING, POSTLOAD, SURROGATE, CPEPTIDE, UNSPECIFIED (UNSPEC).

Assumptions recorded (ambiguities resolved):
- A1. Secretion uses (hypoglycaemia, insulinoma) are tagged by analyte: insulin drawn "at hypoglycaemia or during a fast" = FASTING; stimulated or mixed-meal C-peptide = POSTLOAD plus CPEPTIDE. These are not IR uses; the tag only says which sample type the evidence used.
- A2. "Insulin concentrations" with no sampling time stated (ES 2017 Rec 1.7, PCOS "insulin assays", insulin-assay comparison studies) = UNSPEC, with FASTING noted where the rationale text names fasting insulin.
- A3. Interaction trials that say only "insulin resistance", "insulin sensitivity" or "baseline insulin" with no measure in the files = UNSPEC (stated as "not determinable from the files").
- A4. DIETFITS "INS-30" (30-min insulin after glucose, per evidence-searcher.md L67) = POSTLOAD. Gardner 2016 "insulin-AUC median split" (evidence-searcher.md L66) = POSTLOAD.
- A5. SIRD/SIDD and DPP-cluster analyses are tagged by the index the files name (HOMA2-IR for Ahlqvist/Dennis clusters, scientist.md L95; "22 biomarkers" for DPP k-means = UNSPEC).
- A6. Claim counts in section 6 are rough: a claim can carry more than one tag.

---

## 1. Scope summary

1. The bottom lines rest almost entirely on FASTING evidence (fasting insulin, HOMA-IR) plus SURROGATE evidence (TyG, TG/HDL-C). Headline wording ("IR measurement") hides this.
2. Bottom line 1 (no routine utility) is supported by guideline text on "insulin assays" (PCOS), HOMA-IR/OGTT estimates (MASLD) and insulin concentrations (paediatric obesity), and by FASTING-based prediction nulls. It is not supported by any study of post-load insulin as a predictor.
3. Bottom line 2 ("shown not to add value") mixes evidence that points in different directions by measure: FASTING nulls (Hu, WHI, NHANES), conflicting SURROGATE results (ATTICA vs Liu 2026), and one prespecified null that is POSTLOAD (DIETFITS, INS-30), on a weight-loss outcome.
4. POSTLOAD insulin and OGTT-derived indices (Matsuda, OGIS, Stumvoll, WBISI, insulin AUC, insulinogenic index) are named in the files but carried into the conclusion only through DIETFITS, PERSON, EASL "OGTT-derived estimates" and teplizumab. No conclusion is about them as a class.
5. CLAMP appears only as the reference in validity claims. CPEPTIDE rests on a separate, well-sourced use-case list (classification, hypoglycaemia, graft, teplizumab) and is correctly kept out of the "IR" verdict, but one sentence ("No guideline ties an IR measurement to a management change", L16) is wrong for C-peptide.
6. The strongest measurement conclusion (L55) is correctly scoped to fasting insulin/HOMA-IR, but L54 says Matsuda/TyG variation is "not covered" while the files hold OGIS, Stumvoll, WBISI and 2-h insulin test-retest data.
7. Roughly 30 of about 124 claims are UNSPEC, mostly interaction-trial rows, guideline sentences about "insulin assays" and registry rows.
8. Rather than "no utility of IR measurement", the supportable statement is "no established utility of routine fasting insulin, HOMA-IR or TyG/TG-HDL-C; post-load and C-peptide measures were evaluated only in niche uses".
9. The skeptic review (reviews/skeptic-merged.md) scoped BL1 by "routine" versus not, never by measure type.
10. The use-case file carries a Kind column (secretion / classification / IR / research) that groups by purpose, not by measure; rows with the same measure sit in different kinds.

---

## 2. Matrix: measure category x question

Legend: EVIDENCE = evidence in the files (cell cites file, section, PMIDs). MENTION ONLY = named, no evidence carried into the conclusion. NONE = not addressed in any file. Where the files carry evidence but the merged conclusion does not, the cell says "not carried".

Columns: (a) diagnosis/classification, (b) risk prediction/incremental value, (c) treatment selection/effect modification, (d) monitoring/response, (e) measurement quality, (f) guidelines.

| Category | (a) Dx/classif. | (b) Prediction | (c) Treatment selection | (d) Monitoring | (e) Measurement quality | (f) Guidelines |
|---|---|---|---|---|---|---|
| CLAMP | EVIDENCE as reference only: HOMA r -0.82, kappa 0.63 (10857969); TyG r -0.68 (20484475); merged L32; biostatistician.md S2, scientist.md S2 | NONE | NONE | MENTION ONLY: surrogates did not track clamp change after RYGB (28202439), chemist.md S2; not carried | MENTION ONLY: single dose, research tool (scientist.md 2.1; 17957034); no clamp reproducibility in any file | NONE (clamp = research tool, endocrinologist.md S1) |
| FASTING | EVIDENCE: JDS fasting insulin >30 (35463863); cutoff studies (27658115, 31108989, 34380182); usecases rows 12, 14-16 | EVIDENCE: Hu 38191206, WHI 25944628, NHANES 42702103, Framingham 17533210, Wang 35700159, Gast 23300589, 36181637 (merged L24-30) | EVIDENCE: IRIS 26886418, LAMP 42145088, MA.32 35608580/42063220, presurgical metformin 22564993, LIRA-ADD2 34132018, GRADE 38190619 (merged L31, L68-85) | EVIDENCE (variability argument only, derived): EuBIVAS 38987271, ARIC 29618016, Jayagopal 12401750; NAFLD change 34674510 (merged L47, L100). No clinical monitoring outcome study | EVIDENCE (strongest): 38987271, 29618016, 18535197, 34380182, 40802520, 35177563, 17272483, 19325009, 28660493 (merged L36-55) | EVIDENCE: PCOS PP 1.9.12/3.1.10 (37580314), EASL (38851997), ES 2017 Rec 1.7 (28359099), ADA 3.13, AACE R9.4, JDS (merged L13-22; usecases rows 12-16). Negatives regex-limited |
| POSTLOAD | EVIDENCE for non-IR uses: OGTT-induced hypoglycaemia (ENETS 26742109, row 23), post-bariatric (30101281, 34802853, row 5). For IR diagnosis MENTION ONLY: Matsuda r 0.73 (10480510), Abdul-Ghani (17192339), scientist.md 2.4; not carried | EVIDENCE, not carried: Health ABC 19700136 (OGTT, insulin, HOMA none improved HF prediction), Framingham Gutt ISI (17533210, biostatistician.md S2), Wagner OGTT phenotypes (33398163, endocrinologist.md S2). No dedicated search pass (evidence-searcher.md L308) | EVIDENCE: DIETFITS INS-30 P=0.47 (29466592), Gardner 2016 (26638192), PERSON (36599304), teplizumab MMTT C-peptide (FDA label, row 29), Herold OGTT C-peptide (31180194, row 30) | EVIDENCE (research endpoint): MMTT C-peptide in T1D trials (14693724, 18628574, 32219329; row 8); RYGB surrogates fail (28202439). Not carried in merged | EVIDENCE, not carried: Hudak OGIS CV 6.5% (34679116), Gordon OGIS 7.8%, Stumvoll 14.4% (21945562), Hani WBISI (39726936), Mooy (8721775); chemist-round2.md 2.1. Merged L54 says "not covered" | EVIDENCE: PCOS 1.9.9 (OGTT glucose, not insulin), EASL "OGTT-derived estimates", ISPAD CFRD (36537525, insulin not in screening), Igls (29528967), FDA label; usecases rows 14, 19, 29 |
| SURROGATE | EVIDENCE (validity): TyG vs clamp (20484475), review AUC 0.59-0.88 (32256572), TG/HDL (14623617, 21730284), 15983289 | EVIDENCE: Liu 2026 42569452, ATTICA 41178693, 39117485, Barzegar 32993633, NHANES 42702103, Pang 36093151, Tai 35999546 (evidence-searcher.md S3.1) | MENTION ONLY: eGDR in FIDELITY/FINEARTS-HF (no insulin assay), TriMaster routine-features model (merged L86, L78) | NONE (no TyG repeatability or TyG monitoring study found; chemist-round2.md 2.1) | EVIDENCE (TG/HDL only): CV 23.0%, MDC 1.4 (29618016). TyG repeatability NONE. Portability advantage stated | EVIDENCE (one statement): ADA/EASD 2023 TyG "moderate evidence" CVD prediction (37794253, merged L21) |
| CPEPTIDE | EVIDENCE: Holt 34590174, Jones 23413806, PMDI 37794142, Cryer 19088155, HI guideline 37454648, PES 25957977, JDS fulminant/SPIDDM (24843620, 38184802); usecases rows 1-7, 31-33, 46-47 | EVIDENCE (thin): bariatric remission scores 22963817, 32873586 (no incremental C-peptide analysis); Herold OGTT C-peptide HR 0.19 (31180194, hypothesis-generating) | EVIDENCE: teplizumab Stage 3 eligibility (FDA label, row 29); presurgical metformin: C-peptide did not modify (22564993); GRADE C-peptide response (38190619, evidence-searcher.md L160; merged cites HOMA2-%S only) | EVIDENCE: T1D trial endpoints (rows 8), Igls graft (29528967, 29453879, 34061967), TPIAT (38895780) | EVIDENCE: Zhou 24.5% to 5.7% (35177563), Little 18420730, Wiedmeyer 17332147, Hörber 36630986, Rohlfing 39803820, TaMADOR 38549041, renal clearance (30794834). C-peptide CVI ~24%, n=12. EuBIVAS C-peptide NONE found | EVIDENCE: ADA 2026 s2 (41358893), HI guideline Rec 1.1/1.4, Igls, FDA label, Holt consensus, JDS. Proinsulin only in hypoglycaemia (b-d, proinsulin: NONE) |
| UNSPEC | MENTION ONLY: "IR phenotypes" (Wagner), PCOS "insulin assays" sentence; no measure fixed | EVIDENCE, measure not determinable: ODYSSEY 42291078 (merged L86) | EVIDENCE, measure not determinable from the files: Cornier 15897479, 39756404, DPP k-means 40497454, PCOS IPD 31647106, ITT-IR ISRCTN11215387, PLIS 34531293 | NONE (usecases row 17: "monitoring tested in none of the sources read") | EVIDENCE: insulin-assay comparisons not sample-type specific: Manley 17363420 (99 fasting/51 postprandial), Rohlfing 40802520, Zhou 35177563, Marcovina 17272483, Tohidi 28150502 | EVIDENCE: PCOS (37580314), ES 2017 (28359099) wording "insulin assays / insulin concentrations" |

---

## 3. Over-general statements (need rewording)

"Categories actually used" = measure categories of the sources cited for that claim, as the files describe them.

### 3.1 merged-conclusion.md

| ID | Location | Short quote | Categories actually used | Suggested rewording |
|---|---|---|---|---|
| M1 | L8 (bottom line 1) | "No established clinical utility today for routine IR measurement (HOMA-IR, fasting insulin, TyG, TG/HDL-C)" | FASTING; SURROGATE; guideline items UNSPEC (PCOS "insulin assays") and FASTING+POSTLOAD (EASL) | "No established clinical utility for routine fasting insulin, HOMA-IR or TyG/TG-HDL-C measurement in [settings]. Post-load insulin, OGTT-derived indices and mixed-meal measures were not separately evaluated for routine use." |
| M2 | L9 (bottom line 2) | "Support is one prespecified null interaction test (DIETFITS, n=609, P = 0.47)" | POSTLOAD (INS-30; weight loss); FASTING nulls (WHI, Hu, NHANES); SURROGATE conflict (ATTICA vs Liu 2026) | State per measure: "For fasting insulin/HOMA-IR, small incremental-value nulls; for TyG, conflicting results; the one prespecified interaction test used 30-min post-glucose insulin and a weight-loss outcome." Keep the 45-50% figure labelled as covering a mixed set. |
| M3 | L10 (bottom line 3) | "Insulin and C-peptide have clinical roles, mostly not as IR screening" | CPEPTIDE; FASTING (insulin at hypoglycaemia); POSTLOAD (MMTT in teplizumab) | "Insulin (drawn during hypoglycaemia) and C-peptide (random, fasting or mixed-meal stimulated) have clinical roles..." Minor. |
| M4 | L16 | "No guideline ties an IR measurement to a management change." | UNSPEC; true for FASTING/POSTLOAD-derived IR estimates; false for CPEPTIDE (Holt, ADA s2, HI guideline, Igls, FDA label) | "No guideline read ties a fasting insulin, HOMA-IR or OGTT-derived IR estimate to a management change; C-peptide-based classification and eligibility rules are the exception (use-case list)." |
| M5 | L17 (PCOS) | "insulin assays are of limited clinical relevance and not recommended in routine care" | UNSPEC (guideline names no index; reason is assay inaccuracy) | Add "(guideline does not specify fasting vs post-load or an index)". Minor. |
| M6 | L19 (paediatric obesity) | "recommends against measuring insulin concentrations" | UNSPEC (sampling time not stated; rationale text names fasting insulin) | Add "(rationale names fasting insulin; OGTT insulin not addressed in the text read)". Minor. |
| M7 | L23 | "Incremental prediction is thin where tested." | FASTING (Hu, WHI, NHANES, Framingham, Wang); SURROGATE (Liu, Barzegar, ATTICA, 39117485); POSTLOAD not carried (Health ABC 19700136, Gutt ISI) | "For fasting insulin/HOMA-IR, incremental prediction was small or null in the cohorts found; for TyG, results conflict; post-load insulin and C-peptide were not evaluated as predictors in the conclusion." |
| M8 | L32 | "Surrogates are modest." | SURROGATE (TyG, TG/HDL-C); FASTING (HOMA vs clamp); CLAMP; POSTLOAD (Matsuda r 0.73) not carried | "Fasting indices and non-insulin surrogates agree modestly with the clamp (...). OGTT-derived indices (Matsuda r 0.73, 10480510) are in the files but not weighed here." |
| M9 | L54 | "Not covered: TyG or Matsuda biological variation" | POSTLOAD; SURROGATE | "Not covered: TyG repeatability (none found) and Matsuda-specific variation. OGIS CV 6.5-7.8%, Stumvoll 14.4%, WBISI and 2-h insulin test-retest data exist (34679116, 21945562, 39726936, 8721775) and are not carried here." |
| M10 | L55 | "a single fasting insulin or HOMA-IR cannot reliably classify an individual near a cutoff" | FASTING (correctly scoped) | Add that this is "the strongest measurement conclusion for fasting measures; not tested for post-load indices". Minor. |
| M11 | L58 | "No randomized trial comparing IR-measurement-guided care with usual care was found." | UNSPEC (strings HOMA-IR/IR-guided; searcher also found a measure-comparison trial ACTRN12624000306516, mixed-meal vs fasting vs OGTT vs clamp) | Name the measures searched; add the ACTRN trial as a diagnostic-comparison design, not an outcome trial. |
| M12 | L67-83 (table header "Randomized or trial-based interaction evidence") | "Randomized or trial-based interaction evidence" | Mixed: POSTLOAD (DIETFITS, Gardner, PERSON), FASTING (HOMA), UNSPEC (Cornier, 39756404, DPP k-means, PCOS IPD, ODYSSEY) | Add a "Measure" column; 5 of the 13 rows have no measure stated in the files (not determinable). |
| M13 | L88 | "no baseline-IR interaction in the CV outcome trials" | FASTING (search string was HOMA-IR) | "no baseline HOMA-IR interaction..." |
| M14 | L125 (gap 3) | "treatment-by-baseline-IR interaction evidence with hard outcomes" | UNSPEC | "treatment-by-baseline (fasting, post-load or C-peptide) measure interaction..." and say which measure each gap targets. |

### 3.2 usecases-verified.md

| ID | Location | Short quote | Categories actually used | Suggested rewording |
|---|---|---|---|---|
| U1 | row 17, L34 | "Unsupported (routine use)" for "HOMA-IR, TyG" prediction, monitoring, screening | FASTING+SURROGATE; sources are consistency checks, "prediction-model papers not re-verified"; monitoring "tested in none of the sources read" | Split into three rows, each with its measure; mark monitoring "not determinable from the files (variability argument only)". |
| U2 | row 15, L32 | "Fasting insulin, HOMA-IR" / "Unsupported for routine care" | Guideline says "insulin assays" (UNSPEC) | "Unsupported for routine care (guideline: insulin assays, no index named)". |
| U3 | row 36, L53 | "Fasting insulin, HOMA-IR" / "Unsupported" in children with obesity and prediabetes/T2D | Rec 1.7 concerns obesity evaluation, not dysglycaemia detection; row says "Same source and caveats as row 16" | "Unsupported by extension from Rec 1.7; no source read addresses insulin testing for dysglycaemia in these children." |
| U4 | rows 42-44, L59-61 | "None" / "Unsupported" | No measure; absence of any insulin test from sources, two read only as secondary snippets | Label "no insulin or C-peptide use found in sources read" instead of "Unsupported". |
| U5 | rows 35 and 45, L52, L62 | "Research-only" (first-trimester HOMA-IR; postpartum IR cohorts) | FASTING/UNSPEC, title-level only | "Not evaluated (title-level); status not determinable from the files". |
| U6 | L79 | "No row classed as an insulin-resistance use reaches 'established'." | IR-kind rows are FASTING (12, 13, 15, 16, 17, 35, 36, 37, 39) and POSTLOAD (14, 18, 38); Kind assigned by purpose | "No row using fasting insulin, HOMA-IR or OGTT-derived measures for an IR question reaches established." |
| U7 | L175 | "every IR-kind row is limited, research-only or unsupported" | FASTING, POSTLOAD; reviewers did not touch incremental-value papers (L161) | Say the use-case review supports the verdict for use-case rows only; prediction not reviewed. |

### 3.3 analysis/ files (bottom lines stated as general)

| ID | Location | Short quote | Categories actually used | Suggested rewording |
|---|---|---|---|---|
| A1 | analysis/pcp.md L8 | "Routine IR measurement (fasting insulin, HOMA-IR, or similar) is not useful in primary care today." | FASTING (Hu E2, Gast E3, Bonora E4); "or similar" UNSPEC; no POSTLOAD, CPEPTIDE or TyG evidence | "Routine fasting insulin or HOMA-IR..."; drop "or similar". |
| A2 | analysis/endocrinologist.md L125 | "Measuring IR (HOMA-IR, fasting insulin, TyG) is not guideline-supported as a diagnostic or treatment-selection tool" | FASTING; mostly [recall]/[opinion]; TyG cited only as definition (19067533) | Mark guideline statements as recall-based (L80, L88 say "verify") and drop TyG from the list. |
| A3 | analysis/biostatistician.md L17 | "gain was nil to negligible (Framingham Offspring, Hu 2024, ARIC)" | FASTING (Hu); Framingham FASTING+POSTLOAD (Gutt ISI); ARIC rules did not test insulin (its own S2 row 4) | Remove ARIC from the list of insulin-based nulls. |
| A4 | analysis/biostatistician.md L19 | "There is no defensible universal cutoff." (thresholds 1.4-3.6) | FASTING (HOMA-IR only) | "no defensible universal HOMA-IR cutoff"; TyG, OGTT-index cutoffs not assessed. |

Not over-general (scoped adequately): merged L12 (JDS fasting insulin), L13 (IRIS HOMA-IR >3.0), L24-31 (study-specific), L36-53 (fasting HOMA-IR/insulin and named assay studies), L85 (LAMP); chemist.md L35; scientist.md L87.

Count: 14 (merged) + 7 (use-cases) + 4 (analysis) = 25 statements need rewording; 4 of them are minor (M3, M5, M6, M10).

---

## 4. Post-load and mixed-meal evidence in the files, not used or weakly used

| # | Item (file, section; PMIDs as written) | How merged/usecases use it |
|---|---|---|
| 1 | DIETFITS INS-30 interaction, n=609, P=0.47 (evidence-searcher.md S2.1 L67; PMID 29466592) | Used as "the" prespecified null, labelled generically in BL2 (L9); POSTLOAD not stated there |
| 2 | Gardner 2016 pilot insulin-AUC strata (26638192); Follis 2026 (41436888); Soto-Mota 2023 (36811468) (evidence-searcher.md L66-69) | Gardner in table only; the other two not carried |
| 3 | PERSON OGTT-derived muscle vs liver IR, n=242 (36599304; evidence-searcher.md L70) | In table with null primary; no "POSTLOAD" label |
| 4 | Matsuda vs clamp r 0.73, n=153; naive mean-G/mean-I r -0.02 (10480510; scientist.md 2.4); Abdul-Ghani muscle r 0.78, liver r 0.64 (17192339), contested (17596506); Elisha 27931981 | Not in merged L32; merged L112 calls tissue-weighting "weak or uncited" (scientist.md cites 17192339 for OGTT-derived tissue indices; HOMA hepatic weighting is a "mechanistic reading", 15161807) |
| 5 | Reproducibility: Hudak 34679116 (OGIS CV 6.5 +/- 5.1%, revised QUICKI 2.8%), Gordon 21945562 (OGIS 7.8%, Stumvoll 14.4%), Hani 39726936 (WBISI more reproducible than fasting indices, 257 children), Mooy 8721775, Schousboe 12564620 (chemist-round2.md 2.1; evidence-searcher.md L330-340) | Merged L54 says "Not covered" |
| 6 | Incremental prediction: Kalogeropoulos 19700136 (OGTT, fasting insulin, HOMA-IR none improved HF prediction, evidence-searcher.md L114); Framingham Gutt ISI 17533210 (biostatistician.md S2) | Merged cites 17533210 only for HOMA-IR/insulin |
| 7 | Wagner 2021 33398163, OGTT-derived subphenotypes (endocrinologist.md S2) | Dismissed at merged L108 as "not an IR index"; not weighed as POSTLOAD |
| 8 | Mixed-meal: ACTRN12624000306516 randomized crossover, mixed-meal vs fasting vs OGTT vs clamp, n=255 (evidence-searcher.md L92) | Not mentioned in merged |
| 9 | Stimulated C-peptide: MMTT in T1D trials (14693724, 18628574, 32219329, row 8); TPIAT (38895780, 39994886, row 27); Herold OGTT C-peptide HR 0.19 (31180194, row 30); Igls (29528967, 29453879, 34061967, row 10) | Only teplizumab (row 29) reaches BL3 (L11) |
| 10 | OGTT insulin for postprandial insulinoma (ENETS 26742109, row 23); post-bariatric nadir insulin (30101281, 34802853, row 5) | Not in merged |
| 11 | CFRD: ISPAD 36537525 (insulin not part of screening), insulinogenic index study 22743620 (row 19) | Not in merged |
| 12 | Bojsen-Moller 28202439: after RYGB fasting and OGTT surrogates did not track clamp change (chemist.md S2) | Not carried; bears on monitoring (d) |
| 13 | Manley 17363420 (99 fasting, 51 postprandial sera, factor 2); Rohlfing 40802520 (underestimated above 300 pmol/L; evidence-searcher.md L214, chemist-round2.md 2.1) | Cited only as fasting-range disagreement; not tied to post-load values |
| 14 | Surrogate-vs-clamp reviews: Otten 24891021, Renklint 39013634, Malagon-Soriano 38715798 (evidence-searcher.md L375, L233) | Not in merged |
| 15 | GRADE C-peptide response (38190619; evidence-searcher.md L160) | Merged cites HOMA2-%S only |

---

## 5. Gaps that would need new searches (ranked by potential to change a bottom line)

1. POSTLOAD, (b): do OGTT insulin, Matsuda, insulin AUC or insulinogenic index add discrimination/reclassification over fasting glucose, HbA1c, 2-h glucose and BMI for T2D and CVD? Only one pass (Q2t, 41 records, evidence-searcher.md L308, L564). Could limit BL1 and BL2 to fasting measures or overturn them for post-load.
2. FASTING / POSTLOAD / CPEPTIDE, (c): prespecified treatment-by-baseline-measure interaction with hard outcomes, per measure (current gap 3 is measure-blind). DIETFITS (POSTLOAD) is the only prespecified test; the rest are exploratory or have no stated measure.
3. SURROGATE, (b): TyG/TG-HDL-C over PCE/SCORE2 with calibration and decision curve; 145 decision-curve records unscreened (steelman.md S3). Could settle the ATTICA vs Liu 2026 conflict in BL2.
4. POSTLOAD, (e)+(a): clamp-anchored accuracy and reproducibility of OGTT indices versus fasting indices in adults (Otten 24891021 and Hudak/Hani abstracts are unscreened beyond title/abstract). Could change the "strongest measurement conclusion" scope (L55).
5. CPEPTIDE, (b)-(c): fasting or stimulated C-peptide as predictor or effect modifier of drug response in T2D (steelman.md P10, 138 records, not screened). Could add a treatment-selection use not in the 47 rows.
6. UNSPEC resolution (no new search; read the records): which measure was used in Cornier 15897479, 39756404, DPP k-means 40497454, PCOS IPD 31647106, ODYSSEY 42291078, PLIS 34531293, ITT-IR, TRIO-BD 35120288. Not determinable from the files.
7. POSTLOAD, (c): replication or full text of PERSON-type OGTT-phenotype-matched trials; results of ACTRN12624000306516 when available.
8. FASTING/CPEPTIDE, (e): EuBIVAS insulin and C-peptide CVI/CVG (33554550 letter values not retrieved), proinsulin cross-reactivity on current platforms, EQA data, TyG repeatability (all open in chemist-round2.md S6). Affects measurement scope, not a bottom line directly.
9. FASTING/POSTLOAD, (a)-(b): early-pregnancy IR measures for GDM; PCOS testing-strategy literature (merged L103; evidence-searcher.md L307 "fewer strings").

---

## 6. Measure-type tag counts (rough; a claim may carry more than one tag)

| Claim group | n | CLAMP | FASTING | POSTLOAD | SURROGATE | CPEPTIDE | UNSPEC | No measure |
|---|---|---|---|---|---|---|---|---|
| Bottom lines (BL1, BL2, BL3 three sub-bullets) | 5 | 0 | 5 | 2 | 2 | 1 | 2 | 0 |
| Merged "well supported" findings (guidelines 6, prediction 8, association 2, IRIS 1, surrogates 3) | 20 | 2 | 11 | 3 | 10 | 0 | 2 | 0 |
| Merged measurement findings (L36-55) | 9 | 0 | 5 | 0 | 0 | 3 | 4 | 0 |
| Merged trial rows: registry/design items (6 registry, ITT-IR, PLIS, no-RCT claim) | 9 | 0 | 3 | 1 | 0 | 1 | 5 | 0 |
| Merged trial table (13 rows) plus LAMP, eGDR, ODYSSEY | 16 | 0 | 7 | 3 | 1 | 2 | 5 | 0 |
| Steelman and other additions (oncology, psychiatry x2, MAFLD, MR, far-from-cutoff, bariatric, eGDR-T1D, NAFLD change, STAR/Quantose, "go team's way", not-tested, niche trial) | 13 | 0 | 6 | 0 | 2 | 1 | 5 | 0 |
| "Not supported" and corrections (IR phenotypes, PCOS, grade, 1-h glucose, clamp/HOMA tissue weighting) | 5 | 1 | 2 | 2 | 0 | 0 | 3 | 0 |
| Use-case rows 1-47 (usecases-verified.md) | 47 | 1 | 16 | 11 | 2 | 26 | 4 | 7 |
| Total | 124 | 4 | 55 | 22 | 17 | 34 | 30 | 7 |

Use-case row assignment (by "#"): FASTING 1-4, 12-18, 24, 35-37, 39. POSTLOAD 5, 8, 9, 14, 18, 19, 23, 27, 29, 30, 38. CPEPTIDE 1-11, 14, 20, 21, 24, 25, 27-33, 38, 46, 47. SURROGATE 17, 41. CLAMP 18. UNSPEC 20, 21 (insulin sampling time), 22, 45. No measure (negative entries) 26, 30 (selection), 34, 40, 42, 43, 44.

UNSPECIFIED claims (by group):
- Bottom lines: BL1 headline wording, BL2 headline wording.
- Well supported: PCOS guideline sentence (L17), limits of "no recommendation found" (L22).
- Measurement: assay-disagreement (L38), inter-laboratory disagreement (L39-44), reference-method statements (L49-53), pre-analytical (L54).
- Trials: "no RCT of IR-guided care" (L58), ITT-IR, PLIS, IRCT20170812035642N11, NCT06856291, Cornier 2005, 39756404, DPP k-means, PCOS IPD, ODYSSEY.
- Steelman additions: TRIO-BD, pioglitazone in depression, STAR/Quantose, "points that go the team's way" (TODAY etc.), "not tested by anyone" list.
- "Not supported": IR phenotypes (L108), PCOS "adds nothing", grading of "don't test" verdicts.
- Use cases: rows 20, 21, 22, 45.

---

## Summary (10 lines)

1. The bottom lines were written about fasting insulin/HOMA-IR plus TyG/TG-HDL-C but are phrased as "IR measurement".
2. 25 statements need rewording (14 in merged-conclusion.md, 7 in usecases-verified.md, 4 in analysis files); 4 of these are minor.
3. BL2's only prespecified null (DIETFITS) is a post-load (INS-30) test on weight loss, not fasting; this is not stated in the bottom line.
4. "Incremental prediction is thin" (L23) mixes FASTING nulls with conflicting TyG results and omits POSTLOAD data (Health ABC, Gutt ISI).
5. "No guideline ties an IR measurement to a management change" (L16) is false for C-peptide; it holds only for fasting and OGTT-derived IR estimates.
6. L54 says Matsuda variation is "not covered" while the files hold OGIS, Stumvoll, WBISI and 2-h insulin reproducibility data (not carried).
7. About 30 of roughly 124 claims are UNSPECIFIED, mostly interaction trials, "insulin assay" guideline wording and registry rows; the measure used is not determinable from the files for several.
8. The Kind column in usecases-verified.md groups by purpose, so the "no IR use is established" count is not a statement by measure type.
9. Top three gaps: (1) post-load insulin/index incremental value over glucose and BMI; (2) per-measure treatment-by-baseline interaction with hard outcomes; (3) TyG/TG-HDL-C incremental value with calibration and decision curve (145 records unscreened).
10. Recommended scope for the verdict: "no established utility of routine fasting insulin, HOMA-IR or TyG/TG-HDL-C"; post-load and C-peptide are evaluated only for niche uses.
