---
name: reference-working-chat
description: How to find the long working chat that built the IR project; its session ID is kept locally, not in the public repo
metadata:
  type: reference
---

The long working chat (title "Team agents enabled", started the evening of 2026-10-18) built the project. Its session ID, and the ID of the hook test chat, are in `.claude/working-chat-id.txt`. That file is git-ignored and not published, because session IDs are local identifiers with no use to readers of the public repo. A fresh clone does not have it.

How to find the chat: the transcript search tool (search_session_transcripts) matches text across other sessions' transcripts and returns session IDs and snippets; it excludes the calling session, so a new chat can find the working chat by a phrase from it (for example "Team agents enabled" or "scoring rubric"). get_session, list_events and export_transcript take a session ID to read or export a chat; take the ID from the local file or from the search result. About 13 team sessions ("IR: ...") and a few "btw" side chats belong to the same project. The start and end hook also logs session IDs and titles in `.claude/sessions.log` (git-ignored).

**Why:** the user wanted new chats able to retrieve what was decided and why, without publishing identifiers. **How to apply:** read `DECISIONS.md` and `HANDOFF.md` first; search transcripts only for details they do not hold.
