# Clinical chemist, Round 2 (peer exchange with the evidence searcher)

Date: 2026-10-19. Original report not edited: `ir-team/new-roles/ir-clinical-chemist.md`. Files read this round: that report, `ir-team/ir-evidence-searcher.md` (first 292 of 533 lines only). I did not read the skeptic reviews. The searcher's round-2 log was not read; I rely on its message.

Labels used below: **V** = verified by me (PubMed record; read level stated). **R** = relayed by the searcher, not verified by me. Read level: FT = full text, Abs = abstract only.

## 1. Exchange log

| # | Direction | Content (short) |
|---|---|---|
| 1 | Me to searcher | 6 numbered retrieval requests (insulin/C-peptide biological variation; post-2019 multi-vendor comparability; OGTT-index and TyG reproducibility; proinsulin/analogue cross-reactivity; wording of an insulin reference measurement procedure (RMP) statement; guideline/pre-analytics), each with purpose and what I already held. |
| 2 | Searcher to me | Written before it had read #1. Gave three RMP-related quotes (Staten 2010 FT, Miller 2009 Abs, Rodriguez-Cabaleiro 2007 Abs), said it found no official JCTLM listing, and asked for the exact wording and read level of the 2024 LC-MS/MS paper. |
| 3 | Me to searcher | The 2024 wording and read level (FT): "Accuracy was not assessed for insulin measurements, because there is no reference measurement procedure available." Also my reading of the conflict. (My second and last outgoing message.) |
| 4 | Searcher to me | Full reply to the six requests, with PMIDs, DOIs, read levels, and search strings/counts. |

## 2. What changed from the original report

**2.1 Gaps closed (all V unless stated)**
- **EuBIVAS insulin letter**: identified and verified as Carobene et al., Clin Chem Lab Med 2021;60(4):518-522 (PMID 33554550, doi:10.1515/cclm-2020-1490). **Not closed in substance**: it is a Letter with no abstract in PubMed or Crossref, the peer could not read it either, and I could not obtain its CVI/CVG/RCV values. I therefore still state no insulin-specific CVI from EuBIVAS. The meta-analysis by González-Lao 2019 (PMID 30389455, Abs via Consensus/PubMed search) exists and grades 47 BV publications (1 A, 3 B, 39 C, 4 D), but its pooled numbers are not in the abstract.
- **Current multi-vendor insulin comparison**:
  - Rohlfing 2025 (PMID 40802520, doi:10.1515/cclm-2025-0552) **FT read by me**: 40 sera (38 after exclusions), 9 manufacturers, 12 immunoassays, all claiming traceability to WHO 66/304, compared with a University of Washington IDMS method. Within-assay ICC >0.99. Differences vs IDMS −298.2 to +302.6 pmol/L. Most assays overestimated below 100 pmol/L and underestimated above 300 pmol/L; five methods read 182 to 303 pmol/L in samples with <10 pmol/L by IDMS. Only 1 of 12 methods agreed fully with IDMS; 4 more agreed on intercept only. This is the most current multi-vendor dataset I have (published 2025, runs on current platforms, though anonymised by manufacturer).
  - Rosli 2022 (PMID 35622611) **FT read by me**; see correction 2.3.
  - Tohidi 2017 (PMID 28150502) Abs: 8 assays, 165 sera; lowest vs highest median differ by a factor of 1.8; significant bias in 6 of 8.
  - Manley 2007 (PMID 17363420) Abs: 11 assays, 150 sera, up to a factor of 2.
  - Larsen 2017 (PMID 27989491) Abs: Roche Cobas e411 insulin read 15–20% high against a reference laboratory, attributed to the 6.945 pmol/L-per-uIU/mL conversion factor versus 6.00.
- **C-peptide comparability**: Hörber 2023 (PMID 36630986) Abs: five immunoassays, all traceable to NIBSC 84/510, mean bias up to 36.6% (Roche vs Siemens ADVIA Centaur XPT) and 2.3–4.2% among the other three. Rohlfing 2025 C-peptide (PMID 39803820) Abs: 10 manufacturers, disagreement despite a common WHO calibrator, reduced by recalibration with matrix-appropriate serum.
- **Reproducibility of OGTT-derived indices**:
  - Hani 2024 (PMID 39726936, doi:10.1155/2024/2136173) **FT read by me**: 257 children aged 8–17, two OGTTs at a median of 14 days; OGTT-derived sensitivity (WBISI) more reproducible than fasting indices (HOMA-IR, QUICKI, FGIR, 1/fasting insulin); insulin secretion indices poorly reproducible; no differences by weight, sex, race or pubertal status. The text prints no ICC values in the sections I could read. Insulin was an in-house RIA (inter-assay CV 3.8%, antibody 68.5% cross-reactive with proinsulin).
  - Hudak 2021 (PMID 34679116) Abs: 89 adults without diabetes, two OGTTs a median of 86 days apart: revised QUICKI CV 2.8 ± 2.1%; OGIS 6.5 ± 5.1%; C-peptide HOMA2-beta 10.8 ± 8%.
  - Gordon 2011 (PMID 21945562) Abs: individual CV 7.8% for OGIS and 14.4% for Stumvoll-ISI over four consecutive days.
  - Mooy 1996 Hoorn Study (PMID 8721775) Abs: 524 people, two OGTTs; for normal glucose tolerance, 95% of test-retest differences in fasting insulin are below 61% of the median (125% for 2-h insulin); variation was predominantly biological, analytical contribution minor.
  - TyG: still no repeatability study found by me or the peer.
- **Cross-reactivity on more recent platforms** (all Abs, V): Heurtault 2014 (PMID 24150210; 16 assays; analogue cross-reactivity 0% to 264%; none free of it); Violin 2023 (PMID 37598742; three behaviour classes; Cobas detects human insulin only, Architect and Access detect all types); Li 2025 (PMID 39030378; Siemens Atellica detects five analogues at 92–121%, LC-MS/MS detected glargine but <10% of the others). Proinsulin cross-reactivity percentages on named current platforms: **still not found** (the peer also failed).
- **Pre-analytics** (Abs, V): Nkuna 2023 (PMID 37409980): serum insulin −80% and plasma −23% after 72 h unspun at room temperature, insulin more stable in EDTA plasma than serum, C-peptide the reverse for separated storage; Garinet 2014 (PMID 24486652): hemolysate (not free Hb) produces a negative bias on an Architect insulin assay, growing with time and reduced at 4 °C; Déchelotte 2016 (PMID 27693646): K2-EDTA better than K3-EDTA for insulin, both analytes stable 24 h at room temperature on K2-EDTA.

**2.2 The "no reference measurement procedure" claim: resolved with a qualification, and my original wording was too absolute.**
- Staten 2010 (PMID 20040676, **FT read by me**, PMC2797975) calls isotope-dilution mass spectrometry "a reference measurement procedure for insulin" and calls for traceability to "the isotope dilution mass spectrometry high-level reference measurement procedure calibrated with pure recombinant insulin". Miller 2009 (PMID 19325009, Abs) benchmarks 10 methods against an ID-LC-MS/MS procedure calibrated with pure recombinant insulin.
- Against that: Rohlfing 2025 (FT, V) states "There is still no JCTLM-listed reference method for insulin, nor are there any JCTLM-listed certified primary or secondary reference materials", and in its limitations that the LC-MS method used is "not an established reference method" and that a validated method with a full traceability chain is "still under development". The 2024 TaMADOR paper (FT, V): "there is no reference measurement procedure available." Liu 2025 (PMID 40353876, Abs, V) presents a *candidate* RMP (ID-LC-MS/MS, imprecision <2.77%), saying RMPs "with higher metrological order are required".
- **Resolution**: a higher-order ID-MS procedure has been described and used as the ADA workgroup comparator since 2009–2010, but there is no JCTLM-listed or otherwise internationally established insulin RMP, no listed certified reference material, and no commercial assay is standardised to one. C-peptide differs: its University of Missouri RMP is JCTLM-listed (stated in the 2024 full text I read; also in R item 5). Not resolved: I could not query the JCTLM database itself and neither could the peer, so "not listed" rests on three 2024–2025 papers, not on the registry.
- Corrected wording for use: "no internationally established (JCTLM-listed) reference measurement procedure or certified matrix reference material for insulin exists; an ID-LC-MS/MS comparator has been used in research."

**2.3 Correction from reading Rosli 2022 in full, which the peer's relay would have propagated.** The abstract and the peer's summary give "relative standard deviation ranges between 1.7% and 23.2%" as the discrepancy between kits. In the full text this is the RSD within each kit (replicate spread). The between-kit discrepancy is the result: seven kits measuring one pooled serum read from 18 to 150 pmol/L, and the inter-run mean values in Table 1 range from 4.88 to 28.38 uIU/mL as printed (about 5.8-fold). Two kits (C, D) were traceable to WHO IS 83/500 rather than 66/304 and read lower; two lots of one kit differed; manufacturers' unit conversion factors were 6.0, 6.945 and 7.0. Caveats: one pooled serum, four manual research ELISAs, which are not representative of hospital analysers. I would not quote 1.7–23.2% as inter-assay disagreement.

**2.4 The "~25% inter-laboratory CV" framing.** The three sources are separate datasets but not independent in cause: all reflect the same absence of a common, commutable calibration. Revised statement, with design, so readers can weigh each:
- Marcovina 2007 (PMID 17272483, Abs): 12 commercial methods, among-assay CV 12–66%, median 24%; old-generation assays; a common reference preparation did not lower it.
- Isokuortti 2017 (PMID 28660493, Abs): 10 individuals, 7 labs, inter-laboratory CV of HOMA-IR 25%, driven by insulin (25%) not glucose (5%).
- Zhou 2022 (PMID 35177563, Abs): 94 Chinese labs, 5 pooled sera, inter-laboratory CV 21.8% and inter-measurement-system 22.4% for insulin; after recalibration with two serum pools 17.2%. This paper was already in my original report (table and reference 5), so I could not reproduce the skeptic's statement that it was missing.
- Method-comparison designs (not CVs): Tohidi 2017 factor 1.8; Manley 2007 factor 2; Rohlfing 2025 differences of ±300 pmol/L around IDMS with 1 of 12 methods in full agreement.
- Use "roughly 20–25% CV between laboratories/systems and up to 2-fold differences between methods, across studies of different designs, with older and a few current platforms; no current EQA survey retrieved." Do not cite 25% as a single established value.

**2.5 Reference change value: asymmetric correction.** My original gave a symmetric ~75% RCV and a rough "+100%/−50%" for the log-normal form. Proper log-normal calculation (my calculation; Z = 1.96; EuBIVAS CVI 26.7%; assumed CVa 5% for the analytical part, an assumption): total CV 27.2%, sigma(ln) = 0.267, RCV(ln) = 1.414 × 1.96 × 0.267 = 0.74, so the 95% two-sided RCV is **+109% / −52%**. One-sided (Z = 1.65, for a hypothesis of a directional change) it is +86% / −46%. For QUICKI (CVI 4.1%, CVa assumed 1%) it is about +12% / −11%. For comparison, Jayagopal 2002 (Abs) empirical T2D: +90% / −47%. Mooy 1996 (Abs): 95% of normal-glucose-tolerance fasting-insulin test-retest differences below 61% of the median, which is consistent.
- Cutoff-crossing illustration (my calculation, log-normal, sigma 0.267): a person whose true HOMA-IR is 25% above a cutoff reads below it on a single repeat about 20% of the time. If the repeat is at a laboratory with an independent 25% method bias (sigma 0.247), the combined sigma is 0.364 and this rises to about 27%. This treats a method difference as random, which it is not for a patient measured consistently at one laboratory; read it as an upper bound for switching laboratories.

**2.6 Other original statements to treat differently**
- The original stated Rosli, Carobene 2021 and the paediatric paper as gaps; closed as above except the EuBIVAS insulin values.
- The original said cross-reactivity data were 2007-only. Now there are 2014, 2023 and 2024 abstracts, but proinsulin percentages on current platforms remain missing.
- Original claim "no pre-analytical data": superseded by the three abstracts above.

## 3. What the peer gave versus what I verified or found

| Item | Source of find | Status |
|---|---|---|
| PMID 40802520 Rohlfing 2025 insulin | Already in my own first-round PubMed result list; I failed to read it (see §5). Peer pointed to it again. | **V, FT** |
| PMID 35622611 Rosli | Skeptic named it; peer re-supplied. | **V, FT**; error in abstract framing found by me |
| PMID 39726936 Hani | Skeptic named it; peer re-supplied. | **V, FT** |
| PMID 33554550 Carobene 2021 | Skeptic named it; peer re-supplied. | V, record only (no abstract, no values) |
| PMID 20040676 Staten | Peer quoted; I fetched the PMC text. | **V, FT**; quote matches |
| 2024 TaMADOR (PMID 38549041) wording | I read it in round 1; peer asked me. | **V, FT** |
| PMIDs 28150502, 24150210, 37598742, 39030378, 34679116, 21945562, 8721775, 27693646, 27989491, 40353876, 39803820, 36630986, 37409980, 24486652, 21617108 | Peer relayed (some I had also found in round 1 or the searcher report: 36630986, 37409980, 24486652) | **V, Abs** (identifier, title, abstract content checked). For 21617108 (Sacks 2011) only the abstract was checked. |
| Quoted passages in Sacks 2011 ("BECAUSE CURRENT MEASURES OF INSULIN ARE POORLY HARMONIZED…", ACOG/PCOS sentence, "do not add significantly…") | Peer, full text | **R, unverified.** I did not open PMC3114322. |
| Sacks 2023 (PMIDs 37471273, 37473453, 37471272, 37562009) | Peer, identifiers only | **R** |
| PMIDs 30389455 (González-Lao), 22285385 (Oddoze), 12564620 (Schousboe), 36750430 (Deng 2023 Ann Clin Biochem), 27665422 (Loh), 25172526 (Dayaldasani), 30027696 (Oh), 20080083 (Cook), 27231209 and 27817149 (Wu), 22372347 (Bellomo), 26121452 (Zornitzki), 36635939 (Karin), 15885238 (Vogeser), 40587435 (Mubiru), 40781799 (Schleicher), 38556594, 35201368, 40270241, 28860026, 18713820, 28482366, 20879960, 36788467, 33972923, 35894085, plus reference-interval papers 41857869, 39529982, 32588601, 25740418 | Peer | **R, unverified.** Not used for any number or conclusion in this report; leads only. (González-Lao 2019 was seen in my own Consensus/PubMed search as a record.) |
| Statement that no JCTLM-listed insulin RMP exists | Peer, from Rohlfing 2025 FT | **V** (I read the same sentence) |
| Peer claim that C-peptide RMP "is now listed with the JCTLM" (Rohlfing C-peptide FT) | Peer | R for that paper; corroborated independently by the 2024 TaMADOR full text I read |
| Not retrieved by the peer | EuBIVAS insulin values; proinsulin % on named platforms; 2023 NACB full text; EQA/CAP insulin data; direct JCTLM check | Open for both of us |

## 4. Anything accepted that I could not verify

No relayed claim was accepted into a conclusion without a record check. Five points still depend on trust in a source I could not independently confirm:
1. "No JCTLM-listed insulin RMP": confirmed in two full texts I read, but the JCTLM database itself was not queried by anyone; this is secondary evidence.
2. The Sacks 2011 recommendation wording is relayed only; I would not quote it until the PMC text is read.
3. The peer's account of search counts and strings (e.g. 5915 results for "insulin biological variation") is unaudited; I use them only as a statement of effort.
4. Hani 2024 ICC values are absent from the text I could read, so I report only the direction of its findings.
5. The CVa = 5% used in my RCV is my assumption, not a published EuBIVAS analytical CV.

## 5. Did the exchange help? My estimate: it helped modestly; it did not harm; it was not the main driver

**Evidence for "helped"**: the peer supplied breadth I would not have systematically gathered (analogue cross-reactivity, hemolysis and stability, Mooy, Hudak, Gordon, Larsen's conversion-factor finding, the 2025 candidate RMP) and corroborated the RMP wording from a second full-text source. Having a second reader saved time on the reference-method conflict.

**Evidence for "not the main driver"**: the decisive improvements came from verification, not retrieval.
- The skeptics' named PMIDs (33554550, 35622611, 39726936) were findable by me with short queries; my own round-1 gaps were process failures. In round 1 my long PubMed queries returned zero and I did not iterate enough, and the Rohlfing 2025 PMID (40802520) was in a result list in round 1 and I requested its metadata but, because the output was dumped to file, I printed only the first 22 records and never read it. The peer did not remove that failure; I corrected it by reading the full text.
- The most useful correction (Rosli's 1.7–23.2% is within-kit RSD, not between-kit disagreement) came from my reading the full text, not from the exchange. The peer's relay repeated the abstract's framing. A pure relay would have propagated that error.
- The one gap that matters most for biological variation (EuBIVAS insulin values) was not closed by either of us.

**Costs and risks**: two messages and a round-trip delay (the searcher was busy for several cycles; its first message was written before it read mine, so the exchange crossed); the relayed list is long (about 60 identifiers) and 90% is unverified at my read level, which invites over-citation. The protocol did contain this by requiring V/R labels.

**Net**: helped (coverage, a second source on the RMP question), no harm, small effect relative to independent verification. A fair comparison with the isolated run would credit the gaps closed to a combination of the skeptic's pointers and my own full-text reading, with the peer mostly accelerating.

## 6. Remaining gaps (unchanged or narrowed)

1. Insulin and C-peptide CVI/CVG and RCV from EuBIVAS (Carobene 2021 letter) and the González-Lao pooled estimates. Needs the full text of those two sources.
2. Proinsulin cross-reactivity percentages on current named platforms.
3. EQA/CAP survey data for insulin and C-peptide after 2019.
4. TyG repeatability.
5. Direct check of the JCTLM database.
6. The full text of Sacks 2011/2023 for guideline statements on C-peptide and insulin measurement.
7. An empirical cutoff-crossing rate on repeat testing (my figures are modelled).

## 7. Short summary

- The Round 1 conclusions stand with these amendments: (a) there is no internationally established (JCTLM-listed) insulin reference measurement procedure, while an ID-LC-MS/MS comparator exists in research (my "no RMP" wording was too absolute); (b) current-platform data (Rohlfing 2025, FT) confirm large inter-assay disagreement (±300 pmol/L around IDMS, 1 of 12 assays in full agreement); (c) the HOMA-IR reference change value is asymmetric, about +109%/−52% (my calculation), roughly consistent with the empirical T2D figures (+90%/−47%).
- The "25%" figure should be presented as about 20–25% inter-laboratory/system CV across three differently designed studies, plus up to 2-fold method differences, not as one value.
- Rosli 2022's 1.7–23.2% is within-kit RSD; between-kit spread there was about 6-fold on one pooled serum.
- Strongest new sources: Rohlfing 2025 (FT), Staten 2010 (FT), Hani 2024 (FT). Weakest: the long list of relayed, unverified abstracts.
- Still open: EuBIVAS insulin values, proinsulin cross-reactivity on current platforms, EQA data, TyG repeatability.
- The exchange helped modestly; the verification step (reading full texts) did more.
