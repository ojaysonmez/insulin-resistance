---
title: "Research prompt: repeat C-peptide as a trigger for a clinical decision"
---

Status: prompt written 2026-10-25 (user request); revised the same day to fit jay-research's file layout and to carry the row data inline. Not yet run.

**How to run:** in a fresh cloud session with only the `ojaysonmez/insulin-resistance` repository, on `main`, type `/jay-research standard:` followed by everything below the line. Standard means 3 researchers with up to 10 tool calls each. After the run, the main session copies the report to `usecases/scoring/serial-cpeptide-trigger.md`, makes the DOCX, runs a skeptic review, and commits when the user asks.

---

## Where to write (read first)

- Use **`analysis/jay-research/`** (project-root-relative) as the research directory. Create `analysis/jay-research/research_notes/<title>/` and `analysis/jay-research/reports/` there, not at the repository root. If the skill cannot do that, use its default and say so in the summary.
- Write no other file in the repository. Do not edit `usecases/scoring/metsulin-fit.md`, `usecases-verified.md`, `merged-conclusion.md` or `claims/claims.csv`.
- **Do not commit or push.**
- Do not stop to ask questions. Record your assumptions and continue.

## Question

Is there evidence that a **change in C-peptide between two or more tests** should lead to a clinical action? An action means a treatment, a dose change, a referral, a diagnosis change or the next test being moved earlier. A single C-peptide value that sets eligibility or classification does not count; this project already has those.

## Context

This is the insulin-resistance evidence review (public repository). It scored 50 uses of insulin and C-peptide measurement. For a home capillary device that measures **insulin, C-peptide and glucose**, the user's threshold is 5-10 or more tests per person per year. Only about 4 uses reach it, and only one, islet or pancreas graft monitoring, is in routine care. The occasional uses would become frequent only if a change between repeat results drove a decision. No source read so far ties a serial C-peptide value to an action, except in graft monitoring. Glucose is already on the device, so do not report "measure glucose" as a gap.

Current frequencies (from `usecases/scoring/metsulin-fit.md`, section 1a; judgements unless a source is named):

| ID | Use | Tests/yr now | Analyte | Timing | Status |
|---|---|---|---|---|---|
| Row 10 | Islet or pancreas graft, first year | 4-12 (fasting C-peptide every 1-3 months, survey PMID 35019897) | C-peptide | Fasting | Routine care |
| Row 49, N3 | Stage 1-2 type 1 diabetes | OGTT 1-2; 4-12 in an untested home version | C-peptide | Post-load or post-meal | Research |
| N1 | Residual beta-cell function after diagnosis | 6.5 pairs a year up to weekly (home dried blood spot) | C-peptide | Post-meal and fasting | Research |
| N2 | Response after teplizumab or another disease-modifying drug | 4-12 | C-peptide | Post-meal | Trial endpoint |
| Row 31, N4 | Insulin step-down after random C-peptide | Once now; 3-5 in a serial protocol | C-peptide | Random | Serial testing unsupported |
| Row 32 | Ketosis-prone diabetes after DKA | 1-3 in year one | C-peptide | Fasting | Tier B |
| Row 47 | Slowly progressive type 1 diabetes | 1-2 | C-peptide | Fasting | Tier B |
| Row 27 | TPIAT follow-up | 2-4 | C-peptide | Fasting or post-meal | Weak evidence |
| Row 5, N5 | Recurrent hypoglycaemia capture | 3-6 episodes | Insulin and C-peptide | Timed at symptoms | Unsupported |
| N7 | Stem-cell-derived islet recipients (no product approved) | About 4 (clinic MMTT every 3 months) | C-peptide | Post-meal | Investigational |

## Settings to cover (answer each separately)

1. Early type 1 diabetes after a disease-modifying drug (teplizumab, others): does a C-peptide decline time a second course, a second drug or a switch?
2. Stage 1-2 type 1 diabetes before diagnosis: does a C-peptide change (fasting, random, post-meal, OGTT, Index60) move the diagnosis or treatment earlier?
3. Insulin step-down or withdrawal in adults with uncertain diabetes type: is repeat C-peptide used during or after step-down?
4. Slowly progressive type 1 diabetes (SPIDDM, LADA): does a C-peptide decline set when insulin starts?
5. Ketosis-prone diabetes after DKA: does repeat C-peptide decide insulin withdrawal or restart?
6. Islet, pancreas or stem-cell-derived islet grafts: what C-peptide change defines graft dysfunction, and what action follows?
7. Cross-cutting: **within-person biological variation and reference change value** of fasting, random and post-meal C-peptide. The project's gap search found none published for insulin-treated adults; confirm or refute.

Record any repeat-**insulin** evidence found in passing, labelled separately.

## Sources to prioritise

- Guidelines and consensus: ADA Standards, ISPAD, the 2024 consensus on monitoring autoantibody-positive people (PMID 38912694), IPITA or transplant society guidance, Japan Diabetes Society SPIDDM criteria.
- Drug labels: the teplizumab (Tzield) US label and EMA documents, the monitoring sections.
- Trial and network protocols: TrialNet, INNODIA, ITAD (PMID 32399500), CIT protocols and CITR reports.
- Primary studies: C-peptide trajectories that predict outcomes, biological variation studies, trials of a C-peptide-triggered intervention.

## Evidence rules

- For every paper, give both the PMID and the DOI, verified against PubMed or Crossref, plus the read level (full text, abstract or title only). Never invent a citation; if an identifier cannot be verified, say so.
- Name the measure type for every claim: fasting, post-meal or mixed-meal (MMTT), post-load (OGTT), random, or stimulated (glucagon). Do not write "C-peptide testing" in general.
- Separate what a source states from inference, which must be labelled "judgement". Keep the labels abstract-level, single-source and unverified.
- Absence claims are search-limited: write "not found in N searches", not "does not exist".
- Coverage and reimbursement are out of scope.

## Report content (inside the skill's own report file)

1. **Summary:** at most 10 lines, one verdict per setting: *Action defined* (a guideline, label or protocol states an action tied to a C-peptide change), *Action proposed* (studies only), or *None found*.
2. **Evidence table**, one row per finding, with exactly these columns:
   `setting | source (author year) | PMID | DOI | read level | source type (guideline, label, protocol, trial, cohort, review) | measure type | sampling interval | C-peptide change or threshold | action tied to it | stated or judgement | tests per person per year implied | notes`
3. **Biological variation:** CV within person, CV between people, reference change value, with measure type and population for each.
4. **Effect on the project:** for each row in the context table above, the implied tests per year and whether it now reaches 5-10. This is a proposal only.
5. **Not searched or not found.**
