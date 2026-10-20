---
name: feedback-verify-before-commit
description: Make a change work and show it working before asking to commit; do not ask for a commit as the first step
metadata:
  type: feedback
---

When building a tool, schedule or pipeline, run it and verify it works first, then ask for the commit. Do not put "commit" as the first step of a plan or ask to commit work that has not been shown to work.

**Why:** the user said on 2026-10-19: "why are we committing before making it work; we should do the work, and if it works then make the commit." A commit of untested work adds noise to the history and asks the user to approve something they cannot judge yet.

**How to apply:** order a task as build, run or test, show the result, then offer one commit for the working state. Docs and plans that are only text can be committed when the user asks, but code, schedules and scoring runs are committed after a successful test run. Commit and push still only on the user's word. Related: [[user-working-style]], [[lessons-learned]].
