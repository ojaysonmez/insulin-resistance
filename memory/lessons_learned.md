---
name: lessons-learned
description: What failed in the IR project and how it was fixed, so mistakes are not repeated
metadata:
  type: feedback
---

Lessons from the first long session (2026-10-18 and 10-19). Each is a failure that actually happened.

**Evidence handling**
- **Abstract-only reading hides detail.** Full texts changed claims several times (PERSON's "matched" arm was the opposite of its hypothesis; MA.32 had 72 unadjusted tests; Rosli's range was within-kit spread; EASL's full text held a recommendation the abstract hid). Tag the read level of every source; read open-access or repository full text for anything load-bearing.
- **Truncated or summarised reads of long guidelines miss things.** Read raw text in chunks and say how much was read; a "no recommendation found" statement must give that.
- **Over-narrow search strings and top-page screening produce false "not found".** Use short strings, screen full result sets when small, log strings and counts, and word negatives as "not found in the screened records".
- **Copying claims into the merged conclusion loses caveats and introduces errors** (ATTICA, the presurgical metformin P value, Health ABC wording). A skeptic reviews every substantive change before it is committed; the claim ledger is designed for this.
- **Generic "IR measurement" wording hid which measure the evidence used.** Tag every claim with its measure type (fasting-based, post-load, surrogate, C-peptide).

**Tools and process**
- **Test tools against known answers.** The citation checker evaluated Crossref notices only for DOIs written in the files and silently missed 8 known corrections; comparing its output with what the skeptics had found exposed it.
- **Peer messages cross and relay errors.** In the chemist and searcher exchange the messages crossed, and a relayed abstract framing would have spread an error that only independent full-text reading caught. Verify anything received.
- **Long inline scripts in the shell fail.** Very long here-documents failed to parse, and the shell and Python do not share the same temp folder. Write content with the file tool and keep shell scripts short.
- **Role files register as agent types only when a session starts in the project folder.** Early runs used a general agent told to read the role file.
- **Long skeptic reviews can hit the usage limit.** Recover by sending a follow-up message to resume the session.

**Folders and sessions**
- **Renaming the project folder is blocked while the Claude app holds it.** Running session processes keep the folder as their working directory; quit the app first. Transcripts are stored under a folder named after the path, so rename that folder too (or move the chat's transcript).
- **Create files where they belong** (see the file-locations note); parked drafts confused the user.
- **Hooks and `CLAUDE.md` take effect in the next session, not the current one.**
- **Paywalled papers cannot be read.** Only open-access text is available; supplements and detail behind paywalls remain unseen unless the user supplies PDFs (not committed to the public repo).
