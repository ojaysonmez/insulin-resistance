# Ledger build step 1: notes for `usecases-verified.md`

Built 2026-10-24 by a subagent (no web or PubMed search; file-only). Output: `claims/build/usecases-rows.csv` (header plus 83 rows). Not yet merged into `claims/claims.csv`; not reviewed.

## Row count
- 50 use-case rows: UC-01 to UC-50 (kind `status`). Status assigned: 16 supported, 30 qualified, 4 unverified (UC-35, UC-36, UC-44, UC-45).
- 12 count rows: UC-COUNTS-01 to -05 (section 2 table, one per line including Total) and UC-COUNTS-06 to -12 (the seven "Notes on the counts" bullets), kind `number`.
- 21 absence rows: UC-ABS-01 to UC-ABS-21 (sections 3 to 6), kind `absence`.
- Total 83.

Count check: the section 2 table was recounted from the Kind and Final status columns of section 1, and every cell matches (21/10/18/1 rows; 11/17/10/10/2 totals). The draft-row note (rows 1-19: 7/6/3/3) also matches. The pre-skeptic count (45 rows: 13/11/10/11) cannot be recounted from the file and is marked qualified (UC-COUNTS-08).

## Rows with no identifier in the sources column
These rows name documents only, with no PMID, DOI, PMC or registry ID in their sources cell. Their `source_ids` lists the document names as written; no identifiers were added from elsewhere in the file.
- UC-03: "Cryer 2009 abstract; PES 2015 full text" (PMIDs 19088155 and 25957977 appear in rows 1 and 2).
- UC-17: guideline consistency only (EASL, PCOS guideline, ES 2017, IRIS statement, ADA 2026 s3, AACE 2022); prediction-model papers not re-verified.
- UC-23: "ENETS 2016, full text" (PMID 26742109 appears in rows 1 and 22).
- UC-29: FDA Tzield label and EMA record (no identifier).
- Partly named only: UC-02, UC-05, UC-20, UC-21 (Cryer 2009 or PES 2015 without PMID), UC-24 (ENETS 2016), UC-31 (Holt 2021, Jones and Hattersley 2013), UC-32 (Jones and Hattersley 2013), UC-35 (PMDI), UC-36 (Endocrine Society 2017), UC-38 (PCOS guideline), UC-45 (ADA 2026 s3), UC-30 (FDA label).
- Absence rows with no named source: UC-ABS-02, -03, -06, -07, -08, -17 (recorded as "(none named)").
- No DOIs: most UC rows carry PMIDs only, because the sources column gives no DOI. CLAUDE.md asks for both; DOIs need adding later (with verification, not done here). UC-50 states "no DOI in any record".

## Identifiers in the caveats column but not in the sources column (not added to `source_ids`)
UC-01 (DOI 10.1210/jc.2008-1410); UC-04 (PMIDs 35416981, 26908106 and DOIs); UC-06 (PMIDs 33131101, 25572256, 41752170 and DOIs); UC-07 (PMID 41086125, DOIs for 23289766 and 21270186); UC-08 (PMID 24757230, retracted, cite-not); UC-09 (PMID 42633332); UC-10 (PMC5867272, PMIDs 34599533, 30501589 and DOIs); UC-14 (PMIDs 37364790, 37363821); UC-16 (PMID 36622115); UC-18 (NCT06856291, ISRCTN74144960, CTRI/2026/09/117733); UC-27 (PMIDs 37889837, 42146813 and DOIs); UC-28 (PMID 36272764, DOI); UC-30 (PMID 31180194). The main session should decide whether these become separate EV rows or join `source_ids`.

## Ambiguities and decisions taken
1. **Status mapping for Research-only and Unsupported.** The brief maps only Established/Limited, hedges, recall/not determinable and Not evaluated. Research-only and Unsupported rows were given `supported` when the row carries no hedge or dispute, `qualified` otherwise. A row was treated as hedged when its final status has a qualifier in parentheses or after a comma (for example "Established, as part of the panel"), or the row records an open conflict. "Recall" made a row `unverified` only when the status itself rests on recall or is "not determinable"; a [recall] caveat alone gave `qualified` (UC-03, UC-05, UC-10, UC-12, UC-21).
2. **UC-17** is counted as Unsupported, but its monitoring part is Not evaluated. Set to `qualified`, not `unverified`.
3. **UC-42, UC-43** have final status Unsupported, but their caveats say "Not evaluated: ... the source was not read directly". Set to `qualified`; could be argued `unverified`.
4. **UC-35, UC-45: internal conflict.** The status column (updated 2026-10-24) says the cohorts were read at abstract level by the specialty review and skeptic; the sources and caveats columns still say title only and "not determinable from the files". Set to `unverified` per the brief, with the conflict recorded in `conflicts`. The file needs one of the two columns corrected.
5. **UC-14: internal conflict.** The test column says "92% agreement" was confirmed (2026-10-24); the caveats column says it was "not rechecked by M". Recorded in `conflicts`.
6. **reviewer_verdict.** "not reviewed" was used where no review is named. Where a review is named but no verdict given (UC-17, UC-28, UC-46 to UC-50), "verdict not stated in row" was used, since "not reviewed" would contradict `reviewed_by`. "holds" or "holds with edit" was used only where the row states the reviewer's correction or confirmation; these are the builder's labels for that stated text.
7. **reviewed_by** lists only skeptic or specialty reviews named in the row. The H, C and M reviewers are not listed. The header of the file says the skeptic did not re-verify rows 5, 11, 19, 25, 27, 32, 35 (cohort papers) and 39-45; other rows were in the skeptic's scope, but are left empty unless the row names the skeptic.
8. **claim_text** is "Patient type: ...; Test: ...; Final status: ...", copied from the three columns. Cut by truncation in UC-14 (test), UC-17, UC-35, UC-43 and UC-45 (status). The labels "Patient type", "Test", "Final status" are added structure. The count-table rows are written as "Kind: column value; ..." using the table's own column headers.
9. **caveats** are verbatim segments of the caveats column joined by " ... "; the build script checked every segment against the file. UC-24 has an empty caveats column.
10. **Counts and absence rows.** `source_ids` for count rows is the merged table (or the documents the note names); read_level "n/a". Absence rows have empty `search_log_ref`, because the file names no search strings (rule 3 of `claims/CLAIM-LEDGER.md` not met; a later step must add them from the reviewer reports).
11. **Section 4 is out of date in places.** It still lists as unretrieved: the Igls 2018 threshold (row 10 says the skeptic read it), KDIGO 2022 (row 28 says it was scanned), ADA 2026 s2 (rows 6 and 49 say it was read), the ES 2017 rest (row 16 says the raw text was read), and the JDS and ADA 3.13/AACE verbatim checks (rows 12 and 13 say done). UC-ABS-05 and UC-ABS-10 carry this in `conflicts`; UC-ABS-10 is `superseded`. The section 5 header still lists "OPTN Policy 11" as unread, although row 10 says excerpts were read.
12. **Superseded absence claims.** UC-ABS-16 (M's "no mention of insulin resistance" in ADA 3.13) is `superseded` by the skeptic's verbatim read. UC-ABS-15 ("AASLD and ADA negatives (partial text)") is `qualified`, with a note that row 14 says the AASLD search is now complete.
13. **Section 3 items** are mostly recall-level uses, not absence claims; only the three statements of absence (AAP 2023, HAIR-AN criterion, post-bariatric threshold) were made into ABS rows.
14. **File header** says "Rows 1-19 are the draft rows. Rows 20-45 are new uses"; rows 46-50 were added later (skeptic and 2026-10-24). Not a ledger row.
15. **DOI format.** The ledger design says DOIs as https://doi.org/..; DOIs here are kept as the file writes them ("DOI 10.xxxx").
