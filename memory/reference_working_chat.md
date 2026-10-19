---
name: reference-working-chat
description: How to find the long working chat that built the IR project; its session ID is kept locally, not in the public repo
metadata:
  type: reference
---

The long working chat (title "Team agents enabled", started the evening of 2026-10-18) built the project. Its session ID, and the ID of the hook test chat, are in `.claude/sessions.log` (lines marked `event=Manual`, with both ID forms where known). That log is git-ignored and not published, because session IDs are local identifiers with no use to readers of the public repo. A fresh clone does not have it.

How to find the chat: the transcript search tool (search_session_transcripts) matches text across other sessions' transcripts and returns session IDs and snippets; it excludes the calling session, so a new chat can find the working chat by a phrase from it (for example "Team agents enabled" or "scoring rubric"). get_session, list_events and export_transcript take a session ID to read or export a chat; take the ID from the local file or from the search result. About 13 team sessions ("IR: ...") and a few "btw" side chats belong to the same project. The start and end hook writes the other lines of that log. Each chat has two IDs: the `local_...` ID the session tools use and a UUID (the transcript file name) that the hook logs; no tool field links them, but a chat's transcript contains its own `local_...` ID, which is how the pairs were matched. A fresh clone does not have the log.

**Why:** the user wanted new chats able to retrieve what was decided and why, without publishing identifiers. **How to apply:** read `DECISIONS.md` and `HANDOFF.md` first; search transcripts only for details they do not hold.
