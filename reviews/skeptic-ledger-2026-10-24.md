# Skeptic review of the claim ledger, build step 3 (2026-10-24)

Scope: `claims/claims.csv` (323 rows) checked against `merged-conclusion.md` and `usecases-verified.md`. I checked every BL, CONF, ABS and UC-ABS row and every row whose status is not `supported` (217 rows), plus 20 random `supported` rows. Inputs: `claims/CLAIM-LEDGER.md`, `claims/build/usecases-notes.md`, `claims/build/citation-report-ledger.md`, `reviews/confidence-rederivation-2026-10-23.md`, `reviews/skeptic-stage3-2026-10-23.md`, `DECISIONS.md` (D-17, D-45). Nothing was edited except this file. Confidence statements here are judgements.

Method: scripted checks plus reading rows by hand. (1) claim_text against the deliverable, after removing markdown and splitting on "...": every merged-conclusion segment is found verbatim. Every UC claim_text equals "Patient type. Test. Final status" copied from the table cells, except the five truncations the build notes already list. (2) Every identifier in UC `source_ids` appears in that row's sources cell, and every sources-cell identifier is in `source_ids`. No invented identifiers were found in any row. (3) I recounted the section 2 counts from the table, and they match UC-COUNTS-01 to -05. (4) One PubMed metadata call (5 records: 37947085, 42265997, 39380079, 21441124, 26526047), used only for BL, CONF and disputed rows. It confirmed the identifiers, the PREVENT ΔC 0.004-0.005 cited in EV-22, and the dialysis point under MEAS-06.

`claims/build/merged-conclusion-notes.md` does not exist. Four rows say "see notes" (GL-18, GL-34, MEAS-36, EV-35), and those references point nowhere.

## 1. Rows needing correction

Severity: H = wrong against a settled decision or the file; M = status, source or caveat error that would mislead a summary editor; L = completeness.

| # | Sev | claim_id | field | current value | corrected value |
|---|---|---|---|---|---|
| 1 | H | UC-35 | status | unverified | qualified. The final status (Unsupported for (b)) was set by the user in D-45 after an abstract-level reading. The ledger rule "unverified when not determinable" relies on stale text in the sources and caveats columns. |
| 2 | H | UC-35 | read_level | "...title only (sources column); the status column says ... abstract level" | "PMIDs 26754418, 34449903, 36675721, 38017369: abstract (specialty review and skeptic, 2026-10-24; D-45); sources and caveats columns of the deliverable still say title only (deliverable to fix)" |
| 3 | H | UC-45 | status / read_level | unverified / title only (sources column) | qualified / "PMIDs 32184821, 21926287, 19937225: abstract (D-45); deliverable sources column stale" |
| 4 | H | UC-35, UC-45 | claim_text | Final status truncated before ": four cohorts read at abstract level..." / "...: the three postpartum cohorts are cross-sectional..." | The full status cell. The truncation removes exactly the text that resolves the read-level conflict. |
| 5 | M | MEAS-06 | status | disputed | qualified. The deliverable does not dispute the claim; it reports that two studies disagree. |
| 6 | M | MEAS-06 | caveats | "Very small studies; not re-read by the skeptic" | Add: "The 10-patient PD study (26526047) re-analysed the same 12 HD patients as 21441124 and found HOMA-IR weak in both groups, so the disagreement is partly a difference of analysis on overlapping patients (PubMed abstracts, checked in this review)." This is also a deliverable wording issue. |
| 7 | M | MEAS-30 | status | disputed | qualified (supported would also do). The file settles the conflict: the asymmetric form is adopted (MEAS-27). |
| 8 | M | MEAS-32 | status | disputed | qualified, with caveat "wording not yet re-reviewed". Pending re-review is not a dispute. |
| 9 | M | GL-32 | status | disputed | qualified. It is true that the paper says this; the file disputes the paper's reading of its own source, which belongs in `conflicts`. |
| 10 | M | GL-32 | read_level / source_ids | not stated / PMID 39380079 | "full text (per usecases-verified row 36)" / add DOI 10.1186/s13052-024-01767-x (PubMed-verified) |
| 11 | M | CONF-08 | status | disputed | supported or qualified. The main session already decided ("Use Set A's Low"). Under rule 4 a resolved conflict is not `disputed`. If the project wants rejected claims labelled, use one status for all of section "What is not supported as stated" and for the Corrections section (see section 3). |
| 12 | M | CONF-03, CONF-04 | source_ids / caveats | empty / "Whose figure: not named" | source_ids: reviews/confidence-rederivation-2026-10-23.md; reviews/skeptic-stage3-2026-10-23.md. caveats: "Main-session proposal (fasting 40-45%, TyG 25-35%) narrowed by the stage-3 skeptic to about 40% (35-45) and about 30% (25-35) and adopted; the deliverable states only the point figures." |
| 13 | L | CONF-02 | source_ids | "Set B skeptics; first-round skeptic" | add reviews/confidence-rederivation-2026-10-23.md; reviews/skeptic-stage3-2026-10-23.md (both keep 80-85%) |
| 14 | M | BL2 | depends_on | CONF-03; CONF-04; EV-07; EV-08; EV-09; ABS-01; ABS-02; ABS-03; TRI-23; TRI-31 | add TRI-01 (the DIETFITS/MA.32 sentence inside BL2), CONF-05, CONF-06, EV-25 |
| 15 | L | BL1 | depends_on | ...; EV-29 | add EV-06 (scope limit), TRI-02 and GL-11 (the IRIS exception that BL1 names), GL-35 and GL-36 (limits of the negatives). EV-29 is association evidence and does not bear on utility; keep it only as context. |
| 16 | L | BL1, GL-01 | read_level | "PMID 37947085: not stated" | "PMID 37947085: abstract (as stated in EV-22)" |
| 17 | L | BL3 | depends_on | EV-10; EV-11; GL-06 to GL-12 | add UC-COUNTS-05, UC-COUNTS-08 |
| 18 | M | EV-31, EV-32, EV-44, TRI-53, MEAS-01, MEAS-03, MEAS-47 | status | qualified | unverified, matching EV-19, EV-37 and MEAS-39 (the same "no identifier in the file" basis). The other option is to move those three to qualified. Either way, one rule. |
| 19 | M | MEAS-26, ABS-04, EV-12 (cutoff part), GL-29 | status vs EV-21, EV-23, EV-42, MEAS-35, TRI-48 | qualified vs unverified for labelled inferences | Pick one rule. I recommend `qualified` with caveat "inference (labelled in file)" for all of them: the deliverable itself labels them as inferences, and `unverified` should be kept for recall and unretrieved sources. |
| 20 | M | TRI-21 | status / reviewed_by | unverified / empty | qualified / usecases-verified rows 18 and 38 (reviewer M read the NCT07412028 record; section 6 item 9 agrees). It was not confirmed by a skeptic. |
| 21 | M | EV-01 | status / conflicts | supported / empty | qualified / "claims/build/citation-report-ledger.md: one retraction (PMID 24757230, cited only as do-not-cite in UC-08) and 18 correction or erratum notices on cited DOIs, not only the two EASL corrections" |
| 22 | M | MEAS-36 | source_ids | "2024 paper" | PMID 38549041 (the "2024 LC-MS/MS paper" in the same bullet; the next sentence, MEAS-37, says "the same 2024 paper" and uses this PMID). Mark it as inferred from context. |
| 23 | M | GL-34 | conflicts / status | conflict noted / qualified | Keep qualified, and flag the deliverable for correction: "Liu 2026 and ATTICA nulls" contradicts EV-20 (ATTICA is not a null). |
| 24 | M | GL-18 | conflicts | empty (issue sits in caveats) | Move it to conflicts: "the JDS criterion 'triggers genetic and antibody testing' vs 'neither changes ... work-up'; the EASL 'possible MASLD' passage also says 'requiring further tests'". This is an internal contradiction in the deliverable. |
| 25 | M | UC-19, UC-27, UC-32, UC-39, UC-40 | status | supported | qualified. The file header says the skeptic did not re-verify rows 5, 11, 19, 25, 27, 32, 35 and 39-45 ("confidence there is lower"); the ledger rule ignores that file-level caveat. UC-32 also rests partly on a title-only source (PMID 14602731). |
| 26 | L | UC-01 | status | qualified | supported, if the stated rule (a hedge only in the status column, or an open conflict) applies. Otherwise add "hedges in caveats" to the written rule, which would also make UC-02 qualified. |
| 27 | L | UC-10 | source_ids | (no PMC5867272) | add PMC5867272 (Igls 2018 full text read by the skeptic, named in the caveats) |
| 28 | L | UC-ABS-01 | source_ids | AAP 2023 obesity guideline | add PMID 36622115 (named in row 16 and section 4) |
| 29 | L | UC-ABS-05 | status | qualified | split it, or mark the threshold half `superseded` as in UC-ABS-10: row 10 says the skeptic read Igls 2018 in full (no numeric threshold). The Igls 2.0 half stands. |
| 30 | L | UC-01, -04, -06, -07, -09, -14, -16, -18, -27, -28, -30 | source_ids | identifiers in caveats left out | add the caveat identifiers that support the row (list in `claims/build/usecases-notes.md`); do not add PMID 24757230 (UC-08, retracted). |
| 31 | L | GL-10 | read_level | not stated | "full text (keyword windows), per usecases-verified row 12" |
| 32 | L | GL-45 | caveats | ADA 2025 and other ADA 2026 sections not yet read in full | add "ADA 2026 s3: Rec 3.13 read verbatim; last 59k characters unread (UC-45)" |
| 33 | L | All ABS and UC-ABS rows | search_log_ref | empty in ABS-01, -04 to -06, -09, -13, -21 and all 21 UC-ABS; elsewhere free text | Rule 3 requires file and string IDs, counts and records screened. Fill these from the searcher, steelman and reviewer reports, or write "search log not recorded in the deliverable" explicitly in every row. |
| 34 | L | ~136 PMIDs ledger-wide | source_ids | PMID without DOI | Add the PubMed-verified DOIs listed in `claims/build/citation-report-ledger.md` (CLAUDE.md identifier rule). |

Deliverable fixes found along the way. These are not ledger edits; the main session applies them after review:
- `usecases-verified.md` rows 35 and 45: the sources and caveats columns still say title only, which contradicts the status column and D-45.
- `merged-conclusion.md`:
  - line 26 says "ATTICA nulls".
  - line 18 contradicts itself (GL-18).
  - line 99 says pioglitazone-depression was read in full text, while lines 110 and 135 say no one read it in full.
  - line 36 has an unbalanced parenthesis (TRI-09 and TRI-10).
  - line 134 is missing a full stop ("AAP 2023 The OPTN").
  - line 95, in the steelman header, says "no retractions or corrections in Crossref", but the citation report lists corrections for two items in that section: Hopkins 2018 (10.1038/s41586-018-0343-4) and Claxton 2015 (10.3233/JAD-141791).

## 2. Coverage gaps (claims with no ledger row)

merged-conclusion.md (coverage is good; all body text except headings and connectives maps to rows):
1. Line 95, steelman section header: "PMIDs checked, no retractions or corrections in Crossref". No row, and the citation report contradicts it (see above).
2. Line 3: "The searcher and chemist roles were each run twice". No row.
3. Line 51: "Liver and kidney disease add a further limit to fasting insulin and HOMA-IR ... and to C-peptide" (the lead claim of the MEAS-22 to MEAS-26 block). No row.
4. Line 11: "DIETFITS used post-load insulin and no longer counts for fasting measures". It is only a TRI-01 caveat, but it is load-bearing for the BL2 figure, so it needs its own row.
5. Open gap 1: "two chemist 'gaps' were found by two-word queries" and the list of databases not searched. Open gap 4 (no study of cutoff crossing) is partly covered by ABS-05.

usecases-verified.md:
6. Section 3: 15 of the 18 numbered recall items have no row (items 1-12, 14, 15, 17, 18; only 13, 16 and the bariatric-threshold inline item became UC-ABS rows). Rule 1 says claims from memory get rows with read_level `recall` and status `unverified`. The builder treated them as uses rather than claims (note 13); they are still statements in the deliverable.
7. Section 4: about 25 source-gap statements have no row. They include H's Cryer 2009 full text, the NICTH/IAS reviews, and the accuracy of the factitious pattern; C's ADA 2026 s2/s14, ISPAD 2022 classification, AAP 2023 (403), the ES 2017 first-100k limit, Endocr Rev 2008, PROTECT and paediatric prediabetes screening; and M's ADA/APA 2004, ADA s2/4/8, AACE beyond 100k, AASLD beyond 100k, the JDS/ADA/AACE verbatim check, the lipodystrophy supplement, HINT2/STAR and the registries. Several are stale against the table and should be marked `superseded`: ADA 2026 s2 (read, row 6), ES 2017 (raw text read, row 16), JDS/ADA/AACE (verbatim, rows 12 and 13), AASLD (complete, row 14) and the first-trimester cohorts (abstract, D-45). These are exactly the items a summary editor could misuse.
8. Section 5, conflict 13: "Status vocabulary ... labels are not calibrated across reviewers" has no row. It qualifies every UC status and should be a row that every UC row depends on.
9. Section 5 conflicts 1-6 and 10-12 (resolved) and section 6 items 2-8: only UC-ABS-16, -19, -20 and -21 exist. Resolved conflicts can be one `superseded` row each, or one row that cites the section 5 resolution paragraph.
10. Header: "the skeptic did not re-verify rows 5, 11, 19, 25, 27, 32, 35 cohort papers, 39-45". No row and not applied to statuses (correction 25).

## 3. Status rule: what is being used, and whether it is sound

Rule found in the merged-conclusion rows:
- `supported`: a claim stated without a limiting qualifier.
- `qualified`: the file attaches a limiter in the same sentence (abstract or excerpt level, small n, scan level, single source). Absence claims are always qualified.
- `unverified`: the file says "not verified / not re-verified / not independently confirmed", or the claim rests on a title, on recall, or (inconsistently) on a missing identifier or a labelled inference.
- `disputed`: used for six different things (see below).
- `superseded`: used twice.

Rule found in the use-case rows (stated in note 1 of the build notes):
- Established or Limited with no qualifier gives `supported`; a qualifier in the status cell or an open conflict gives `qualified`.
- Research-only and Unsupported are handled the same way, so a plain "Unsupported" row is `supported`. Here the ledger status grades the deliverable's verdict, not the use.
- Not evaluated, or a status resting on recall or "not determinable", gives `unverified`.
- Columns that contradict each other give `unverified`.

Verdict: partly sound.
- Sound: treating Research-only and Unsupported as claims whose verdict can be supported. It is logically right, but it must be written into `claims/CLAIM-LEDGER.md` so that no one reads a `supported` "Unsupported" row as support for the use. Mapping Not evaluated to `unverified` is also right.
- Not sound, case 1: `disputed` is used for (a) claims the deliverable rejects (EV-51, EV-52, EV-53, CONF-08, ABS-11), (b) evidence conflicts the file merely reports (MEAS-06), (c) conflicts the file has resolved (MEAS-30), (d) pending re-review (MEAS-32), (e) a source that overstates its own source (GL-32), and (f) a genuinely unresolved reviewer disagreement (EV-28). Only (f) fits rule 4. Meanwhile the Corrections-section rows (GL-41, MEAS-46, EV-56, EV-57, MEAS-48), which are the same logical type as (a), are `supported`. Proposed rule: rejected or corrected claims get `superseded` with the replacement claim ID; `disputed` is kept for unresolved disagreement only.
- Not sound, case 2: the missing-identifier and labelled-inference cases go both ways (corrections 18 and 19).
- Not sound, case 3: the use-case rule uses the surface form of the status cell and ignores the file-level "not re-verified" caveat (correction 25). It also overrode a user decision by trusting stale columns (UC-35, UC-45).
- After these fixes, a summary editor can rely on "supported or qualified" as the design intends.

## 4. Spot-check of 20 random supported rows (seed 20261024)

The 20 rows: GL-45, GL-31, UC-38, EV-11, MEAS-08, UC-19, EV-04, GL-35, EV-55, UC-COUNTS-04, TRI-01, UC-COUNTS-01, GL-42, GL-07, MEAS-13, EV-49, EV-48, EV-60, MEAS-16, TRI-20.
- In all 20, claim_text and source_ids are faithful.
- Three findings, already in the table above: UC-19 should be qualified (correction 25); UC-38 conflicts with the MC row TRI-21 on NCT07412028 (correction 20); GL-45 lacks the ADA s3 partial-read caveat (correction 32).
- GL-07 could carry the Igls PMIDs from UC-10.

## 5. Claims that survived

- Every merged-conclusion claim_text is verbatim. No invented identifiers. The UC `source_ids` match the sources cells exactly.
- The counts in UC-COUNTS-01 to -05 match a recount.
- CONF rows are attached to the right quantities: CONF-02 to BL1 at 80-85%; CONF-03 to BL2 for fasting insulin and HOMA-IR at about 40%; CONF-04 to BL2 for TyG at about 30%; CONF-05 and CONF-06 are marked as earlier or other figures. Whose figure each is checks out against the rederivation and stage-3 reviews, apart from the attribution in correction 12.
- The PREVENT ΔC 0.004-0.005 (EV-22) matches the PubMed abstract.
- The retracted DiaPep277 paper appears only as a do-not-cite caveat.
- The builder correctly flagged the internal conflicts in UC-14, UC-35, UC-45, TRI-49 and EV-48.

## 6. Overall verdict

Not releasable as version 1 today; it can be released after one correction pass that needs no new searching. The ledger is faithful to the readable files at the level of text and identifiers, which is the hardest part. The problems are in the status layer and in coverage:
- UC-35 and UC-45 contradict D-45.
- `disputed`, inference and missing-identifier statuses are applied inconsistently (about 25 rows).
- The skeptic's "not re-verified" rows are marked `supported`.
- The absence rows have no search logs.
- About 136 PMIDs lack DOIs.
- About 40 section 3-5 statements in `usecases-verified.md` have no row.
- The merged-conclusion build notes that four rows cite are missing.

Corrections 1-25 and gaps 1, 6-8 and 10 should be done before release. The search-log and DOI gaps (corrections 33-34) could ship as an explicitly labelled known limitation of v1, if the main session records that decision in `DECISIONS.md`.
