# Article corpus (pilot)

Every article cited in `merged-conclusion.md` and `usecases-verified.md`, one row per article, in a spreadsheet. Pilot scope: PubMed IDs only (143 articles on 2026-10-20). Decision D-34.

| File | What it is |
|---|---|
| `corpus.xlsx` | The working spreadsheet (sheets `Corpus` and `Legend`). Blue headers are filled automatically; orange headers are filled by reading the article and are never overwritten by the script |
| `corpus.csv` | Generated copy of the same table, for version history (the `.xlsx` shows no useful changes in git). Do not edit it by hand |
| `pdf-wanted.md` | Generated, ranked list of articles that have no local text yet, so PDFs can be supplied by ID |
| `fulltext/` | LOCAL ONLY (git-ignored, blocked by the pre-commit check): `C001.txt`, `C001.pdf` and so on, named by the article ID. Full texts are copyrighted and are never committed |

## Columns
- **Automatic (blue):** PMID, DOI, title, first author, journal, year, PubMed type, PMCID, open access (a PubMed Central copy exists), integrity status (Clean, Correction or erratum, RETRACTED, from PubMed and Crossref notices), where it is cited, the use-case rows, the read level written next to the citation (line-level only), local full text (txt, pdf, both, none), also in the eLFA corpus (yes or no by DOI; that separate device-technology workbook is not copied), last checked.
- **To fill by reading (orange):** role in the work (key evidence, context, counter-evidence, do not cite), design, population and size, measure type (fasting-based, post-load or mixed-meal, non-insulin surrogate, C-peptide), assay or platform, key numbers, source passage (section or quote so a number can be re-checked), quality note, claims supported, notes. They are empty until an extraction step fills them.

## Commands (project root)
```
python tools/corpus_build.py              # refresh the table from the two documents (network: PubMed, Crossref)
python tools/corpus_build.py --no-network # refresh from the local caches only (keeps the PMCIDs already stored)
python tools/corpus_fulltext.py           # store open full texts (PubMed Central) in corpus/fulltext/
```
Re-running never overwrites the orange columns. New PMIDs get the next ID (C144, ...); IDs never change.

## Limits
- PubMed IDs only: DOIs cited without a PMID (and papers outside PubMed) are not in yet.
- "Read level (as recorded)" is taken from the words on the same line as the citation, so a line that cites several papers shares them; treat it as a hint, not as the verified read level.
- 53 articles have no open copy (listed in `pdf-wanted.md`); open access in PubMed Central does not always mean free reuse of the text.
