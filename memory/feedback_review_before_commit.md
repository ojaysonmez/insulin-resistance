---
name: feedback-review-before-commit
description: Show the changes and wait; do not commit or push until the user has reviewed them and says so
metadata:
  type: feedback
---

After making changes, stop and let the user review them (open the diff pane, say what changed). Do not commit or push in the same turn, and do not offer "commit and push" as the default button; ask only after the user has looked.

**Why:** the user said on 2026-10-26: "dont commit and push immediately before i review your changes from now on". The repository is public and a push cannot be undone.

**How to apply:** finish the work, log it in `CHANGELOG.md`, show the diff (diff pane) or summarise the files changed, then wait. Commit and push only on an explicit request that comes after the review. Related: [[feedback-verify-before-commit]].
