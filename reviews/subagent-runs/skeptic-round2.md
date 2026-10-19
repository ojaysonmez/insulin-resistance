# Skeptic review, round 2 corrections (Measurement section of merged-conclusion.md)

Scope: the three bullets in "Measurement (clinical chemist, checked by three skeptics)": (1) inter-laboratory/inter-assay imprecision incl. the Rosli correction, (2) reference change value, (3) reference measurement procedure. I did not read other skeptic reviews. merged-conclusion.md was not edited.

Verification tools: Scholar Sidekick verifyCitation and checkRetraction both returned "You are not subscribed to this API", so I used PubMed metadata (PMIDs, titles, authors, DOIs) plus the Crossref API directly (works/{DOI}; no `update-to` or `updated-by` notices for any of the 11 DOIs below, titles match). JCTLM database could not be queried (the bipm.org URL I tried returned 404), so JCTLM statements rest on author statements only.

## Sources and read level

| Source | PMID | DOI | Read level |
|---|---|---|---|
| Rosli 2022 | 35622611 | 10.1002/jcla.24521 | full text (PMC9279959), incl. Table 1; figures not viewable |
| Rohlfing 2025 | 40802520 | 10.1515/cclm-2025-0552 | full text (PMC12452087) |
| Staten 2010 | 20040676 | 10.2337/dc09-1206 | full text (PMC2797975; a 2-page commentary, no abstract) |
| Moradian 2024 LC-MS/MS | 38549041 | 10.1093/clinchem/hvae034 | full text (PMC12052497) |
| Zhou 2022 | 35177563 | 10.3343/alm.2022.42.4.428 | full text (PMC8859554); per-pool values for the middle pools came from a WebFetch summary of Tables 1-3 (cross-checked: the per-pool values reproduce the published means 21.8 and 22.4) |
| Marcovina 2007 | 17272483 | 10.1373/clinchem.2006.082214 | abstract only |
| Tohidi 2017 | 28150502 | 10.1080/00365513.2016.1278260 | abstract only |
| Miller 2009 | 19325009 | 10.1373/clinchem.2008.118380 | abstract only |
| Liu 2025 (candidate RMP) | 40353876 | 10.1007/s00216-025-05900-5 | abstract only |
| Carobene 2024 (EuBIVAS) | 38987271 | 10.1515/cclm-2024-0672 | abstract only |
| Jayagopal 2002 | 12401750 | 10.2337/diacare.25.11.2022 | abstract only (full text blocked, HTTP 403) |

All 11 identifiers resolve to the papers named; no fabricated or mis-numbered citation. Note: merged-conclusion.md gives no PMID or DOI for Jayagopal 2002 (see problem 5).

## Ranked problems

### 1. HIGH. The Rosli "correction" introduces its own errors
Claim: "seven kits measuring one pooled serum read from 18 to 150 pmol/L, about 5.8-fold apart (one pooled serum, four manual research ELISAs, so not representative of hospital analysers)".

What the primary text says. Verified: Rosli's text reads "The results were spread from 18 pmol/L to 150 pmol/L, and the RSD in each kit showed ranges from 1.7% to 23.2%". So the within-kit reading of 1.7-23.2% is correct, and the correction of the abstract's ambiguous phrasing is justified. The problems are in the rest of the sentence:
- Arithmetic does not match: 150/18 = 8.3-fold, not 5.8-fold. The 5.8 appears to be the ratio of Table 1 inter-run means in uIU/mL (kit E 28.38 vs kit D 4.88 = 5.82), which is a different quantity from the 18-150 pmol/L text range. Table 1 itself, converted to pmol/L, gives kit means of about 29 to 197 (manufacturer factors) or 29 to 170 (factor 6.0), which also does not equal 18-150. The paper is internally loose, and the merged text pairs two numbers that do not describe the same thing. The text range includes within-kit variation and two lots of kit A ("Including the within kit variations... two different lots showed different ranges").
- "four manual research ELISAs" is wrong as a description of the seven kits. Methods: four manual ELISAs (Mercodia, Alpco, Epitope Diagnostics, Abcam) plus three automated CLIA kits on Siemens Centaur XP, Beckman Unicel Dxl800 and Roche Cobas e801, i.e. hospital analyser platforms. Using Table 1 inter-run means with the manufacturers' unit factors, the three CLIA systems span about 131 to 197 pmol/L (about 1.5-fold). The big spread is driven by kits C and D, both ELISAs traceable to WHO IS 83/500 rather than 66/304 (the authors' explanation; they say they could not tell why that standard reads lower). So "not representative of hospital analysers" is half right (one pooled commercial serum, three runs) but the stated reason is factually wrong, and the paper itself shows that the automated platforms agreed much better.
- Rosli also shows that "all methods trace to WHO 66/304" (line 38 of the section) is not universal: two kits trace to IS 83/500.
Evidence that would fix it: restate as "within-kit RSD 1.7-23.2% (paper's text; Table 1 intra-run RSD 0.1-19.7%, inter-run 0.6-15.2%); between kits, one pooled serum read about 18-150 pmol/L by the paper's text, about 6-fold between kit means in Table 1 (4.88 vs 28.38 uIU/mL); 4 ELISAs + 3 automated CLIA; the three CLIA platforms were within about 1.5-fold; the lowest two kits trace to a different WHO standard".

### 2. HIGH. "roughly 20-25% CV across three differently designed studies" is not supported as written
- Tohidi 2017 (abstract) reports no CV: it reports a 1.8-fold difference between lowest and highest median across 8 assays and correlations 0.844-0.992. Only two of the three studies (Zhou, Marcovina) give a CV.
- Zhou 21.8% and 22.4% are means over five pooled sera (confirmed in the abstract and text) that hide a large concentration gradient. Authors' own range: inter-laboratory 8.4-64.3% and inter-measurement-system 10.7-58.3% for insulin, with the lowest pool (<0.06 nmol/L, i.e. below about 60 pmol/L, the fasting range relevant to HOMA-IR) at 64.3% and 58.3%. From the per-pool values (Table 1/2 via summary), the other four pools average about 11% (inter-lab) and 13% (inter-system); the means reproduce exactly (109.1/5 = 21.8; 111.8/5 = 22.4). The authors speculate the lowest pool may contain exogenous insulin or analogue matrix. After recalibration the lowest pool was still 44.1% (published). The text says "do not cite 25% as one established value" but does not tell the reader that the headline is an average of 8% and 64% values, and it omits that Zhou's insulin recalibration gain was small (22.4 to 17.2%) while the cited C-peptide gain was large (24.5 to 5.7%, correctly given in the next bullet).
- Marcovina 2007: the abstract states 12 methods evaluated but gives the among-assay CV (12-66%, median 24%) and all agreement statistics for 10 assays, so "across 12 methods" is slightly off. Abstract-level only; the CV definition (per sample across assays) was not checked in the full text.
- The "plus up to 2-fold differences between methods" contradicts the 5.8-fold in the same bullet (and Marcovina's 66%).
Evidence that would fix it: "two studies report CV (Zhou mean 21.8%/22.4% across five pools, range 8-64%, worst at lowest concentration; Marcovina median 24%, range 12-66%, 10 assays, 2007); Tohidi reports a 1.8-fold median difference; Rosli 5.8-8-fold between kits".

### 3. MEDIUM. Rohlfing "-298 to +303 pmol/L" and "1 of 12" are stated without context that changes their meaning
Verified against full text: 12 immunoassays, 9 manufacturers, 40 sera collected, differences vs IDMS -298.2 to +302.6 pmol/L; "Only one method (H) demonstrated full agreement". Missing context:
- The samples were non-diabetic, T1D and T2D, fasting and 30/60-min post-meal, range 2.19-1364 pmol/L; the two highest were excluded, so 38 samples; 4 of 12 assays had only 28-37 results. The +303 occurs in the lowest samples (<10 pmol/L, n=3, T1D-type; five methods reading 182-303 pmol/L), and the authors suggest analogue cross-reactivity or autoantibodies; the -298 occurs at high concentrations. These are absolute extremes, not percent bias at fasting HOMA-IR concentrations (the 10-22 pmol/L bin, n=3, read 55-114 pmol/L by the same five methods, which is relevant but tiny n).
- "Full agreement" means the Passing-Bablok 95% CI included slope 1 and intercept 0 with n=38; four more assays had intercept-only agreement. It is a significance criterion, not a magnitude, and is power-limited.
- The comparator is the University of Washington IDMS, which the authors call "not an established reference method". The 12 assays are anonymised and several come from the same manufacturer, so they are not 12 independent platforms.
Fix: add "absolute differences across a 2-1364 pmol/L set, largest at the extremes; agreement judged by Passing-Bablok CI; comparator is not an established reference method; anonymised assays".

### 4. MEDIUM. Reference measurement procedure wording is partly self-contradictory and partly over-inferred
- Staten 2010 (full text) says IDMS is "a reference measurement procedure for insulin" and a "high-level reference measurement procedure". Miller 2009 abstract also says "reference measurement procedures". The 2024 LC-MS/MS paper (full text) says "Accuracy was not assessed for insulin measurements, because there is no reference measurement procedure available". Rohlfing 2025 says the IDMS is "not an established reference method" and "There is still no JCTLM-listed reference method for insulin, nor are there any JCTLM-listed certified primary or secondary reference materials". The section line 43 opens "Not established: 'no reference measurement procedure for insulin exists'" and then cites the 2024 paper, whose literal wording is that none is available. A reader sees a negation and then its own support. Zhou 2022 (full text) independently states "no reference measurement procedure and reference materials are listed in the JCTLM dataset" for insulin and that C-peptide reference procedures and primary materials are listed; that is a second, older source for the JCTLM claim and should be added.
- Staten 2010 is a two-page commentary by workgroup authors; it does not itself use the word "comparator" or describe an experiment. The comparator use is in Miller 2009 (abstract: 39 sera, 10 methods vs IDMS). Attributing "used as ADA workgroup comparator" to Staten should be to Miller.
- "no commercial assay is standardised to one": authors say "no assay has been successfully standardized" (Rohlfing intro) and "no CRM with complete metrological traceability to SI is commercially available" (Rosli), and all assays claim only WHO 66/304 traceability. Nobody surveyed manufacturers' traceability claims, so this is an inference from author statements, not a checked fact.
- Liu 2025 (abstract) is a candidate procedure from an IVD manufacturer's reference laboratory (Autobio); worth flagging as non-independent.
- Line 95 of the section on the niche trial says an isotope-dilution-traceable assay "cannot currently be met". Miller 2009 and Zhou show serum-panel recalibration to IDMS is feasible in principle; what is missing is a JCTLM-listed RMP and manufacturer adoption. Soften to "no assay is currently calibrated to a JCTLM-listed reference system".
- Counterweight omitted: in the 2024 paper, three laboratories using the same LC-MS/MS protocol and shared calibrators had median insulin imprecision 22.2% (IQR 20.9%) for single measurements, 15.3% averaged (C-peptide 13.4% / 10.8%). So MS standardisation is not shown to remove variability; this supports line 43's "LC-MS/MS is no better than immunoassay is not established" in a different direction and should be mentioned or at least not contradicted.
- The JCTLM database itself is still unqueried (the section says so; add it to Open gaps).

### 5. MEDIUM-LOW. Reference change value bullet
Recomputed (log-normal, sigma = sqrt(ln(1+CV^2)), RCV = exp(+-Z*sqrt(2)*sigma_total) - 1):
- CVI 26.7%, CVa 0, Z 1.96: +107.0% / -51.7% (matches the skeptic figure +107/-52).
- CVa 5%, Z 1.96: +109.7% / -52.3% (the bullet says +109%; rounding gives +110%, trivial).
- CVa 5%, Z 1.645 one-sided: +86.2% / -46.3% (matches +86/-46; the Z is not stated in the text).
- QUICKI CVI 4.1%: CVa 0, Z 1.96 gives +12.0% / -10.7%, matching +12/-11. Applying a 5% analytical CV directly to QUICKI would give +19.6/-16.4, so the bullet's wording implies the wrong thing if read as "CVa 5% for QUICKI too". The +12/-11 only holds if the insulin CVa is propagated through the log transform (QUICKI CVa about 0.7%, giving about +12/-11) or CVa is ignored. State which.
- Jayagopal 2002 abstract: "a subsequent sample must increase by >90% or decrease by >47%". Verified. But: n=12 postmenopausal women with diet-controlled T2D (plus 11 controls), 10 samples at 4-day intervals, 2002 assay. The same abstract reports HOMA-IR log-Gaussian in T2D and Gaussian in controls, and mean intra-individual variation 1.05 (T2D) vs 0.15 (controls), "after accounting for analytical variation" (units not given in the abstract). So the non-diabetic controls were far less variable than EuBIVAS's 26.7%. "close to the empirical T2D figure" reads as validation of the EuBIVAS-based derivation; it is a coincidence of two different populations, and the one study that measured both groups points to a lower non-diabetic variation. It also does not support the log-normal assumption for non-diabetic people. Recommend: "similar in size to, but from a different population (T2D) than, the EuBIVAS-derived figure; do not read as confirmation", and add PMID 12401750, DOI 10.2337/diacare.25.11.2022.
- Assumptions that are honest: the "derived, not published" and "assumed analytical CV is the chemist's own" statements. Not stated: stationarity and homogeneity of CVI across individuals (EuBIVAS gives a group mean), same laboratory and assay at both time points (RCV does not cover a lab or assay switch), log-normality (not tested in EuBIVAS abstract). The 5% CVa is unsourced but consistent with Zhou intra-measurement-system 4.8%; sensitivity is negligible (CVa 0 vs 5% moves RCV by about 3 points).
- Spot check of line 42 (not in scope): sigma 0.264, true value 1.2x cutoff reads below 24.5%, 1.5x 6.2%, 2x 0.4%; matches.

### 6. LOW. Scope of the variability claim
Inter-laboratory disagreement affects transporting cutoffs and pooling studies; it does not affect a patient tracked at one lab with one assay (only within-person and analytical CV do). The bullet blends these. Add one sentence on which clinical use each figure bears on. Also, none of this measures clinical utility; it limits individual-level classification and evidence synthesis. Net line 45 ("cannot reliably classify an individual near a cutoff or detect individual change") is supported for single measurements near cutoffs by EuBIVAS plus the RCV arithmetic, but "detect individual change" is supported only by RCV (+109/-52), which is large, not "cannot".

## Claims that survived scrutiny
- 1.7-23.2% in Rosli is a within-kit RSD (text: "the RSD in each kit"); the abstract is ambiguous and the correction is right in direction.
- Rosli: seven kits, pooled serum, errors are systematic not random ("not caused by random error but rather by systematic bias"), two WHO IS traceability chains.
- Rohlfing: 12 immunoassays, 9 manufacturers, -298.2 to +302.6 pmol/L, only one full agreement, all claim WHO 66/304 traceability, quote "There is still no JCTLM-listed reference method for insulin" is verbatim.
- 2024 paper: "no reference measurement procedure available" verbatim; C-peptide University of Missouri method described as JCTLM-listed; Zhou independently says insulin has no JCTLM-listed procedure or material and C-peptide does.
- Zhou: 21.8% inter-lab, 22.4% inter-system for insulin; 24.5% to 5.7% for C-peptide after recalibration; 94 laboratories (91 complete).
- Tohidi: 1.8-fold difference across 8 assays.
- Miller 2009: IDMS comparator in ADA workgroup (abstract).
- RCV figures reproduce (above); Jayagopal >90% / >47% verified at abstract level.
- No retractions, corrections or expressions of concern in Crossref for any cited DOI.

## Verdict
The three edits are justified in direction (more accurate than the earlier wording, all sources real), but not as currently worded. Needed before relying on them: fix the Rosli sentence (kit composition, 5.8 vs 18-150), drop "three studies" for the 20-25% CV and report Zhou's 8-64% range, add context to the Rohlfing range, resolve the RMP wording against Staten/Miller, and de-emphasise "close to" for the Jayagopal comparison with its PMID/DOI added. None of these changes the section's net conclusion that single-sample insulin and HOMA-IR are unreliable near a cutoff; they affect precision of the supporting figures. Confidence that the edits, once reworded as above, are accurate: about 80%; confidence that they are accurate as currently written: about 55%.
