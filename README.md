# Is measuring insulin resistance clinically useful?

An AI-assisted evidence review of one question, built as a team of specialised AI roles that check each other, with every step kept as an audit trail.

> **Read this first:** These are AI-assisted research notes, not medical advice and not peer reviewed. Claims were checked by skeptic reviews, but many rest on abstracts or single sources, some items are marked unverified, and the latest corrections have had only one review. Citations were checked for identity and retractions by hand, not exhaustively. Confidence figures are judgements, not computations. Use `merged-conclusion.md` with its stated caveats and verify anything you rely on against the primary sources.

## The question
Insulin resistance (IR) is measured in research and in some clinics with fasting insulin, HOMA-IR or surrogate indices such as the triglyceride-glucose (TyG) index. Does measuring it change what a clinician does or improve patient outcomes? And, separately, when are insulin and C-peptide measurements useful for other clinical questions? Coverage and reimbursement are out of scope.

## Short answer (with caveats)
- **No established clinical utility today for routine IR measurement** (fasting insulin, HOMA-IR, TyG) in primary care, prediabetes, type 2 diabetes, PCOS, MASLD or obesity. Post-load insulin and OGTT-derived indices were examined in only a few studies and not weighed separately (the two prediction results found are nulls). Judged at about 80-85%; this is a judgement of how well the verdict survives further checking, not a calculation.
- **"Shown not to add value" is a weaker claim,** about 45-50%. The evidence is thin and narrow, and the searches that would find a decisive study were incomplete.
- **The strongest finding is about measurement:** a single fasting insulin or HOMA-IR value cannot reliably classify a person near a cutoff or detect individual change (within-person variation is roughly 25-30%, assays disagree, cutoffs do not transfer).
- **Insulin and C-peptide do have established uses, mostly not as IR screening:** hypoglycaemia work-up, diabetes classification, and some specialist settings. `usecases-verified.md` lists 49 uses by patient type: 11 established, 16 limited, 11 research-only, 11 unsupported (most of these mean no use was found in the sources read). All established uses are secretion, hypersecretion or classification uses; no IR-measurement use is established.

## Why this exists
1. **The question is contested and the evidence is scattered** across prediction studies, guidelines, trials, laboratory standardisation papers and registries. A reader needs one place that says what each source actually shows and how strong it is.
2. **A single AI pass over the literature is unreliable for this.** In this project, independent reviewers repeatedly found abstract-only reading, studies attached to the wrong claim, evidence graded more strongly than its source allowed, "not found" claims built on searches that could not have found anything, and caveats lost when claims were copied into the summary. The system is built to catch these failures, not to trust the first answer.
3. **A test of the method.** The same roles were run twice (as separate sessions and as subagents) to see whether a second run adds confidence. It mostly measured how incomplete a single search is; the conclusions agreed.
4. **A review that can be kept current.** The plan in `update-watch/` describes a weekly watch for retractions, trial results and guideline changes, with nothing changing the conclusion until a skeptic has reviewed it.

## How it works

### Architecture
```
                        main session (orchestrator)
     launches roles, merges their reports, applies corrections, logs every change
                                    |
        +---------------------------+----------------------------+
        |                           |                            |
  Analysis track              Use-case track               Review layer
  evidence searcher           3 use-case reviewers         skeptic (checks every output)
        |                     (one per clinical area)      steelman (finds what was missed)
  analysts: endocrinologist,        |                      specialty reviewers (planned)
  PCP, biostatistician,       consolidated list
  clinical chemist,                 |
  scientist (on call)         skeptic review
        |                           |
  merged-conclusion.md       usecases-verified.md
        \___________________________/
                      |
          summary editor -> summary.md (planned)
```

- **Roles are agent definitions.** Each role is one markdown file in `.claude/agents/` (name, description, instructions): what it does, what it reads, what it must verify, what it writes. There is no application code; the files are the instruction sets.
- **The main session is the orchestrator.** A Claude Code session launches each role, saves its report, reconciles disagreements, applies corrections and records them in `CHANGELOG.md`. It is the only place where results are combined, so agents work from files and do not message each other (one early experiment let two sessions exchange messages; it helped modestly and is not the default).
- **Subagents are the default way to run a role.** Each run is a background subagent started from the role's definition; it returns a report that is saved to a file. Separate sessions are used only when someone wants to watch or talk to a run, or for peer messaging. The first round was run both ways to compare them; neither was clearly better, so the cheaper subagent mode is the default.
- **Independence.** Analysis-stage runs do not read one another's files, so agreement means something. The skeptic reviews an output without reading other skeptics' reviews. Independent runs of the same role are compared, not blended.
- **Two tracks.** The analysis track answers whether measuring IR is useful. The use-case track lists where insulin and C-peptide measurement is used and how well each use is supported.
- **Verification layers.** (1) Every role records identifiers (PMID and DOI), the read level (full text, abstract, title) and caveats for each claim. (2) A skeptic checks each output against primary sources and verifies citations and retractions. (3) A steelman argues the opposite case and looks for evidence the team did not search for. (4) A script (`tools/check_citations.py`) checks identifiers and retraction or correction notices. (5) Corrections get their own skeptic pass. (6) Every change is logged and kept in git history.
- **Tools the roles use.** PubMed, Crossref, clinical trial registries, and guideline full texts from PMC or Europe PMC. A citation verification service was tried but was unavailable, so verification was done with PubMed and Crossref directly.

### The roles

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

Flow: searcher, then analysts, then skeptic and steelman, then a merged conclusion that a skeptic reviews again. Details and file locations are in `CONVENTIONS.md`.

## What to read
| File | What it is |
|---|---|
| `summary.md` | Start here: the plain-language summary of both documents, with a glossary and a trace of each sentence to its source (not yet skeptic-reviewed) |
| `merged-conclusion.md` | The main findings, with confidence figures, caveats and open gaps |
| `usecases-verified.md` | Uses of insulin and C-peptide measurement by patient type (49 rows) |
| `CHANGELOG.md` | What changed, when and why |
| `DECISIONS.md` | Why the project is the way it is: each decision, the alternatives and who decided |
| `HANDOFF.md` | Where things stand and the next step, for picking the work up in a new session |
| `CONVENTIONS.md` | How runs are organised, where files go, the citation rule |

The folders hold interim working material and the audit trail, not documents to read for the findings:

| Folder | Contents |
|---|---|
| `analysis/` | Analyst reports from session runs; the evidence searcher's evidence base; `subagent-runs/` has the matching subagent reports |
| `reviews/` | Skeptic reviews, the steelman, the comparison of the two runs; `subagent-runs/` has subagent reviews |
| `usecases/` | The unverified draft list and `reviewers/`, the area reviewer reports behind the verified list |
| `update-watch/` | Update plan, watchlist and pending queue for keeping the conclusion current (draft, not running) |
| `claims/` | Claim ledger design and its empty `claims.csv` |
| `tools/` | Scripts (citation checker, session-start context for the hook) and how to install the hook |
| `memory/` | Project memory: working style, preferences, lessons learned, pointers to earlier chats; read at session start |
| `archive/` | Superseded files |
| `.claude/agents/` | The role definitions |

## Status
- **Done:** the merged conclusion and the 49-row use-case list (rows 48 and 49 added after their own skeptic review), each through skeptic review and corrections; the draft update system.
- **Not done:** specialty reviews (cardiology first), the plain-language summary, the claim ledger build, a first run of the citation script, the update watch dry run. The most recent corrections to the measurement section have had one review.
- **Known limits:** searches used PubMed and registries only (no Embase, Cochrane or non-English literature); several guideline texts could not be read in full; many sources were read at abstract level only; the two-run comparison was one pair per role with no control.

## Reusing the approach
To apply it to another clinical question: edit the role files in `.claude/agents/` for the new topic, keep the independence and verification rules, run the searcher first, then the analysts and skeptic, and require every claim to carry its source, read level and caveats. `claims/CLAIM-LEDGER.md` describes a structure for tracking claims.
