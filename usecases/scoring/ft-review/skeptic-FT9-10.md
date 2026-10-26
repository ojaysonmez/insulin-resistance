# Skeptic review of FT9 and FT10 (full-text claim reviews)

Read: FT9.json, FT10.json, corpus/fulltext/<ID>.txt for all 14 papers, merged-conclusion.md lines 35, 88, 97, 100, 101, 105, 106, 109, 115, 123, usecases-verified.md line 127, claims/claims.csv rows for the cited claim IDs. Text search used whitespace-insensitive matching plus manual grep for variants. No web, no git.

## 1. Quote checks

| Paper | Quote found? | Note |
|---|---|---|
| C061 | yes (exact) | "Homeostasis model assessment (HOMA)-insulin resistance score 2.5." The "or more" sign is not in the text. |
| C062 | yes (exact) | The sentence continues "This may also due to the quality of this analysis..." (hedged by the authors); the lipid conclusion comes from adjusting for HDL-C and TGs. |
| C075 | yes (exact) | |
| C125 | yes (exact) | |
| C153 | not by whole-string match; found | Two-column interleaving: "Results of these exploratory analyzes must be inter- ... preted with caution given the small numbers of subjects, particularly in subgroups." Extraction artefact. |
| C157 | not by whole-string match; found | Interleaved columns: "Fasting insulin levels were reduced from baseline to peri- ... operative measurements in all patients". Extraction artefact. Also p=0.0005 and IGF-1 0.001 present. |
| C158 | yes (exact) | r = 0.54, p < 0.02. Arms 20/21/19 confirmed. |
| C174 | near-exact | Text reads "95% confidence interval [CI], -10.1 to -1.2"; the quote abbreviates. Numbers match (-5.6 points; 802 randomised; 10.6% vs 9.9%). Abbreviation only. |
| C184 | yes (exact) | Text uses middle dots (0.91 is "0·91", CI 0·80-1·03, p=0·15). |
| C188 | yes (exact) | |
| C002 | yes (exact) | "only modestly reduced the magnitude of these associations"; OR 1.94 (1.05-3.59), 187 events, 2,569 subjects confirmed. |
| C155 | not by whole-string match; found | Interleaved columns: "or glargine metabolites ranged from 0% to 264%. Four assays were more specific to human insulin". Extraction artefact. |
| C167 | not by whole-string match; found | Hyphenated across a line ("prelimi- nary evidence that there may be a role for assessing insulin resistance in PCOS and infertility"). Extraction artefact. |
| C181 | yes (exact) | "in vitro study only"; Atellica 92-121%; LC-MS/MS "nearly half (68%)" for glargine. |

## 2. Claim issue verdicts

| # | Paper | Issue | File and line | Claim IDs | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | C061 | Line 100 accurate; add DOI, full-text label, "lean adults need at least two" | merged-conclusion.md:100 | GL-40, EV-35 | reword | Current text already says "any two suffice in lean adults", so the issue is mostly a no-op. Text reads "HOMA-IR score 2.5": the "or more" sign is not in the extracted text, so the proposal's "2.5 or more" is an assumption; say so. "prediabetes by glucose or HbA1c" is right (fasting glucose, 2-hour post-load glucose or HbA1c). The "Korean authors criticise" clause is not in this paper (grep "Korea" hits only an affiliation); the issue's statement that it comes from elsewhere is true, but that clause is left untouched. The panel size 22 was marked unverified by the reader; not used. |
| 2 | C062 | Lipid caveat stronger: association lost with 28-SNP instrument and with 5-SNP clamp-based instrument | merged-conclusion.md:101 | EV-38 | reword (part rejected) | The 5-SNP result is right: "association was not observed for CAD or MI using 5-SNPs instruments for gold standard measures of IR (p=0.17; p=0.12)". The 28-SNP claim is not supported. Table 2: 28-SNP instrument CAD MR-Egger OR 0.94 (0.30-2.99) is null, but that is the low-power MR-Egger line; weighted median is 1.97 (1.37-2.83), weighted mode 1.86 (1.30-2.67), and the text says "Similar magnitudes of association and no evidence of directional pleiotropy were observed using the 52-SNPs and 28-SNPs instruments." So the association did not vanish with the lipid-free 28-SNP instrument. The lipid conclusion ("major contribution ... via its effect on lipids") comes from adjusting for HDL-C and TGs. CAD OR 1.79 (1.57-2.04), MI 1.78, IS 1.21, SAO 1.80 (1.30-2.49) confirmed. The reader's file also says "associations vanish with the 28-SNP instrument" in full_text_shows; that is wrong and should not propagate. |
| 3 | C125 | eGDR line hides recommendation of routine monitoring; larger studies not significant | merged-conclusion.md:105 | EV-40 | reword | Verified: MACE HR 0.79 (0.72-0.87), moderate heterogeneity; larger studies (>=1,000) HR 0.83 (0.65-1.06) "did not reach statistical significance", but "tests for subgroup differences were non-significant across all analyses", which the proposal omits and which matters (a non-significant stratum is not a difference). Authors: "Clinicians should consider routine monitoring of eGDR". eGDR built from WHR, hypertension and HbA1c: confirmed. "Four different equations" and "no outcome test of acting on eGDR" could not be traced by my greps; "four equations" dropped. |
| 4 | C075 | Add NFS/APRI-only, retrospective, scores disagreed | merged-conclusion.md:106 | EV-41 | reword | Confirmed: n=15,728, men 86%, "retrospectively accessed data from a de-identified database", in APRI-based analysis the BMI change model fitted better (the sentence starting "In contrast, in APRI-based analysis, changes in BMI..." is cut by my grep; NFS AIC 10,248.33 vs 10,368.57 favours HOMA-IR). The authors' shared-component statement concerns NFS ("NFS includes the presence of diabetes or IFG... changes in HOMA-IR may reflect changes in fasting blood glucose"), not APRI, so the proposal's "glucose is a component of both exposure and outcome" is fine only for NFS. "Results differed between the two" is correct in substance (BMI vs HOMA-IR fit) but is stated more safely as the BMI/HOMA-IR fit difference. |
| 5 | C153/C157/C184 | Read level now full text; exploratory glucose and insulin-fall associations; STAMPEDE PFS signal | merged-conclusion.md:97 | TRI-43, TRI-44, EV-35 | reword | Confirmed in C153: HOMA -0.21, p=0.047; baseline glucose at the 5.3 mmol/L median "(-6.1 vs. +1.1 %, p=0.02)" (sign garbled, table shows <5.3 group +1.1, >=5.3 group -6); TUNEL increase with insulin fall >3.5 pmol/L (+0.84 vs +0.13 %, p=0.001); "exploratory analyzes... interpreted with caution". Baseline insulin (<39 pmol/L) and baseline HOMA (<1.28) rows carry p=0.83 and 0.51 for Ki67 change: they are reported as not associated, so "were not reported as predictors" is loose; "not significantly associated" is accurate. HOMA p=0.01 "similar pattern" is ambiguous (garbled), left out. C157: insulin fell, p=0.0005, 10 controls; Ki67 -9.7%, p=0.02. C184: OS HR 0.91 (0.80-1.03), p=0.15; high-volume HR 0.76 (0.64-0.90); the "0·012" interaction p sits before "A similar pattern was seen for metastatic progression-free survival", consistent with the reader; authors say "some evidence of a potential anticancer effect" in high-volume disease. The proposed "baseline fasting glucose above 5.3" should read "at or above the 5.3 mmol/L median" (split at median, a tie rule is not stated). C153 sentence said "insulin, HOMA or C-peptide": C-peptide appears only as a rationale, not an outcome. |
| 6 | C158 | Measure now named (HOMA-IR; OGTT insulin AUC second index); APOE-4 moderator | merged-conclusion.md:109 | ABS-15 | confirmed (minor) | Text: HOMA-IR defined; OGTT used; "Higher insulin resistance at baseline predicted greater improvement with the 40 IU dose (r = 0.54, p < 0.02)"; APOE-4 effect "improvement for APOE-4 carriers (p < 0.02), and worsening for non-carriers (p < 0.02)". The paper text read does not tie r to an index, so the proposal's caveat is right. I could not read the correction notice either. Apply with the shorter edit below (the proposed wording duplicates existing text before the quote point). |
| 7 | C174 | "Benefit remains debated" understates TOBOGM first-outcome result | merged-conclusion.md:109 | ABS-14 | confirmed (with fitted wording) | 802 randomised; neonatal composite 94/378 (24.9%) vs 113/370 (30.5%); adjusted RD -5.6 (-10.1 to -1.2), P=0.02; hypertension 40/378 (10.6%) vs 37/372 (9.9%), RD 0.7 (-1.6 to 2.9); lean mass 2.86 kg figure present. Glucose OGTT only. I did not grep "no insulin measurement" across the whole paper; the reader's statement is consistent with the diagnostic criteria seen (WHO 2013), and I flag it as not exhaustively checked. |
| 8 | C188 | TyG is a non-insulin surrogate; association only; authors overreach | merged-conclusion.md:109 | EV-46 | reword | OR 2.51 (2.18, 2.90), p<0.00001; 220,985 subjects; countries India, China, Iran, Mexico, South Korea. Authors: "the TyG index can be used for the early diagnosis of pregnancy complications and APOs ... monitoring ... in early pregnancy can facilitate early identification". No "GRADE" in the text (grep). I did not verify "23 studies", "I2 80%" or "no standard cutoff"; those are dropped from the wording. |
| 9 | C002 | Fully adjusted interval 1.05-3.59 close to 1; 187 events; non-diabetic | merged-conclusion.md:35 (line 123 needs no change) | EV-30, EV-56 | confirmed (trimmed) | OR 1.94, 95% CI 1.05-3.59, P trend 0.02; 187 events; 2,569 subjects free of diabetes at baseline; adjusted for LDL, triglycerides, HDL, SBP, smoking, alcohol, exercise and waist. The 2.52 (1.46-4.36) figure is from the project text and the reader; I did not re-read the age/sex/ethnicity-adjusted line, so I keep "OR 2.52 to 1.94" as written. Line 123 "only modestly reduced" is a verbatim match to the paper: no edit. |
| 10 | C167 | RR 1.03 is per U/mL fasting insulin on 4 RCTs and 741 women; HOMA-IR 1.14; letrozole null | merged-conclusion.md:88 and :115 | TRI-38, TRI-52, EV-52 | confirmed | Table rows: "Fasting insulin (U/mL) 4 741 1.03 1.01-1.06 0"; "HOMA-IR 4 736 1.14 1.03-1.25 0"; the other (letrozole vs CC) table "Fasting insulin (U/mL) 3 977 1.01 1.00-1.02"; "HOMA-IR 3 975 1.04 0.98-1.09". Text: "the results of subgroup analyses were all considered exploratory" and "considered exploratory due to multiplicity"; "preliminary evidence that there may be a role for assessing insulin resistance"; the guideline "does not recommend" routine testing. The proposal covers line 88 only; line 115 also says "abstract" and "unit, sampling time and assay ... not stated in the abstract", which the full text partly resolves (unit and fasting basis), so edit both. Assay harmonisation is not addressed here (not traced). |
| 11 | C155 / C181 | Both assay studies in vitro; upgrade to full text; Atellica one concentration | usecases-verified.md:127 (and section 4, claim UC-GAP-04) | UC-GAP-04 | reword | C155: 0-264%, four human-specific assays confirmed; "Immulite ... results were not included". C181: Atellica "92% to 121% for all insulin analogs", "in vitro study only", LC-MS/MS glargine "nearly half (68%)". The "single 10 ng/mL spike" statement was not re-checked by me; kept as "stated by the reader, not re-checked" is avoided in the wording and the figure is omitted. Where "section 4" of usecases-verified.md carries the same sentence I did not find a second copy beyond line 127 by the grep for "264". |

## 3. Apply

Each item gives the exact old text (single occurrence expected in the named file) and the new text. Confidence figures are not touched. All keep PMID and DOI.

### A. merged-conclusion.md line 100 (issue 1)

Old:
`(PMID 32278004; criteria table read in full) lists HOMA-IR of 2.5 or more as one of seven optional metabolic risk criteria (waist, BP, triglycerides, HDL, prediabetes, HOMA-IR, hs-CRP); any two suffice in lean adults, so an insulin assay is never required.`

New:
`(PMID 32278004, DOI 10.1016/j.jhep.2020.03.039; criteria table read in full) lists a HOMA-IR score of 2.5 (fasting-based; the "or more" sign is not recoverable from the extracted text) as one of seven optional metabolic risk criteria (waist, BP, triglycerides, HDL, prediabetes by fasting glucose, 2-hour post-load glucose or HbA1c, HOMA-IR, hs-CRP); lean or normal-weight adults need at least two, so an insulin assay is never required.`

### B. merged-conclusion.md line 101 (issue 2, reworded; do not apply the 28-SNP statement)

Old:
`carry OR 1.79 for CAD and 1.80 for small-artery stroke. The lipid instruments have their own pathways,`

New:
`carry OR 1.79 for CAD and 1.80 for small-artery stroke (DOI 10.1136/bmjdrc-2020-001217; full text read). In the authors' sensitivity analyses the association was not observed for CAD or MI with 5-SNP instruments for gold-standard measures of IR (p=0.17, 0.12), and they conclude that the major contribution to CAD/MI is via lipids; a 28-SNP instrument outside HDL-C and triglyceride loci gave similar-magnitude estimates in the weighted-median analysis (CAD 1.97, 1.37-2.83), so the sensitivity picture is mixed. The lipid instruments have their own pathways,`

### C. merged-conclusion.md line 105 (issue 3)

Old:
`eGDR in type 1 diabetes (PMID 40841970, observational).`

New:
`eGDR (non-insulin surrogate from waist-hip ratio, hypertension and HbA1c) in type 1 diabetes (PMID 40841970, DOI 10.1186/s13098-025-01900-8; full text read, observational meta-analysis): pooled HR per unit 0.79 (0.72-0.87) for MACE; in studies with 1,000 or more participants HR 0.83 (0.65-1.06), not significant, although the authors' tests for subgroup differences were non-significant; the authors suggest considering routine eGDR monitoring, which association data do not show to change outcomes.`

### D. merged-conclusion.md line 106 (issue 4)

Old:
`(PMID 34674510, n=15,728, 86% men): exposure and outcome share components`

New:
`(PMID 34674510, DOI 10.3803/enm.2021.1110; full text read; n=15,728, 86% men, retrospective, fasting-based; fibrosis judged by NFS and APRI scores only, and the two scores did not agree on whether BMI change or HOMA-IR change fitted better): exposure and outcome share components`

### E. merged-conclusion.md line 97 (issue 5)

Old:
`(for example PMIDs 22933030, 24972190; abstracts) insulin, HOMA or C-peptide was an outcome that metformin lowered, not an effect modifier, and the STAMPEDE metformin arm in metastatic prostate cancer (PMID 40639383, DOI 10.1016/S1470-2045(25)00231-1; abstract per the oncology reviewer) was null for overall survival and reports no baseline insulin subgroup in its abstract.`

New:
`(for example PMIDs 22933030, 24972190; full text read) fasting insulin or HOMA (fasting-based) was an outcome that metformin lowered; in the breast study baseline insulin and HOMA were not significantly associated with Ki67 change, while exploratory subgroups linked baseline fasting glucose at or above the 5.3 mmol/L median (p=0.02) and an on-treatment insulin fall (TUNEL, p=0.001) to tumour response, in small subgroups the authors say must be interpreted with caution; and the STAMPEDE metformin arm in metastatic prostate cancer (PMID 40639383, DOI 10.1016/S1470-2045(25)00231-1; full text read) was null for overall survival (HR 0.91, 0.80-1.03), showed a progression-free survival signal in high-volume disease (HR 0.76, 0.64-0.90; reported interaction p=0.012) and tested no insulin or C-peptide subgroup.`

### F. merged-conclusion.md line 109, Claxton (issue 6)

Old:
`Claxton 2015, PMID 25374101, DOI 10.3233/JAD-141791, abstract; insulin-resistance measure not named in the abstract; not a stratified or interaction test)`

New:
`Claxton 2015, PMID 25374101, DOI 10.3233/JAD-141791, full text read; insulin resistance was HOMA-IR from fasting values, with an OGTT insulin AUC as a second (post-load) index, and the passages read do not say which index the correlation uses; APOE-4 status, not insulin resistance, moderated the main memory effect; correction notice not read; not a stratified or interaction test)`

### G. merged-conclusion.md line 109, TOBOGM (issue 7)

Old:
`and the benefit of treating even glucose-defined early GDM remains debated (TOBOGM, PMID 37144983, DOI 10.1056/NEJMoa2214956, abstract)`

New:
`and the benefit of treating glucose-defined early GDM is mixed across outcomes (TOBOGM, PMID 37144983, DOI 10.1056/NEJMoa2214956, full text read; glucose OGTT criteria, no insulin or C-peptide test: fewer adverse neonatal outcomes with immediate treatment, 24.9% vs 30.5%, adjusted risk difference -5.6 percentage points, 95% CI -10.1 to -1.2, with no difference in pregnancy-related hypertension, 10.6% vs 9.9%)`

### H. merged-conclusion.md line 109, TyG (issue 8)

Old:
`a 2026 meta-analysis of early-pregnancy TyG (PMID 42110441, DOI 10.3389/fmed.2026.1811358; abstract) reports associations only;`

New:
`a 2026 meta-analysis of early-pregnancy fasting TyG, a non-insulin surrogate (PMID 42110441, DOI 10.3389/fmed.2026.1811358; full text read: 220,985 subjects, mostly Asian cohorts, GDM OR 2.51, 95% CI 2.18-2.90) reports associations only, although its authors say TyG can be used for early diagnosis;`

### I. merged-conclusion.md line 35 (issue 9)

Old:
`(San Antonio, PMID 12087016: OR 2.52 to 1.94).`

New:
`(San Antonio, PMID 12087016, DOI 10.2337/diacare.25.7.1177; full text read; 2,569 adults free of diabetes at baseline, 187 combined cardiovascular events, fasting HOMA-IR: OR 2.52 to 1.94, the fully adjusted 95% CI being 1.05-3.59, close to 1).`

### J. merged-conclusion.md line 88 (issue 10)

Old:
`| PCOS IPD meta-analysis (31647106) | baseline insulin | interaction for clomiphene plus metformin vs clomiphene, live birth RR 1.03 (1.01-1.06) |`

New:
`| PCOS IPD meta-analysis (31647106; DOI 10.1093/humupd/dmz029; full text read) | baseline fasting insulin, per U/mL (fasting-based) | exploratory interaction for clomiphene plus metformin vs clomiphene, live birth RR 1.03 (1.01-1.06), 4 RCTs, 741 women; HOMA-IR interaction 1.14 (1.03-1.25), 4 RCTs, 736 women; no cutoff; letrozole vs clomiphene fasting-insulin interaction 1.01 (1.00-1.02), HOMA-IR 1.04 (0.98-1.09) |`

### K. merged-conclusion.md line 115, part 1 (issue 10)

Old:
`DOI 10.1093/humupd/dmz029, abstract: an interaction between baseline serum insulin`

New:
`DOI 10.1093/humupd/dmz029, full text read: an exploratory interaction between baseline serum insulin`

### L. merged-conclusion.md line 115, part 2 (issue 10)

Old:
`the unit, sampling time and assay of the insulin variable are not stated in the abstract;`

New:
`the full text shows the 1.03 is per U/mL of fasting insulin on 4 RCTs and 741 women, not the 907-woman live-birth set, and that the subgroup analyses were labelled exploratory;`

### M. usecases-verified.md line 127 (issue 11)

Old:
`Heurtault 2014, PMID 24150210, DOI 10.1515/cclm-2013-0427, 16 assays, analogue cross-reactivity 0-264%;`

New:
`Heurtault 2014, PMID 24150210, DOI 10.1515/cclm-2013-0427, full text read, in vitro spiking of 16 immunoassays, analogue cross-reactivity 0-264% depending on assay and concentration;`

### N. usecases-verified.md line 127 (issue 11)

Old:
`Li 2025, PMID 39030378, DOI 10.1007/s12020-024-03970-6, Atellica 92-121% for five analogues; abstracts re-checked in PubMed 2026-10-24).`

New:
`Li 2025, PMID 39030378, DOI 10.1007/s12020-024-03970-6, full text read, in vitro only (the authors' stated limitation), Atellica recovery 92-121% for five analogues, LC-MS/MS 68% for glargine and little detection of other analogues; Violin 2023 abstract re-checked in PubMed 2026-10-24).`

## 4. Not verified / notes

- Not re-checked by me: C125 "four equations", "1 study high risk of bias"; C075 NFS/APRI progression counts; C188 "23 studies", I2 80%, no cutoff; C002 age/sex-adjusted OR 2.52 (1.46-4.36); C181 single 10 ng/mL spike; C167 assay harmonisation; C158 correction notice; C061 panel size.
- Claim-ledger rows (claims/claims.csv) carry the old wording and read levels ("abstract"); they will need the same updates by the main session if these edits are applied. I did not edit them.
- The 28-SNP error in FT9 (C062) is the main substantive finding: do not apply the FT9 proposed wording for line 101.
- Tool calls used: 12 (reads and greps), plus this write.
