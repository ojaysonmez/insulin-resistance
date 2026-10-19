# IR project: file index

Question: is measuring insulin resistance (fasting insulin, HOMA-IR, TyG) clinically useful, and what are the uses of insulin and C-peptide measurement? Coverage and reimbursement are out of scope. This folder holds the findings, the work behind them, and the plans for keeping them current.

## Read these first
| File | What it is |
|---|---|
| `merged-conclusion.md` | The main findings, with confidence figures and open gaps |
| `usecases-verified.md` | Uses of insulin and C-peptide measurement by patient type (47 rows) |
| `summary.md` | Plain-language summary (not written yet; see the summary editor role) |
| `CHANGELOG.md` | What changed, when and why |

## Folder map
| Folder | Contents |
|---|---|
| `analysis/` | Interim analyst reports from session runs: endocrinologist, scientist, PCP, biostatistician, clinical chemist (and its round 2), and the evidence searcher's evidence base (retrieval only, no grading; section 12 holds the round 2 additions) |
| `analysis/subagent-runs/` | The matching reports from subagent runs of the same roles |
| `reviews/` | Skeptic reviews, the steelman and the comparison of the two runs |
| `reviews/subagent-runs/` | Skeptic reviews run as subagents, including the review of the round 2 corrections |
| `usecases/` | The unverified draft list (`usecases-draft.md`) and `reviewers/`, the three area reviewer reports behind `usecases-verified.md` |
| `update-system/` | Plan, watchlist and pending queue for keeping the conclusion current, the claim ledger design and its empty `claims.csv`, and `check_citations.py` (not yet run) |
| `archive/` | Superseded or audit-trail files (the searcher's round 2 file, content merged into `analysis/evidence-searcher.md`) |
| `.claude/agents/` | The role definitions (evidence searcher, endocrinologist, PCP, biostatistician, clinical chemist, scientist, skeptic, steelman, use-case reviewer, specialty reviewer, summary editor) |

Everything under `analysis/`, `reviews/` and `usecases/reviewers/` is interim working material and audit trail, not documents to read for the findings.

## Convention
One current report per role per run mode; further rounds update the file or go to `archive/`. Add new files here when created, and log them in `CHANGELOG.md`.

## Running convention (agreed 2026-10-19)
Role definitions are in `.claude/agents/`. All paths in these files are relative to the project root (the folder that contains `.claude/` and these files); do not write absolute paths in files or agent prompts, so the folder can be renamed or moved. Each run of a role is either a subagent or a separate session.

- **Default: subagents for every role** (launched in the background, report handed back to the main session). This includes the evidence searcher, endocrinologist, PCP, biostatistician, clinical chemist, scientist, use-case reviewers, specialty reviewers, summary editor, skeptic and steelman. Reasons: reports arrive directly, they are cheaper and parallel, they are easy to keep independent, and a named subagent can be resumed with a follow-up message, so follow-up alone does not need a session. The skeptic subagents run so far (Set B and the new roles) delivered reports of the same kind as the session skeptics.
- **Sessions only on request or when needed:** the user wants to watch or talk to a run, or the run needs peer-to-peer messaging (that needs session IDs). Skeptic and steelman were run as sessions earlier only by the first pattern we used, not because they need peer messaging. A long source-heavy review can hit a usage limit in either mode; recover by sending a follow-up message to resume it.
- **Evidence for the choice is weak.** The one comparison of the two modes (session set vs subagent set, `reviews/comparison.md`) found neither clearly better; differences came from prompts, tools and instructions, not from the mode. Do not run the same role in both modes on the same question; that only measured search incompleteness and cost 150,000 to 400,000 tokens per run.
- **Independence:** analysis-stage runs do not read each other's files. All coordination goes through the main session. Peer messaging is allowed only for specific conflicts or handoffs, with at most two messages each, and anything received must be verified before use.
- **Specialty reviewers:** the main session names the specialty in the prompt (cardiology, hepatology, reproductive and obstetric medicine, nephrology, oncology, psychiatry). If none is named, the role defaults to cardiology and records that.
- **Order:** evidence searcher, then analysts, then skeptic and steelman, then merge (`merged-conclusion.md`), then specialty reviewers, then a skeptic on the new findings, then the summary editor. The use-case track (use-case reviewers, then `usecases-verified.md`, then a skeptic) runs separately.
- **Where files go:** session-run analyst reports in `analysis/`, subagent-run reports in `analysis/subagent-runs/`; session-run skeptic and steelman reviews in `reviews/`, subagent-run reviews in `reviews/subagent-runs/`; use-case reviewer reports in `usecases/reviewers/`; plans and tools in `update-system/`; final documents in the project root. No other new folders without a changelog entry. The project root was flattened and reorganised on 2026-10-19: older reports and changelog entries still mention the former `ir-team/` and `subagents/` folders, and bare file names in older documents (for example `ir-skeptic.md`) now live in `analysis/`, `reviews/` or `usecases/`, without the `ir-` prefix (that one is now `reviews/skeptic.md`). Report files have no `ir-` prefix; the role definitions in `.claude/agents/` keep theirs. Agents record both PMID and DOI for every paper (see the citation rule below).

## Citation rule (proposed 2026-10-19)
One link per source, with the identifier shown beside it:
1. Paper with a DOI: `https://doi.org/<DOI>` plus the PMID if it has one.
2. Paper with a PMID but no DOI: `https://pubmed.ncbi.nlm.nih.gov/<PMID>/`.
3. Trial: registry ID plus its registry link (e.g. `https://clinicaltrials.gov/study/NCT00091949`, `https://www.isrctn.com/ISRCTN11215387`).
4. Report or document with neither: source URL plus title, issuing body and date (URLs can move or break).
A link is an address, not a check: verify that the title on the record matches the claim. State the read level (full text / abstract / title only) for every item. Publisher pages often block automated readers; doi.org and PubMed links are the safest for agents.
