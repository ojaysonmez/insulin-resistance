# Handoff

Updated: 2026-10-19 (end of the first long working session; brief checked in a new session the same evening)

The current state and the next step, written by hand at the end of a working session. It is overwritten each time (history lives in `CHANGELOG.md` and git). `tools/session_start_context.py` prints this note's main sections at the start of each session. Update it at the end of every working session.

## Where we are
- The merged conclusion and the 47-row use-case list are written, skeptic-reviewed and rescoped by measure type; the repository is public with a disclaimer.
- The use-case scoring rubric is settled (US commonality, weights utility 0.40, commonality 0.25, stakes 0.20, readiness 0.15, all candidates ranked with a setting tag); nothing is scored yet.
- Session continuity is set up this session: `CLAUDE.md`, the session-start hook, `DECISIONS.md`, this note and in-repo project memory (`memory/`).
- Check the session brief for unpushed commits and uncommitted changes (it shows the live git state).

## Next step
- Run the scoring pilot on rows 6, 5 and 13 (needs searching for US commonality) once the user agrees, then score about 30 candidates by dimension.
- The pilot is drafted as a workflow script, `usecases/pilot-scoring.workflow.js` (six agents, not run, review first). Running it needs the user's explicit go-ahead for the Workflow tool and room under the usage limit.
- The session-start brief and the in-repo memory rule were both verified in a new session on 2026-10-19; nothing is pending there.
- Then, as the user chooses: specialty reviews (cardiology first), summary editor, claim ledger build, update-watch dry run.

## Waiting on the user
- Whether to move the hook from `.claude/settings.local.json` to the shared `settings.json`. (The local file is now tracked in git, so this matters less.)
- Whether to supply PDFs for the 20-30 load-bearing papers that were read only at abstract level (user said not yet).
- Permission to start search-heavy agent runs (the user is watching a usage limit).

## Watch out for
- Do not launch search-heavy agents or push to the public repo without being asked.
- Create files where they belong, not as drafts in another folder.
- Deferred wording items from the scope review: about ten generic "IR" statements, rows 17, 35 and 45 relabelling, and a check of whether WBISI is the Matsuda index.
- Confidence figures (80-85% and 45-50%) were not re-derived after the measure-type rescoping.
- Read `DECISIONS.md` before changing a settled decision.
- Constraints from the user: coverage and reimbursement are out of scope; nothing is published or pushed without a request; PDFs are "not yet"; the memory folder is tracked in the public repo.
- Compaction check (2026-10-19): the session-start hook fired once after compaction of the working chat, so the brief is not duplicated. That chat's transcript file shrank from about 5.2 MB to about 0.86 MB for an unconfirmed reason, so treat the repository files, not the transcript, as the reliable record.
- Advice given when the working chat reached about 96% context: start a new chat for the next task (the scoring pilot) instead of continuing in a compacted one, because a long context costs more per message against the usage limit.

## Earlier chats
- The long working chat that built all of this can be searched from a new session with the transcript search tool (it searches other sessions' transcripts by text). Its session ID is in the git-ignored local log `.claude/sessions.log` (the `event=Manual` lines); `memory/reference_working_chat.md` explains how to find it.
