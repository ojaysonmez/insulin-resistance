# FT8 full-text review (9 papers)

Full-text reader report. Detail, quotes and numbers are in `usecases/scoring/ft-review/FT8.json`. No use-case score changes are proposed.

## Per paper

- **C073 PLIS (PMID 34531293): adds nuance.** The local text is the medRxiv preprint, not the Diabetes paper. Stratification used OGTT insulin (Matsuda index, insulinogenic and disposition indices) plus MRS liver fat, so it is post-load insulin, not fasting. The project line (not evidence for care guided by fasting insulin or HOMA-IR) holds, but it should say what the stratifier was. No arm tests stratified against unstratified care.
- **C131 LAMP (PMID 42145088): adds nuance.** All interaction numbers match (P 0.02; spline 0.07 and nonlinear 0.02; HR 0.30 vs 1.22; control 18.1% vs 9.5%). The counts 636 and 114 are not in the main text (522 after insulin exclusion, 510 complete). The insulin exclusion was for fasting insulin and HOMA-IR; analogue cross-reactivity and C-peptide are not mentioned. Authors call it hypothesis-generating.
- **C133 ODYSSEY OUTCOMES (PMID 42291078): adds nuance.** The IR measure is fasting HOMA-IR split at the median (3.31), used only to compare sdLDL-C and LDL-C splines in the placebo group. Alirocumab effect was not tested by HOMA-IR, so "leans toward no IR modification" has no analysis behind it.
- **C144 cirrhosis (PMID 8077319): confirms.** Clearance 725 vs 1165, sensitivity 2.82 vs 5.86, r=0.75 with shunt. Stimulated iv glucose test with C-peptide deconvolution, not a fasting measure. Text partly garbled.
- **C147 TIPS (PMID 20489042): adds nuance.** Numbers confirmed. Uncontrolled before-after study (n=11, clamp n=10, 6 months); the unchanged clearance was the clamp steady-state value, while the authors read the C-peptide:insulin ratio fall as reduced clearance and only suggest the shunt explanation.
- **C160 CKD (PMID 26823551): adds nuance.** Numbers confirmed. The clearance gap is modest (adjusted -85 mL/min), follows sensitivity and lean mass rather than eGFR, and people with diabetes were excluded. Fasting insulin was higher in CKD (10.1 vs 7.3). That fasting indices are biased in CKD is the authors' premise, not a finding.
- **C161 NAFLD/HCV (PMID 27150853): confirms.** The index is the OGTT C-peptide:insulin AUC ratio (0.135 vs 0.098, P=0.013 in NAFLD; same direction in 74 HCV patients). HOMA-beta, not HOMA-IR, is reported. Text partly garbled.
- **C177 FIDELITY (PMID 38151465): adds nuance.** Numbers confirmed (12,964 is the eGDR-split total of 13,026). CV HR 0.81 vs 0.92 by eGDR half, continuous P=0.063 described as near significance, underpowered, Bayer-sponsored. "Null" should be softened to "no significant interaction".
- **C185 FINEARTS-HF (PMID 40916719): confirms.** aRR 1.63 and P interaction 0.64 match. Exploratory race interaction (P 0.012) and diabetes-status interaction (P 0.06) are not mentioned in the project text. Text partly garbled.

## Claim issues (proposed wording in the JSON)

1. merged-conclusion.md line 65, PLIS (TRI-14): state the OGTT insulin and liver fat stratifier and the preprint caveat.
2. Line 51, MEAS-21: LAMP excluded recent insulin therapy to protect fasting insulin and HOMA-IR; analogue cross-reactivity is not in the paper.
3. Line 90, LAMP (TRI-39): counts 636 and 114 not in the main text.
4. Line 91, ODYSSEY (TRI-42): replace "leans toward no IR modification" with a statement that treatment effect was not tested by HOMA-IR.
5. Line 51, MEAS-22 and MEAS-23: add method labels and the before-after, uncontrolled design of the TIPS study.
6. Line 51, MEAS-24 to MEAS-26 and EV-42: the summary sentence reaches beyond the papers (no HOMA-IR result in C161; modest CKD clearance gap; bias in fasting indices is an authors' premise).
7. Line 91, TRI-40, TRI-41 and ABS-16: soften "null" and add the HR split, continuous P 0.063, sponsorship and exploratory interactions.

Confidence: the full texts lower confidence slightly in the cirrhosis/CKD summary sentence and the ODYSSEY phrase, and leave the trial numbers unchanged.

Tool calls used: 25.
