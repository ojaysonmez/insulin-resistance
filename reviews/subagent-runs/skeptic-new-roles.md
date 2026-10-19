# Skeptic review of Set B: ir-clinical-chemist and ir-evidence-searcher

Reviewer: ir-skeptic (independent run). Date: 2026-10-18. Coverage and reimbursement out of scope.
I read only the role file and the two Set B reports. No other file in `ir-team\` was opened.

## 0. How I checked, and tool status

- Scholar Sidekick (`verifyCitation`, `checkRetraction`) failed on every call with "You are not subscribed to this API". The searcher saw the same failure. I did not get a Sidekick verdict on any citation.
- Fallback used:
  - Identity: PubMed MCP `get_article_metadata` for about 28 PMIDs, plus PubMed E-utilities `esummary` for another 33. Title, journal, year and DOI were compared with the reports.
  - Retraction: Crossref API `works/{doi}`, looking at the `updated-by` field, for 22 load-bearing DOIs. None has a retraction, correction or expression-of-concern notice. This is a weaker check than Sidekick because it only reflects what Crossref holds.
- Read levels. My abstract checks ran on the PubMed records. Full text was read only where noted:
  - Europe PMC XML for the LAMP post hoc paper (PMC13281981), the 2023 PCOS guideline (PMC10477934) and the EASL-EASD-EASO MASLD guideline (PMC11299976).
  - NCBI PMC XML for IRIS (PMC4887756).
  - ClinicalTrials.gov API records for NCT07710274, NCT06856291 and NCT07618663.
- Not verifiable by me: ADA 2026 S3 text (PMC full text unavailable to my tools), AACE 2022 text, ESC and ACC/AHA windows, and the ICTRP records (CTRI, IRCT, ISRCTN, ChiCTR).

Identity result: every PMID and DOI I checked resolves and the title matches the report's description. I found no fabricated or mismatched identifier in either report. Ones I checked:
- Chemist: 40802520, 38987271, 29618016, 10102917, 34380182, 38549041, 37141618, 36750430, 35622611, 12401750, 37465325, 29940866, 40827462, 40353876, 39030378, 37598742, 41371327, 35939943, 40587435.
- Searcher: 34531293, 42145088, 26886418, 29466592, 25944628, 42569452, 37580037, 17272483, 18535197, 20040676, and the other 30 or so in the esummary batch.

Minor caveat on identity: the PubMed record for 40802520 is titled "The current status of serum insulin measurements and the need for standardization" (Rohlfing, Clin Chem Lab Med 2025). The chemist's text calls it "Rohlfing 2025" only, so this is fine.

---

## 1. Ranked problems

### Chemist report

**C1. HIGH. The "70-80 %" change threshold and the RCVs are computed on a symmetric scale, and the report's own T2DM source contradicts its headline.**
- Claim: derived RCV is about 72 to 79 % for insulin and HOMA-IR, and "detecting an individual change of less than about 70-80 % ... cannot be supported" (sections 2 and 3).
- Arithmetic: the numbers are correct for the symmetric formula (2.77 x 26 = 72; 2.77 x 26.7 = 74; with CVA 10 % about 79; QUICKI 2.77 x 4.1 = 11). The report does say the log-normal RCV is asymmetric, but it does not apply it.
- Why it fails: for HOMA-IR, which the T2DM source itself says is log-Gaussian, the right threshold is asymmetric. My calculation from the same CVI:

| CVI | Rise needed | Fall needed |
|---|---|---|
| 26.7 % | about +107 % | about -52 % |
| 28.5 % (CVA about 10 %) | about +117 % | about -54 % |

  - A treatment-response claim is usually a fall, so the operative figure is about -52 %, not "70-80 %". The text overstates the barrier to detecting a decrease and understates the barrier to detecting an increase.
  - The Jayagopal figures (+90 % / -47 %) back-calculate to a CV of about 23 %. That is no larger than the EuBIVAS CVI, so in relative terms T2DM is not more variable.
- Second problem: the table row for PMID 12401750 reads "mean intra-individual variation 1.05 in T2DM vs 0.15 in controls (HOMA-IR units)". The abstract gives only "mean 1.05 vs 0.15" with no unit. The "HOMA-IR units" label is the chemist's inference. The row implies T2DM is much more variable, but in relative terms the +90 / -47 % thresholds say it is not.
- Fix: restate RCV as asymmetric (about -52 % / +107 %), label the unit for PMID 12401750 as "not stated in abstract", and drop the implication that T2DM is relatively more variable.

**C2. HIGH. The headline claim "a fixed cutoff cannot be stable" and "cannot classify an individual" is stronger than anything cited.**
- Claim: bottom line 1, section 3 ("a person whose true HOMA-IR is near a cutoff will often cross it").
- Support: the report admits (gap 2) that no study quantifies cutoff crossing. The inference is qualitative, from an abstract-level CVI. The EuBIVAS authors' own conclusion is softer ("limits the value of single measurements").
- What the numbers support (my calculation, CVI 26.7 %, log-normal, single sample, analytic error ignored): a person whose true value equals the cutoff has a 50 % chance of measuring either side. At true/cutoff 1.2, 24 % of measurements fall below the cutoff. At 1.5, 6 %. At 2.0, under 1 %. So classification is unreliable within roughly +/-20 to 30 % of the cutoff and fine far from it.
- The chemist's "cannot" for "binary IR diagnosis" is therefore true only for people near the cutoff. The report does say "flagrant outliers" are fine, but the first-line wording is categorical.
- Fix: soften to "unreliable near the cutoff", and cite the calculation as derived.

**C3. MEDIUM-HIGH. All BV figures are abstract-level, from three small or non-diabetic or old cohorts, applied to "the individual".**
- The report states abstract-only reading, which is honest.
- Widjaja 1999 has 12 healthy 22-year-olds on RIA and is the only source for the C-peptide claim ("same CV as insulin, no advantage"). Note the individuality index in that abstract is CVW/CVG, i.e. total within-subject CV over between-subject CV, not CVI over CVG. The report writes "CVI 26 %; individuality 1.0" as though both used CVI. The distinction is small but the indices are not the same quantity.
- ARIC's 30.4 % is a repeat interval of mean 46 days (range 28 to 102) in adults aged 68 to 88, and it includes analytic variation. The report puts it in the same column as BV without saying it includes CVA.
- The claim that C-peptide has "no advantage" is therefore resting on n = 12 with one of the two assays being RIA. The report calls this "rough comparator only" in section 6 but not in the bottom line.

**C4. MEDIUM. The assay-disagreement headline uses an absolute range dominated by high concentrations.**
- Claim: "differ from an isotope-dilution MS reference by -298 to +303 pmol/L" (bottom line 2, table row 1).
- The abstract (PMID 40802520) gives the range but samples included T1D and T2D patients, and the abstract says assays over-read at low and under-read at high concentrations. The report does not say what the bias is at fasting concentrations in non-diabetic people. A 300 pmol/L difference matters for insulinoma or post-load samples. It tells us little about a fasting HOMA-IR near 2 to 3. n = 40.
- The older, more relevant numbers the searcher found are better for this question: Manley 2008 (HOMA-IR medians 0.8 to 2.0 across 11 assays in normoglycaemia) and Marcovina 2007 (among-assay CV 12 to 66 %, median 24 %; 6 of 10 assays within the 32 % allowable total error). The chemist cites neither. They show the problem is long-standing and also that some assays do agree acceptably.
- The statement "only 1 of 12 in full agreement" is accurate to the abstract.

**C5. MEDIUM. Selective handling of evidence pointing the other way.**
- PMID 37465325 (Leipzig) is used only for age-specific ranges and for "prognostic association does not establish individual diagnostic accuracy". The same abstract says new insulin-based thresholds in children with obesity were "superior to fasting glucose and HbA1c" for detecting later dysglycaemia (HR 1.88 for HOMA-IR, CI 1.1 to 3.21; fasting glucose HR 1.03). It also reports intra-individual stability. That is relevant counter-evidence on utility and is omitted.
- Mubiru 2025: the report quotes 51 % (C-peptide) and 62 % (insulin) from uncentrifuged serum. The abstract gives P = 0.006 for C-peptide but P = 0.083 for insulin, i.e. the insulin drop was not significant. n = 8 after 2 haemolysis exclusions. The report says "magnitudes imprecise" but not that one headline figure was non-significant.

**C6. MEDIUM. "TyG: no true biological variation study found" is under-searched.**
- The report's own log shows TyG variability papers were surfaced only by Consensus and never searched in PubMed. A PubMed string for TyG with biological variation / intra-individual / test-retest / visit-to-visit variability returns 130 records (first page is 2026 titles). Most will be variability-as-exposure studies, not formal BV studies, but "not found" is not supported by a search that was not run.

**C7. LOW-MEDIUM. Cutoff section.**
- Item 3 correctly separates reference limit from diagnostic threshold. Item 5 ("no source re-derives or validates a HOMA-IR cutoff on LC-MS/MS scale") is a null result from a log the chemist did not publish. The report gives no search strings. I cannot judge its adequacy. Flag: the chemist report has no search log at all, unlike the searcher's.
- Pre-analytical section: single-analyser, single-author and n = 8 studies are flagged by the report itself. The statement that serum and EDTA are "consistent with" haemolysis work is a fair qualitative reading.

### Evidence-searcher report

**S1. HIGH. Several "not found" claims rest on strings too narrow to support them; at least two are demonstrably wrong or weak.**
- Statin / PCSK9 / colchicine / canakinumab / icosapent with baseline HOMA-IR or TyG: "0 hits" (S100). The string requires all of: IR term, one of five drugs, "cardiovascular outcomes" exact, "baseline", an IR measure, and subgroup/post hoc. That conjunction was bound to return nothing whatever the literature holds. A simpler string (statin names AND randomized AND IR terms AND subgroup/baseline AND "cardiovascular events") returns 13 records. One is directly relevant: PMID 42291078 (ODYSSEY OUTCOMES, 11,837 patients, Am J Prev Cardiol 2026), which states findings were "similar in patients with greater or lesser degrees of insulin resistance" and that alirocumab benefit did not vary across sdLDL-C/LDL-C. It is not a clean treatment-by-IR interaction test (the IR split is a secondary stratifier of an sdLDL question), but it is a large RCT with an IR-stratified analysis of a PCSK9 inhibitor, which the report says does not exist in the index. Also PMID 27347563 (JUPITER, a lipoprotein IR score and incident diabetes on rosuvastatin vs placebo) is a related but not equivalent hit.
- HOMA-IR incremental value: S031 (`"HOMA-IR" AND ("net reclassification" OR "NRI") AND (cardiovascular OR "coronary heart disease")`) returned 3 hits "none an HOMA-IR incremental-value analysis". The WHI paper that the searcher itself found (PMID 25944628) uses "reclassification" and "discrimination" and is not an NRI paper, so exact "net reclassification" would miss it. A broader string with "reclassification" or "C statistic" or "C-index" returns 246 records, none of which the searcher screened by title (the closest the log gets is M04 with 188 hits, 25 returned, "not individually screened"). So the statement "yield of formal incremental-value analyses was small" for HOMA-IR/fasting insulin reflects the strings, not necessarily the literature.
- S076 (`HOMA-IR AND reference interval AND NHANES ...`) returned 0 even though the Gutenberg reference-interval paper (PMID 34380182, found by the chemist) exists. S082 returned 0 for a known author and topic (the report admits finding the paper by title).
- S006/S007 (14,328 and 14,327 hits) and M02 (3,320 hits, "top 20 not screened") are unscreened. The headline "no randomized strategy trial" relies partly on them.
- S110 to S114 on ICTRP: S113 and S114 returned "no count text". That could mean zero results or a failed page load; the report lists them under negative results as "no records".
- Effect: the Q1 headline ("no randomized strategy trial of IR-guided care") may well be right, but the log supports "none found with the strings used", not "none exists". The report words it as a retrieval result, which is fair; downstream readers should not read it as stronger.

**S2. MEDIUM-HIGH. The LAMP post hoc study is described accurately but incompletely, in ways that matter for weight.**
- Verified from the abstract and full text (PMC13281981): HOMA-IR cutoff 2.5, P for interaction 0.02, ARR 12.3 %, post hoc, small sample, open-label. All accurate.
- Omitted from the full text:
  - Follow-up is 3 months (stroke recurrence in the HOMA-IR >=2.5 control group 18.1 %, a very high figure for minor stroke over 90 days, which hints at selection or ascertainment issues).
  - The parent trial was terminated early "due to loss of funding" before reaching its pre-specified events.
  - Only 510 of 636 patients (80 %) were analysed (complete case, excluding those without glucose/insulin or on recent insulin). Multiple imputation gave interaction P = 0.025.
  - "No formal adjustment for multiple comparisons ... P values should be interpreted with appropriate caution" (paper's own words).
  - The cutoff is borrowed from Asian-population studies; a 2.0 sensitivity analysis kept the primary results but lost the functional-outcome interaction.
- The overall LAMP effect was already positive (stroke recurrence 7.6 % vs 15.3 %, HR 0.48), so the interaction is about a larger benefit in some, not benefit versus none. The report says "none in <2.5" (abstract: "no significant benefit"), which is fair but could be read as absence of effect.
- Verdict: the entry is accurate; a reader would over-weight it without these points.

**S3. MEDIUM. PLIS description is accurate on design but its placement can mislead.**
- Abstract confirms: 1,105 people with prediabetes, stratified into high or low risk by insulin secretion, insulin sensitivity and liver fat thresholds, then randomised within stratum.
- Low-risk people got conventional vs control; high-risk people got conventional vs intensified. The two strata therefore test different contrasts, and there is no arm in which phenotype-discordant care was given. PLIS cannot show that the phenotype "guides" better care than not using it. The phenotype is also multi-component (liver fat from MRI, OGTT-derived indices), not a single IR assay. The report's table gives the design but its heading "stratified by, or analysed by, IR status" and its inclusion in Q1 could suggest it is evidence of IR-guided care.
- Also in the 1c table: NCT07710274 (PRISM-I) is listed as "IR-defined or IR-guided allocation". The registry record shows HOMA-IR >= 2.5 as an eligibility criterion and HOMA-IR as the primary outcome of a precision-lifestyle pilot. That is IR-enriched, with IR as an outcome, not IR-guided allocation. NCT07618663 was read but not reported (glucose-pattern-guided, not IR; correct to leave out).

**S4. MEDIUM. IRIS item: one open question is answerable from text the searcher already had.**
- The report says it did not extract whether HOMA-IR was one of the 13 pre-specified subgroups. The full text of IRIS (checked in PMC4887756) shows the Figure 2 legend defines HOMA-IR among the subgroup variables, "no significant differences in any of the prespecified subgroups", with the multiplicity-adjusted P of 0.94. So there was no gradient of pioglitazone effect by HOMA-IR within an IR-only population. I did not retrieve the HOMA-IR cut-points of that subgroup. This weakens the use of IRIS as proof that the HOMA-IR value, rather than the population, matters.
- The "assay and calibration" discussion quote in the report is accurate (confirmed: insulin "not globally standardized", central labs, replicating needs the IRIS assays or calibration).

**S5. MEDIUM. Selective emphasis in the TyG meta-analysis row.**
- PMID 42569452: the report gives the pooled gain 0.0004 (-0.0092 to 0.0100), certainty very low. Correct. The abstract also reports that excluding one study (Barzegar 2020) raised the pooled gain to 0.0051 (0.0007 to 0.0094). Omitting this sensitivity analysis slightly overstates the null. Either way the gain is below 0.01 C-index.
- Cohort figure 0.731 to 0.732 (P = 0.559) is correct.

**S6. LOW-MEDIUM. Read levels are honestly stated; some table rows claim more than the read level supports.**
- Rows marked ABS carry result details that came from the abstract only (DEXLIFE cluster results, GRADE heterogeneity P-values, FIDELITY P interaction 0.23 / 0.28, DPP k-means). That is acceptable at descriptor level but not for the interpretive phrases ("Metformin benefit greater in subgroup 1") that other roles will quote.
- The Q3 table mixes pre-specified interaction tests (DIETFITS, IRIS), post hoc clusters (DPP, DEXLIFE, ADOPT), and a surrogate that is not an insulin measure (eGDR in FIDELITY and FINEARTS-HF; eGDR uses waist, HbA1c and hypertension). The report flags eGDR as non-insulin. It does not mark which rows are pre-specified versus post hoc. A reader could not rank them. The report says "no evidence is graded", which is its remit, but a pre-specified/post hoc flag is a design descriptor, not a grade.
- "Whether insulin-based variables were among them not confirmed" for DPP is honest.

**S7. LOW. Guideline rows.**
- PCOS 2023: verified in full text. Practice points 1.9.12 and 3.1.10 say insulin assays "are of limited clinical relevance and are not recommended in routine care" / "should not be used in routine care". Accurate. Note they are practice points (consensus, ungraded), not evidence-based recommendations.
- EASL-EASD-EASO MASLD: verified. "Assessment of insulin resistance (e.g., HOMA-IR or OGTT-derived estimates) may be considered ... (LoE 3, weak recommendation, consensus)". The agreement was 92 % in the voting. The same text says interpretation of HOMA-IR "requires standardised measurement of insulin and/or C-peptide". Accurate.
- ADA 2026 S3 pioglitazone/insulin resistance row, AACE 2022 row, ESC/ACC windows: I could not re-read them. The report appropriately says WebFetch windows were partial and "no hit" is not absence.
- Guideline negatives (ADA S2 / S10 "no hit", ACC/AHA 0 matches in a 100k window of 533k chars): carry the stated caveat; not independently checked.

**S8. LOW. Housekeeping.**
- S001 and S002 are the same string. The log is otherwise clear about which counts were screened. Two strings with counts of 14,000 and 3,000 are included without screening and should not be counted as searches that "found nothing".
- Q4 has a long "not retrieved" list (ADA 1997, ACE 2003, ISPAD, NICE, AHA CKM, KDIGO, AHA NAFLD). The report states it. This is a real gap for the question "what do guidelines say", because the historical documents that introduced "insulin resistance syndrome" are the ones that would say whether measurement was ever recommended.

---

## 2. Missing searches and databases

- Embase, Cochrane CENTRAL, Scopus, Web of Science: not searched (stated by the searcher). CENTRAL is the most direct place for "IR-guided" or "IR-stratified" trials.
- EU Clinical Trials Register / CTIS, jRCT, ANZCTR: not searched; ICTRP covers some but only via basic search.
- No MeSH-based search (e.g. Insulin Resistance[Majr] with Randomized Controlled Trial[pt] and "Patient Selection" or "Precision Medicine"); every PubMed string is free-text.
- Incremental value: no systematic screen of the 246-record broader reclassification string or of decision-curve/calibration hits; no screen of prediction-model registries (e.g. systematic reviews of diabetes risk scores that test fasting insulin).
- Treatment-by-IR interactions: missing targeted searches for large CV outcome trials (SGLT2i, GLP-1RA, statins, PCSK9, colchicine) with IR or TyG subgroups using broader strings. The one hit I found (ODYSSEY OUTCOMES) shows the first search was not exhaustive. Also not searched: Look AHEAD and DPP baseline insulin-by-treatment analyses (S010 and S158 are the only attempts; S158 returned 0 on a five-clause conjunction).
- Non-insulin comparators for the "beyond BMI, glucose, HbA1c, lipids" question: no search specifically for studies adjusting for BMI/waist and showing IR adds nothing (partly covered by WHI).
- Chemist side: no EFLM BV database / BIVAC check (stated), no PubMed search for TyG or Matsuda variability, no search for proinsulin cross-reactivity on current platforms (stated), no direct Crossref check (stated).

---

## 3. Claims that survived scrutiny

Chemist:
- Within-person CV of fasting insulin and HOMA-IR about 25 to 30 %. Confirmed in three independent abstracts (EuBIVAS 26.7 %, 95 % CI 25.5 to 28.3; Widjaja 26 %; ARIC 30.4 %). The EuBIVAS authors state HOMA-IR "is highly variable in the same individual which limits the value of single measurements".
- QUICKI CVI 4.1 % is a log-scale artefact, not better sensitivity (the abstract says so; the report's caveat is right).
- TG/HDL-C within-person CV 23.0 %, ICC 0.80, MDC95 1.4; HOMA-IR ICC 0.70, MDC95 2.3 (ARIC).
- Insulin assay disagreement is large and persistent despite WHO 66/304 traceability claims (Rohlfing 2025); consistent with Marcovina 2007, Manley 2008 and the 2022 seven-kit comparison.
- Gutenberg reference interval (n = 1,065 reference group, median 1.09, 97.5th percentile 2.35) is for one assay, with the authors concluding assay-specific intervals are required.
- Haemolysis lowers insulin (14.1 % at HI 51; 90.8 % at HI 1022 on Cobas e801).
- HOMA-IR, QUICKI and FIRI are monotone transforms (PMID 29940866 argues for repeatability and discrimination beyond clamp correlation).
- All RCV arithmetic is correct for the symmetric formula (see C1 for the asymmetry caveat).

Searcher:
- No fabricated identifiers; all checked PMIDs and DOIs match titles; no retraction notices in Crossref for 22 DOIs.
- WHI (PMID 25944628): fasting insulin, HOMA-IR and TG/HDL-C did not improve discrimination or reclassification; associations disappeared after adjusting for HDL-C. Accurately reported.
- TyG incremental value: very small pooled C-index gain (0.0004; 0.0051 on sensitivity analysis); the positive single-cohort TyG findings (e.g. C-index +0.005 in PMID 39117485) are association-heavy and small.
- DIETFITS: diet x INS-30 interaction P = 0.47. Accurate.
- IRIS: HOMA-IR > 3.0 entry criterion, HR 0.76, central-lab assay and calibration caveat. Accurate. No IR-negative comparator, no subgroup interaction.
- LAMP: statistics as stated (with the omissions in S2).
- PCOS 2023 guideline recommends against routine insulin assays; EASL MASLD gives a weak "may be considered".
- Registry identifiers NCT07710274 (n = 200 estimated, recruiting) and NCT06856291 (n = 40, completed) confirmed.

---

## 4. Overlap with the lead question: what Set B implies for clinical utility

- Analytical and biological variation set a hard limit on single-value individual use. Both reports agree on that, and the chemist's evidence for it is fair if one corrects the RCV asymmetry (C1) and the "cannot" language (C2).
- On outcomes and decisions, the searcher's evidence is thin: there is no IR-guided strategy RCT in the searched sources; the only incremental-value analyses with formal reclassification found so far (WHI, TyG pooled, Japanese cohort for HOMA-IR) are null or tiny; the one treatment-modification signal for a measured IR value (LAMP) is post hoc, early-terminated and complete-case; IRIS used HOMA-IR to define the population without an IR-negative arm and found no HOMA-IR subgroup gradient.
- The two reports do not conflict. Where they touch (assay standardisation, IRIS's central-lab caveat, HOMA-IR cutoff differences across trials: 2.5, 3.0, 3.46/3.8, FIRI 2.7), they are consistent and mutually reinforcing: the trial cutoffs are not transferable across assays.
- The most useful addition for the final team: treat the 2.5 / 3.0 / 3.46 / 3.8 cutoffs as assay-specific and not comparable.

## 5. Verdict

Overall, Set B supports a strong case against using a single fasting insulin or HOMA-IR value to classify an individual or detect individual change, and a weak-to-absent case for demonstrated clinical utility of measuring IR beyond BMI, glucose, HbA1c and lipids. The chemist report is accurate in its numbers and needs three corrections: asymmetric RCV (about -52 % / +107 %), a softer "cannot classify" (unreliable near the cutoff, fine far from it), and the two omissions in section C5. The searcher report is accurate in identifiers and design descriptions, but several negative claims are artefacts of narrow strings (statin/PCSK9 subgroup, reclassification, reference interval). The LAMP entry needs the early-termination, 3-month, complete-case and no-multiplicity caveats. I found no fabricated, mismatched or retracted citation.

Confidence: about 80 % that the chemist's central conclusion (single-value individual use unreliable) and the searcher's central finding (no IR-guided strategy RCT; weak incremental value) will survive further checking. About 55 to 60 % that the searcher's negative-result list is complete: the log shows narrow strings and unscreened large counts, and my quick re-searches surfaced at least one relevant RCT analysis the report said did not exist in its index. Full-text reading remains absent for most chemist sources and many searcher rows, so abstract-level caveats apply throughout.
