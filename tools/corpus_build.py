#!/usr/bin/env python3
"""Build and refresh the article corpus table (no model, standard library plus openpyxl).

Scope: every PMID cited in the files named with --from (default: merged-conclusion.md and
usecases-verified.md). For each article it fills the automatic columns (identity from PubMed,
integrity status from PubMed and Crossref notices, where the article is cited, the read level
written next to it, open-access status, local full-text files, overlap with the eLFA corpus by
DOI). The columns that need reading (role, design, population, measure type, assay, key numbers,
source passage, quality note, claims) are left for an extraction step and are PRESERVED when
this script is run again, so manual or agent-filled cells are never overwritten.

Writes corpus/corpus.xlsx (the working spreadsheet) and corpus/corpus.csv (generated copy for
version history). Full texts are NOT in the repository: corpus/fulltext/ is git-ignored.

Usage (project root):
  python tools/corpus_build.py [--from FILE ...] [--elfa "I:/My Drive/SCIENCE/eLFA Articles.xlsx"] [--no-network]
  python tools/corpus_build.py --check    offline and instant: says how many cited PMIDs are not in corpus/corpus.csv yet
                                          (silent when none); exit code 0 either way. Used by the session-start brief and
                                          the deliverable reminder so the corpus is rebuilt when citations change.
"""
import argparse
import csv
import datetime
import json
import re
import sys
import time
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_citations import (Cache, ESUMMARY, NOTICE_TYPES, URGENT_TYPES, clean_doi, fetch_crossref,  # noqa: E402
                             fetch_pubmed, http_get, scan_file)

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
COLUMNS = ["ID", "PMID", "DOI", "Title", "First author", "Journal", "Year", "PubMed type", "PMCID", "Open access (PMC)",
           "Integrity status", "Integrity note", "Cited in", "Use-case rows", "Read level (as recorded)",
           "Role in the work", "Design", "Population and size", "Measure type", "Assay or platform", "Key numbers",
           "Source passage", "Quality note", "Claims supported", "Full text local", "Also in eLFA corpus", "Notes", "Last checked"]
AUTO = {"PMID", "DOI", "Title", "First author", "Journal", "Year", "PubMed type", "PMCID", "Open access (PMC)",
        "Integrity status", "Integrity note", "Cited in", "Use-case rows", "Read level (as recorded)",
        "Full text local", "Also in eLFA corpus", "Last checked"}
READ_WORDS = [("full text", "full text"), ("full-text", "full text"), ("abstract", "abstract"), ("title only", "title only"),
              ("title level", "title only"), ("[recall]", "recall"), ("snippet", "snippet")]


def cited_locations(files):
    """pmid -> {'where': set of 'file: place', 'rows': set of ints, 'read': set of words}."""
    out = {}
    for f in files:
        path = ROOT / f
        name = path.stem
        heading = ""
        for ln in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if ln.startswith("#"):
                heading = re.sub(r"^#+\s*", "", ln).strip()[:70]
            row = re.match(r"^\|\s*(\d+)\s*\|", ln)
            for _, pmids, _d in scan_file_line(ln):
                for p in pmids:
                    o = out.setdefault(p, {"where": set(), "rows": set(), "read": set()})
                    if row:
                        o["rows"].add(int(row.group(1)))
                        o["where"].add(f"{name}: row {row.group(1)}")
                    else:
                        o["where"].add(f"{name}: {heading or 'text'}")
                    low = ln.lower()
                    for w, label in READ_WORDS:
                        if w in low:
                            o["read"].add(label)
    return out


def scan_file_line(line):
    """Reuse check_citations' scanner on a single line."""
    import tempfile
    from check_citations import PMID_BLOCK, PUBMED_URL, DIGITS
    pmids = set()
    for m in PMID_BLOCK.finditer(line):
        pmids |= set(DIGITS.findall(m.group(1)))
    pmids |= set(PUBMED_URL.findall(line))
    return [(0, pmids, set())] if pmids else []


def pubmed_extra(pmids):
    """PMCID and full author-less metadata not kept in the checker cache."""
    out = {}
    pmids = sorted(pmids)
    for i in range(0, len(pmids), 150):
        batch = pmids[i:i + 150]
        status, body = http_get(ESUMMARY + "?" + urllib.parse.urlencode({"db": "pubmed", "id": ",".join(batch), "retmode": "json"}))
        time.sleep(0.4)
        res = json.loads(body).get("result", {})
        for p in batch:
            r = res.get(p, {})
            pmc = ""
            for a in r.get("articleids", []):
                if a.get("idtype") == "pmc":
                    pmc = a.get("value", "")
            out[p] = {"pmcid": pmc, "pubdate": r.get("pubdate", "")}
    return out


def integrity(pm, cr, doi):
    types = " ".join(pm.get("pubtype", [])).lower()
    if "retracted publication" in types:
        return "RETRACTED", "PubMed marks it as a retracted publication"
    notes = []
    for dd in {doi} if doi else set():
        c = cr.get(dd, {})
        for n in c.get("notices", []) or []:
            t = n.get("type", "")
            if t in URGENT_TYPES:
                return "RETRACTED", f"Crossref notice {t} ({n.get('doi', '')})"
            if t in NOTICE_TYPES:
                notes.append(f"{t} ({n.get('doi', '')})")
    if "retraction of publication" in types:
        return "Retraction notice", "this record is the retraction notice"
    if notes:
        return "Correction or erratum", "; ".join(notes)[:200]
    return "Clean", ""


def load_elfa(path):
    if not path:
        return None
    try:
        import openpyxl
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        ws = wb["Literature Table"]
        rows = ws.iter_rows(values_only=True)
        hdr = next(rows)
        i = hdr.index("DOI")
        return {re.sub(r"^https?://(dx\.)?doi\.org/", "", str(r[i]).strip().lower()).rstrip(".,;)") for r in rows if r[i]}
    except Exception as e:
        print("note: eLFA workbook not read:", e, file=sys.stderr)
        return None


def fulltext_state(cid):
    d = CORPUS / "fulltext"
    has_txt, has_pdf = (d / f"{cid}.txt").exists(), (d / f"{cid}.pdf").exists()
    return "txt+pdf" if has_txt and has_pdf else "txt" if has_txt else "pdf" if has_pdf else "none"


def read_existing():
    f = CORPUS / "corpus.xlsx"
    if not f.exists():
        return {}
    import openpyxl
    ws = openpyxl.load_workbook(f).active
    rows = list(ws.iter_rows(values_only=True))
    hdr = list(rows[0])
    out = {}
    for r in rows[1:]:
        d = {h: v for h, v in zip(hdr, r)}
        if d.get("PMID"):
            out[str(d["PMID"])] = d
    return out


def write_xlsx(records):
    import openpyxl
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Corpus"
    ws.append(COLUMNS)
    for r in records:
        ws.append([r.get(c, "") for c in COLUMNS])
    fill_auto, fill_man = PatternFill("solid", fgColor="DCE6F1"), PatternFill("solid", fgColor="FDE9D9")
    for j, c in enumerate(COLUMNS, 1):
        cell = ws.cell(1, j)
        cell.font = Font(bold=True)
        cell.fill = fill_auto if (c in AUTO or c == "ID") else fill_man
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    widths = {"ID": 7, "PMID": 10, "DOI": 26, "Title": 50, "First author": 16, "Journal": 22, "Year": 6, "PubMed type": 20,
              "PMCID": 12, "Integrity note": 28, "Cited in": 36, "Use-case rows": 12, "Source passage": 36, "Quality note": 32, "Key numbers": 32}
    for j, c in enumerate(COLUMNS, 1):
        ws.column_dimensions[get_column_letter(j)].width = widths.get(c, 16)
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "E2"
    ws.auto_filter.ref = ws.dimensions
    lg = wb.create_sheet("Legend")
    lg.append(["Column group", "Meaning"])
    for a, b in [
        ("Blue headers", "Filled automatically by tools/corpus_build.py from PubMed, Crossref notices, the repository files and the local full-text folder; overwritten on every run."),
        ("Orange headers", "Filled by reading the article (extraction step or by hand); never overwritten by the script. Empty until extracted."),
        ("Integrity status", "Clean, Correction or erratum, RETRACTED, or Retraction notice, from PubMed publication types and Crossref notices at the date in 'Last checked'."),
        ("Cited in", "Where the article is cited in the two main documents (section or use-case row). 'Use-case rows' lists the row numbers."),
        ("Read level (as recorded)", "Words found on the same line as the citation (full text, abstract, title only, recall). Line-level only: a line with several papers shares them. The project's own read-level labels in the files are the reference."),
        ("Full text local", "txt, pdf or both in corpus/fulltext/ named by ID (git-ignored; never committed). 'none' if not stored."),
        ("Also in eLFA corpus", "yes if the DOI is in the separate eLFA Articles workbook (device-technology corpus); the content of that workbook is not copied."),
        ("Scope", "Pilot: every PMID cited in merged-conclusion.md and usecases-verified.md. DOIs without a PMID are not yet included."),
    ]:
        lg.append([a, b])
    lg.column_dimensions["A"].width = 26
    lg.column_dimensions["B"].width = 120
    for row in lg.iter_rows():
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(CORPUS / "corpus.xlsx")
    with (CORPUS / "corpus.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(COLUMNS)
        for r in records:
            w.writerow([str(r.get(c, "") if r.get(c) is not None else "") for c in COLUMNS])


def main():
    ap = argparse.ArgumentParser(description="Build or refresh the article corpus table (no model).")
    ap.add_argument("--from", dest="sources", nargs="+", default=["merged-conclusion.md", "usecases-verified.md"])
    ap.add_argument("--elfa", default="I:/My Drive/SCIENCE/eLFA Articles.xlsx")
    ap.add_argument("--no-network", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.check:
        cited = set(cited_locations(a.sources))
        try:
            with (CORPUS / "corpus.csv").open(encoding="utf-8", newline="") as f:
                have = {r["PMID"].strip() for r in csv.DictReader(f)}
        except Exception:
            have = set()
        new = sorted(cited - have, key=int)
        if new:
            print(f"corpus is {len(new)} cited article(s) behind (e.g. PMID {', '.join(new[:3])}); rebuild with: python tools/corpus_build.py")
        return 0
    CORPUS.mkdir(exist_ok=True)
    loc = cited_locations(a.sources)
    pmids = sorted(loc, key=int)
    cache = Cache(str(ROOT / "tools" / ".citation-cache.json"))
    existing = read_existing()
    if a.no_network:
        pm = {p: cache.data["pubmed"].get(p, {"found": False}) for p in pmids}
        # offline: keep the PMCID already in the workbook instead of blanking it
        extra = {p: {"pmcid": (existing.get(p, {}).get("PMCID") or ""), "pubdate": ""} for p in pmids}
        cr = cache.data["crossref"]
    else:
        pm = fetch_pubmed(set(pmids), cache, 0.4)
        dois = {v["doi"] for v in pm.values() if v.get("found") and v.get("doi")}
        cr = fetch_crossref(dois, cache, 0.15)
        cache.save()
        extra = pubmed_extra(pmids)
    elfa = load_elfa(a.elfa)
    have_ft = (CORPUS / "fulltext").is_dir()  # absent in a fresh clone (cloud): then keep the stored value, do not mark everything 'none'
    next_id = max([int(str(v["ID"])[1:]) for v in existing.values() if v.get("ID")] + [0]) + 1
    today = datetime.date.today().isoformat()
    records, missing = [], []
    for p in pmids:
        rec = existing.get(p, {})
        if not rec.get("ID"):
            rec["ID"] = f"C{next_id:03d}"
            next_id += 1
        m = pm.get(p, {})
        if not m.get("found"):
            missing.append(p)
        doi = m.get("doi", "") if m.get("found") else ""
        st, note = integrity(m, cr, doi) if m.get("found") else ("PMID not found", "")
        o = loc[p]
        rec.update({
            "PMID": p, "DOI": doi, "Title": m.get("title", ""), "First author": m.get("first_author", ""),
            "Journal": m.get("journal", ""), "Year": m.get("year", ""), "PubMed type": ", ".join(m.get("pubtype", [])[:3]),
            "PMCID": extra.get(p, {}).get("pmcid", ""), "Open access (PMC)": "yes" if extra.get(p, {}).get("pmcid") else "no PMC copy",
            "Integrity status": st, "Integrity note": note, "Cited in": "; ".join(sorted(o["where"]))[:300],
            "Use-case rows": ",".join(str(x) for x in sorted(o["rows"])), "Read level (as recorded)": ", ".join(sorted(o["read"])),
            "Full text local": fulltext_state(rec["ID"]) if have_ft else (rec.get("Full text local") or "unknown (no local folder)"),
            "Also in eLFA corpus": ("yes" if doi.lower() in elfa else "no") if elfa is not None and doi else (rec.get("Also in eLFA corpus") or ""),
            "Last checked": today})
        records.append(rec)
    write_xlsx(records)
    # ranked list of articles with no local text: most-cited first, so PDFs can be supplied by ID
    want = [r for r in records if r["Full text local"] == "none"]
    want.sort(key=lambda r: (-len(str(r["Cited in"]).split(";")), r["ID"]))
    L = ["# PDFs or texts wanted (generated by tools/corpus_build.py)", "",
         f"{len(want)} article(s) have no local text (no open PubMed Central copy was found). Save a PDF as `corpus/fulltext/<ID>.pdf` (and, if you like, a text version as `<ID>.txt`); the folder is git-ignored and the pre-commit check blocks it. Ranked by how many places cite the article.", "",
         "| ID | PMID | DOI | First author, year | Title | Cited in | Rows | Read level recorded | Integrity |", "|---|---|---|---|---|---|---|---|---|"]
    for r in want:
        L.append(f"| {r['ID']} | {r['PMID']} | {r['DOI']} | {r['First author']} {r['Year']} | {str(r['Title'])[:90]} | {len(str(r['Cited in']).split(';'))} | {r['Use-case rows']} | {r['Read level (as recorded)']} | {r['Integrity status']} |")
    if have_ft:  # the wanted list is only meaningful where the local full-text folder exists
        (CORPUS / "pdf-wanted.md").write_text(chr(10).join(L) + chr(10), encoding="utf-8")
    cnt = {}
    for r in records:
        cnt[r["Integrity status"]] = cnt.get(r["Integrity status"], 0) + 1
    print(f"corpus: {len(records)} articles -> corpus/corpus.xlsx and corpus/corpus.csv; integrity {cnt}; PMC copies {sum(1 for r in records if r['PMCID'])}; not found in PubMed {len(missing)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
