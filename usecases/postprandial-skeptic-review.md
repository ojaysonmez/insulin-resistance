# Skeptic review: revised postprandial rows D1-D6

Reviewer: skeptic subagent, 2026-10-19. File reviewed: `usecases/postprandial-additions-revised.md`. Context read: `usecases-verified.md` rows 4, 5, 6, 9, 18, 23, 24, 27, 30, 31 (first columns only). I did not read the scout draft, the full-text check or the candidates file; every figure below was re-checked by me against the source with the project helpers (`tools/pmc_text.py`, `tools/watch_fetch.py`, `tools/check_citations.py`). Tool calls used: 9 (of 30 allowed). Citation report: `scratch/skeptic-citations.md`.

## Summary of verdicts

| Row | Verdict | One-line reason |
|---|---|---|
| D1 | Accept with edits | Research-only is right; one factual error about where the insulin phenotype comes from (IVGTT, not the meal test); Cryer 2009 is unread |
| D2 | Accept with edits (limited) | phi-total claim correct only for the multivariable model; the "8-fold" note is wrong arithmetic in the paper; Index60 description needs the derivation detail |
| D3 | Accept as research-only, with edits | Numbers match the abstracts; the row's use-case content is thin and one cited paper is not a post-load-insulin study of the stated design |
| D4 | Reject as a use-case row | The preoperative predictors are glucose-based; no decision is supported by an insulin or C-peptide test. Keep as a caveat on row 9 or a negative entry |
| D5 | Accept with edits, or fold into rows 6 and 31 | Numbers traced except one; it mostly duplicates existing rows |
| D6 | Accept as research-only, with edits | Numbers match the abstract; test is a drug-trial endpoint |

## Citation check (point e)

Command: `python tools/check_citations.py usecases/postprandial-additions-revised.md --refresh --out scratch/skeptic-citations.md`.
- PMID 24408401 (DOI 10.2337/dc13-1392): PubMed marks it a RETRACTED PUBLICATION and Crossref has a retraction notice (10.2337/dc15-rt01a). It appears only in the "Not part of the rows" section as a do-not-cite note. It is not cited in any row. Required: keep it out of any merged row and out of any reference list; if the note is carried into `usecases-verified.md`, state that it is retracted.
- "DOI 10.1016/s2213-8587(25" flagged as not found in Crossref: this is a checker parsing artefact. The DOI in D3 is `10.1016/s2213-8587(25)00163-9`; the checker cut it at the closing bracket. PubMed (via `watch_fetch.py`) returned PMID 40812331 with exactly that DOI. No defect. The same applies to D5 `10.1002/14651858.cd006165.pub3`, which the PubMed record confirms.
- ADA Standards 2026 (PMID 41358893): the row gives the PMCID but not the DOI. Fill: 10.2337/dc26-s002 (suggested by the checker from PubMed). Required edit in D2.
- Spot-checked records match (Cryer 2009 PMID 19088155; Insel 2015 PMID 26404926; ADA 2026 PMID 41358893). No corrections or retractions found for the other PMIDs or DOIs in the file. The checker only compared identifiers; it did not check any claim.
- PMID and DOI both present: yes for all cited papers except 36464132's, 21901702's and 40781799's PMIDs/DOIs are present; the D2 ADA entry lacks the DOI (edit above); D5 and D6 case reports are listed by PMID only and are "title only, not read" (acceptable, as they are not relied on).

## Quotes and figures re-verified (more than the 10 required)

1. D2, 35998266 (PMC9643141): "AUC C-peptide increased from baseline until 1.5 years prediagnosis (DPT-1, P = 0.004; TNPTP, P = 0.012) and then decreased from 1.5 to 0.5 years prediagnosis (DPT-1, P = 0.017; TNPTP, P = 0.093)". Matches the row. Note: the 0.093 appears in the abstract for TNPTP.
2. D2: "Median Index60 values of DPT-1 (1.44) and TNPTP (1.05) progressors to T1D 1.5 years prediagnosis ... were used as thresholds to identify individuals at high risk for T1D in the full cohort at baseline (5-year risk of 0.75-0.88 for those above thresholds)". Matches. Full text adds: thresholds applied to baseline OGTTs of TNPTP n = 6,567 and DPT-1 n = 711. Conclusion text: "The median Index60 value at that time point can be used as a pathophysiologic-based threshold".
3. D2, 39992257 (PMC12527456): "φ total was the only one significantly associated with the risk of progression ... (OR 0.92 [0.86, 0.98], P = .016)"; "Other variables, including age, BMI, sex, AUC C-peptide ... did not show significant associations". Table 3: AUC C-peptide OR 0.999 (0.999, 1.000), P = .330; n = 57. Matches the row's claim.
4. D2: the same paper's Results say "progressors exhibited lower insulin secretion metrics, including φ total and AUC C-peptide" (Table S1, univariate), and "DPTRS and Index60 were elevated in the progressor group". So AUC C-peptide differed in the group comparison but not in the multivariable model. The row's "AUC C-peptide was not [associated]" is correct only for the multivariable logistic model (n = 57; 16 progressors, 41 non-progressors). Also AUC C-peptide did not differ between stage 1 and stage 2 (P = .362).
5. D2: the paper's "8-fold reduction" per 10 units of phi-total. An OR of 0.92 per unit compounds to about 0.92^10 = 0.43 (about 2.3-fold lower odds), not 8-fold; Table 3 reports 0.922 (0.863, 0.985). The row says the mismatch "was not resolved"; the arithmetic resolves it as a paper error or a different unit scaling, which the row should say rather than leave open. The Discussion repeats "8 times lower odds".
6. D2: the same paper's limitation "the follow-up of this cohort was relatively short (~19 months), so we likely included only those with a more advanced disease progression, thus limiting the generalizability". Matches "limited generalisability".
7. D2, Insel 2015 (PMC5321245): "At 4 years from the time of a 20% decrease in C-peptide from baseline, there is a 47% risk of symptomatic type 1 diabetes, with a positive predictive value of symptomatic type 1 diabetes within 5 years of 78%". Matches. The passage says "C-peptide", not "stimulated C-peptide"; the row's "stimulated" is an inference I could not confirm from the window I read.
8. D2, ADA Standards 2026 (PMC12690183): "2.6 Screen for presymptomatic type 1 diabetes by testing autoantibodies ..." and "2.7 Autoantibody-based screening ... should be offered to those with a family history ...". Matches "autoantibody screening only".
9. D4, 37889837 (PMC10876401): "33 patients developed diabetes", "74.1% at 36 months", "IGT before surgery (HR 2.650, 95% CI 1.216-5.772, P < .05) ... in Model 1, and the AUCs for glucose ... (HR 1.002, 95% CI 1.001-1.004 ...) in Model 3". Table 3: AUC CPR HR 1.002 (1.000-1.004) NS (Model 1), 1.009 and 1.000 NS in other models. Insulinogenic index 15.2 +/- 1.8 vs 9.1 +/- 0.9 mIU/mmol (P < .01) at 1 month. Abstract: "impaired glucose tolerance as a preoperative factor as well as a decreased insulinogenic index and impaired glucose tolerance at 1 month postoperatively were identified as risk factors". All match the row.
10. D4, 42146813 (PMC13178281): "new-onset DM developed in 14.8% (4/27) and 50.9% (28/55), respectively (p = 0.002)" for CP and DP. The row says the 14.8% was not seen in the full-text windows; it is in the Results text and in the abstract, so the "unverified" flag can be removed. OGTT subgroup 37 (CP 12, DP 25) matches; abstract says IRI AUC (p = 0.010) and CPR AUC (p = 0.022) fell after DP.
11. D1, 33916952 (PMC8067537): abstract "Forty subjects ... Twelve (30%) ... hypoglycemic symptoms and glucose level <=55 mg/dL during five-hour OGTT"; Methods "The cut off glucose value for hypoglycemia during OGTT was set on <=55 mg/dL [18]"; Introduction "lack of standardized biochemical test and lack of glucose cut off value". Matches. MMTT was done in the study group.
12. D1, 41829992 (PMC12986748): abstract "A total of 69 non-diabetic adults ... with obesity ... underwent a 4 h MMTT to define RH, and an intravenous glucose tolerance test (IVGTT) to characterize RH (via insulin sensitivity, the acute insulin response to glucose ..., insulin clearance, and the disposition index)"; "A total of 19 of the 69 participants had a reactive hypoglycemic response". Methods: median decline -1.2 mg/dL/min; RH if post-peak decline <= -1.2 mg/dL/min and early nadir at least 5 mg/dL below fasting glucose (the first of two alternative criteria; the second condition was not shown in my window). The 69 and 19 are therefore confirmed in the abstract; the draft's "unverified" refers only to the full-text windows (19 vs the power calculation of 25 is in the Discussion).
13. D3, 39013634 abstract: "33 articles, encompassing 5362 individuals", "HOMA-beta's pooled correlation to the reference methods was 0.48 (95% CI 0.40 to 0.56)"; HOMA-beta and IGI30 validated in 17 and 13 studies. Abstract truncated after "The pooled correlation of IGI to the". 40812331 abstract (design, ISSI-2 and IGI/FPI as OGTT indices): matches. 39963280 abstract: 9,452 participants, 39.2% of NGT had 1-h PG >= 8.6, "early insulin secretion impairment" similar to I-IFG. Matches.
14. D5: 41752170 (PMC12940418): "C-peptide concentration 6 min after glucagon administration (4.6 ng/mL vs. 1.35 ng/mL, p < 0.001)" for T2DM vs autoimmune group; matches the row's 1.35 and 4.6. The 0.10 ng/mL fasting value at about 7 years was not searched for by me (see untraced list). 25572256 (PMC4297398): 32 LADA, 33 type 1, 30 type 2; "capacity of stimulated C-peptide secretion that is intermediate between types 1 and 2". Matches.
15. D6, 35416981 abstract: "28% (P <= 0.001) and 30% (P = 0.01) increase in AUC of glucose" on MMTT and OPTT; "AUC of insulin was unchanged during the MMTT and almost twofold higher (P = 0.004) during the OPTT"; "a subset of eight subjects". Matches. 26908106 abstract: truncated at about 1,400 characters; the visible text has no protein or leucine test (the row says "visible text", which is correct).

## Row D1: non-surgical reactive hypoglycaemia (post-load OGTT and MMTT)

Verdict: accept with edits.

Status: research-only is correct. Both studies set their own thresholds (55 mg/dL by 33916952; a decline-rate definition by 41829992), 33916952 states the lack of a standardised test and cut-off, and no insulin or C-peptide threshold appears in either. No guideline passage recommending the test for this decision was read, so established is not allowed; limited would need at least a consensus statement, which the row does not have.

Cryer 2009 (PMID 19088155): the row's "NOT read" is accurate. I did not read it either. The citation record is valid (checker spot check). Because it is the main guideline for hypoglycaemic disorders in adults, the row's status of "research-only" rests on an unread document; the correct wording is "research-only on the sources read; the Endocrine Society guideline is unread and might change the status". My recollection is that it discourages OGTT for diagnosing reactive hypoglycaemia [recall, not verified; do not enter as a fact].

Required edits:
1. Row text: "insulin appears as a phenotype (insulin sensitivity, disposition index)" must say that these phenotypes came from an intravenous glucose tolerance test (IVGTT), not from the meal test. The abstract says so explicitly. So the post-meal test in 41829992 is a glucose-only definition; the insulin measure there is IVGTT-based and does not qualify as a post-meal insulin test. Say so under "Test" and "Caveats".
2. Test column: 33916952 collected insulin during the OGTT, but the 12/40 diagnosis rested on glucose <= 55 mg/dL plus symptoms. State that the insulin value was not part of the diagnostic criterion. (The row already says "No insulin threshold found"; make this explicit in the Test column too: "glucose is the diagnostic measure; insulin collected but not used".)
3. Remove "unverified" from the counts 69 and 19 and write "confirmed in the abstract (PubMed); not located in the full-text windows". Add that the study is in healthy adults with obesity aged 21-50, not symptomatic patients.
4. Replace "Research-only (no accepted criteria in the screened records)" with "Research-only (no accepted criteria in the sources read; Cryer 2009 unread)".
5. 36464132 reads at abstract level: it does support the Whipple triad as a first step. Keep as context only.
6. The "[recall, not verified here]" statement about healthy people and OGTT-induced low glucose must be either sourced or deleted before merging.

## Row D2: prognosis in autoantibody-positive relatives

Verdict: accept with edits. Status limited is defensible only because it rests on cohort data plus one descriptive consensus statement; the rule for limited does not require a recommendation. It is not established: neither Insel 2015 nor ADA 2026 recommends the test.

(a) Is "only phi-total, not AUC C-peptide" correct? Yes, for the multivariable logistic model (Table 3, n = 57: phi total OR 0.922 [0.863-0.985], P = .016; AUC C-peptide OR 0.999 [0.999-1.000], P = .330). But the same paper states that progressors had lower AUC C-peptide in the univariate comparison (Table S1), so a reader would be misled by the unqualified statement. The row also needs to say that the progression outcome was to stage 2 or 3 over a median follow-up of 19 +/- 15 months, 16 progressors vs 41 non-progressors, and the cohort size (30 stage 1, 27 stage 2) is small. The row says "n=30 stage 1 and 27 stage 2": confirmed by Table 3 n = 57.

Does the Index60 threshold description match the paper? Mostly. What the paper did: it took the median Index60 among progressors followed longitudinally at 1.5 years before diagnosis (DPT-1: 1.44; TNPTP: 1.05) and applied these as risk thresholds to the baseline OGTT of the full cohorts (TNPTP n = 6,567; DPT-1 n = 711), giving 5-year risk 0.75-0.88 above the threshold. The row's wording "applied as thresholds to the full cohorts" is right but omits: (i) the threshold was derived from the same cohorts it was then tested in (the paper's conclusion calls it validated in "two independent cohorts" for the inflection, but the risk estimate for the thresholds is not an external validation); (ii) the thresholds are cohort-specific (1.44 vs 1.05) and not one transferable cut-off; (iii) the fall in AUC C-peptide in TNPTP was not significant (the row has this).

Required edits:
1. Write: "In the multivariable model (n = 57) only phi-total was associated with progression; in the univariate comparison progressors also had lower AUC C-peptide (Table S1 of that paper, not read)". The supplement was not read.
2. Replace "the text's '8-fold reduction' per 10 units does not match that odds ratio and was not resolved" with: "The paper's '8-fold lower odds per 10 units' is inconsistent with its own OR of 0.92 per unit (0.92^10 is about 0.43, roughly 2.3-fold); do not quote the 8-fold figure."
3. Add "full cohorts n = 6,567 (TrialNet) and n = 711 (DPT-1); thresholds are cohort-specific medians derived in progressors, not independent external validation".
4. Insel "stimulated C-peptide decline": the passage I read says "C-peptide"; remove "stimulated" or cite the exact sentence in which the statement uses OGTT.
5. Add DOI 10.2337/dc26-s002 for PMID 41358893.
6. 42684379 is abstract-only; the abstract says "Data-driven cutoffs ... identified small subsets at very high risk (>50% 2-year progression)". The row's summary "most consistently associated" is a fair paraphrase of "strong and consistent associations"; keep as abstract-level support and add that the cut-offs are data-driven (derived in the same data).
7. Name the measure type: post-load OGTT glucose plus C-peptide (the minimal model also uses insulin for sensitivity, per the paper's Methods). The row says "C-peptide, not insulin"; correct that to "C-peptide for secretion; insulin only for the minimal-model sensitivity estimate".

Overlap: row 30 (teplizumab selection is by autoantibodies and OGTT dysglycaemia; the table lists staging as "unsupported for selection and staging") is a different decision. Not a duplicate, but the row must stay consistent with row 30: keep "prognosis and monitoring intensity only".

## Row D3: post-load insulin indices, first-phase secretion, prediabetes remission

Verdict: accept as research-only, with edits.

Numbers match the abstracts (see item 13). Status check: no guideline passage; abstract-only evidence cannot exceed limited, and the row itself says no decision is supported, so research-only is correct. Measure type: mixed. HOMA-beta is fasting-based and 39013634 covers fasting, OGTT and meal-test surrogates; 40812331 uses OGTT-derived ISSI-2 and IGI/FPI; 39963280 uses OGTT-derived IGI30 and oral DI. The row names these correctly.

Required edits:
1. 40812331 is a prospective cohort in postpartum women (after pregnancy screening for gestational diabetes), not a general adult population. The row title says "Adults with normal glucose, prediabetes or early T2D". Add "postpartum women with prediabetes" for this study. The abstract also shows the study's design and conclusion title ("central role of recovery of beta-cell function"), but the abstract I read was truncated before the effect sizes; do not report any result from it.
2. 39963280 is described in the row as "cross-sectional or retrospective" in the caveats; the abstract says "retrospective study". Fine. Add the exact endpoint (1-h PG >= 8.6 mmol/L) and that it is not a treatment decision.
3. "The main T10 hit 42892651 was not read": remove the internal pointer or state its PMID/DOI status; it is an uncited hit and has no place in the row.
4. Overlap with row 18 (research-only IR endpoints, HOMA-IR, clamp, OGTT insulin): D3 is largely a new citation set for the same research-only category. Recommendation: merge into row 18 as additional abstract-level citations, or keep as a separate row only if the main session wants a beta-cell-function row. State this overlap in the verdict.
5. The IGI pooled correlation in 39013634 is truncated in the abstract I obtained; the row correctly says it was not read. Keep.

## Row D4: distal pancreatectomy, preoperative OGTT insulin or C-peptide

Verdict: reject as a use-case row for an insulin and C-peptide list. (b) The revised wording is supported; the conclusion should go further.

Evidence: In 37889837 the preoperative risk factors in the multivariable Cox models were IGT (HR 2.650) and OGTT glucose AUC (HR 1.002). The preoperative AUC CPR hazard ratios in Table 3 were not significant (NS in all three models: 1.002, 1.009, 1.000). The insulinogenic index and IGT at 1 month postoperatively were the risk factors involving insulin, and those are postoperative measures. The paper's introduction says a decrease in the preoperative insulinogenic index predicted diabetes after pancreaticoduodenectomy (PD), not after distal pancreatectomy (DP); the DP finding is absent. In 42146813 the insulin and C-peptide AUC fall after DP is a post-surgical group change, and CP versus DP is chosen on tumour location and not on any OGTT insulin result. The 14.8% vs 50.9% difference concerns the operation, not the test.

So the row's "Decision informed" (counselling; surgical choice) is not supported for insulin or C-peptide. The test that does inform counselling is the glucose-based OGTT or HbA1c, which is outside this list. Keeping a "Research-only" row would advertise an insulin or C-peptide use that the sources do not show. The row also says "Prognostic", but the insulin measure predicts nothing before surgery in these data.

Required action: do not add D4 as a numbered row. Optional: add one sentence to row 9 or row 27 (or to a negative-entry list) saying "OGTT insulin or C-peptide before distal pancreatectomy: no preoperative predictive value shown in 37889837 (preoperative AUC CPR not significant); predictors were glucose-based; 42146813 describes postoperative falls only", citing both papers with their PMIDs and DOIs. If the main session keeps the row anyway, it must: (1) state the status as research-only/negative, (2) delete the "counselling" and "surgical choice" decisions, (3) change "Kind" from Prognostic to Descriptive, (4) remove the "unverified" flag on 14.8% (confirmed), and (5) add that the abstract's postoperative insulinogenic-index finding cannot guide the operation.

## Row D5: LADA and newly diagnosed diabetes, stimulated C-peptide

Verdict: accept with edits, or fold into rows 6 and 31.

Traced: 32/33/30 and "intermediate" (25572256); 1.35 vs 4.6 ng/mL after glucagon (41752170). Status research-only for treatment choice is right: no cut-off for selecting treatment appears, and the Cochrane abstract (all studies high risk of bias) lists no C-peptide-guided arm in the portion I read (truncated).

Required edits:
1. In 41752170 the 4.6 vs 1.35 comparison is T2DM vs the autoimmune-diabetes group (LADA pooled with T1D in the main comparison, as the Introduction says). The row says "type 1 group against 4.6 in type 2" which is acceptable; add "LADA pooled with type 1" next to the number so a reader does not read 1.35 as a LADA value. The row already states this later; move it up.
2. The fasting C-peptide "0.10 ng/mL at about 7 years" was not traced by me (not searched). Mark it untraced or re-check it before merging.
3. 41752170 is a single cohort; 25572256 is cross-sectional with 95 subjects. State "single-centre, cross-sectional" so that the claim "supports row 6 and row 31" is not read as stronger than those rows (row 6 and row 31 are established on the Holt 2021 consensus).
4. Overlap: rows 6 and 31 already cover C-peptide for classification (random C-peptide with concurrent glucose). D5's additional content is the stimulated (MMTT and glucagon) variants. State this, and consider listing the two papers as extra citations in row 6 rather than a new row.
5. 40781799: the abstract says the ADA/EASD cut-offs are "<0.2 nmol/L ... type 1" and ">0.6 nmol/L ... type 2" (second-hand; the row's "remain second-hand" is correct; do not enter these numbers without the primary source, Holt 2021).

## Row D6: oral protein tolerance test in congenital hyperinsulinism

Verdict: accept as research-only, with edits.

Numbers match the abstract (item 15). Status: a drug-trial endpoint in 8 children, abstract level only, so research-only is right and the ceiling is limited anyway. Measure type: the row names post-meal (MMTT) and post-protein (OPTT) glucose and insulin; correct.

Required edits:
1. The study tested exendin-(9-39), an investigational drug; the sentence "Measurement of protein-sensitive hypoglycaemia as a trial endpoint" is fine, but add that the 16 children in the fasting part were separate from the 8 in the MMTT/OPTT part.
2. Add the abstract result that the OPTT hypoglycaemia reduction was 82% (P = 0.007) (the abstract text reads "Administration of exendin-(9-39) during the OPTT resulted in 82% (P = 0.007) reduction in the [truncated]"; the truncated endpoint is not read, so cite it only as "a reduction", or omit).
3. Remove 26908106 from the evidence column or label it "reviewed: no protein or leucine test in the visible abstract; context only"; absence in a truncated abstract is not evidence.
4. Overlap: rows 4 and 24 are already cited correctly. The row adds no diagnostic use; consider a one-line mention under row 4 ("OPTT used as a research endpoint") instead of a numbered row.

## Claims that could not be traced to a source I read

- Cryer 2009 (PMID 19088155): not read; any claim about what it recommends is untraced.
- D1 "[recall, not verified here]" statement about OGTT-induced low glucose in healthy people.
- D1: the second inclusion condition of the 41829992 RH definition (only the first was in my window).
- D2: Table S1 and Fig. S2 of 39992257 (supplement) not read; the "stimulated" qualifier for the Insel passage; 42684379 beyond its abstract; the 5-9 timed samples needed for Index60 and the minimal model (not searched; the paper says Index60 integrates glucose and C-peptide values, which I did not check against a sampling schedule).
- D3: the IGI pooled correlation (abstract truncated); the effect sizes for ISSI-2 and IGI/FPI in 40812331 (truncated); PMID 42892651 not read.
- D5: fasting C-peptide 0.10 ng/mL at about 7 years; the claim that Cochrane 21901702 does not mention C-peptide-guided treatment (abstract truncated, so only "not seen in the visible text").
- D6: the OPTT hypoglycaemia reduction endpoint (abstract truncated); case reports 25915078, 31119523, 27383869 not read.
- Rows 6, 30, 31 of `usecases-verified.md`: only the first columns were read; consistency with their caveats was not fully checked.

## Assumptions

- I treated an abstract confirmation (for example the 69 and 19 counts) as verified at abstract level, and left the "full-text windows" caveat in place.
- The Crossref "not found" flag for the Lancet Diabetes & Endocrinology DOI is an artefact of the checker's DOI parsing at the closing bracket; PubMed returns the same DOI for PMID 40812331.
