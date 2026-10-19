# Skeptic review of Set A: ir-clinical-chemist.md and ir-evidence-searcher.md

Reviewer: ir-skeptic (session). Date: 2026-10-18. Coverage and reimbursement out of scope. Other files in `ir-team/` were not read.

## 0. How I checked, and what failed

| Check | Tool | Outcome |
|---|---|---|
| Citation identity (title/identifier/numbers) | PubMed metadata (abstracts) for 9 chemist PMIDs and 8 searcher PMIDs | Done. Scholar Sidekick `verifyCitation` returned "not subscribed to this API"; `checkRetraction` returned "Too many requests". Neither worked, so PubMed was used for identity. |
| Retraction | Crossref API `works/{doi}` (`update-to` / `updated-by`) | Done for 8 DOIs: EuBIVAS 2024, LAMP 2026, IRIS 2016, Isokuortti 2017, Marcovina 2007, ARIC 2018, Barzegar 2020, Liu 2026. All show no update notices. Hu 2024 (bmjdrc-2023-003680) and the remaining ~25 cited papers were **not** retraction-checked (my script crashed on a Unicode title for Hu 2024). |
| Primary text | PCOS guideline full text (Europe PMC XML), ISRCTN API record | Read. Everything else I checked at abstract level only. I did not re-read the 2024 LC-MS/MS full text. |
| "Not found" claims | My own PubMed E-utilities searches | Done; results in sections 1.3 and 2.3. |

Same limit as the authors: most of my claim checks are against abstracts. Where an abstract could not settle the matter I say so.

---

## 1. Clinical chemist report

### 1.1 Ranked problems

**HIGH-1. Missed, directly relevant sources that the report lists as "gaps" (Section 7, gaps 1–3).** Two quick PubMed queries find them:
- PMID 33554550, Carobene et al., *Biological variation of serum insulin: updated estimates from EuBIVAS and meta-analysis*, Clin Chem Lab Med 2022 (a letter; PubMed shows no abstract). The report states that biological variation of insulin itself, and C-peptide, from EuBIVAS was "not directly retrieved" and that the index of individuality is unverifiable. The search `EuBIVAS AND insulin AND biological variation` returns exactly two records, this one and the HOMA-IR paper the report cites. So the gap exists because the search was not run, not because the source is hard to find. I have not read the letter's numbers, so I can't say whether it changes the headline.
- PMID 35622611, Rosli et al., *Measurement comparability of insulin assays using conventional immunoassay kits*, J Clin Lab Anal 2022. Seven current kits (4 ELISA, 3 CLIA including Siemens Centaur/Dxl800 and Cobas e801): relative SD between 1.7% and 23.2%, and the authors say traceability chains and unit conversions are not harmonized. The report's headline caveat is that the ADA platforms are old and that current multi-vendor data are a "gap". This paper partly fills it and supports the claim, but the spread is smaller than 12–66%. That matters for the "~25% inter-lab CV" framing (see HIGH-3).
- PMID 39726936 (Pediatr Diabetes 2024) on reproducibility of insulin sensitivity/secretion indices in children. Gap 3 (Matsuda/OGTT reproducibility) is therefore not empty either, though this is paediatric only. A further 145 records matched my broad Matsuda/reproducibility query; I did not screen them.

**HIGH-2. "Reference method for insulin: none available" is overstated and conflicts with the other Set A report.** The chemist's table (Section 2, LC-MS/MS row) and headline 1 say no reference measurement procedure exists, citing the 2024 full text. But Miller 2009 (which the chemist cites, and which I verified) benchmarks 10 assays "against an ID-LC-MS/MS measurement procedure calibrated using purified recombinant insulin", and the searcher records a Staten 2010 statement that a reference measurement procedure (ID-MS) exists. The defensible version is "no accepted/JCTLM-type reference system with a certified reference material and a deployed traceability chain". The 2024 paper's exact wording determines this, and the chemist should quote it. As written, the report contradicts its own Miller 2009 row.

**HIGH-3. The "25%" figure, and what it supports.**
- Verified: Isokuortti abstract says inter-laboratory CV of HOMA-IR 25%, insulin 25%, glucose 5%, ten individuals, seven labs. Marcovina 2007: among-assay CV 12–66%, median 24%. Zhou 2022: inter-laboratory 21.8%, inter-system 22.4%. All numbers match.
- Not independent, and different quantities. Marcovina measures among-*assay* CV across 10–12 kits; Zhou measures inter-lab CV on five **pooled** sera; Isokuortti is 7 labs on 10 individuals. The report acknowledges "not independent proof", but then Section 6 recommends citing "about 22–25% across three independent studies". Those are not three independent estimates of one parameter. Rosli 2022 (above) gives 1.7–23.2%, so current kits may be tighter than "~25%". The report should present this as a range of 2–25% depending on kit set, with the ADA-era end being the high one.
- "The same patient with HOMA-IR 2.0 in Helsinki would read 1.3 to 2.1 in six other labs" (headline 2 and table). The abstract says "The 2.0 HOMA-IR measured in Helsinki corresponded to 1.3, 1.6, 1.8, 1.8, 2.0 and 2.1 in six other laboratories." It does not say one patient. This reads like a regression-based translation across the ten samples. Turning it into a single-patient illustration is the chemist's gloss, and I could not confirm it from the abstract.

**HIGH-4. "Inter-lab imprecision for insulin by LC-MS/MS was not better than immunoassay" (Section 2 table, LC-MS/MS row) is an inference the source does not make.** From the abstract: verification precision was 2.7–3.7% CV; the 22.2% (IQR 20.9) figure is the *median across three laboratories on de-identified leftover clinical samples using single-point calibration*, falling to 15.3% when replicates are averaged. The authors conclude the assay is "robust". Comparing that median per-sample imprecision with the ADA among-assay CV across 10 vendors is a comparison of different metrics on different sample sets, with no statistical comparison. At minimum the report should state that this is its own comparison and note that sample concentrations (likely low) probably drive the figure. This is the one source the chemist read in full, so it is the one place the report should be most careful.

**MEDIUM-5. Arithmetic: checked and mostly correct, with three flaws.**
- RCV for HOMA-IR: 1.414 × 1.96 × √(5² + 26.7²) = 75.3%. Correct. Log-normal asymmetric version: ≈ +109% / −52%; the report says ≈ +100% / −50%. Fine. But CVa = 5% is an assumption; the report labels it as such. Using the ADA end of range (10.6%) gives ~85%. Harmless.
- Cutoff-crossing: a true value 25% above the cutoff with CV 27% gives P(read below) ≈ Φ(−0.84) ≈ 20%. Correct for a single repeat, but it uses "true mean" as the log-scale centre; if 25% above the cutoff is the arithmetic mean, the median is lower and the probability is a little higher. Minor.
- "Combined ±73%": √(27² + 25²) = 36.8%; × 1.96 = 72%. Correct as a 95% band for **one result relative to its true value**. It then says this "exceeds the gap between published cutoffs (1.9 to 2.7, about 40%)". The comparison is not like-for-like: the 40% gap is between cutoffs derived from different populations and different insulin assays, so part of that gap *is* the between-assay spread the report is adding on top. Presenting noise as larger than the disagreement double counts. Also the ±73% mixes CVI (within-person, one lab) and inter-lab CV (which only applies if the repeat is at a different lab), so it is a worst case, not a typical case.
- "Minimum detectable change 2.3 is larger than most published cutoffs (1.9–2.7)" (table). MDC95 is in absolute HOMA units measured in 102 adults aged 68–88 with a particular mean level; cutoffs are in different populations and assays. The comparison of an absolute MDC in one cohort to cutoffs from other cohorts is rhetorical. It says nothing about the proportional noise.

**MEDIUM-6. Two statement-versus-source slips.**
- Headline 3: "Within-run analytical imprecision of most insulin assays is 3.7–10.6% (ADA 2007)". The abstract: range 3.7–39.0%, with 7 of 10 assays ≤10.6%. The report gives the range correctly in the table but not in the headline.
- Marcovina's own conclusion was "most assays had acceptable imprecision and specificity" and 6/10 assays agreed within the allowable 32% total error. The report's tone (insulin "not harmonized") is supported, but it omits that the same abstract credits most assays with acceptable imprecision. The chemist quotes the 6/10 figure but not the conclusion sentence.

**MEDIUM-7. Evidence strength.** The report is honest that all but one source were read as abstracts, and I found no number in the abstracts I checked that was misquoted (EuBIVAS CVI 26.7% [25.5–28.3], QUICKI 4.1% [3.9–4.3]; ARIC CV 30.4%, ICC 0.70, MDC 2.3; Borai RCV 68.5/79.0/93.4%; Jayagopal >90% / >47%; Zhou recalibration 22.4→17.2 and 24.5→5.7; Miller bias >15.5% for 7/10). So the quoted numbers are accurate. The weaker point is interpretation, which cannot be settled from abstracts: e.g. whether EuBIVAS HOMA-IR CVI used insulin from one central lab (it likely did, which matters for generalizing to real-world between-lab use), and whether the ARIC 46-day interval includes real physiological drift (ICC 0.70 over six weeks in people aged 68–88 mixes biology and time).

**LOW-8. Unsupported or unverified items the chemist already flagged but still uses.** "Glucose and lipid assays are well harmonized (general knowledge)", "typical trial reduction of 20–40% (not verified)", and the hemolysis/stability statements. Fine as labelled, but the 20–40% line supports the "treatment-response monitoring not supported" bullet in Section 3 and should be dropped or sourced.

**LOW-9. Reference list formatting.** ARIC and the 2024 LC-MS/MS entries lack authors. PubMed gives first authors Poon (ARIC) and Moradian (LC-MS/MS). The searcher's list names Moradian; the chemist's does not.

### 1.2 Does the central conclusion hold?
The central claim is that single-value HOMA-IR near a cutoff cannot classify an individual, because within-person CV is about 27–30% and inter-assay spread is of the order of 20%. The quoted numbers are verified, and the RCV arithmetic is right. I'd rate the *biological variation* half as well supported (EuBIVAS n=90 × 10 occasions, plus ARIC, Jayagopal and Borai in the same range). The *inter-laboratory* half is weaker than presented (non-independent sources, old kits, Rosli's lower figures). The recommendation is conservative and sensible; the strength of its numbers is somewhat overstated in Sections 1 and 6.

### 1.3 Negative claims checked
- "TyG repeatability: searches returned nothing, which is not evidence of absence": correct caution. My broad PubMed query `TyG AND (biological variation OR repeatability OR …)` returns 760 records, mostly irrelevant; I did not screen them, so I can't confirm or refute absence. Flag as unresolved.
- "EuBIVAS insulin BV not retrieved": refuted as a retrieval failure, see HIGH-1.
- "Current-platform multi-vendor comparison not retrieved": partly refuted (Rosli 2022).
- "Matsuda/OGIS reproducibility not retrieved": partly refuted (paediatric study exists).

### 1.4 Survived
Existence of large inter-assay differences; the EuBIVAS HOMA-IR/QUICKI numbers; the ARIC repeatability numbers; C-peptide recalibration gain (verified in Zhou's abstract); the Isokuortti numbers; cutoff heterogeneity by derivation logic (I checked Isokuortti's 1.9/2.0 and 87%/79%; Tohidi, Geloneze and Peplies I did not check in this pass); the "not supported" list in Section 3.

---

## 2. Evidence-searcher report

### 2.1 Spot checks of identifiers and read levels

| Item | Result |
|---|---|
| PMIDs 42145088 (LAMP post hoc), 26886418 (IRIS), 38191206 (Hu), 42569452 (Liu), 32993633 (Barzegar), 41178693 (Mavraganis), 28359099 (Endocrine Soc. paediatric obesity), 37580314 (PCOS guideline), 38852583 (MASLD) | All resolve to the stated titles/journals. DOIs match. |
| Date mismatch | Mavraganis is listed as 2026; PubMed epub date is 2025-11-03 (volume year may be 2026). Trivial. Same pattern is possible elsewhere and I did not check it. |
| LAMP numbers | Abstract confirms 636 enrolled, 510 analysed, HOMA-IR cut 2.5, P for interaction 0.02, 5.8% vs 18.1%, "post hoc". The searcher's description is accurate, including the note that HOMA-IR assays were local. |
| IRIS | Abstract confirms HOMA-IR > 3.0 entry, 3876 participants, NCT00091949. |
| Liu 2026 | Abstract confirms C-index 0.731 → 0.732, P = 0.559, pooled ΔC 0.0004 (−0.0092 to 0.0100), 0.0051 (0.0007–0.0094) without Barzegar, "very low" GRADE. Accurate. Note that the abstract also says adding TyG **quartiles** improved IDI/NRI; the searcher's table lists only the C-index outcomes. Omission, not an error, but the table's "Reported metrics" cell is therefore not the full result. |
| Barzegar | Abstract says no improvement of FRS by IDI in those aged <60, and "adding TyG-index to FRS does not provide better risk prediction". The searcher flags the garbled table header and reproduces the printed values (C-index 0.789 vs 0.771) without interpreting. That was honest, though the subgroup restriction (<60 years, n = 6175 of 7521) is the thing to carry forward and the searcher put it only in a parenthetical. |
| Mavraganis (ATTICA) | NRI 0.668 / 0.469 and ΔC 0.054 / 0.044 confirmed. The abstract states the 8.46 cutoff was *derived in the same derivation cohort* (n = 1677), which makes the derivation-cohort figures optimistic. The searcher doesn't say so; the role file prohibits interpretation, so I only note it. |
| PCOS guideline wording | Read in the Europe PMC full text: rec 1.9.12 and 3.1.10 quoted exactly, including "limited clinical relevance and are not recommended" (1.9.12) / "should not be used in routine care" (3.1.10), and the sentence "routinely available measures of insulin resistance are inaccurate". Accurate. |
| ISRCTN11215387 | Record read: title, 604 target and 757 final enrolment, recruitment start 2016-04-05, **recruitment end 2016-06-30**, overall end 2021-06-30. The searcher says the size fields were "604 and 757 (field labels not shown in XML)". The labels *are* in the XML (`targetEnrolment`, `totalFinalEnrolment`); a recruitment window of three months with 757 final enrolment is odd and unexplained (cluster design, or an admin entry). This is the single closest thing to an "IR-guided strategy" trial, and the unresolved metadata is worth fixing. |

Read levels: the searcher uses an explicit code (FT-scan, Abs, Title, Reg, Snip) for every row, which is good practice. "FT-scan" means regular-expression scanning of text, which the report admits can miss synonyms; the guideline "0 hits" statements rest on that. I verified one guideline positive (PCOS) but not a negative. For example the claim that AASLD 2023 and ADA §8/§10 contain no IR-measurement recommendation depends entirely on the scan patterns; this is plausible but unverified by me.

### 2.2 Do the trial and interaction findings read accurately?
- Trials: the report states no trial randomises IR measurement vs no measurement, and describes IRIS as an enrichment trial and LAMP as a post hoc interaction. Both descriptions match the sources. It avoids calling LAMP's 5.8% vs 18.1% a result in itself.
- Interaction table: LAMP and the IRIS entry criterion are accurate. DIETFITS "P = 0.47" for the INS-30 interaction is stated as being in the abstract; I did not verify it. GRADE (Utzschneider) "P = 0.009 heterogeneity" and LIRA-ADD2SGLT2i "no significant HOMA-IR interaction" are abstract-level and unverified by me.
- One risk of misreading: the interaction table puts a positive post hoc result (LAMP) next to null or unverified ones with one-line design descriptions. The searcher does record "post hoc/exploratory" and "assays local", so the information is there.

### 2.3 Do the logs support the "not found" claims?

The report's five headline negatives (Section 9, (a)–(e)) are weaker than the wording suggests.

**MEDIUM-1. Several decisive "0" searches were over-constrained or broken, and the report is candid about it, but the top-line "Not found by any search" paragraph does not repeat the caveats.**
- (a) "No trial randomising IR measurement": supported by *many* strings (Q1a, Q1b, B1, B9, C3, R1a–R1h, ICTRP A-I1/A-I3, TrialCore, global search) none of which returned a qualifying record. Q1a is a five-way AND of exact phrases and returning 0 is uninformative on its own. Q1b returned 1 irrelevant record. But the combination gives reasonable support. My independent query (RCTs in PCOS with stratification by hyperinsulinaemia/IR and metformin) returned 24 records; the ones I screened by title were insulin-sensitizer trials, not testing-strategy trials, so I found no counter-example. **Survives**, with the caveat that outcome-less trial registries and non-English/regional registries (ChiCTR, JPRN, CTRI) were only covered through ICTRP first pages and one Amass query.
- (b) "No published decision-curve analysis of HOMA-IR/fasting insulin for treatment decisions": Q2c returned **112 records**, of which only the top ~10 were read; B-series counts are similar. "Not found" here means "not found in the top few results of a 112-record search". My own `decision curve OR net benefit` + HOMA/IR + prediabetes/diabetes + prediction query returned 60 records, which I did not screen. This claim is **not supported at the strength stated**.
- (c) "No ΔC/NRI study of HOMA-IR over PCE/SCORE2/QRISK": built on Q2b (64 records, top 8–12 read) and the TyG strings. My query `HOMA-IR AND (UK Biobank OR NHANES) AND (QRISK OR Pooled Cohort OR SCORE2) AND (reclassification OR C-index OR C-statistic)` returns 0, which is consistent with the claim, but it is narrow; neither search nor mine excluded studies that use "insulin resistance" generically or use models not named in the abstract. Moderate support.
- (d) "No baseline-HOMA-IR interaction analysis in the pivotal GLP-1/SGLT2 CV outcome trials": Q3f returned 269 records and the **top 10 only** were read; the report says "not exhaustively screened" in the log but states the negative flatly in Section 9. Q3a (20), Q3b (14), Q3t (11) were read more fully. **Not established.** The searcher found LIRA-ADD2SGLT2i and LAMP, so there is a track record of surfacing such papers, but 259 unscreened records is too many to claim absence.
- (e) "No guideline recommending routine insulin/HOMA-IR outside EASL conditional statement and JDS criteria": supported by 16 full-text scans, but six relevant documents (ESC 2021, AHA 2023, AACE 2026, ADA/EASD 2026, 2018 cholesterol, EASL 2016) could not be read. The negative should read "among the 16 documents scanned".

**MEDIUM-2. Malformed or ambiguous queries.** Q5q and Q4b are admitted as malformed (OR precedence; 41,789 and 3.7 M hits). Q5a (8,733), Q5e (2,406), Q5g (1,902), Q5v (21,228) and Q4f (21,548) are too broad to screen, so these produced no usable negative and no usable positive. The log is transparent about the two malformed ones but the other very large counts are not flagged as "unscreened" in Section 9. They do not drive a negative claim, so the damage is limited.

**MEDIUM-3. A found-by-accident pattern in the standardisation group.** The Group 5 table has 25 rows, but several appear to be lookup-by-title (Q5aa–Q5ac were exact-title searches for papers already known from Consensus snippets). The EuBIVAS 2022 insulin variation letter (PMID 33554550) and Rosli 2022 (PMID 35622611) are not in the list, although both are two-word-query findable. They are chemist-domain items, but the searcher was the one assigned to build the evidence set for assay variability, and Q5e (`HOMA-IR AND variability…`, 2,406 hits) was not screened beyond the top page. So the Group 5 set is incomplete on the very topic where the chemist then reports "gaps". This is the clearest evidence that the searcher's "top page only" practice had a cost, and it affects the chemist's report downstream.

**LOW-4. Search tooling.** ICTRP: first page (≤11 rows) per search only; the liver search I8 was not re-run with status = ALL. Both are disclosed. The Recruiting-default discovery and re-run is good practice and I credit it.

### 2.4 Still missing
- **Databases:** Embase, Cochrane CENTRAL, Scopus/Web of Science (admitted); Google Scholar / citation chasing (admitted).
- **Registries:** ChiCTR, CTRI, JPRN, EU CTR/CTIS, DRKS were not queried directly; only via ICTRP first pages, Amass, and one `global_trial_search`.
- **Guidelines:** NICE (NG28/NG246/CG189), KDIGO, ISPAD, IDF, Endocrine Society 2022+ obesity or PCOS updates, AACE/ACE PCOS 2015, ESHRE, Chinese/Indian diabetes guidelines. The report lists NICE, KDIGO, ISPAD and IDF as not searched; my single check (`insulin resistance AND (NICE OR KDIGO OR ISPAD OR IDF) AND guideline AND (HOMA OR fasting insulin)`) returned 3 records, none obviously a guideline; I did not open them.
- **Standardisation:** IFCC/ NIST and JCTLM reference-material listings; CAP/EQA survey summaries (the chemist also lists this as a gap); post-2019 multi-vendor comparisons beyond Rosli 2022.
- **Biological variation:** EFLM Biological Variation Database; EuBIVAS insulin letter (missed, see above).
- **OGTT insulin / C-peptide as predictors:** a handful of strings only (report admits it).
- **Prediction tools:** the TyG and "IR surrogate" literature (>1000 records) was covered by meta-analyses and a few incremental-value strings; the unscreened remainder is where a missed incremental-value study could sit.
- **Grey literature:** regulator/HTA documents, society position statements outside guidelines.

### 2.5 Survived
Identifier integrity (no mismatches in 9 spot-checked PMIDs); the LAMP, IRIS, Liu 2026 and PCOS-guideline descriptions; the read-level labelling; the transparent query log including failures; the Recruiting-filter correction; the headline absence of any IR-measurement-vs-no-measurement RCT (supported by convergent searches, not any single one).

---

## 3. Cross-report issues
1. **Conflict:** chemist says no reference measurement procedure for insulin exists; searcher records Staten 2010 saying an ID-MS reference procedure exists, and Miller 2009 (cited by both) used one. Needs the exact 2024 wording.
2. **Handoff gap:** the searcher's evidence set lacks the EuBIVAS insulin BV letter and Rosli 2022 that the chemist lists as gaps. Neither role found them. Re-running Q5-type searches with short queries would close it.
3. **Shared weakness (consistent with earlier recurring problems):** abstract-only reading. The chemist read 1 of 17 sources in full; the searcher read ~36 full texts, but by regular-expression scan, not end to end. The searcher's positives are mostly precise; its negatives are the weak part (top-page-only screening of large result sets).
4. **Retractions:** none found for the 8 DOIs I could check via Crossref. Retraction status was not verified for the remainder, and Scholar Sidekick failed, so identity checks were PubMed-based.

## 4. Verdict

**Chemist:** The measured numbers are accurate (every figure I compared with an abstract matched). The overall message (single HOMA-IR near a cutoff is unreliable; cutoffs are assay-specific) is well supported on the biological-variation side and plausibly supported on the inter-assay side. The weaknesses are (i) an unforced retrieval failure (EuBIVAS insulin letter, Rosli 2022), (ii) an overreach on LC-MS/MS performance and on "no reference method", (iii) the single-patient gloss on Isokuortti, and (iv) double-counting in the "noise exceeds cutoff gap" argument. Confidence that the main conclusion stands after full-text review: about 80%. Confidence that every specific numeric framing (e.g. "~25% universal CV", "LC-MS/MS not better") stands: about 50%.

**Searcher:** A careful, well-documented retrieval; identifiers are sound and the positive items are described accurately. The negatives are the issue: (a) and (e) are reasonably supported; (b), (c) and (d) rest on unscreened result sets and should be worded as "not found in the screened records". Confidence in the evidence set as a basis for the analysts' work: about 75%; confidence in the stated "not found" list as written: about 55%.
