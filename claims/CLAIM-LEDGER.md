# Claim ledger: design (draft, not yet built)

> Paths: this file lives in `claims/`. The deliverables (`merged-conclusion.md`, `usecases-verified.md`) are in the project root; reviews are in `reviews/`; reports in `analysis/` and `usecases/`. Other files named here without a folder are in `claims/`.

Status: version 1 built 2026-10-24 (D-46): `claims.csv` holds the rows extracted from `merged-conclusion.md` and `usecases-verified.md` by two file-only agents (`claims/build/`), corrected after a skeptic sample (`reviews/skeptic-ledger-2026-10-24.md`). Known v1 limits: absence rows carry no search-string log (marked 'search log not recorded in the deliverable'); the ID-consistency script in Open points is not written.

## Why
Most corrections the skeptics made to `merged-conclusion.md` came from claims being copied from reports into the merged file with caveats lost (ATTICA filed as "small or no gain", PERSON called "matched", the presurgical metformin 0.07 treated as a replication, MA.32's 72 unadjusted tests dropped, the Rosli within-kit RSD read as between-kit disagreement, stale "single-source" tags). A ledger keeps each claim, its source, its read level and its caveats in one place, so the merged conclusion and the summary can be built from and checked against it. For the update system (`UPDATE-PLAN.md`) it also gives the weekly watch something specific to compare new evidence against.

## What it is
One row per claim in `claims.csv` (plain CSV, one header row). It is the project's source of truth for statements; `merged-conclusion.md` and `usecases-verified.md` are the readable views. If the two disagree, fix the one that is wrong and add a `CHANGELOG.md` entry.

## Columns
| Column | Meaning |
|---|---|
| claim_id | Stable ID. `BL1`-`BL3` bottom lines; `GL-xx` guideline claims; `EV-xx` evidence claims; `MEAS-xx` measurement; `TRI-xx` trials and interactions; `UC-xx` use-case rows (UC-01 = usecases-verified row 1); `ABS-xx` absence claims ("no trial found"); `CONF-xx` confidence figures |
| section | Section of the readable file where it appears |
| claim_text | The claim in one or two sentences, exactly as stated in the deliverable |
| kind | finding / number / status / absence / confidence / definition |
| source_ids | PMID, DOI (https://doi.org/..), registry ID or document URL, separated by `;` (identifier rule: record both PMID and DOI) |
| read_level | full text / abstract / title / second-hand / recall, per source if they differ |
| caveats | The qualifiers that must travel with the claim (design, population, multiplicity, assumptions, single-source) |
| status | supported / qualified / disputed / unverified / superseded |
| confidence | Stated figure or grade with what it is a judgement of (for absence claims: strings run and screened) |
| search_log_ref | For absence claims: the file and string IDs of the searches (empty otherwise) |
| reviewed_by | Skeptic or specialty review files that checked this claim, with date |
| reviewer_verdict | holds / holds with edit / disputed / not reviewed, plus one line |
| conflicts | Other claim IDs or sources that disagree, and how it was resolved (main session decides, with the reason) |
| depends_on | Claim IDs this one is built from (a bottom line depends on its supporting claims) |
| last_checked | Date of the last check against the source |
| changelog_ref | CHANGELOG entry date or PENDING ID that last changed the row |

## Rules
1. **No claim in a deliverable without a row, and no row without a source.** A claim from memory gets read_level `recall` and status `unverified` until someone retrieves it.
2. **Caveats are mandatory.** A row with a number must carry the design, population and any multiplicity or assumption that limits it. When the deliverable is written from the ledger, the caveats are copied with the claim.
3. **Absence claims name their searches.** `ABS` rows list the strings run, the counts and how many records were screened; "not found in the screened records" is the default wording.
4. **Conflicts stay visible.** When two reviewers disagree, both verdicts go in `reviewer_verdict`/`conflicts`; the main session picks the status and writes the reason. It does not average or smooth.
5. **Status changes only through the gate** in `UPDATE-PLAN.md` (triage, then a skeptic review) and get a CHANGELOG entry. The weekly watch never edits the ledger; it proposes changes in `PENDING.md` that name claim IDs.
6. **Confidence figures are rows too** (`CONF-xx`), with what they are a judgement of and whose figure it is (for example the skeptics' 80-85% for bottom line 1), so the same number cannot be attached to two different quantities.
7. **Citation check.** Before a ledger release, run `check_citations.py` over the readable files and the ledger's `source_ids`; fix flags before reviewers see it.

## Status rule (written 2026-10-24, from the skeptic sample)
- `supported`: the deliverable states the claim without a limiting qualifier. For a use-case row the status grades the deliverable's verdict, not the use: a plain "Unsupported" or "Research-only" row can be `supported` (the verdict is supported), which is not support for the use.
- `qualified`: the deliverable attaches a limiter (abstract, excerpt or scan level, small n, single source, labelled inference, no identifier in the file, a resolved conflict, pending re-review, or a file-level "not re-verified" caveat). All absence claims are `qualified`.
- `unverified`: recall, title-only or unretrieved sources, or a Not evaluated use-case row.
- `disputed`: the deliverable rejects the claim, or two sources disagree and the main session has not resolved it.
- `superseded`: replaced by a later row or decision.

## How it is used
- **Merge:** the main session edits ledger rows, then updates the readable view; a skeptic compares the view to the ledger, not just to the reports.
- **Summary editor:** traces each summary sentence to claim IDs; every ID must have status supported or qualified, otherwise the sentence carries the uncertainty label.
- **Update watch:** `PENDING.md` entries name the claim IDs they could change; the monthly triage reads the ledger rows rather than re-reading the whole conclusion.
- **Re-running searches after improvements:** a new search run proposes row changes; absence rows list which searches to repeat.

## Building the first version (not done)
1. An agent (subagent, no search) reads `merged-conclusion.md` and `usecases-verified.md` and writes one row per statement, copying caveats and sources exactly; it adds nothing and flags any statement it cannot source. Expect roughly 150 to 250 rows.
2. Run `check_citations.py` on the two files and the CSV.
3. A skeptic checks a sample of rows (all `ABS`, `CONF` and `BL` rows, and every row with status other than supported) against the readable files and primary sources.
4. Record the build in `CHANGELOG.md`. From then on, edits go ledger first.

## Examples (illustrative, not seeded in `claims.csv`)
| claim_id | claim_text | source_ids | read_level | caveats | status |
|---|---|---|---|---|---|
| TRI-03 | MA.32 exploratory interaction analyses with baseline insulin and HOMA are compatible with chance | PMID 42063220; PMID 35608580 | full text (interaction paper); abstract (main trial) | 72 unadjusted interaction tests, up to 4 expected by chance; invasive disease-free survival interactions null; authors say variables failed to predict an effect | supported |
| MEAS-02 | Rosli 2022's 1.7-23.2% is the within-kit RSD, not disagreement between kits | PMID 35622611 | full text | One pooled serum; three of seven kits are automated CLIA platforms | supported |
| ABS-01 | No randomized trial comparing IR-measurement-guided care with usual care was found | (search strings in the searcher's log) | n/a | Convergent searches across PubMed and registries; ICTRP first pages only; "not found in the screened records" | qualified |
| CONF-02 | "Shown not to add value" is about 45-50% likely true | n/a | n/a | A judgement, not a computation; the steelman skeptic's own figure is 45-55% | qualified |

## Open points
- Whether the ledger is a CSV, a table in markdown, or a small JSON file; CSV is easiest to diff in git and for a script to read.
- Who owns it: the main session, with agents proposing changes. Agents never edit it directly during a run.
- ID and source consistency: `tools/check_ledger.py` (written 2026-10-24) checks columns, unique IDs, status values, one UC row per use case, dangling depends_on/conflicts IDs, and PMIDs cited in the readable files versus the ledger; report in `claims/build/ledger-check.md`. Run it after every ledger or deliverable edit. It does not yet check claim IDs cited inside the readable files (none are cited there yet).
