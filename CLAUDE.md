# IR project (rules for Claude Code sessions)

Active since 2026-10-19 (installed from the draft in `update-system/SESSION-HOOK.md`). Loaded automatically at the start of every session.

This repository is an AI-assisted evidence review of whether measuring insulin resistance is clinically useful, plus a verified list of insulin and C-peptide uses. Start with `README.md`; the final documents are `merged-conclusion.md` and `usecases-verified.md`. Coverage and reimbursement are out of scope.

## Rules
- **Paths:** use project-root-relative paths in files and in agent prompts. Never write absolute paths.
- **Citations:** record both the PMID and the DOI for every paper, with the read level (full text, abstract, title only). Never invent a citation; verify identifiers against PubMed or Crossref.
- **Scope:** say which measure type a claim covers (fasting-based, post-load or mixed-meal, non-insulin surrogate, C-peptide). Do not write "IR measurement" generally. Confidence figures are judgements, not computations.
- **Deliverables:** `merged-conclusion.md`, `usecases-verified.md` and `update-system/claims.csv` are changed only by the main session, after a skeptic review for substantive changes. Subagents write their own report files and do not edit deliverables.
- **Unattended runs never stop to ask a question.** Record assumptions and failures in the output and continue.
- **Independence:** analysis-stage agents do not read each other's reports. Coordination goes through the main session.
- **Run mode:** subagents by default; sessions only when the user wants to watch or for peer messaging (`CONVENTIONS.md`).
- **Changes:** log every change in `CHANGELOG.md`. Commit and push only when the user asks; the repository is public.
- **File locations:** create a file where it is meant to live (for example `CLAUDE.md` in the project root) and mark unfinished work inside the file, not by parking a draft elsewhere.
- **Files:** no PDFs or copyrighted full texts in the repository. Interim material stays under `analysis/`, `reviews/` and `usecases/reviewers/`.
- **Language:** plain wording, no unqualified claims; keep uncertainty labels (abstract-level, single-source, unverified, not reviewed).
