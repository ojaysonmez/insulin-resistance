# Evidence searcher: Round 2 report (peer exchange with the clinical chemist)

**Date:** 2026-10-19. Original report (`ir-team/ir-evidence-searcher.md`) was not edited. Read levels use the codes of the original report (FT = full text read at the relevant passage, Abs = PubMed abstract, Title = record only). All PMIDs/DOIs listed were pulled back from PubMed (`efetch`) on 2026-10-19; the full list of Round 2 strings and counts is in the appendix. Coverage and reimbursement stay out of scope.

## (i) Exchange log

| # | Direction | Content (short) |
|---|---|---|
| 1 | Me → chemist | Staten 2010 (PMID 20040676, FT-scan): "isotope dilution mass spectrometry, a reference measurement procedure for insulin…"; Miller 2009 (PMID 19325009, Abs) and Rodríguez-Cabaleiro 2007 (PMID 17586588, Abs) wording; stated that I had seen no JCTLM listing. Asked for the exact wording of the 2024 LC-MS/MS paper (PMID 38549041) on a reference procedure and for the request list. |
| 2 | Chemist → me | Six retrieval requests: (1) insulin/C-peptide biological variation; (2) post-2019 multi-vendor comparability; (3) OGTT-index and TyG reproducibility; (4) proinsulin and analogue cross-reactivity on current platforms; (5) source and wording of the ID-MS reference procedure statement and JCTLM status; (6) guideline statements on C-peptide handling, reference ranges and insulin pre-analytics. The chemist did **not** answer my question about the 2024 paper's wording (I read it myself, below). |
| 3 | Me → chemist | One numbered reply covering all six requests (identifiers, one-line contents, read levels, strings searched, what was not found). **Correction needed to message 3:** I gave PMID 21617108 the DOI `10.1373/clinchem.2010.161596` and the citation "Clin Chem 2011;57:e1". PubMed shows PMID 21617108 is the Diabetes Care version (Sacks DB 2011, doi:10.2337/dc11-9998); `10.1373/clinchem.2010.161596` belongs to PMID 21617152 (Clin Chem version). I had used up my two outgoing messages, so this correction has not been sent to the chemist. |

## (ii) New items, new search log, what changed

### Request 1 — biological variation
- **Carobene 2022**, PMID 33554550, doi:10.1515/cclm-2020-1490 (CCLM letter, "Biological variation of serum insulin: updated estimates from EuBIVAS and meta-analysis"). Read level: **Title only**; PubMed has no abstract, Crossref has no abstract, no open-access copy found. The CVI/CVG/RCV values were not retrieved.
- González-Lao 2019, PMID 30389455, doi:10.1016/j.cca.2018.10.031 (Abs): systematic review of BV data for diabetes-related analytes (47 publications; C-peptide publications all BIVAC grade C; global estimates produced for insulin and C-peptide; numbers not in abstract).
- Mooy 1996, PMID 8721775, doi:10.1007/BF00418345 (Abs): two 75-g OGTTs, SDdif of fasting insulin 23–32 pmol/L and of 2-h insulin 190–304 pmol/L, by glucose-tolerance category; Schousboe 2002, PMID 12564620, doi:10.1080/003655102764654358 (Abs): duplicate OGTTs, CV of insulin and HOMA.
- No C-peptide EuBIVAS paper found.

### Request 2 — post-2019 comparability
- **Rohlfing 2025**, PMID 40802520, doi:10.1515/cclm-2025-0552 (FT): 12 insulin immunoassays from 9 manufacturers on 40 sera vs an IDMS method; ICC > 0.99 within assay; differences vs LC-MS −298.2 to +302.6 pmol/L; only one assay in full agreement.
- Rosli 2022, PMID 35622611, doi:10.1002/jcla.24521 (FT): 7 kits, RSD 1.7–23.2 %.
- Deng 2023, PMID 36750430 (serum-pool commutability, Abs); Tohidi 2017, PMID 28150502 (8 assays, factor 1.8, Abs); Loh 2017, PMID 27665422 (Title); Rohlfing 2025 C-peptide, PMID 39803820, doi:10.1515/cclm-2024-1260 (FT); Schleicher 2025, PMID 40781799 (Abs); Cosma 2019, PMID 30978327 (Abs); Larsen 2017, PMID 27989491 (Abs).
- Not found: CAP or other EQA survey data for insulin.

### Request 3 — reproducibility of OGTT-derived indices and TyG
- Hudak 2021, PMID 34679116 (Abs): 89 persons, two OGTTs; CV OGIS 6.5 ± 5.1 %, revised QUICKI 2.8 ± 2.1 %. Hani 2024, PMID 39726936 (Abs): 257 children. Gordon 2011, PMID 21945562 (Abs): OGIS CV 7.8 %, Stumvoll ISI 14.4 %. Also PMIDs 18713820, 28482366, 20879960, 36788467, 33972923, 35894085 (Abs).
- **Not found:** any TyG test-retest or biological-variation study (10 strings, see log). Jeong 2021 (PMID 34724122) is a validity study, not repeatability.

### Request 4 — cross-reactivity
- Li 2025, PMID 39030378 (Atellica 92–121 % for five analogues, Abs); Heurtault 2014, PMID 24150210 (16 assays, 0–264 %, Abs); Violin 2023, PMID 37598742 (Abs); Dayaldasani 2015, PMID 25172526 (Abs); Oh 2018, PMID 30027696 (Lumipulse, Abs, proinsulin value truncated); older single-platform studies (PMIDs 16690737, 20392753, 21239867; Titles for 14709671, 21410416, 39086570).
- **Not retrieved:** proinsulin cross-reactivity percentages on named current platforms (only Lumipulse tested it, and the value was not in the abstract text I could read).

### Request 5 — reference procedure and JCTLM
- Rohlfing 2025 (FT, PMC12452087): "There is still no JCTLM-listed reference method for insulin, nor are there any JCTLM-listed certified primary or secondary reference materials available."
- Moradian 2024, PMID 38549041 (FT, PMC12052497): "Accuracy was not assessed for insulin measurements, because there is no reference measurement procedure available"; the same paper states the University of Missouri C-peptide reference method is JCTLM-listed.
- Rohlfing C-peptide 2025 (FT): the Missouri LC-MS C-peptide reference measurement procedure "is now listed with the JCTLM".
- Candidate insulin RMP and CRM papers: Liu 2025, PMID 40353876 (Abs, "candidate reference measurement procedure"); Ma 2024, PMID 38556594; Wang 2022, PMID 35201368; Luo 2025, PMID 40270241 (Abs).
- Sacks/NACB 2011, PMID 21617108 (Diabetes Care version; FT via PMC3114322): graded GPP recommendation that a standardized insulin assay should be developed; text says the ADA workgroup called for traceability to an ID-LC-MS/MS reference.
- Not done: direct query of the JCTLM database (script-driven site, not queryable here); a web search found no insulin RMP entry but did not settle it.
- **Resolution of the conflict in my original report:** Staten 2010 says ID-MS is "a reference measurement procedure for insulin" in the ADA workgroup's usage; three later sources (2024, 2025, 2025) say no insulin RMP is JCTLM-listed or available. The sources describe different things (a workgroup's measurement procedure vs a listed, internationally recognised RMP). I relayed both and did not rule between them.

### Request 6 — guidelines and pre-analytics
- Sacks 2011 NACB/ADA (PMID 21617108, FT; companion PMID 21617152): states insulin assays are poorly harmonized; routine insulin measurements for PCOS are not recommended (cited to ACOG); C-peptide interlab CVs > 10 % within-run and 18 % between-run (15 labs, 9 methods).
- Sacks 2023 update (PMIDs 37471273, 37473453 and executive summaries 37471272, 37562009): **abstract only**; full text behind a browser check that I did not bypass.
- Hemolysis: PMIDs 26121452, 20080083, 27231209, 27817149, 22372347, 41371327, 42351586, 36635939, 24486652 (Abs/Title). Tubes and time: Vogeser 2005 PMID 15885238, Déchelotte 2016 PMID 27693646, Mubiru 2025 PMID 40587435, Nkuna 2023 PMID 37409980, Oddoze 2012 PMID 22285385. Reference intervals: PMIDs 27989491, 41857869, 39529982, 32588601, 25740418, 24530467, 17332147.
- No guideline specific to insulin pre-analytics found.

### What changed in the evidence set
- About 60 new identifiers, mostly in Group 5 (assay comparability, reference procedure, BV, cross-reactivity, pre-analytics) where the original had about 25.
- The original's Group 5 "variability" gap (biological variation, repeatability) is now partly filled: EuBIVAS letter identified (values not read), OGTT-index CVs from three papers, no TyG repeatability found.
- The original statement that an ID-MS reference procedure exists is now qualified (see Request 5).
- New guideline-level source for insulin standardization: Sacks 2011/2023.


**Late note (message received after the report was written):** the chemist confirmed by reading the full text that Moradian 2024 says "Accuracy was not assessed for insulin measurements, because there is no reference measurement procedure available" and that Staten 2010 (PMC2797975) carries the quote I sent. The chemist reads the two as consistent: an ID-MS procedure used by the ADA workgroup, but no internationally recognised or JCTLM-listed insulin RMP with a network. JCTLM database status remains unverified by both of us. This was not counted as an outgoing message of mine.

## (iii) Negative claims from the original report re-tested with broader strings

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

## (iv) Did the exchange help?

**Estimate: modestly helped, but I cannot separate it from the effect of the skeptic feedback.**
- *Helped:* The six numbered requests were specific and told me which gaps mattered (RCV and individuality for insulin itself, post-2019 comparability, pre-analytics), so I searched topics my original report had skipped (hemolysis, tube type, cross-reactivity, reference intervals). The first message forced me to re-read Staten 2010 and then look at what later papers say about an insulin reference procedure, which turned a vague conflict into three FT quotes that point the same way. The chemist's list of items already held saved me from resending known papers.
- *Did not depend on the exchange:* Most of the improvement came from using short, broad strings and reading at least the top 25 records of large sets, which the skeptic review had already asked for. That would have worked without the chemist.
- *Limits and risks:* The chemist did not answer my question about the 2024 paper's wording, so I read it myself; the exchange cap meant I could not send the DOI correction for PMID 21617108; the main gaps persisted (EuBIVAS numbers, proinsulin percentages on current platforms, 2023 NACB full text, JCTLM database check). Nothing here showed that a peer exchange beats a searcher who simply gets a list of gaps.
- No harm found beyond the uncorrected DOI error in message 3, which the chemist's own PubMed check should catch.

## Appendix — Round 2 search log

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
