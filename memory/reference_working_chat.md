---
name: reference-working-chat
description: Session ID of the long working chat that built the IR project, and how to search earlier chats
metadata:
  type: reference
---

The long working chat (title "Team agents enabled", started the evening of 2026-10-18, working directory `C:\dev\ir` after the 2026-10-19 rename) has session ID `local_7bc99541-fc52-4336-88ea-1e1a76bcdaca`.

How to use it: the transcript search tool (search_session_transcripts) matches text across other sessions' transcripts and returns session IDs and snippets; it excludes the calling session, so a new chat can find this one by a phrase from it. get_session, list_events and export_transcript take a session ID to read or export a chat. About 13 team sessions ("IR: ...") and a few "btw" side chats belong to the same project.

**Why:** the user wanted new chats able to retrieve what was decided and why. **How to apply:** read `DECISIONS.md` and `HANDOFF.md` first; search transcripts only for details they do not hold.
