# Clinical chemist report: can an insulin, C-peptide or derived-index result support an individual clinical decision?

Role: ir-clinical-chemist (independent run; no prior ir-team files read). Coverage and reimbursement out of scope.
Date: 2026-10-18. Tools: PubMed (E-utilities via MCP), Consensus. Crossref was not queried directly; DOIs come from PubMed records.
Evidence level for every source: abstract read in the PubMed record. I did not read full text of any source. All numbers below are from abstracts. Where I derive a number myself it is labelled "derived".

## 1. Bottom line

1. Single-value fasting insulin, HOMA-IR and the lipid-based indices cannot reliably classify an individual as "insulin resistant" or track change in an individual over weeks to months. Within-person variation alone (about 25-30 % CV for insulin and HOMA-IR) is too large for a fixed cutoff to be stable.
2. Between-assay disagreement in insulin is large and unresolved. All 12 commercial immunoassays tested claim traceability to WHO 66/304, yet differ from an isotope-dilution MS reference by -298 to +303 pmol/L (PMID 40802520). A HOMA-IR cutoff is tied to the insulin assay it was derived on and does not transfer without verification.
3. C-peptide has about the same within-person CV as insulin (24 %) and a similar index of individuality (0.9; Widjaja 1999, n=12, young, RIA era). It offers no advantage for single-value IR classification, and its harmonization is also incomplete.
4. TG/HDL-C and TyG avoid the insulin assay, which is their main analytical advantage. TG/HDL-C was the most repeatable common index in the one study found (within-person CV 23 %, ICC 0.80). Their cutoffs are no better standardised than HOMA-IR cutoffs.
5. Single values can support: group-level comparisons, flagrant outliers far beyond analytical bias plus RCV, and trend only when repeat samples and RCV are respected. They cannot support: a binary IR diagnosis, a treatment-response call from one before/after pair, or use of a published cutoff on an unmatched assay.

## 2. Measure-by-measure table

| Measure | Analytical performance | Within-person biological variation | Repeatability / RCV | Source |
|---|---|---|---|---|
| Fasting insulin (12 commercial immunoassays vs ID-MS) | Intra-assay ICC >0.99, but inter-assay difference vs ID-MS from -298.2 to +302.6 pmol/L; several assays overestimate at low and underestimate at high concentrations; only 1 of 12 in full agreement with ID-MS (40 samples, 9 manufacturers) | n/a | n/a | PMID 40802520, DOI 10.1515/cclm-2025-0552 |
| Fasting insulin (7 kits) | Relative SD between kits 1.7-23.2 %; traceability chains and unit conversion factors not harmonized; reference materials not matrix-applicable | n/a | n/a | PMID 35622611, DOI 10.1002/jcla.24521 |
| Fasting insulin | n/a | CVI 26 % (12 healthy young adults, 12 consecutive days, RIA); individuality index 1.0 | Derived RCV = 2.77 x 26 = about 72 % (CVA ignored) | PMID 10102917 (Widjaja 1999; no DOI in record) |
| Insulin, harmonization status | Serum pools commutable among most of 6 immunoassays; lyophilised EQA samples non-commutable among most; recalibration with pools improved agreement at middle/high but not low insulin | n/a | n/a | PMID 36750430, DOI 10.1177/00045632231159291 |
| Insulin by antibody-free LC-MS/MS | Verification CV 2.7-3.7 %; median imprecision across 3 laboratories on clinical samples 22.2 % (IQR 20.9 %) single, 15.3 % (IQR 14.9 %) when replicates averaged; LLMI 0.03 ng/mL | n/a | n/a | PMID 38549041, DOI 10.1093/clinchem/hvae034 |
| Insulin candidate reference method | ID-LC-MS/MS after immunoaffinity extraction; imprecision <2.77 %; expanded uncertainty <=3.5 %; insulin analogues did not interfere; authors attribute immunoassay inconsistency mainly to antibody cross-reactivity | n/a | n/a | PMID 40353876, DOI 10.1007/s00216-025-05900-5 (manufacturer-affiliated authors) |
| C-peptide | LC-MS/MS inter-lab median imprecision 13.4 % (IQR 11.6 %) single, 10.8 % averaged; method comparison to Missouri reference method slope 1.044, r2 0.99. Current EQA materials commutable on only a few of 6 immunoassays; WHO ISR 13/146-derived materials non-commutable on over half | CVI 24 %, individuality index 0.9 (same n=12 study) | Derived RCV = 2.77 x 24 = about 67 % | PMID 38549041; PMID 37141618, DOI 10.1515/cclm-2023-0215; PMID 10102917 |
| HOMA-IR | Inherits insulin assay error plus glucose. In a three-assay substudy, "unsatisfactory correlation" and systematic differences in calculated HOMA-IR | CVI 26.7 % (95 % CI 25.5-28.3), EuBIVAS, 90 non-diabetic adults, 10 weekly samples; no difference by sex or by age below/above 50 | Derived RCV = 2.77 x 26.7 = about 74 % (about 79 % if CVA 10 %). ARIC (n=102, adults 68-88 y, mean 46 days apart): ICC 0.70, within-person CV 30.4 %, MDC95 2.3 HOMA-IR units | PMID 38987271, DOI 10.1515/cclm-2024-0672; PMID 29618016, DOI 10.1210/jc.2017-02437; PMID 34380182, DOI 10.1515/cclm-2021-0643 |
| HOMA-IR in type 2 diabetes | n/a | Mean intra-individual variation 1.05 in T2DM vs 0.15 in controls (HOMA-IR units; 12 vs 11 postmenopausal women, 10 samples each 4 days apart) | Authors: a repeat must rise >90 % or fall >47 % to differ significantly | PMID 12401750, DOI 10.2337/diacare.25.11.2022 (2002, small, older assay) |
| QUICKI | Same insulin dependence; log transform damps error | CVI 4.1 % (95 % CI 3.9-4.3) | Derived RCV about 11 %. The low percentage reflects the compressed log scale, so it is not equivalent to a small change in sensitivity | PMID 38987271 |
| Fasting glucose (component) | n/a | CVI 4.8 % (Widjaja); within-person CV 5.6 % (ARIC) | n/a | PMID 10102917; PMID 29618016 |
| TG/HDL-C | No insulin assay; lipid methods not separately assessed | Within-person CV 23.0 % (TG 20.6 %, HDL-C 8.2 %); ICC 0.80 | MDC95 1.4 TG/HDL-C units | PMID 29618016 |
| TyG | Not assessed analytically | No true biological variation study found | Not derivable | see section 7 (Consensus-surfaced only) |
| Matsuda / OGTT indices | Insulin assay dependent; no inter-lab study retrieved | OGIS 7.8 % and Stumvoll ISI 14.4 % CV over 4 consecutive days (small trial, Consensus abstract only) | Not derivable | see section 7 (Consensus-surfaced only) |

RCV = 2^0.5 x 1.96 x sqrt(CVA^2 + CVI^2), approximated as 2.77 x CVI when CVA is omitted. The EuBIVAS paper lists reference change values among its keywords, but the specific values were not in the abstract, so mine are derived and should be checked against the full text. For log-normal data an asymmetric RCV applies, consistent with the +90 % / -47 % in PMID 12401750.

## 3. What single-value use can and cannot support

Can support:
- Group-level comparisons and trials with many participants. The ARIC authors give a minimum detectable difference of 0.8 HOMA-IR units for n=100 (PMID 29618016).
- Recognising values far outside both inter-assay bias (hundreds of pmol/L at some concentrations) and the RCV.
- A repeat-sample strategy. Replicates reduce analytical error (LC-MS/MS inter-lab CV 22.2 % to 15.3 % with replicates, PMID 38549041); samples on different days are needed to reduce biological variation.

Cannot support:
- Classifying an individual as insulin resistant or not at a cutoff. With CVI about 27 %, a person whose true HOMA-IR is near a cutoff will often cross it on repeat testing (qualitative inference from the CV; I found no study that quantifies cutoff crossing, see gaps).
- Detecting an individual change of less than about 70-80 % (insulin, HOMA-IR) from two samples; about 11 % for QUICKI with the caveat above.
- Applying a cutoff built on one insulin assay to another assay or laboratory without verification.
- Treating HOMA-IR, QUICKI and FIRI as independent confirmations: they are one-to-one transformations of each other (PMID 29940866, DOI 10.1186/s12874-018-0521-y).
- Extending 2002 T2DM variance data to current platforms.

## 4. Pre-analytical and interference issues

- Haemolysis: insulin-degrading enzyme released from erythrocytes lowers insulin in serum. On a Roche Cobas e801, median haemolysis index 51 already gave a 14.1 % decrease (desirable bias 10.5 %); at HI 1022 the fall was 90.8 %. FC-Mix plasma stayed within -0.3 to -1.8 % (PMID 41371327, DOI 10.1016/j.cca.2025.120773; single-author, one analyser).
- Sample type and delay: in 8 analysable healthy volunteers, uncentrifuged serum at room temperature fell to 51 % (C-peptide) and 62 % (insulin) of baseline within 24 h, while K2EDTA plasma stayed above 90 % (PMID 40587435, DOI 10.1371/journal.pone.0312065; non-fasted, tiny n). Direction is consistent with the haemolysis work; magnitudes are imprecise.
- Cross-reactivity with analogues: immunoassays fall into three groups (detect all insulins; human only; analogues in variable proportions) (PMID 37598742, DOI 10.1016/j.cca.2023.117516). A Siemens Atellica study found 92-121 % analogue recovery, whereas LC-MS/MS detected only glargine (PMID 39030378, DOI 10.1007/s12020-024-03970-6). A review summarises adsorption, degradation and cross-reactivity pitfalls (PMID 40827462, DOI 10.1080/10408363.2025.2528877; abstract only). Relevance to IR: in patients on insulin therapy, "endogenous" insulin results are not comparable across assays.
- Proinsulin cross-reactivity: I did not retrieve a verified source with assay-specific percentages for current platforms. Gap.
- Fasting requirement: not examined in a retrieved source. The BV studies used overnight fasted samples, so their CVI applies to that protocol.

## 5. Cutoff and reference-interval problems

1. Assay dependence. In the Gutenberg Health Study (10,340 participants with data) the most stringent reference group (n=1,065) had median HOMA-IR 1.09 and 97.5th percentile 2.35, for one specific insulin immunoassay. A three-assay substudy showed systematic differences, and the authors conclude assay-specific reference intervals are required (PMID 34380182). This is the clearest direct evidence on HOMA-IR cutoff portability.
2. Population and covariates. A narrative review reports high variability in HOMA-IR and TyG thresholds and dependence on age, sex and race (PMID 35939943, DOI 10.1016/j.dsx.2022.102581). A Leipzig study built age- and puberty-specific reference ranges from 6,994 observations in 5,512 non-obese people aged 5-80 y, with strong age dependence across the life span (PMID 37465325, DOI 10.1016/j.lanepe.2023.100652). A single adult cutoff is therefore not transferable to children; ethnic and BMI effects are asserted by the review, not quantified here.
3. Derivation. Cutoffs come either from percentiles of a healthy cohort (reference limits) or from ROC against a clamp, metabolic syndrome or outcome. These are different constructs. The Gutenberg 97.5th percentile (2.35) is a reference limit, not a diagnostic threshold. Prognostic association in children (HR 1.88 for dysglycaemia, PMID 37465325) does not establish individual diagnostic accuracy.
4. Index of individuality about 1.0 for insulin and C-peptide (PMID 10102917) is in the zone where population reference intervals are of limited use for judging an individual. That study is small, young and RIA-based. For HOMA-IR I did not confirm CVG or an individuality index from the EuBIVAS abstract.
5. External validation across assays: none retrieved. No source re-derives or validates a HOMA-IR cutoff on an LC-MS/MS or WHO-harmonized scale.
6. Methodology: correlation with the clamp is not sufficient; repeatability, reproducibility, systematic bias and discrimination should also be assessed (PMID 29940866).

## 6. Figures that may not apply to current platforms

- Widjaja 1999 (insulin, C-peptide CVI): RIA, 12 healthy young adults. Older generation; rough comparator only.
- Jayagopal 2002 (HOMA-IR in T2DM): 23 postmenopausal women, 2002 assay.
- ARIC repeatability: adults 68-88 y without diabetes; assay generation not stated in the abstract.
- EuBIVAS 2024 is the best BV source but covers non-diabetic adults; BV in obesity, PCOS, children, prediabetes or on glucose-lowering drugs was not retrieved.
- Inter-assay comparisons (2022, 2025) are current-generation and are the strongest evidence on analytical comparability.

## 7. Verification log and source quality

Verified in PubMed record (title, PMID, abstract read; DOI as listed): 38549041, 36750430, 37141618, 38987271, 40802520, 35622611, 12401750, 37465325, 29618016, 29940866, 40827462, 40353876, 39030378, 37598742, 41371327, 35939943, 40587435, 34380182 (DOI from esummary), 10102917 (no DOI in record).

Surfaced by Consensus only, not verified in PubMed or Crossref, and not relied on for conclusions: Gordon 2011 OGTT reproducibility (Diabetes Res Clin Pract), Kostopoulou 2021 OGTT repetitiveness (World J Clin Pediatr), Xie 2026 TyG stability (Sci Rep), Li 2022 TyG variability and CVD (Cardiovasc Diabetol), Rodriguez-Garcia 2026 IDE inhibitor (Diagnostics), Jones 2019 and Roys 2024 RCV-from-database methods (Clin Chem), Albayaty 2026 Iraq HOMA-IR (Ann Clin Biochem).

Strongest sources:
- Rohlfing 2025 (PMID 40802520): 12 commercial assays vs IDMS, direct measure of the problem. Limit: 40 samples.
- Carobene 2024 EuBIVAS (PMID 38987271): rigorous protocol, 90 subjects, 10 weekly samples. Limit: abstract lacks RCV and CVG; non-diabetic only.
- Matli 2021 (PMID 34380182): large cohort with a cross-assay substudy. Limit: single German centre, one assay for the reference interval.
- Poon 2018 ARIC (PMID 29618016): real-world repeatability with MDC95, covers TG/HDL-C. Limit: older adults, n=102.
- Moradian 2024 (PMID 38549041): inter-lab MS data. Limit: three research laboratories.

Weakest sources:
- Widjaja 1999 (n=12, RIA) and Jayagopal 2002 (n=23): small and old, yet the only BV figures for C-peptide and for T2DM.
- Mubiru 2025 (n=8 analysable, non-fasted) and Ercan 2025 (single author, one analyser).
- Tahapary 2022: narrative review.
- Liu 2025 cRMP: manufacturer-affiliated.

## 8. Open gaps

1. No EFLM Biological Variation Database entry or BIVAC grade retrieved for insulin, C-peptide, glucose, TG or HDL-C. Pull these before quoting RCVs in any deliverable.
2. No study quantifying how often a person crosses an IR cutoff on repeat testing. A biostatistician can compute it from CVI 26.7 %, log-normal shape and a candidate cutoff.
3. EuBIVAS full text needed for CVA, CVG, individuality index and published RCVs for HOMA-IR.
4. No verified biological-variation data for TyG, or for Matsuda/OGTT-derived sensitivity, in PubMed.
5. No current-platform proinsulin cross-reactivity data; no C-peptide immunoassay inter-assay comparison against the reference method beyond the 2023 commutability study.
6. No external validation of HOMA-IR cutoffs across assays, ethnicities or BMI classes.
7. CVI for insulin and HOMA-IR in obesity, PCOS, prediabetes, T2DM and children on current assays is unquantified; only the 2002 T2DM study exists.
8. Fasting duration, posture, recent exercise and seasonal effects were not examined.
9. Crossref was not queried directly; DOIs were verified through PubMed records only.
