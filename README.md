# Is measuring insulin resistance clinically useful?

An AI-assisted evidence review of one question, built as a team of specialised AI roles that check each other, with every step kept as an audit trail.

> **Read this first:** These are AI-assisted research notes, not medical advice and not peer reviewed. Claims were checked by skeptic reviews, but many rest on abstracts or single sources, some items are marked unverified, and the latest corrections have had only one review. Citations were checked for identity and retractions by hand, not exhaustively. Confidence figures are judgements, not computations. Use `merged-conclusion.md` with its stated caveats and verify anything you rely on against the primary sources.

## The question
Insulin resistance (IR) is measured in research and in some clinics with fasting insulin, HOMA-IR or surrogate indices such as the triglyceride-glucose (TyG) index. Does measuring it change what a clinician does or improve patient outcomes? And, separately, when are insulin and C-peptide measurements useful for other clinical questions? Coverage and reimbursement are out of scope.

## Short answer (with caveats)
- **No established clinical utility today for routine IR measurement** (fasting insulin, HOMA-IR, TyG) in primary care, prediabetes, type 2 diabetes, PCOS, MASLD or obesity. Judged at about 80-85%; this is a judgement of how well the verdict survives further checking, not a calculation.
- **"Shown not to add value" is a weaker claim,** about 45-50%. The evidence is thin and narrow, and the searches that would find a decisive study were incomplete.
- **The strongest finding is about measurement:** a single fasting insulin or HOMA-IR value cannot reliably classify a person near a cutoff or detect individual change (within-person variation is roughly 25-30%, assays disagree, cutoffs do not transfer).
- **Insulin and C-peptide do have established uses, mostly not as IR screening:** hypoglycaemia work-up, diabetes classification, and some specialist settings. `usecases-verified.md` lists 47 uses by patient type: 11 established, 15 limited, 10 research-only, 11 unsupported. All established uses are secretion, hypersecretion or classification uses; no IR-measurement use is established.

## Why this exists
1. **The question is contested and the evidence is scattered** across prediction studies, guidelines, trials, laboratory standardisation papers and registries. A reader needs one place that says what each source actually shows and how strong it is.
2. **A single AI pass over the literature is unreliable for this.** In this project, independent reviewers repeatedly found abstract-only reading, studies attached to the wrong claim, evidence graded more strongly than its source allowed, "not found" claims built on searches that could not have found anything, and caveats lost when claims were copied into the summary. The system is built to catch these failures, not to trust the first answer.
3. **A test of the method.** The same roles were run twice (as separate sessions and as subagents) to see whether a second run adds confidence. It mostly measured how incomplete a single search is; the conclusions agreed.
4. **A review that can be kept current.** The plan in `update-system/` describes a weekly watch for retractions, trial results and guideline changes, with nothing changing the conclusion until a skeptic has reviewed it.

## How it works
Roles are defined in `.claude/agents/` and run with Claude Code. Each role has one job:

| Role | Job |
|---|---|
| Evidence searcher | Builds a documented evidence set with reproducible searches, registry checks and guideline full texts; does not grade |
| Endocrinologist, PCP | Judge whether measuring IR would change specialist or everyday care |
| Biostatistician | Appraises prediction, cutoff and bias evidence |
| Clinical chemist | Owns assay quality, variability and cutoffs |
| Scientist | On-call physiology |
| Skeptic | Checks claims against sources, verifies citations, challenges overreach |
| Steelman | Builds the strongest case for utility and finds what the team missed |
| Use-case reviewers | Verify and extend the list of insulin and C-peptide uses by patient area |
| Specialty reviewer, summary editor | Defined, not yet run: specialty checks of the conclusion, and a plain-language summary |

Flow: searcher, then analysts, then skeptic and steelman, then a merged conclusion that a skeptic reviews again. Analysis-stage runs are kept independent of one another; all coordination goes through a main session. Every correction is logged in `CHANGELOG.md`. Details are in `CONVENTIONS.md`.

## What to read
| File | What it is |
|---|---|
| `merged-conclusion.md` | The main findings, with confidence figures, caveats and open gaps |
| `usecases-verified.md` | Uses of insulin and C-peptide measurement by patient type (47 rows) |
| `CHANGELOG.md` | What changed, when and why |
| `CONVENTIONS.md` | How runs are organised, where files go, the citation rule |

The folders hold interim working material and the audit trail, not documents to read for the findings:

| Folder | Contents |
|---|---|
| `analysis/` | Analyst reports from session runs; the evidence searcher's evidence base; `subagent-runs/` has the matching subagent reports |
| `reviews/` | Skeptic reviews, the steelman, the comparison of the two runs; `subagent-runs/` has subagent reviews |
| `usecases/` | The unverified draft list and `reviewers/`, the area reviewer reports behind the verified list |
| `update-system/` | Update plan, watchlist, pending queue, claim ledger design, citation checker script (not yet run) |
| `archive/` | Superseded files |
| `.claude/agents/` | The role definitions |

## Status
- **Done:** the merged conclusion and the 47-row use-case list, each through skeptic review and corrections; the draft update system.
- **Not done:** specialty reviews (cardiology first), the plain-language summary, the claim ledger build, a first run of the citation script, the update watch dry run. The most recent corrections to the measurement section have had one review.
- **Known limits:** searches used PubMed and registries only (no Embase, Cochrane or non-English literature); several guideline texts could not be read in full; many sources were read at abstract level only; the two-run comparison was one pair per role with no control.

## Reusing the approach
To apply it to another clinical question: edit the role files in `.claude/agents/` for the new topic, keep the independence and verification rules, run the searcher first, then the analysts and skeptic, and require every claim to carry its source, read level and caveats. `update-system/CLAIM-LEDGER.md` describes a structure for tracking claims.
