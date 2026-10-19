# Skeptic review of the scope rewording (uncommitted diff)

Target: `git diff HEAD -- merged-conclusion.md usecases-verified.md README.md`, from `update-system/scope-audit.md`.
Method: local files only. No web, PubMed, Crossref or Scholar Sidekick calls were made (instruction: usage limit), so no citation was re-verified externally and no retraction check was run by me. "Not traceable in the files" means exactly that; I left those items alone.
Assumption recorded: the diff implements audit items M1-M14 and U1-U7 (21 statements); A1-A4 (analysis/ files) were deliberately not touched.

## 1. Ranked problems

### P1 (high). The new measure list for the interaction trials contains two false "not determinable" entries
- Claim (merged-conclusion.md, intro to the interaction table): "for Cornier 2005, the 2025 Obesity RCT, DPP k-means, the PCOS IPD meta-analysis and ODYSSEY the measure is not determinable from the files".
- Why it fails: the files do state the measure for two of the five.
  - Cornier 2005 (PMID 15897479, DOI 10.1038/oby.2005.79): strata were "insulin-sensitive (fasting insulin <10) vs insulin-resistant (>15 microU/mL)". That is a fasting-insulin measure. Source: `analysis/subagent-runs/evidence-searcher.md` line 25.
  - 2025 Obesity RCT (PMID 39756404, DOI 10.1002/oby.24201): "SI and acute insulin response from IVGTT tested as modifiers". An IVGTT-derived measure, neither fasting nor OGTT. Source: same file, line 27.
  - The audit (matrix row UNSPEC; M12 "5 of the 13 rows have no measure stated") read `analysis/*.md` only and missed `analysis/subagent-runs/`. The audit's UNSPEC tally (30) is inflated by these.
- Also incomplete: the sentence is headed "Measure used, per the files" but does not classify MA.32 (insulin/HOMA, skeptic file), TriMaster (cluster approach with HOMA), or the semaglutide/dapagliflozin SIRD/SIDD row. A reader will assume the list is exhaustive.
- Fix: Cornier = fasting insulin; 2025 RCT = IVGTT-derived insulin sensitivity; add MA.32 and TriMaster; keep DPP k-means, PCOS IPD ("baseline serum insulin", sampling time not stated) and ODYSSEY as not determinable. Better, add the measure column the audit asked for (M12) rather than a prose list.

### P2 (moderate-high). "No guideline read ties a fasting insulin, HOMA-IR or OGTT-derived IR estimate to a management change" is still too absolute
- EASL-EASD-EASO 2024 (PMIDs 38851997, 38852583, 38869512): a weak "may be considered" recommendation to assess IR with HOMA-IR or OGTT-derived estimates "to clarify metabolic dysfunction" (read verbatim, `reviews/skeptic-usecases.md` line 27). The first sub-bullet is handled well ("weak, consensus-based... not linked to a change in fibrosis work-up or therapy"). But the headline sentence directly above still denies any tie, and "clarify metabolic dysfunction" is a diagnostic-labelling decision that can determine whether a patient is classed as MASLD. Whether that counts as a "management change" is a judgement the sentence hides.
- JDS 2022 (PMID 35463863): fasting insulin >30 uU/mL is the only biochemical major sign; use-case row 12 gives the decision informed as "who gets genetic or antibody testing; treat as severe-IR syndrome". That is a fasting-insulin-to-action tie in a society criteria document. `usecases-verified.md` section 6 item 6 itself flags this as "possibly in tension" with the sentence, and the rewording did not resolve it (it is only dealt with in Bottom line 3 as "limited").
- The appended clause "C-peptide-based classification and eligibility rules are the exception" is a category slip: C-peptide is not in the set of measures the sentence covers, so it cannot be an exception to it. (Teplizumab eligibility is an FDA label, not a guideline.)
- Fix: "No guideline read requires a fasting insulin, HOMA-IR or OGTT-derived estimate or ties one to a change in treatment. The nearest ties are EASL's weak 'may be considered' recommendation and the JDS fasting-insulin criterion for severe IR syndromes; neither changes treatment or work-up as documented." Delete the C-peptide "exception" clause (C-peptide is covered in point 3).

### P3 (moderate). Health ABC is described beyond what the files say, and is mis-slotted as purely post-load
- Merged text: "Health ABC (PMID 19700136), where OGTT insulin, fasting insulin and HOMA-IR did not improve heart-failure prediction".
- Files (`analysis/evidence-searcher.md` line 114; DOI 10.1016/j.cardfail.2009.03.001): "OGTT, fasting insulin, HbA1c, HOMA-IR, HOMA-B added to fasting glucose... none improved HF prediction", abstract level. The files never say "OGTT insulin"; "OGTT" may be OGTT glucose. "OGTT insulin" is not traceable in the files. The audit itself wrote "OGTT, fasting insulin, HOMA-IR".
- Health ABC also tested fasting insulin and HOMA-IR, so it is a fasting-measure null as well. That strengthens the fasting-scoped Bottom line 1 and Hu/WHI/NHANES, yet it is placed only in the "post-load, not weighed" bucket.
- Fix: say "OGTT (measure not specified in the files), fasting insulin and HOMA-IR"; note the heart-failure outcome and abstract level; move it into the fasting nulls.

### P4 (moderate). Scope note contradicts the file's own later sentence
- Scope note: post-load measures "were evaluated only through a few trials and use cases, and C-peptide only for niche uses; neither was evaluated as a predictor".
- Same file, "Incremental prediction" bullet: "The files hold two post-load prediction results not weighed here: Health ABC... and the Gutt index in Framingham (PMID 17533210)". C-peptide as a predictor also appears (bariatric remission scores, "no incremental C-peptide analysis"; Herold OGTT C-peptide HR 0.19, usecases row 30).
- The accurate statement is "not weighed as predictors in this conclusion", not "not evaluated". The same overreach is in README ("not separately evaluated") and in Bottom line 1 ("not separately evaluated for routine use"), which are softer but easy to misread as "no data".
- Gutt caveat missing next to the citation: the biostatistician (`analysis/biostatistician.md` lines 30, 50; DOI 10.1001/archinte.167.10.1068) says Gutt ISI was added with no gain (AROC 0.850-0.854), but the evidence searcher (line 117) says "Not verified whether insulin was included". The new sentence cites the paper as a post-load result without the conflict (the conflict is flagged only in the older bullet further down).
- Direction: both post-load prediction items in the files are nulls, the same direction as Bottom line 1. The rewording therefore reads more agnostic than the files warrant.

### P5 (moderate). "Not tested for post-load indices" in the measurement conclusion is false against the files
- New text: the strongest measurement conclusion "is established for fasting measures and not tested for post-load indices".
- The same paragraph, a few lines up, lists post-load test-retest data: OGIS CV 6.5% (Hudak, PMID 34679116) and 7.8% (Gordon, PMID 21945562), Stumvoll ISI 14.4%, WBISI more reproducible than fasting indices in 257 children (Hani, PMID 39726936, DOI 10.1155/2024/2136173, full text read by the chemist), and Mooy 1996 (PMID 8721775, DOI 10.1007/BF00418345).
- Mooy (`analysis/clinical-chemist-round2.md` line 31): 95% of test-retest differences below 61% of the median for fasting insulin and 125% for 2-h insulin. That points to worse reproducibility for 2-h insulin than for fasting insulin; the rewording lists the PMID without direction.
- Therefore: reproducibility of post-load indices has been measured and is mixed (OGIS and WBISI good, Stumvoll moderate, 2-h insulin poor); what has not been tested is classification at a cutoff or detection of individual change. Rewrite to that.
- Domain note, not traceable in the files: WBISI is, to my knowledge, the Matsuda index in the paediatric literature; if so, "Matsuda-specific variation not covered" is contradicted by Hani. Left unverified (no search allowed); worth one check.

### P6 (moderate). Use-case status counts and labels no longer match their notes
- Row 17 is now labelled "Unsupported... ; monitoring not determinable from the files" and row 45 "Research-only" with the caveat "status ... not determinable from the files". Both are still counted in the 8 "unsupported" and 6 "research-only" cells. A row cannot be both counted in a determinate status and labelled "not determinable"; the audit proposed relabelling ("Not evaluated").
- Row 35 was in audit item U5 ("rows 35 and 45") but is unchanged in the diff; its (b) HOMA-IR cohorts are title-level too. Inconsistent treatment of identical evidence.
- Rows 42-44 now say "Unsupported" means "no insulin or C-peptide use found in the sources read, not that a use was tested and rejected"; row 36 is "by extension". With rows 17 (partly), 36, 42, 43, 44 and the 3 negative entries, most of the 11 "unsupported" rows are absence-of-evidence, not tested-and-rejected. The note under the counts table still says only the three negative entries (26, 30, 34) have that character, and README and Bottom line 3 still say "11 unsupported" without qualification.
- Counts themselves are arithmetically unchanged and consistent (IR kind 17 = 0/3/6/8; total 11/15/10/11). The inconsistency is in meaning, not numbers.
- Audit item U1 (split row 17 into three) was not done; only the status text changed.
- Fix: update the counts notes to say which "unsupported" rows are absence-of-evidence; either relabel rows 17, 35 and 45 or state in the notes that they are counted by default category; apply U5 to row 35 too.

### P7 (moderate-low). Confidence figures left unchanged after the evidential basis was rewritten
- Bottom line 2 previously listed DIETFITS as the main support (and Liu 2026 among the nulls); it now says DIETFITS is post-load and moves Liu 2026 to a TyG conflict, then keeps "about 45-50%". The number was set by skeptics for the old basis; nothing says it was re-derived. Same for 80-85% in Bottom line 1, now attached to a narrower claim.
- WHI (PMID 25944628) tested fasting insulin, HOMA-IR and TG/HDL-C; NHANES (PMID 42702103) tested TyG and HOMA-IR. So "fasting insulin/HOMA-IR nulls (WHI, Hu, NHANES)" is correct but the same papers are also TyG-side evidence; the "TyG conflict" sentence omits that NHANES and Barzegar are TyG nulls (it names only ATTICA against Liu 2026).
- Fix: add "figures were set before the rescoping and have not been re-derived" and list the TyG nulls.

### P8 (low-moderate). Stale quote and leftover general wording
See section 3. Most important: `usecases-verified.md` section 6 item 6 quotes the old merged wording as if current.

### P9 (low). "Open gaps" does not carry the scope gaps
- Gap 3 was made per-measure. But the audit's top-ranked gap (do OGTT insulin, Matsuda, insulin AUC, insulinogenic index add discrimination over fasting glucose, HbA1c, 2-h glucose and BMI; audit section 5 item 1, supported by `analysis/evidence-searcher.md` line 308) is not listed, though the scope note says post-load was not evaluated. Gap 2 names only "HOMA-IR/TyG". The C-peptide-as-predictor gap (steelman P10, 138 records unscreened) is also absent.

### P10 (low). Citation housekeeping for new additions
- New PMIDs added by the rewording: 19700136, 10480510, 34679116, 21945562, 39726936, 8721775 (and 38190619/36599304 context). The project's citation rule (CONVENTIONS.md lines 18-19: identifier beside each source) and `update-system/citation-report.md` (124 PMIDs, run before the rewording; none of these appear) mean they have not been identity-checked. DOIs are in the files for 19700136, 10480510, 39726936, 8721775, 17533210; I found none for 34679116 and 21945562. Rerun `update-system/check_citations.py` after committing.

## 2. Overstatement / understatement checks (requested items)

- Rescoped Bottom line 1: accurate for the evidence cited (fasting and surrogate measures). The added clause "C-peptide and insulin are evaluated only for the uses in point 3" is accurate for use cases. It understates the existing post-load nulls (P3, P4). Not an overstatement of utility.
- Rescoped Bottom line 2: now accurate about DIETFITS (INS-30, 30-minute post-glucose insulin, 12-month weight change, P = 0.47: `analysis/evidence-searcher.md` lines 67, 156). Gains honesty, loses a stated basis for the unchanged number (P7).
- Rescoped Bottom line 3: "Insulin (drawn during hypoglycaemia) and C-peptide (random, fasting or mixed-meal stimulated)" matches use-case rows 1-7, 29, 46, 47. Fine. Minor: row 5 and 38 also use post-load insulin; the parenthetical is not exhaustive but is not wrong.
- "Post-load measures were not separately evaluated": true only in the sense of no dedicated search or synthesis (searcher: "only a handful of strings"; "no dedicated pass on 2-h insulin or C-peptide as predictors", line 308). False if read as "no data in the files" (P4). Suggest "examined in only a few studies, none weighed here; the two prediction results found are null".
- EASL handling: see P2. The sub-bullet handles it; the headline does not.
- "Kind" clarification: consistent with the counts (IR = 0 established; all 11 established are secretion/classification). Good. But "No row using fasting insulin, HOMA-IR or OGTT-derived measures for an insulin-resistance question" does not mention stimulated or other post-load measures (row 38 insulin and C-peptide during oral glucose challenge is IR*, research-only) or IVGTT; harmless but incomplete.
- "Unsupported" clarification: partly done (P6).
- ES 2017 and PCOS parentheticals: both survive. ES 2017 rationale names fasting insulin verbatim ("Measuring fasting insulin concentrations to try to diagnose insulin resistance within general practice should be abandoned": `reviews/skeptic-usecases.md` line 25, raw PMC HTML, PMID 28359099). "OGTT insulin is not addressed in the text read" is hedged correctly (first 100k of 470k characters in the summariser route; skeptic read the raw HTML for the quoted passages). PCOS: the text quoted in the files says "insulin assays" and "routinely available measures of insulin resistance" and names no index (`analysis/evidence-searcher.md` line 180), but the reading was keyword windows over a 117k-character XML, so "names no index" is "in the text read".

## 3. Internal consistency and leftover general wording

Scope note, bottom lines, README and open gaps do not fully agree: README bullet 1 omits TG/HDL-C, mixed-meal and C-peptide scope that Bottom line 1 carries; scope note says "not evaluated as predictor" while the prediction bullet says two post-load results exist; open gaps omit the post-load gap. Statements still general that the audit missed or the rewording left (line numbers are current-file):

1. `merged-conclusion.md` line 1 title: "clinical utility of insulin resistance (IR) measurement".
2. `merged-conclusion.md` line 93 (steelman intro): "strongest case that measuring IR is useful. It confirmed that routine measurement still has no established utility".
3. `merged-conclusion.md` line 104: "Points that go the team's way... all favour clinical features over IR" (mixes HOMA, TriMaster routine features, PCOS predictors; TODAY insulin sensitivity measure not stated).
4. `merged-conclusion.md` line 105: "Not tested by anyone: early-pregnancy IR measures..." (measure unstated).
5. `merged-conclusion.md` line 107: "(1) Routine verdict: the pre-specified incremental-value study already listed as open gap 2... plus any trial of measurement-guided care" (no measure named; audit M14 fixed only gap 3).
6. `merged-conclusion.md` line 110: Wagner clusters "built from imaging, genetics and OGTT variables, not an IR index" (audit item 7: post-load evidence dismissed rather than scoped).
7. `merged-conclusion.md` line 111: "IR testing adds nothing to PCOS management" (generic; guideline says insulin assays, no index).
8. `merged-conclusion.md` line 117: "'IR is not in the MASLD guideline' is wrong" (fine, but generic "IR").
9. `usecases-verified.md` section 6 item 6: quotes "No guideline ties an IR measurement to a management change" as merged-conclusion.md's wording; that wording no longer exists (stale quote).
10. `usecases-verified.md` last line of section 6 and `README.md` line 14: "routine IR measurement lacks established clinical utility" and "no IR-measurement use is established" are still unscoped, despite the new Kind clarification; README bullet 1 also still leads "routine IR measurement" with a measure list in parentheses.

## 4. Spot-check of the audit's own load-bearing claims (8)

| # | Audit claim | Result |
|---|---|---|
| 1 | DIETFITS INS-30 = 30-min post-glucose insulin; n=609; P=0.47 (evidence-searcher L67, L156) | Matches (PMID 29466592, DOI 10.1001/jama.2018.0245). Read level: full-text scan of methods plus abstract. |
| 2 | Gardner 2016 insulin-AUC strata = post-load | Matches via subagent file ("median split of OGTT insulin AUC", `analysis/subagent-runs/evidence-searcher.md` line 26); the main searcher file says only "insulin-AUC median-split". Traceable, one file only. |
| 3 | Health ABC (19700136): OGTT, fasting insulin, HOMA-IR did not improve HF prediction | Matches except it is also fasting evidence, and "OGTT insulin" (merged wording) is not in the files (P3). |
| 4 | Framingham Gutt ISI (17533210) | Matches biostatistician; contradicted by searcher "not verified whether insulin was included"; audit does not mention the conflict (P4). |
| 5 | Matsuda vs clamp r 0.73, n=153 (10480510) | Matches `analysis/scientist.md` line 44 (DOI 10.2337/diacare.22.9.1462). |
| 6 | OGIS 6.5% (34679116), OGIS 7.8% and Stumvoll 14.4% (21945562), WBISI children (39726936), Mooy (8721775) | All match `analysis/evidence-searcher.md` line 340 and `analysis/clinical-chemist-round2.md` lines 28-31. Audit wrongly implies Mooy supports a neutral "not carried" item; it shows poor 2-h insulin reproducibility (P5). |
| 7 | "Only one pass (Q2t, 41 records)" on post-load incremental value | Q2t is 41 records (line 564), but line 308 says "a handful of strings (Q2t, Q2u, Q5i, Q5z, Q5x)"; "one pass" slightly understates the searching done. |
| 8 | Cornier and 2025 RCT measures are UNSPEC; 30 of 124 claims UNSPEC | Wrong for two rows (P1); tag arithmetic of the table otherwise adds up (55/22/17/34/30/4/7 and 124 reconcile), so the total is right but UNSPEC is overcounted by about two. |
| 9 | ACTRN12624000306516 n=255, mixed-meal vs fasting vs OGTT vs clamp | Matches (evidence-searcher L92: "255 actual", recruiting; registry list only). Merged text "n=255" is enrolment per registry; fine as "not independently checked". |
| 10 | GRADE includes a C-peptide response (38190619) | Matches (line 160: "HOMA2-%S and C-peptide response"). But the heterogeneity P = 0.009 quoted in the merged table is for HOMA2-%S; the new sentence could mislead by placing GRADE under "C-peptide". |
| 11 | IRIS, LAMP, presurgical metformin, LIRA-ADD2 = HOMA-IR | All match the files (IRIS entry >3.0; LAMP 2.5; presurgical HOMA >2.8; LIRA-ADD2 HOMA-IR tertiles). PERSON = OGTT-derived muscle vs liver IR matches (line 70). |
| 12 | ES 2017 rationale names fasting insulin; PCOS guideline names no index | Match, with the read-level caveats in section 2. |

Citation identity and retractions: not re-checked by me (no network use). `update-system/citation-report.md` lists the earlier 124 PMIDs and flags only PMID 24757230 as retracted; the new PMIDs are outside that run.

## 5. Claims that survived scrutiny

- The core scoping: Bottom line 1 is now correctly limited to fasting insulin, HOMA-IR and TyG/TG-HDL-C; the files do rest almost entirely on those measures.
- DIETFITS is a post-load (30-minute) insulin test on a weight-loss outcome. The new sentence is accurate and is the most useful change.
- PERSON, Gardner 2016, IRIS, LAMP, presurgical metformin, LIRA-ADD2 measure attributions.
- Matsuda r 0.73, OGIS 6.5-7.8%, Stumvoll 14.4%, WBISI, ACTRN n=255 and its "not independently checked" label.
- ES 2017 and PCOS parentheticals (read-limited, hedged).
- Changing `usecases-verified.md` last line to "use-case rows only; did not evaluate incremental-value papers" (accurate per its own gap list item 15).
- Row 36 relabel ("by extension from Rec 1.7") and rows 42-44 caveats: accurate and clearer.
- DOI/PMID: DIETFITS, Gardner, PERSON, Matsuda identifiers all trace to files.

## 6. Verdict

The direction of the rewording is right and mostly honest: it narrows verdicts to the measures the files actually support, and most of the 21 changes are accurate. It is not ready to commit as is. Before committing, fix at least: P1 (two factual errors in the new measure list), P2 (headline sentence vs EASL/JDS), P3 and P4 (Health ABC wording and the "neither was evaluated as a predictor" contradiction), and P5 ("not tested for post-load" is false). P6-P7 are consistency and labelling repairs that can be small edits. None of the problems makes a conclusion more favourable to IR measurement; the verdict itself (no established routine utility for fasting measures) is unchanged.

Confidence that the rewording is directionally justified: about 85%. Confidence that it is correct and consistent enough to commit without further edits: about 40%. After the fixes above: about 80%.
