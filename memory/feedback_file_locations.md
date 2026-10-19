---
name: feedback-file-locations
description: Create files at their intended location, not in a parked drafts folder
metadata:
  type: feedback
---

When producing a draft of a file that has a defined home (for example CLAUDE.md in the project root), create it at that location and mark it unfinished inside the file, instead of saving it elsewhere with a .draft suffix.

**Why:** The user could not find CLAUDE.md.draft in the root and said next time the draft should be wherever the original file is supposed to be (2026-10-19). **How to apply:** write files with a fixed place (CLAUDE.md, .claude/settings*.json, README sections, role files) in place. If something auto-loads and must not go live yet, say so in the reply and in the file header rather than hiding it in another folder.
