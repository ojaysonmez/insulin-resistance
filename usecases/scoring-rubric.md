# Use-case scoring rubric (draft for review)

Status: DRAFT written 2026-10-19 for the user to review. Nothing has been scored. The rubric defines how the use cases in `usecases-verified.md` would be compared, so the best candidates for a clinical workflow can be found. Coverage and reimbursement are out of scope.

## Purpose
Rank the uses of insulin or C-peptide measurement by (a) how good the clinical utility is and (b) how many patients the situation applies to, so impactful use cases can be separated from rare-but-strong, common-but-weak and well-supported-but-niche ones. Scores are comparisons, not truths: every score carries a source, a confidence, and a one-line reason.

## Unit of scoring
One use case = one row of `usecases-verified.md` (some rows are close variants, such as rows 4 and 24 or 9 and 27; merge them if the user prefers). Score the *use of the measurement in that clinical situation*, not the disease.

## Candidates (triage rule, to be confirmed)
- **Include:** rows with status established (1, 2, 3, 4, 6, 7, 10, 22, 24, 29, 31) or limited (5, 9, 11, 12, 13, 14, 20, 21, 23, 25, 27, 32, 33, 46, 47, 49): 27 rows.
- **Include if the situation may be common:** research-only rows 8, 28, 35, 45 and 48 (flagged for a commonality check; row 48, reactive hypoglycaemia, added 2026-10-19).
- **Exclude:** negative entries (26, 30, 34, 40, 42, 43, 44), rows recording no use found, and research endpoints or very rare research uses (18, 19, 37, 38, 39, 41).
- Result: about 30 candidates. The user can add or drop rows.

## Dimensions
Scored 0-4 unless stated. Each score needs: the number, one or two sentences of reasoning, the source (PMID with DOI, guideline name and year, registry ID, or file and section), a confidence (high / medium / low), and whether it came from the project's files or a new search. If the files and sources cannot support a score, write "not determinable" and do not guess.

**Utility quality (UQ): does the result help the patient?**

| ID | Dimension | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| D1 | Decision change: what the result changes | Nothing | Counselling only | Chooses among accepted options or supports a diagnosis | Determines diagnosis, classification or treatment choice | Required step or eligibility criterion |
| D2 | Evidence for that decision impact (not mere association) | None or opinion | Case series or expert opinion | Observational accuracy or cohort data | Consensus or guideline backed by studies | Randomized evidence, multiple high-quality studies or regulatory approval |
| D8 | Added value over available alternatives (clinical features, other tests) | Alternatives do as well or better | Marginal | Useful in a defined subgroup | Clearly adds beyond alternatives | Irreplaceable (no alternative) |

**Readiness (R): could it work in a clinic today?**

| ID | Dimension | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| D3 | Guideline or regulatory status | Recommended against | Not addressed | Option or "may be considered" | Recommended in a specific population | Required or standard (guideline or label) |
| D4 | Analytical feasibility: assay, sample, protocol, standardization | Research only | Specialised or send-out | Widely available but unstandardized or needs a timed protocol | Standard laboratory test | Point-of-care or routine panel |
| D5 | Workflow fit: who orders it, where, how many steps | No clear owner | Specialist only with a complex protocol | Specialist outpatient | Primary care or routine laboratory | Fits an existing routine visit or panel |
| D6 | Safety and burden (higher = safer): false-result consequences, patient burden | Serious harm risk | Notable burden or risk | Moderate | Low | Negligible |

**Commonality (C): how many patients?**

| ID | Dimension | Scale |
|---|---|---|
| D7 | Patients per year in the United States in whom the clinical situation arises (not the number of tests) | 0: under 100; 1: 100 to 1,000; 2: 1,000 to 10,000; 3: 10,000 to 100,000; 4: 100,000 to 1,000,000; 5: over 1,000,000. Give the number, its source and a range; a rough epidemiological estimate is acceptable if the range is stated |

**Commonality base (agreed 2026-10-19): the United States only.** A "patient" means a patient in whom the clinical situation arises in a year: new cases plus patients who need the test again that year. It is not the number of tests and not everyone who has the underlying disease (for example, classification of adult-onset diabetes counts newly diagnosed adults each year, not all people with diabetes). Use US sources (CDC, NHANES, national registries, published US incidence and prevalence); no global column is scored.

**Stakes (S, part of the composite; decided 2026-10-19):** how serious the harm is when the right decision is not made, so how much the use case matters to each patient, as a second dimension beside commonality. Score the consequence of *not having the information* in that clinical situation, not the severity of the disease in general. 0: minor or self-limited; 1: symptomatic but reversible; 2: moderate morbidity or delayed harm; 3: serious morbidity (hospitalisation, organ injury, permanent disability); 4: life-threatening or irreversible. Rare uses such as insulinoma and congenital hyperinsulinism score low on commonality but high on stakes.

**Path to viability (PV, added 2026-10-19 with decision D-30; recorded for every candidate, not part of the composite):** the one missing piece that would move this use to the next tier, as a short sentence (for example external validation of a threshold, a trial comparing measurement-guided care with usual care, an agreed assay cutoff, a guideline recommendation, a workflow or point-of-care assay), its type (evidence, assay, guideline, workflow) and a rough effort (small: months with existing data; medium: a prospective study; large: a randomized trial). PV answers what would make this use viable. It lets the map separate viable now, close to viable and far, and it names where research effort should go. It is a judgement with a source or a stated reason, not a score.

## Anchor clarifications (approved by the user 2026-10-19; apply these whenever the anchors above are read)
These come from the anchor problems reported by units U1, S1, S2, S3 and S4 (`usecases/scoring/anchor-proposals.md`).
1. **D7, chronic conditions:** count new cases per year plus the share of the existing pool that is evaluated or retested in a year; write the share as a stated assumption.
2. **D7, population:** use the narrowest population in which the guideline or study applies the test; state a broader reading as a note.
3. **D7, bins:** score the bin that contains the point estimate; mark confidence low when the range spans bins; the score must equal the bin of the stated number.
4. **D7, situations not diagnoses:** count patients in whom the clinical question arises (for example everyone worked up for hypoglycaemia), not only those with the final diagnosis.
5. **D3, measurement not drug:** D3 is about the measurement. A guideline that recommends a drug or names the condition the test identifies but not the test scores 2; 3 only if it recommends or requires the measurement.
6. **D3, national criteria:** score status for the US setting. National criteria from elsewhere count as 1 (not addressed in the US) unless a US or international body adopts them; note them.
7. **D3, standard diagnostic step:** 4 only when the guideline or label requires the test for the decision; a recommended step is 3.
8. **D2, trial entry criterion:** a trial that used the measure as an entry criterion but never tested measurement-guided selection scores 2 at most.
9. **D2, surrogate approval:** regulatory approval on a surrogate endpoint scores 3; 4 only for hard-outcome randomized evidence for the decision.
10. **D2, research endpoints:** for research-endpoint uses score the evidence that the measure is an accepted surrogate (2 for cohort evidence, 3 for a consensus statement) and say so.
11. **D1, prognosis:** prognosis that sets monitoring intensity or counselling is 1; prognosis that selects a treatment or a diagnostic step is 2.
12. **D1, national criteria:** 4 only where the criterion is a legal or regulatory requirement for the decision in the scoring country; national diagnostic criteria elsewhere are 3.
Scores given before this date (unit U1) used the earlier wording; the pilot review (unit U6) compares them with the clarified reading.

### Pilot clarifications (adopted by the user 2026-10-20 after the pilot skeptic review U6; `usecases/scoring/U6.md`)
These refine the twelve clarifications above. Where they differ, these apply.
13. **D3, the decision named:** D3 is scored for the decision named in the use case. 4 only when a guideline, consensus or label says the test must be done before that decision; if the use case spans several decisions, score the primary one and note any decision where the test is required.
14. **D3, broader population:** a recommendation for the measurement in a broader population that includes this one scores 2 unless the guideline text covers the use-case population explicitly; then 3.
15. **D1, name the decision:** 4 if a guideline requires the result before that decision; 3 if the result determines the decision but other tests can substitute; 2 if it chooses among accepted options or only supports a diagnosis.
16. **D5, ownership and steps only:** D5 scores who orders the test, where, and how many steps. Do not score assay standardisation (D4) or consequences of a wrong result (D6). Score 0 only if no specialty owns the decision.
17. **D6, the lower of two:** D6 = the lower of the test burden score and the false-result consequence score; write both numbers in the reason. 3 = low (reversible, minor), 2 = moderate (reversible harm needing treatment), 1 = notable, 0 = serious.
18. **Stakes, marginal harm:** S = the harm that results when the decision is made without the measurement, assuming the usual default action (for example continue insulin, or give pioglitazone on the other guideline trigger). Do not score the severity of the disease. If the default action is itself harmful, say so.
19. **D8, within the population:** score against the alternatives within the stated population. 3 requires data or guideline text showing the measurement changes the answer given the alternatives (for example a reclassification rate); mechanism alone scores at most 2. 'Not determinable' is allowed.
20. **D4, US assays:** score US-marketed assays. Where only non-US or older-generation data exist, score from them, cap confidence at medium, and say so. Separate protocol burden (D5) from assay standardisation (D4).
21. **D7, sourced chains:** each share in the chain needs a source or is labelled an assumption with its own range. If the range of the bin-deciding share crosses a bin boundary, record 'bin 3 or 4, low confidence' (or not determinable) instead of a single bin.
22. **Setting tag:** tag by who orders the test in the guideline or evidence pathway for the decision.
23. **Corrections and later units:** a score corrected by the main session keeps `original_score` and a `correction` note in its JSON; a later unit may replace earlier scores of other units by listing them in `supersedes` (for example researched patient counts replacing screening estimates).
24. **D7, unsourced shares (D-37):** where a share in the chain is an assumption (clarification 21) and the JSON needs one integer, score the bin of the point estimate (clarification 3), set confidence to low, and write the alternative bin and the share that decides it in the reason. The ranking shows a sensitivity column with the alternative bin for such rows. Do not switch to the broader 'situation arises' count to avoid the assumption; give that count as a note.

### Clarifications 25 to 29 (drafted 2026-10-23 from the stage 2 anchor issues; ADOPTED by the user 2026-10-23, D-39; no score has been changed yet)
Source: the "Anchor issues reported by the units" list in `usecases/scoring/ranking.md`. They apply to every unit scored or rescored from now on; existing scores are unchanged until a rescoring is decided.
25. **D4, the assay only:** score D4 on assay standardisation and US availability and nothing else. A timed protocol, a provocative test or a send-out step belongs to D5 (restates 16 and 20). Where one use bundles several assays (insulin plus drug screen, insulin plus antibody and PEG step, C-peptide plus genetics), score the limiting assay and name it in the reason, with the score of the main assay in brackets.
26. **Stakes, name the default:** state the default action and the harm of the wrong decision in the reason (restates 18). Do not give a score that follows disease severity; if the unit cannot name a default action, give S with low confidence and say why.
27. **Rows with two parts:** score only the part that uses insulin or C-peptide and write in the reason which part was scored (as units already did for row 35). A row where both parts use the measurement is split before scoring, not averaged.
28. **National criteria, one reading:** D1 follows clarification 12 (3 for national diagnostic criteria elsewhere); the US reading goes in the reason, not in the score, because D3 and S already carry it (D-38). Rows 46 and 47 should read the same way (V17 scored row 46 D1 as 3 and V18 as 2).
29. **No individual decision:** for a research endpoint (row 8) or an interpretation limit (row 28), D1 is 1 at most and the reason says no patient decision is named; score D2 and D8 as in clarifications 10 and 19.
Rows whose scores these would touch, for a later rescoring decision: D4 on rows 3, 12, 20, 21, 25 and 35; D1 on rows 28, 46 and 8; S on rows 6, 13, 31 and 32. Nothing is rescored until the user decides.

## Combining the scores
- **UQ** = mean of D1, D2 and D8. **R** = mean of D3 to D6. **C** = D7. **S** = stakes. Each is rescaled to 0-1 before weighting (C = D7/5; S = S/4; the others /4).
- **Primary output is a map, not a single number:** C on one axis, UQ on the other, point size or colour = R, with colour or a label = S. A second view plots need (C and S together) against UQ. Quadrants: common and strong; rare but strong; common but weak; rare and weak; and a high-stakes marker on any of them.
- **Optional composite:** Impact = C-score weighted with UQ, with R as a modifier. The default weights are for the user to set (updated 2026-10-19 to include stakes: UQ 0.40, C 0.25, S 0.20, R 0.15, all on a 0-to-1 scale). Report a sensitivity check showing which candidates stay in the top group when weights change.
- **Never hide a low dimension behind an average:** the table shows every dimension, and a use case with D2 of 0 or 1 is labelled "weak evidence" regardless of its composite.

## Process
1. **Triage** the candidates (file-only).
2. **Score by dimension across all candidates, not by use case.** One agent scores one dimension for every candidate (the biostatistician also writes the PV field for every candidate), so scores are comparable (different agents scoring different use cases drift). Suggested assignment, all as subagents: evidence searcher with biostatistician for D2 and D8; clinical chemist for D4; endocrinologist and PCP together for D5; the same pair for D1 and D6; evidence searcher for D7 and D3.
3. **Calibration:** run a pilot on three candidates chosen to span the range (row 6 diabetes classification, row 5 post-bariatric hypoglycaemia, row 13 IRIS-based pioglitazone selection). Check the anchors work, fix ambiguous definitions, then score all candidates.
4. **Agreement check:** a second independent agent re-scores five random candidates on every dimension. A difference of more than one point on a dimension goes to a skeptic and the anchor is rewritten if needed.
5. **Deep dossiers for the top group only** (about 10): one agent per use case builds a structured evidence summary; a skeptic reviews the top-ranked ones.
6. **Skeptic review of the ranking logic and the weights,** then the map and ranked table are published in the repository.

## Rules
- **Setting tag:** label each candidate routine care, specialist outpatient, or inpatient or procedural; rank all, and make the map filterable by setting.
- Identifier rule applies: record both PMID and DOI for every paper (see `CONVENTIONS.md`).
- Commonality estimates must cite a source and give a range. A range wider than one bin is marked low confidence.
- Do not infer a score from a use case's status in `usecases-verified.md`; the score must be justified from the sources.
- Scores for a use case that rests on measure types the project did not evaluate (post-load, C-peptide as predictor) say so, using the scope audit.
- Unattended runs never stop to ask: choose the most reasonable reading, record the assumption, continue.

## Open decisions for the user
1. ~~Population base for commonality~~ **Decided 2026-10-19: United States only.**
2. ~~Weights~~ **Decided 2026-10-19:** use the suggested start, revised on the same day to include stakes (UQ 0.40, C 0.25, S 0.20, R 0.15), shown with the map and a sensitivity check.
3. ~~Stakes~~ **Decided 2026-10-19 (user):** stakes is a scored dimension in the composite, a second dimension beside commonality. The map still shows S separately so a high-stakes use is never hidden by an average.
4. ~~Candidate set~~ **Default adopted 2026-10-19:** the triage rule above (about 30 candidates). The pilot rows are three of these candidates scored first to test the rubric; they are not a separate set. Near-duplicate rows (4 and 24, 9 and 27) are scored separately and merged later only if the scores are identical in substance.
5. ~~Workflow scope~~ **Decided 2026-10-19 (user: either is fine if it is useful):** rank all candidates and tag each with its setting (routine care, specialist outpatient, inpatient or procedural), so the map can be filtered to routine-care uses.
6. ~~Pilot rows~~ **Decided 2026-10-19 (user delegated):** rows 6, 5 and 13. Row 6: diabetes type classification by random C-peptide (common, established, consensus-backed: high end). Row 5: hypoglycaemia after bariatric surgery by insulin during symptoms (limited, moderately common: middle). Row 13: pioglitazone selection after stroke or TIA by HOMA-IR above 3.0 (single-trial basis, guideline-embedded, no assay named: weak, IR-specific end).
