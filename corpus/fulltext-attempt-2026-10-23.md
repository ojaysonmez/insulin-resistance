# Full-text retrieval attempt, 2026-10-23

Open-access routes only. No article text is in this file. Texts are stored locally in `corpus/fulltext/` (git-ignored). Items not in `corpus/corpus.csv` have no corpus ID and are stored as `P<PMID>.txt`. All PMID/DOI pairs were checked against PubMed esummary on 2026-10-23.

Routes: A = `tools/corpus_fulltext.py` (PMC XML), B = Europe PMC / PMC via the same reader, C = OpenAlex open-access location then society or repository page, D = web search for society page.

| Corpus ID | PMID | DOI | Route tried | Result |
|---|---|---|---|---|
| C074 | 34590174 (same paper as 34593612, DOI 10.2337/dci21-0043) | 10.1007/s00125-021-05568-3 | A (PMC8481000) | obtained |
| C020 | 21270186 | 10.2337/dc10-1293 | A (PMC3024335) | obtained |
| C029 | 24843502 | 10.1111/j.2040-1124.2010.00096.x | A (PMC4014971) | obtained |
| C039 | 26742109 | 10.1159/000443171 | A (PMC4849884) | obtained |
| C026 | 23413806 | 10.1111/dme.12159 | A (PMC3748788) | obtained |
| C091 | 36537518 | 10.1111/pedi.13426 | A (PMC10107883) | obtained |
| C100 | 37794142 | 10.1038/s43856-023-00369-8 | A (PMC10550998) | obtained |
| C121 | 40640995 | 10.5694/mja2.52717 | A (PMC12579922) | obtained |
| none | 37589043 (Gavigan 2023) | 10.1155/2023/9972132 | B (PMC10427225) | obtained, `P37589043.txt` |
| none | 27080317 (Hope 2016) | 10.3399/bjgp16X684961 | B (PMC4838443) | obtained, `P27080317.txt` |
| none | 31558459 (Lynam 2019) | 10.1136/bmjopen-2019-031586 | B (PMC6773323) | obtained, `P31558459.txt` |
| none | 32634859 (Carr 2020) | 10.1111/dme.14361 | B (PMC8086995, author manuscript) | obtained, `P32634859.txt` |
| none | 38252849 (Jones 2024) | 10.2337/dc23-1815 | B (PMC11655402) | obtained, `P38252849.txt` |
| none | 34362814 (ProDiGY) | 10.2337/dc21-0491 | B (PMC8929184) | obtained, `P34362814.txt` |
| none | 41086125 (Exeter calculator update) | 10.2337/dc25-1029 | C (University of Dundee repository PDF) | obtained, `P41086125.txt` (PDF text, layout not clean) |
| C093 | 36537527 (ISPAD 2022 classification) | 10.1111/pedi.13454 | B none; C OpenAlex closed; D ispad.org society PDF | obtained. A string search for "peptide" finds no match in the extracted text |
| C014 | 19088155 (Cryer 2009) | 10.1210/jc.2008-1410 | B none; C OUP PDF refused by server (HTTP 403, not worked around); D socendocrinology.com PDF | obtained from a third-party society page; publisher authorisation of that copy not verified |
| none | 33131101 (Foteinopoulou 2021) | 10.1111/dme.14449 | B none (not in PMC); C OpenAlex green copy at Edinburgh Research Explorer, file refused (HTTP 403) | not available |
| C025 | 23289766 (Besser 2013) | 10.1111/pedi.12008 | B none; C OpenAlex lists Zenodo 3437162 (record deleted by take-down, HTTP 410) and a Wiley PDF (HTTP 403) | not available |
| C033 | 25792383 | 10.1159/000375410 | B none; OpenAlex closed | not available |
| C058 | 32052124 | 10.1007/s00431-020-03606-7 | B none; OpenAlex closed | not available |
| none | 36368478 (Thomas 2022) | 10.1016/j.jclinepi.2022.10.022 | B none; C publisher PDF refused (HTTP 403) | not available |
| none | 19141587 (Placzkowski 2009) | 10.1210/jc.2008-2031 | B none; OpenAlex closed | not available |
| none | 36477488 (Endocrine Society 2023) | 10.1210/clinem/dgac596 | B none; OpenAlex lists OUP PDF, not tried after OUP 403 on the 2009 PDF | not attempted beyond lookup |
| none | 17595353 (Davis 2007) | 10.2337/dc06-2532 | B none | not available (not tried further) |

Not attempted (outside the 25-paper cap or no open route found in the lookups): the other 40-odd items in `corpus/pdf-wanted.md`.

Lookup count: about 36 (18 Europe PMC, 10 OpenAlex, 2 web searches, 6 direct file requests). PDFs were downloaded into the session scratchpad, not the repository; only extracted text is under `corpus/fulltext/`.
