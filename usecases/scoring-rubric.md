# Use-case scoring rubric (draft for review)

Status: DRAFT written 2026-10-19 for the user to review. Nothing has been scored. The rubric defines how the use cases in `usecases-verified.md` would be compared, so the best candidates for a clinical workflow can be found. Coverage and reimbursement are out of scope.

## Purpose
Rank the uses of insulin or C-peptide measurement by (a) how good the clinical utility is and (b) how many patients the situation applies to, so impactful use cases can be separated from rare-but-strong, common-but-weak and well-supported-but-niche ones. Scores are comparisons, not truths: every score carries a source, a confidence, and a one-line reason.

## Unit of scoring
One use case = one row of `usecases-verified.md` (some rows are close variants, such as rows 4 and 24 or 9 and 27; merge them if the user prefers). Score the *use of the measurement in that clinical situation*, not the disease.

## Candidates (triage rule, to be confirmed)
- **Include:** rows with status established (1, 2, 3, 4, 6, 7, 10, 22, 24, 29, 31) or limited (5, 9, 11, 12, 13, 14, 20, 21, 23, 25, 27, 32, 33, 46, 47): 26 rows.
- **Include if the situation may be common:** research-only rows 8, 28, 35 and 45 (flagged for a commonality check).
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

**Stakes (S, reported, not in the default composite):** how serious the condition is if missed (0 minor to 4 life-threatening). Some rare uses, such as insulinoma and congenital hyperinsulinism, matter because of stakes and not commonality.

## Combining the scores
- **UQ** = mean of D1, D2 and D8. **R** = mean of D3 to D6. **C** = D7.
- **Primary output is a map, not a single number:** C on one axis, UQ on the other, point size or colour = R, with S noted. Quadrants: common and strong; rare but strong; common but weak; rare and weak.
- **Optional composite:** Impact = C-score weighted with UQ, with R as a modifier. The default weights are for the user to set (suggested start: UQ 0.5, C 0.3, R 0.2, all on a 0-to-1 scale). Report a sensitivity check showing which candidates stay in the top group when weights change.
- **Never hide a low dimension behind an average:** the table shows every dimension, and a use case with D2 of 0 or 1 is labelled "weak evidence" regardless of its composite.

## Process
1. **Triage** the candidates (file-only).
2. **Score by dimension across all candidates, not by use case.** One agent scores one dimension for every candidate, so scores are comparable (different agents scoring different use cases drift). Suggested assignment, all as subagents: evidence searcher with biostatistician for D2 and D8; clinical chemist for D4; endocrinologist and PCP together for D5; the same pair for D1 and D6; evidence searcher for D7 and D3.
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
2. ~~Weights~~ **Decided 2026-10-19:** use the suggested start (UQ 0.5, C 0.3, R 0.2), shown with the map and a sensitivity check.
3. ~~Stakes~~ **Default adopted 2026-10-19 (user delegated):** S stays a reported label, not part of the composite, so rare but serious uses stay visible on the map without mixing seriousness with test quality. Change only if the user asks.
4. ~~Candidate set~~ **Default adopted 2026-10-19:** the triage rule above (about 30 candidates). The pilot rows are three of these candidates scored first to test the rubric; they are not a separate set. Near-duplicate rows (4 and 24, 9 and 27) are scored separately and merged later only if the scores are identical in substance.
5. ~~Workflow scope~~ **Decided 2026-10-19 (user: either is fine if it is useful):** rank all candidates and tag each with its setting (routine care, specialist outpatient, inpatient or procedural), so the map can be filtered to routine-care uses.
6. ~~Pilot rows~~ **Decided 2026-10-19 (user delegated):** rows 6, 5 and 13. Row 6: diabetes type classification by random C-peptide (common, established, consensus-backed: high end). Row 5: hypoglycaemia after bariatric surgery by insulin during symptoms (limited, moderately common: middle). Row 13: pioglitazone selection after stroke or TIA by HOMA-IR above 3.0 (single-trial basis, guideline-embedded, no assay named: weak, IR-specific end).
