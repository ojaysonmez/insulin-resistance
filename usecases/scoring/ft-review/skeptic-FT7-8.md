# Skeptic review of FT7 and FT8 (full-text claim reviews)

Method: quotes checked by normalised string match (lower case, punctuation and line breaks ignored) against corpus/fulltext/<ID>.txt; numbers by grep of the same files; current wording read from merged-conclusion.md and claims/claims.csv. No web, no git. Words from papers are treated as data. Two-column PDF text (C003, C009, C048 and others) interleaves columns, so some quotes needed manual reconstruction.

## 1. Quote checks

| Paper | Quote found? | Note |
|---|---|---|
| C168 (FT7) | No (not a quote) | Field holds "Not applicable: ...". The text file (319 lines) has 0 hits for insulin, HOMA, C-peptide; no "Table 2". The absence statement is supported; the field is a placeholder, not a passage. |
| C187 | Yes | Line 85, "Insulin resistance drops rapidly with the delivery of the placenta." |
| C003 | Yes, column-interleaved | Lines 31-33 and 140-144: "a subsequent sample must increase by 90% or decrease by 47%". Extraction artefact only. |
| C009 | Yes, column-interleaved | Lines 25-27 abstract: "A common insulin reference preparation did not change the among-assay CV ...". Artefact. |
| C012 | Yes | Line 40. |
| C045 | Yes | Exact match. |
| C048 | Yes, column-interleaved | Lines 84-85. Artefact. |
| C051 | Yes | Exact match ("Prior to examining any data, we modified the primary hypothesis ..."). |
| C053 | Yes | |
| C073 | Yes | Preprint text (medRxiv, posted 30 Jan 2021). |
| C131 | Yes | |
| C133 | Yes | |
| C144 | Yes | |
| C147 | Yes | |
| C160 | Yes | |
| C161 | Yes | |
| C177 | Yes | |
| C185 | Yes | |

Other numbers re-checked and found in the text: C003 +90%/-47%, 2.77 x CVI, 1.05 vs 0.15, CV 10.6%; C009 12 assays from 9 manufacturers, 7 of 10 / 6 of 10 / within-assay CV to 39.0%, "greatest at low insulin concentrations", 40 patient samples; C012 n = 12/18/67, 97 subjects, "up to twofold", HOMA-IR medians 1.30/2.58/2.13 (Table 2 ranges not in text: could not be read); C045 intra-assay CV 0.8-10.1% and inter-assay 1.0-12.9% (QC levels 1-3); C048 25.0% / 25.4% / 4.6%, ten non-diabetic, seven labs, DOI 10.1007/s00125-017-4340-1 in the header; C051 P .47, beta 0.08 (-0.13 to 0.28), 80% power for n=400, 90% post hoc; C073 -0.290 (-0.544 to -0.036) P=0.025; C131 522 enrolled, 510 complete, exclusion "1 week before admission / index event"; C133 median HOMA-IR 3.31, placebo group n=2839 and 2858, 62.6% of 18,924; C144 725 vs 1165, 2.82 vs 5.86, r 0.75, deconvolution, frequently sampled; C147 123 to 193, +14%, +53%, -21%, 4.69 vs 4.85; C160 adjusted -85 (-160 to -10), r 0.72, 876 vs 998; C161 0.135 vs 0.098 P 0.013, r -0.337 P 0.042, hepatitis C 0.167 vs 0.125; C177 13,026, 6,484 / 6,480, HR 0.81 (0.72-0.92) vs 0.92 (0.79-1.06), P 0.063, 6.34 vs 3.76; C185 5851, aRR 1.72 / 1.34 (P interaction 0.06), race P 0.012.

Not found or not traceable in the text read: LAMP counts 636, 114 and 12 (C131); the C161 "HOMA-" symbol is lost in extraction (context is the beta-cell section, so HOMA-beta is likely; HOMA-IR is not reported in what was read); C177 Bayer sponsorship text only in the data-sharing statement (sponsorship itself not re-verified); C185 "Bayer employees are co-authors" not checked.

One error in FT8: its C131 quality_note says "Interaction is unadjusted". The text (line 36 and 48) says both unadjusted and adjusted models were presented and adjusted results (Tables S3, S4) were consistent. This does not affect any proposed wording below, but do not carry it into the files.

## 2. Claim issue verdicts

| # | Issue | File and line | Claim IDs | Verdict | Evidence |
|---|---|---|---|---|---|
| FT7-1 | Tohidi "reports no CV" is wrong | merged-conclusion.md line 47; claims.csv MEAS-15 (MEAS-12 cites it) | MEAS-15, MEAS-12 | reword | Current text confirmed. Paper gives intra-assay CV 0.8-10.1% and inter-assay 1.0-12.9% from QC sera, no among-assay CV. Proposed wording calls both "within-assay"; inter-assay is not within-assay, so reword. DOI added. 85/80 fasting split not re-checked, omitted. |
| FT7-2 | DIETFITS "prespecified" needs caveat | merged-conclusion.md line 76; claims.csv TRI-23 (also TRI-01, TRI-54, ABS-21, and "prespecified" in lines 2 and 132) | TRI-23 (+ others) | reword | Paper: hypothesis added near study onset when funding rose, "Prior to examining any data"; >80% power for original n=400, 90% post hoc for ~600. P .47, beta 0.08 (-0.13 to 0.28). Proposed wording lacks the DOI and the table format; give row-shaped wording. Lines 2/132 and TRI-01/ABS-21 still say "prespecified": flag for the main session (not edited here, as they sit inside long sentences). |
| FT7-3 | Marcovina: upgrade read level, add concentration dependence | merged-conclusion.md line 46; claims.csv MEAS-14 | MEAS-14, MEAS-12 | reword | Confirmed (12 assays/9 manufacturers, 10 analysed, 40 patient samples, CV greatest at low concentrations). Add DOI. |
| FT7-4 | Manley per-assay ranges unverifiable | merged-conclusion.md line 43; claims.csv MEAS-10 | MEAS-10 | reword | Table 2 is not in the text, so the ranges could not be read (not shown wrong). Proposed wording deletes them; better to keep them with an unverified label. DOI added. Partial full text. |
| FT7-5 | APA 2020: keep excerpt label | merged-conclusion.md line 20; claims.csv GL-23 | GL-23 | reword | Confirmed: local text is executive summary only, 0 hits for insulin/HOMA/C-peptide, no Table 2. Proposed wording would drop the DOI and the monitoring list; use a minimal append instead. |
| FT7-6 | ADA s15 now full text | merged-conclusion.md line 21; claims.csv GL-24, EV-12 | GL-24, EV-12 | reword | Confirmed: rec 15.30 75-g OGTT at 4-12 weeks, "progressive insulin resistance in the second and third trimesters", "drops rapidly" (line 85); 0 hits HOMA, C-peptide, TyG (the 2 "triglyceride" hits are lipid-lowering text), fasting insulin. Proposed wording drops IADPSG and the DOI; use targeted replacements. The HOMA-IR cutoff step stays inference. |
| FT7-7 | QUICKI/log-transform sentence is inference | merged-conclusion.md line 42; claims.csv MEAS-08 | MEAS-08 | reword | Paper: one-to-one transforms, Spearman -1; I found no within-person CV discussion. Keep the 4.1% figure with inference label rather than dropping it; add DOI. |
| FT7-8 | Isokuortti DOI | merged-conclusion.md line 50; claims.csv MEAS-19 | MEAS-19 | confirmed (with exact old/new strings below) | DOI 10.1007/s00125-017-4340-1 in the paper header (line 4). 25%, ten samples, seven labs confirmed. Ledger caveat "DOI not recorded" also needs updating. |
| FT8-1 | PLIS stratified on post-load OGTT insulin | merged-conclusion.md line 65; claims.csv TRI-14 | TRI-14 | reword | Confirmed from preprint: stratification by insulin secretion, sensitivity, liver fat with "previously established cut-off levels (14)"; numbers -0.290 (-0.544;-0.036) P 0.025; low risk conventional "not superior to control". No fasting insulin/HOMA in the file (0 hits). Proposed "2-h glucose" is not in the abstract (it says "post-challenge glucose"): reword. Matsuda/insulinogenic/disposition index mentions are present. Label as preprint text; DOI added. |
| FT8-2 | LAMP insulin exclusion reason | merged-conclusion.md line 51; claims.csv MEAS-21 | MEAS-21 | reword | Confirmed: text excludes insulin therapy "1 week before admission" to avoid effect on fasting insulin and HOMA-IR; analogue cross-reactivity and C-peptide are not mentioned. Proposed wording replaces the whole sentence and would delete the general analogue claim, which the issue does not show to be wrong; edit only the LAMP clause. |
| FT8-3 | LAMP counts 636/114 not in text | merged-conclusion.md line 90; claims.csv TRI-39 | TRI-39 | reword | 522 and 510 confirmed (C131 line 42); 636, 114, 12 not found. Keep them as unverified rather than deleting. Ignore the "unadjusted" point (see section 1). |
| FT8-4 | ODYSSEY: HOMA-IR median split, no treatment-by-IR test | merged-conclusion.md line 91; claims.csv TRI-42 | TRI-42 | reword | Confirmed: spline curves "largely superimposable in both HOMA-IR categories", placebo group, median 3.31; treatment spline p 0.36 and 0.50 are for LDL-C and sdLDL-C. "leans toward no IR modification" has no analysis behind it. Proposed wording is supported; add DOI, keep the "found by a skeptic" tail untouched. |
| FT8-5 | Method labels for cirrhosis and TIPS | merged-conclusion.md line 51; claims.csv MEAS-22, MEAS-23 | MEAS-22, MEAS-23 | reword | Confirmed: iv glucose 0.3 g/kg frequently sampled, minimal model, C-peptide deconvolution (C144); TIPS: before-after, OGTT insulin AUC +53% (CI 14-90), C-peptide:insulin -21%, clearance (clamp-calculated) unchanged. Proposed wording is supported but replaces text including DOIs; use targeted edits that keep DOIs. |
| FT8-6 | Liver/CKD summary sentence overreaches | merged-conclusion.md line 51; claims.csv MEAS-24, 25, 26, EV-42 | MEAS-24, MEAS-25, MEAS-26, EV-42 | reword | Confirmed: C161 has no HOMA-IR result (beta only); C160 adjusted clearance -85 (-160 to -10), r 0.72 with sensitivity, no eGFR correlation, "may be biased in CKD" is stated as a premise (line 13), diabetes excluded. Proposed wording supported but drops DOIs and the post-load labels; use targeted edits. Confidence figures untouched. |
| FT8-7 | FIDELITY and FINEARTS-HF "did not differ" hides near-significance | merged-conclusion.md line 91; claims.csv TRI-40, TRI-41, ABS-16 | TRI-40, TRI-41, ABS-16 | reword | Confirmed: HR 0.81 (0.72-0.92) vs 0.92 (0.79-1.06), P interaction .23, continuous .063 "near", 13,026 full set; FINEARTS race P 0.012 and diabetes-status P 0.06 (the latter concerns the eGDR-outcome association, not finerenone). Proposed wording supported; apply as targeted edits that keep DOIs. Bayer sponsorship and "authors call it hypothesis generating/not powered" are in the text (lines 65-70). ABS-16 text needs no change (it says null interaction for FIDELITY; if wanted, add "(continuous P 0.063)" by hand). |

## 3. Apply

Strings are copied from merged-conclusion.md. Unless stated, the same old string also occurs in the matching claims/claims.csv claim text (checked by grep of the claim rows), and the same replacement can be used there; the ledger columns read_level and caveats (for example "abstract", "No CV reported", "DOI not recorded", "PMID 41358885: excerpt") need matching manual updates by the main session. Confidence figures are unchanged by every edit.

1. FT7-1 (merged-conclusion.md line 47; claims MEAS-15)
OLD: `Tohidi 2017 (PMID 28150502, abstract): 8 assays, lowest and highest median differing by a factor of 1.8. It reports no CV.`
NEW: `Tohidi 2017 (PMID 28150502, DOI 10.1080/00365513.2016.1278260, full text): 8 assays on 165 serum samples, lowest and highest median differing by a factor of 1.8; it reports quality-control CVs per assay (intra-assay 0.8-10.1%, inter-assay 1.0-12.9%) but no among-assay CV.`

2. FT7-2 (line 76; claims TRI-23)
OLD: `DIETFITS (PMID 29466592) | n=609; prespecified diet x INS-30 interaction | P = 0.47, null`
NEW: `DIETFITS (PMID 29466592, DOI 10.1001/jama.2018.0245, full text) | n=609; diet x 30-minute post-glucose insulin (INS-30) interaction, specified before data were examined but added after the trial began; non-diabetic adults, weight-loss outcome | P = 0.47 (beta 0.08 per 10 uIU/mL, 95% CI -0.13 to 0.28), null`

3. FT7-3 (line 46; claims MEAS-14)
OLD: `Marcovina 2007 (PMID 17272483, abstract): among-assay CV 12-66%, median 24%, for 10 assays (older generation; a common reference preparation did not lower it).`
NEW: `Marcovina 2007 (PMID 17272483, DOI 10.1373/clinchem.2006.082214, full text): 12 assays from 9 manufacturers were evaluated and results reported for 10, with 40 patient samples; among-assay CV 12-66%, median 24%, greatest at low insulin concentrations; a common reference preparation did not lower it (older-generation assays).`

4. FT7-4 (line 43; claims MEAS-10)
OLD: `HOMA-IR ranges across 11 assays in Manley 2008 (PMID 18535197): 0.8-2.0 in normoglycaemia, 1.9-3.2 in prediabetes, 1.5-2.9 in T2D.`
NEW: `Fasting-based HOMA-IR varied up to twofold depending on the insulin assay across 11 assays in 97 fasting adults (Manley 2008, PMID 18535197, DOI 10.2337/dc08-0097, full text, partial; 12 normoglycaemic, 18 prediabetic, 67 T2D). The per-assay ranges previously listed here (0.8-2.0 in normoglycaemia, 1.9-3.2 in prediabetes, 1.5-2.9 in T2D) are unverified: the tables are not in the local text.`

5. FT7-5 (line 20; claims GL-23)
OLD: `APA 2020 Table 2 (PMID 32867516, DOI 10.1176/appi.ajp.2020.177901; excerpts)`
NEW: `APA 2020 Table 2 (PMID 32867516, DOI 10.1176/appi.ajp.2020.177901; excerpts; the local full text is the executive summary only, mentions no insulin, HOMA or C-peptide test and does not contain Table 2, so Table 2 is still not re-read)`

6a. FT7-6 (line 21; claims GL-24)
OLD: `ADA Standards 2026 section 15 (PMID 41358885, DOI 10.2337/dc26-S015; summarising-fetch excerpts, not verbatim-checked)`
NEW: `ADA Standards 2026 section 15 (PMID 41358885, DOI 10.2337/dc26-S015; full text read: postpartum screening is a 75-g OGTT at 4-12 weeks, rec 15.30, and no fasting-insulin, HOMA-IR, TyG or C-peptide test is named)`

6b. FT7-6 (line 21; claims EV-12)
OLD: `(ADA s15 excerpt; review PMID 38185282`
NEW: `(ADA s15 full text: insulin resistance progresses in the second and third trimesters and drops rapidly after delivery; review PMID 38185282`

7. FT7-7 (line 42; claims MEAS-08)
OLD: `QUICKI's 4.1% reflects its log transform and does not make it more informative. HOMA-IR, QUICKI and FIRI are monotone transforms of one another (PMID 29940866).`
NEW: `The reading that QUICKI's 4.1% reflects its log transform and does not make it more informative is the project's inference; PMID 29940866 does not discuss within-person CV. HOMA-IR, QUICKI and FIRI (fasting-based indices) are one-to-one monotone transforms of one another, so rank-based statistics are identical (PMID 29940866, DOI 10.1186/s12874-018-0521-y, full text; simulation, not clinical data).`

8. FT7-8 (line 50; claims MEAS-19)
OLD: `Isokuortti, PMID 28660493, DOI not recorded in the files; 25%, ten samples, seven labs`
NEW: `Isokuortti 2017, PMID 28660493, DOI 10.1007/s00125-017-4340-1; 25%, ten samples, seven labs`

9. FT8-1 (line 65; claims TRI-14)
OLD: `PLIS (PMID 34531293): a multi-component phenotype (secretion, sensitivity, liver fat), so it tests different contrasts and is not evidence of care guided by a fasting insulin or HOMA-IR measurement.`
NEW: `PLIS (PMID 34531293, DOI 10.2337/db21-0526; full text of the medRxiv preprint, not checked against the published Diabetes version): participants were stratified into high and low risk by a multi-component phenotype from a 75 g OGTT with insulin (post-load: insulin sensitivity, insulin secretion) plus MRS liver fat, using cut-offs from an earlier study. In the high-risk group intensified lifestyle intervention lowered post-challenge glucose more than conventional intervention (-0.290 mmol/l, CI -0.544 to -0.036, P = 0.025); in the low-risk group conventional intervention was not superior to control. No arm compared stratified with unstratified care, so it tests different contrasts and is not evidence of care guided by a fasting insulin or HOMA-IR measurement or of the added value of stratification.`

10. FT8-2 (line 51; claims MEAS-21)
OLD: `LAMP excluded insulin users for this reason.`
NEW: `LAMP excluded patients who had received insulin in the week before the event because exogenous insulin affects fasting insulin and HOMA-IR (fasting-based; the LAMP paper does not mention analogue cross-reactivity or C-peptide).`

11. FT8-3 (line 90; claims TRI-39)
OLD: `Analysis was 510 of 636: 114 excluded for insulin use in the preceding week and 12 for missing glucose or insulin.`
NEW: `Analysis was 510 patients with complete fasting insulin and glucose, out of 522 who had not received insulin in the week before the event (the trial total of 636, 114 insulin exclusions and 12 missing values are not stated in the main text and need a supplement or main-paper check).`

12. FT8-4 (line 91; claims TRI-42)
OLD: `**ODYSSEY OUTCOMES** (PMID 42291078, 11,837 patients): the abstract says sdLDL-C and LDL-C relationships with MACE were similar in patients with greater or lesser insulin resistance, and the treatment effect did not vary by LDL-C or sdLDL-C. It is not a treatment-by-IR test and, if anything, leans toward no IR modification.`
NEW: `**ODYSSEY OUTCOMES** (PMID 42291078, DOI 10.1016/j.ajpc.2026.101643, full text; 11,837 patients, 62.6% of the trial cohort; industry funded, exploratory): in the placebo group, fasting HOMA-IR was split at the median (3.31) and the sdLDL-C and LDL-C splines against MACE were similar in both halves; the alirocumab effect was tested across sdLDL-C and LDL-C (no variation) but not by HOMA-IR. It is a prognostic comparison of two lipid measures, not a treatment-by-IR test, and says nothing for or against IR modification of alirocumab benefit.`
(The claims.csv TRI-42 text is the same sentence with the same OLD string.)

13a. FT8-5 (line 51; claims MEAS-22)
OLD: `(n = 9 per group; PMID 8077319, DOI 10.1210/jcem.77.5.8077319, abstract)`
NEW: `(n = 9 per group; stimulated iv glucose tolerance test with C-peptide deconvolution and minimal model, not a fasting measure, so clearance is calculated rather than measured; PMID 8077319, DOI 10.1210/jcem.77.5.8077319, full text, PDF partly garbled)`

13b. FT8-5 (line 51; claims MEAS-23)
OLD: `measured insulin clearance was reported unchanged and the authors attribute the rise to less insulin reaching the liver through the shunt (n = 11; PMID 20489042, DOI 10.1152/ajpgi.00375.2009, abstract)`
NEW: `OGTT insulin AUC rose 53%, clamp-calculated insulin clearance was reported unchanged, and the authors suggest the rise reflects less insulin reaching the liver through the shunt (n = 11, uncontrolled before-after study at 6 months; PMID 20489042, DOI 10.1152/ajpgi.00375.2009, full text)`

14a. FT8-6 (line 51; claims MEAS-24)
OLD: `(n = 37; PMID 27150853, DOI 10.2169/internalmedicine.55.5288, abstract)`
NEW: `(n = 37; the index is the C-peptide-to-insulin AUC ratio over a 75 g OGTT, a surrogate rather than a measured clearance; the same direction in 74 hepatitis C patients; HOMA-IR is not reported in the text read; PMID 27150853, DOI 10.2169/internalmedicine.55.5288, full text, PDF partly garbled)`

14b. FT8-6 (line 51; claims MEAS-25)
OLD: `neither correlated with eGFR (PMID 26823551, DOI 10.1681/ASN.2015070756, abstract).`
NEW: `neither correlated with eGFR; the adjusted difference in clearance was -85 mL/min (95% CI -160 to -10), and clearance tracked insulin sensitivity and lean mass; people with diabetes were excluded (PMID 26823551, DOI 10.1681/ASN.2015070756, full text).`

14c. FT8-6 (line 51; claims MEAS-26)
OLD: `So in advanced liver disease or CKD a high fasting insulin or HOMA-IR mixes reduced clearance with reduced sensitivity, and the IRIS, MAFLD and JDS cutoffs were not derived in these groups.`
NEW: `It is plausible, but not shown by these studies, that in compensated cirrhosis, in liver fibrosis and in nondiabetic CKD a high fasting insulin or HOMA-IR (fasting-based) mixes reduced clearance with reduced sensitivity; the evidence is small studies of stimulated, post-load or clamp indices, and the IRIS, MAFLD and JDS cutoffs were not derived in these groups.`
(EV-42 claim text says "may be a second reason" and is already hedged; no edit needed.)

15a. FT8-7 (line 91; claims TRI-40)
OLD: `Finerenone's effect did not differ by eGDR category (interaction P = 0.64).`
NEW: `Finerenone's effect did not differ by eGDR category (interaction P = 0.64); an exploratory race interaction for the primary outcome (P 0.012) was also reported, and the eGDR-outcome association differed between people with and without diabetes at P interaction 0.06.`

15b. FT8-7 (line 91; claims TRI-40)
OLD: `(PMID 40916719, DOI 10.1002/ejhf.70034, abstract)`
NEW: `(PMID 40916719, DOI 10.1002/ejhf.70034, full text, PDF partly garbled)`

15c. FT8-7 (line 91; claims TRI-41)
OLD: `(PMID 38151465, DOI 10.2337/dc23-1420, abstract; type 2 diabetes with CKD, n = 12,964)`
NEW: `(PMID 38151465, DOI 10.2337/dc23-1420, full text; type 2 diabetes with CKD, 12,964 of 13,026 in the full analysis set split at the median eGDR)`

15d. FT8-7 (line 91; claims TRI-41)
OLD: `and finerenone's effect did not differ by eGDR (cardiovascular P interaction 0.23, kidney 0.28).`
NEW: `and finerenone's effect did not differ significantly by eGDR (cardiovascular P interaction 0.23, kidney 0.28), although the cardiovascular hazard ratio was 0.81 (0.72-0.92) below the median and 0.92 (0.79-1.06) at or above it, and the continuous interaction was P = 0.063, which the authors call near significance; the analysis was hypothesis-generating, not powered for interaction, and Bayer-sponsored.`

Not applied (no change needed or not supported): C003 (confirms MEAS-29 as written); the "unadjusted" remark about LAMP (contradicted by the paper); changing "prespecified" in merged-conclusion.md lines 2 and 132 and claims TRI-01 and ABS-21 is left to the main session (same caveat as item 2).
