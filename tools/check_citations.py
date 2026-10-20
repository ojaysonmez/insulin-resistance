#!/usr/bin/env python3
"""Citation checker for the project's markdown files (DRAFT, not yet run).

What it does (no AI, no third-party packages, standard library only):
  1. Extracts PMIDs and DOIs from markdown files.
  2. Looks each PMID up in PubMed (NCBI E-utilities esummary) and each DOI in Crossref.
  3. Flags: PMID not found; DOI on the same line as a single PMID that does not match
     PubMed's DOI for that PMID (this would have caught the PMID 21617108 DOI mix-up);
     retractions, corrections and expressions of concern (PubMed publication type and
     Crossref updated-by); and identifiers whose DOI or PMID is missing in the files but
     known to the other database (so gaps can be filled).
  4. Writes a markdown report and an optional JSON file, with a cache so repeat runs
     only fetch what is new.

What it does NOT do: it cannot check that a claim in the text matches the paper. It
checks identity and notices only. A person or skeptic must still compare the title and
abstract with the claim. A link or a matching record is an address, not a check.

Usage (example, run from the project root):
  python tools/check_citations.py merged-conclusion.md usecases-verified.md \
      --out tools/citation-report.md --json tools/citation-report.json \
      --cache tools/.citation-cache.json

Environment variables (optional): NCBI_API_KEY (raises the rate limit),
CROSSREF_MAILTO (an address for Crossref's polite pool; never hard-coded here).
Exit code: 0 = nothing urgent, 1 = at least one urgent flag, 2 = usage or network failure.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PMID_BLOCK = re.compile(r"PMIDs?:?\s*((?:\d{6,8}(?:\s*(?:,|and|;|/|&|-)\s*)?)+)", re.I)
PUBMED_URL = re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d{6,8})", re.I)
DIGITS = re.compile(r"\d{6,8}")
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s|,;)\]>\"'`]+", re.I)
NOTICE_TYPES = {"retraction", "correction", "erratum", "expression_of_concern", "withdrawal",
                "removal", "partial_retraction", "addendum", "clarification"}
URGENT_TYPES = {"retraction", "expression_of_concern", "withdrawal", "removal", "partial_retraction"}

ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
CROSSREF = "https://api.crossref.org/works/"


def clean_doi(raw):
    d = urllib.parse.unquote(raw).strip().rstrip(".,;:)").lower()
    return d


def scan_file(path):
    """Return list of (line_no, pmids(set), dois(set)) for one markdown file."""
    out = []
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    for i, line in enumerate(text.splitlines(), 1):
        pmids = set()
        for m in PMID_BLOCK.finditer(line):
            pmids |= set(DIGITS.findall(m.group(1)))
        pmids |= set(PUBMED_URL.findall(line))
        dois = {clean_doi(d) for d in DOI_RE.findall(line)}
        if pmids or dois:
            out.append((i, pmids, dois))
    return out


class Cache:
    def __init__(self, path):
        self.path = Path(path) if path else None
        self.data = {"pubmed": {}, "crossref": {}}
        if self.path and self.path.exists():
            try:
                self.data = json.loads(self.path.read_text(encoding="utf-8"))
            except Exception:
                pass

    def save(self):
        if self.path:
            self.path.write_text(json.dumps(self.data, indent=1), encoding="utf-8")


def http_get(url, tries=4, pause=1.0):
    last = None
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ir-team-citation-check/0.1"})
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.status, r.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 404, ""
            last = e
        except Exception as e:  # network or timeout
            last = e
        time.sleep(pause * (2 ** k))
    raise RuntimeError(f"request failed after retries: {url} ({last})")


def fetch_pubmed(pmids, cache, delay):
    todo = [p for p in sorted(pmids) if p not in cache.data["pubmed"]]
    for i in range(0, len(todo), 150):
        batch = todo[i:i + 150]
        params = {"db": "pubmed", "id": ",".join(batch), "retmode": "json"}
        key = os.environ.get("NCBI_API_KEY")
        if key:
            params["api_key"] = key
        status, body = http_get(ESUMMARY + "?" + urllib.parse.urlencode(params))
        time.sleep(delay)
        try:
            res = json.loads(body).get("result", {})
        except Exception:
            res = {}
        for p in batch:
            rec = res.get(p)
            if not rec or "error" in rec:
                cache.data["pubmed"][p] = {"found": False}
                continue
            doi = ""
            for a in rec.get("articleids", []):
                if a.get("idtype") == "doi":
                    doi = clean_doi(a.get("value", ""))
            authors = rec.get("authors") or []
            cache.data["pubmed"][p] = {
                "found": True,
                "title": rec.get("title", ""),
                "first_author": authors[0].get("name", "") if authors else "",
                "year": (rec.get("pubdate", "") or "")[:4],
                "journal": rec.get("source", ""),
                "doi": doi,
                "pubtype": rec.get("pubtype", []),
            }
    return {p: cache.data["pubmed"].get(p, {"found": False}) for p in pmids}


def fetch_crossref(dois, cache, delay):
    mailto = os.environ.get("CROSSREF_MAILTO", "")
    for d in sorted(dois):
        if d in cache.data["crossref"]:
            continue
        url = CROSSREF + urllib.parse.quote(d, safe="/")
        if mailto:
            url += "?mailto=" + urllib.parse.quote(mailto)
        status, body = http_get(url)
        time.sleep(delay)
        if status == 404:
            cache.data["crossref"][d] = {"found": False}
            continue
        try:
            msg = json.loads(body).get("message", {})
        except Exception:
            cache.data["crossref"][d] = {"found": False, "error": "bad json"}
            continue
        notices = []
        for u in msg.get("updated-by", []) or []:
            notices.append({"type": (u.get("type") or "").lower(), "doi": u.get("DOI", ""),
                            "label": u.get("label", "")})
        is_notice_of = [(u.get("type") or "").lower() for u in msg.get("update-to", []) or []]
        title = (msg.get("title") or [""])[0]
        cache.data["crossref"][d] = {"found": True, "title": title, "notices": notices,
                                     "is_notice_types": is_notice_of,
                                     "container": (msg.get("container-title") or [""])[0]}
    return {d: cache.data["crossref"].get(d, {"found": False}) for d in dois}


def main():
    ap = argparse.ArgumentParser(description="Check PMIDs and DOIs in markdown files (identity and notices).")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", default="tools/citation-report.md")
    ap.add_argument("--json", default="")
    ap.add_argument("--cache", default="tools/.citation-cache.json")
    ap.add_argument("--no-network", action="store_true", help="extract and cross-check from cache only")
    ap.add_argument("--max", type=int, default=0, help="limit identifiers checked (0 = all), for a dry run")
    ap.add_argument("--refresh", action="store_true",
                    help="ignore cached records for the identifiers checked and fetch them again (use for the update watch: a cached record never shows a retraction posted after it was cached)")
    args = ap.parse_args()

    where = {}      # ("pmid"|"doi", id) -> list of "file:line"
    pairs = []      # (file, line, pmid, doi) for lines with exactly one of each
    for f in args.files:
        for ln, pmids, dois in scan_file(f):
            for p in pmids:
                where.setdefault(("pmid", p), []).append(f"{Path(f).name}:{ln}")
            for d in dois:
                where.setdefault(("doi", d), []).append(f"{Path(f).name}:{ln}")
            if len(pmids) == 1 and len(dois) == 1:
                pairs.append((Path(f).name, ln, next(iter(pmids)), next(iter(dois))))

    all_pm = sorted({i for k, i in where if k == "pmid"})
    all_doi = sorted({i for k, i in where if k == "doi"})
    if args.max:
        all_pm, all_doi = all_pm[:args.max], all_doi[:args.max]

    cache = Cache(args.cache)
    if args.refresh and not args.no_network:
        for p in all_pm:
            old = cache.data["pubmed"].pop(p, None)
            if old and old.get("doi"):
                cache.data["crossref"].pop(old["doi"], None)
        for d in all_doi:
            cache.data["crossref"].pop(d, None)
    delay = 0.12 if os.environ.get("NCBI_API_KEY") else 0.4
    pubmed, crossref = {}, {}
    if args.no_network:
        pubmed = {p: cache.data["pubmed"].get(p, {"found": False, "uncached": True}) for p in all_pm}
        crossref = {d: cache.data["crossref"].get(d, {"found": False, "uncached": True}) for d in all_doi}
    else:
        try:
            pubmed = fetch_pubmed(set(all_pm), cache, delay)
            # also check Crossref notices for DOIs that PubMed knows but the files do not list
            extra = {v["doi"] for v in pubmed.values() if v.get("found") and v.get("doi")}
            crossref = fetch_crossref(set(all_doi) | extra, cache, 0.15)
        except RuntimeError as e:
            cache.save()
            print("NETWORK FAILURE:", e, file=sys.stderr)
            return 2
        cache.save()

    urgent, notes, fill = [], [], []
    for p in all_pm:
        r = pubmed.get(p, {})
        if not r.get("found"):
            urgent.append(f"PMID {p}: not found in PubMed ({'not cached' if r.get('uncached') else 'lookup returned nothing'}); used at {', '.join(where[('pmid', p)][:3])}")
            continue
        types = [t.lower() for t in r.get("pubtype", [])]
        if "retracted publication" in types:
            urgent.append(f"PMID {p}: PubMed marks it as a RETRACTED PUBLICATION ({r['first_author']} {r['year']}, {r['title'][:90]}); used at {', '.join(where[('pmid', p)][:3])}")
        if r.get("doi") and r["doi"] not in {d for k, d in where if k == "doi"}:
            fill.append((p, r["doi"], r["first_author"], r["year"], r["title"]))
    # Evaluate every DOI fetched from Crossref: the ones written in the files AND the ones
    # PubMed knows for the listed PMIDs (a first version only evaluated the former, which
    # missed corrections and errata on papers cited by PMID alone).
    doi_to_pmid = {v["doi"]: p for p, v in pubmed.items() if v.get("found") and v.get("doi")}

    def used_at(d):
        locs = where.get(("doi", d)) or where.get(("pmid", doi_to_pmid.get(d, "")), [])
        via = "" if where.get(("doi", d)) else f" (via PMID {doi_to_pmid.get(d, '?')})"
        return ", ".join(locs[:3]) + via

    for d in sorted(crossref):
        r = crossref.get(d, {})
        if r.get("found"):
            seen_notices = set()
            for n in r.get("notices", []):
                t = n["type"]
                key = (t, n.get("doi", ""))
                if key in seen_notices:  # Crossref sometimes lists the same notice twice
                    continue
                seen_notices.add(key)
                line = f"DOI {d}: Crossref notice '{t}' ({n.get('label','')}, notice DOI {n.get('doi','')}); used at {used_at(d)}"
                (urgent if t in URGENT_TYPES else notes).append(line)
        elif not r.get("uncached"):
            notes.append(f"DOI {d}: not found in Crossref (may be a non-Crossref DOI or a typo); used at {used_at(d)}")
    for f, ln, p, d in pairs:
        r = pubmed.get(p, {})
        if r.get("found") and r.get("doi") and r["doi"] != d:
            urgent.append(f"{f}:{ln}: PMID {p} and DOI {d} appear together, but PubMed lists DOI {r['doi']} for that PMID (possible wrong DOI, or a different version of the paper)")

    lines = ["# Citation check report", "",
             f"Files: {', '.join(Path(f).name for f in args.files)}",
             f"Unique PMIDs: {len(all_pm)}; unique DOIs: {len(all_doi)}. Identity and notice check only; this does not verify that any claim matches its source.",
             "", f"## Urgent flags ({len(urgent)})"]
    lines += [f"- {u}" for u in urgent] or ["- none"]
    lines += ["", f"## Other notices ({len(notes)})"] + ([f"- {n}" for n in notes] or ["- none"])
    lines += ["", f"## DOIs PubMed knows that the files do not record ({len(fill)})",
              "Suggested fills for the identifier rule (PMID with a DOI recorded):"]
    lines += [f"- PMID {p}: https://doi.org/{d} ({a} {y}, {t[:80]})" for p, d, a, y, t in fill] or ["- none"]
    lines += ["", "## Records for manual spot check (PMID, first author, year, journal, title)"]
    for p in all_pm:
        r = pubmed.get(p, {})
        if r.get("found"):
            lines.append(f"- {p}: {r['first_author']} {r['year']}, {r['journal']}: {r['title'][:110]}")
    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    if args.json:
        Path(args.json).write_text(json.dumps({"urgent": urgent, "notes": notes, "fill": fill,
                                               "pubmed": pubmed, "crossref": crossref}, indent=1), encoding="utf-8")
    print(f"wrote {args.out}: {len(urgent)} urgent, {len(notes)} other notices, {len(fill)} DOI fills")
    return 1 if urgent else 0


if __name__ == "__main__":
    sys.exit(main())
