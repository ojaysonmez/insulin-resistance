---
name: user-working-style
description: How Jay likes to work with the assistant on the IR project: explanations, decisions, publishing, limits
metadata:
  type: user
---

Jay is building and directing a multi-agent evidence review (insulin resistance clinical utility). Working style seen across the first long session (2026-10-18 and 10-19):

- Wants jargon explained in plain words and the reasoning behind choices; often asks "why" or "what does that mean" before agreeing. Give options with a recommendation, not a menu.
- Makes the final call on scope, roles and parameters (for example added stakes to the scoring composite against the assistant's default) and delegates details when told "whatever you choose".
- Prefers consistency across runs and wants everything traceable (changelog, decision log, git history).
- Confirms before anything is published or committed; nothing is pushed to the public repo without being asked.
- Is watching a usage limit: avoid search-heavy agent runs unless asked; file-only work is welcome meanwhile.
- Reads results in short summaries first; wants a clear next step and open decisions at the end of a reply.
- Has no personal notes to keep private; the repository's memory folder is fine for everything.

**Why:** observed repeatedly; saves back-and-forth. **How to apply:** open with the answer, define terms, state the recommendation and the cost, and ask only the decisions that are truly the user's. Related: [[feedback-file-locations]], [[reference-working-chat]].
