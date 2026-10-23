# IR project (rules for Claude Code sessions)

Active since 2026-10-19 (installed from the draft in `tools/README.md`). Loaded automatically at the start of every session.

This repository is an AI-assisted evidence review. Its main goal (decision D-30) is to find and score the most viable uses of insulin, C-peptide and insulin-resistance measurement, and what would make the less viable ones viable; the assessment of whether routine insulin-resistance measurement is clinically useful (`merged-conclusion.md`) is the constraint behind that goal, together with a verified list of uses. Start with `README.md`; the final documents are `merged-conclusion.md` and `usecases-verified.md`. Coverage and reimbursement are out of scope.

## Rules
- **Paths:** use project-root-relative paths in files and in agent prompts. Never write absolute paths.
- **Citations:** record both the PMID and the DOI for every paper, with the read level (full text, abstract, title only). Never invent a citation; verify identifiers against PubMed or Crossref.
- **Scope:** say which measure type a claim covers (fasting-based, post-load or mixed-meal, non-insulin surrogate, C-peptide). Do not write "IR measurement" generally. Confidence figures are judgements, not computations.
- **Deliverables:** `merged-conclusion.md`, `usecases-verified.md` and `claims/claims.csv` are changed only by the main session, after a skeptic review for substantive changes. Subagents write their own report files and do not edit deliverables.
- **Unattended runs never stop to ask a question.** Record assumptions and failures in the output and continue.
- **Independence:** analysis-stage agents do not read each other's reports. Coordination goes through the main session.
- **Run mode:** subagents by default; sessions only when the user wants to watch or for peer messaging (`CONVENTIONS.md`).
- **Decisions:** record each decision in `DECISIONS.md` when it is made (what, why, alternatives, who decided), and read the relevant entry before changing a settled decision.
- **Handoff:** at the end of a working session, update `HANDOFF.md` (where we are, next step, waiting on the user, watch out for); the session-start brief prints it.
- **First message "status":** answer in under 15 lines from the session-start brief and `HANDOFF.md`: where we are, the next step, what waits on the user, and any environment problems the brief reports. Change nothing and start no agents. Works the same in local and cloud sessions.
- **Earlier chats:** not used. Local and cloud chats cannot see each other, so the repository files are the only record: `DECISIONS.md`, `HANDOFF.md`, `CHANGELOG.md`, `memory/` and the other documents (D-36). Put anything a later session needs into them before the session ends.
- **Memory:** save notes for future sessions in the `memory/` folder of this repository, not in the private Claude memory folder. One note per file with frontmatter (name, description, type: user, feedback, project or reference), plus a one-line entry in `memory/MEMORY.md`. Record user preferences, lessons learned and pointers there. The repository is public, so write nothing sensitive. The session-start brief prints the memory index.
- **Usage limit:** the user watches a usage limit. Do not start search-heavy agent runs without asking; prefer file-only work.
- **Changes:** log every change in `CHANGELOG.md`. Commit and push only when the user asks; the repository is public.
- **File locations:** create a file where it is meant to live (for example `CLAUDE.md` in the project root) and mark unfinished work inside the file, not by parking a draft elsewhere.
- **Files:** no PDFs or copyrighted full texts in the repository. Interim material stays under `analysis/`, `reviews/` and `usecases/reviewers/`.
- **Language:** plain wording, no unqualified claims; keep uncertainty labels (abstract-level, single-source, unverified, not reviewed).
