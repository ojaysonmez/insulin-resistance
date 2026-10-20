#!/usr/bin/env python3
"""Corresponding-author contacts for the corpus articles (no model, standard library plus openpyxl).

Reads the author front matter that PubMed Central (JATS XML: corresponding-author flags, emails,
affiliations with country) and PubMed (author affiliations, sometimes with an email) publish, and
writes LOCAL files only:
  corpus/local/contacts.xlsx   sheet 'Contacts' (one row per person and article) and 'People'
                               (one row per email, with the number of articles and use-case rows)
  corpus/local/contacts.csv    the same as CSV
corpus/local/ is git-ignored and the pre-commit check blocks it: it holds personal data (names and
published email addresses) that must not go into this public repository. This script prints
counts only, never names or addresses. Only addresses that the articles themselves publish are
collected. Affiliations are as of the publication date; check the current institution before use.

Usage (project root):  python tools/corpus_contacts.py [--delay SECONDS] [--max N]
Needs corpus/corpus.xlsx (python tools/corpus_build.py).
"""
import argparse
import csv
import datetime
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_citations import http_get  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LOCAL = ROOT / "corpus" / "local"
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
EMAIL = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
US_WORDS = re.compile(r"\b(USA|U\.S\.A\.?|United States(?: of America)?)\b", re.I)
US_STATE_ZIP = re.compile(r",\s*(?:[A-Z]{2}|[A-Z][a-z]+\.?)\s+\d{5}(?:-\d{4})?\b")
US_STATES = ("Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|"
             "Maine|Maryland|Massachusetts|Michigan|Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|New Mexico|New York|North Carolina|"
             "North Dakota|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming")
US_STATE_END = re.compile(r",\s*(?:%s|[A-Z]{2})\s*(?:\d{5})?\s*[.,;]?\s*(?:USA|United States)?\s*$" % US_STATES)


def text(el):
    return " ".join("".join(el.itertext()).split()) if el is not None else ""


US_ABBR = ("AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC").split()
_STATE_ALT = US_STATES + "|" + "|".join(US_ABBR)
US_TAIL = re.compile(r"[,(]\s*(?:" + _STATE_ALT + r")\b[^,;]*?(?:\d{5}(?:-\d{4})?)?\s*[.,;)]?\s*(?:USA|U\.S\.A\.?|United States(?: of America)?)?\s*(?:[.;]|$|\s[\w.%+-]+@)")
US_ORGS = re.compile(r"National Institutes? of Health|\bNIH\b|\bVA (?:Medical|Puget|Boston|Palo)|Veterans Affairs|\bCDC\b|Mayo Clinic|Cleveland Clinic|Joslin|Kaiser Permanente|\bJDRF\b", re.I)
COUNTRIES = ("China|Japan|India|Korea|South Korea|Taiwan|Thailand|Singapore|Malaysia|Iran|Iraq|Israel|Turkey|Saudi Arabia|Pakistan|Egypt|Greece|Italy|Spain|Portugal|France|Germany|Netherlands|Belgium|Switzerland|Austria|"
             "Sweden|Norway|Denmark|Finland|Poland|Czech Republic|Hungary|Romania|Russia|Ukraine|United Kingdom|UK|England|Scotland|Wales|Ireland|Canada|Australia|New Zealand|Brazil|Mexico|Argentina|Chile|Colombia|South Africa|Nigeria|Kenya|Qatar|Lebanon|Jordan")
COUNTRY_RX = re.compile(r"\b(" + COUNTRIES + r")\b\s*[.;]?\s*(?:[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,})?\s*\.?\s*$")


def first_affiliation(aff):
    """Several affiliations can be joined with ';': judge the first one when it is long enough to be one."""
    a = aff.strip()
    seg = a.split(";")[0].strip()
    return seg if len(seg) >= 15 else a


def is_us(aff):
    if not aff:
        return ""
    a = first_affiliation(aff)
    if COUNTRY_RX.search(a):
        return "no"
    if US_WORDS.search(a) or US_STATE_ZIP.search(a) or US_TAIL.search(a + ";") or US_ORGS.search(a):
        return "yes"
    return "no"


def country_of(aff):
    if not aff:
        return ""
    a = first_affiliation(aff)
    m = COUNTRY_RX.search(a)
    if m:
        c = m.group(1)
        return "UK" if c in ("United Kingdom", "England", "Scotland", "Wales") else c
    return "USA" if is_us(aff) == "yes" else ""


def pmc_contacts(pmcid):
    """People flagged as corresponding in the PubMed Central front matter, with emails and affiliations."""
    num = re.sub(r"\D", "", pmcid)
    status, body = http_get(EFETCH + "?" + urllib.parse.urlencode({"db": "pmc", "id": num, "retmode": "xml"}))
    art = ET.fromstring(body).find(".//article")
    meta = art.find(".//article-meta") if art is not None else None
    if meta is None:
        return []
    affs = {}
    for a in meta.iter("aff"):
        c = a.find(".//country")
        affs[a.get("id", "")] = (text(a), text(c))
    corresp_notes = {c.get("id", ""): text(c) for c in meta.iter("corresp")}
    people = []
    authors = [c for c in meta.iter("contrib") if c.get("contrib-type", "author") == "author"]
    for i, c in enumerate(authors):
        nm = c.find("name")
        if nm is None:
            continue
        name = (text(nm.find("given-names")) + " " + text(nm.find("surname"))).strip()
        rids = [x.get("rid", "") for x in c.findall("xref")]
        is_corr = c.get("corresp") == "yes" or any(r in corresp_notes for r in rids) or any(x.get("ref-type") == "corresp" for x in c.findall("xref"))
        emails = [text(e) for e in c.findall("email")]
        for r in rids:
            if r in corresp_notes:
                emails += EMAIL.findall(corresp_notes[r])
        aff_txt, ctry = "", ""
        for r in rids:
            if r in affs:
                aff_txt, ctry = affs[r]
                break
        role = "corresponding" if is_corr else ("first" if i == 0 else ("last" if i == len(authors) - 1 else "author"))
        people.append({"name": name, "emails": emails, "aff": aff_txt, "country": ctry, "corr": is_corr, "role": role, "idx": i, "n": len(authors)})
    # a corresponding author with no email of its own: match the loose emails of the notes by surname
    loose = []
    for t in corresp_notes.values():
        loose += EMAIL.findall(t)
    for e in meta.iter("email"):
        loose.append(text(e))
    loose = list(dict.fromkeys(loose))
    for p in people:
        if p["corr"] and not p["emails"]:
            sur = p["name"].split()[-1].lower() if p["name"] else ""
            p["emails"] = [e for e in loose if sur and sur[:5] in e.lower()]
            if not p["emails"] and len([q for q in people if q["corr"]]) == 1 and len(loose) == 1:
                p["emails"] = loose[:]
    return people


def pubmed_contacts(pmids):
    """From PubMed efetch: affiliations (with an email when the record has one). First and last author kept."""
    out = {}
    pmids = list(pmids)
    for i in range(0, len(pmids), 100):
        batch = pmids[i:i + 100]
        status, body = http_get(EFETCH + "?" + urllib.parse.urlencode({"db": "pubmed", "id": ",".join(batch), "retmode": "xml"}))
        time.sleep(0.4)
        for art in ET.fromstring(body).findall(".//PubmedArticle"):
            pmid = text(art.find(".//MedlineCitation/PMID"))
            auths = art.findall(".//AuthorList/Author")
            people = []
            for k, a in enumerate(auths):
                ln, fn = text(a.find("LastName")), text(a.find("ForeName"))
                if not ln:
                    continue
                affs = [text(x) for x in a.findall("AffiliationInfo/Affiliation")]
                emails = []
                for af in affs:
                    emails += EMAIL.findall(af)
                role = "first" if k == 0 else ("last" if k == len(auths) - 1 else "author")
                people.append({"name": f"{fn} {ln}".strip(), "emails": list(dict.fromkeys(emails)), "aff": affs[0] if affs else "", "country": "", "corr": False, "role": role, "idx": k, "n": len(auths)})
            out[pmid] = people
    return out


def main():
    ap = argparse.ArgumentParser(description="Corresponding-author contacts for the corpus (local files only).")
    ap.add_argument("--delay", type=float, default=1.0)
    ap.add_argument("--max", type=int, default=0)
    a = ap.parse_args()
    import openpyxl
    ws = openpyxl.load_workbook(ROOT / "corpus" / "corpus.xlsx")["Corpus"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = list(rows[0])
    recs = [dict(zip(hdr, r)) for r in rows[1:]]
    if a.max:
        recs = recs[:a.max]
    LOCAL.mkdir(parents=True, exist_ok=True)
    pm = pubmed_contacts([str(r["PMID"]) for r in recs])
    contacts, stats = [], {"pmc_ok": 0, "pmc_fail": 0}
    for r in recs:
        pmid = str(r["PMID"])
        found = []
        source = ""
        if r.get("PMCID"):
            try:
                people = pmc_contacts(str(r["PMCID"]))
                time.sleep(a.delay)
                stats["pmc_ok"] += 1
                found = [p for p in people if p["corr"] and (p["emails"] or p["aff"])]
                source = "PubMed Central front matter (corresponding author)"
                if not found:
                    found = [p for p in people if p["emails"]]
                    source = "PubMed Central front matter (email listed)"
            except Exception:
                stats["pmc_fail"] += 1
        if not found:
            people = pm.get(pmid, [])
            found = [p for p in people if p["emails"]]
            source = "PubMed affiliation (email listed)"
            if not found and people:
                # no email: keep the last and first author as likely contacts, flagged as such
                found = [p for p in people if p["role"] in ("last", "first")]
                source = "PubMed author list (no email; likely contact)"
        for p in found:
            aff = p["aff"] or next((q["aff"] for q in pm.get(pmid, []) if q["name"].split()[-1:] == p["name"].split()[-1:]), "")
            us = is_us(aff) if aff else ""
            ctry = country_of(aff) if aff else ""
            if not ctry and p["country"] and re.fullmatch(COUNTRIES + "|USA|United States", p["country"]):
                ctry = p["country"]
            if ctry in ("USA", "United States"):
                ctry, us = "USA", "yes"
            contacts.append({
                "ID": r["ID"], "PMID": pmid, "Article": f"{r['First author']} {r['Year']}: {str(r['Title'])[:90]}", "Use-case rows": r.get("Use-case rows") or "",
                "Contact name": p["name"], "Email": "; ".join(p["emails"]), "Role": p["role"], "Affiliation": p["aff"][:240], "Country": ctry, "US": us,
                "Source": source, "Confidence": "high" if "corresponding author" in source else ("medium" if p["emails"] else "low"),
                "Outreach status": "", "Notes": ""})
    cols = ["ID", "PMID", "Article", "Use-case rows", "Contact name", "Email", "Role", "Affiliation", "Country", "US", "Source", "Confidence", "Outreach status", "Notes"]
    # People sheet: one row per email
    people = {}
    for c in contacts:
        for em in [e for e in c["Email"].split("; ") if e]:
            k = em.lower()
            o = people.setdefault(k, {"Email": em, "Contact name": c["Contact name"], "Affiliation": c["Affiliation"], "Country": c["Country"], "US": c["US"], "Articles": set(), "Rows": set(), "Outreach status": "", "Notes": ""})
            o["Articles"].add(c["ID"])
            o["Rows"] |= {x for x in c["Use-case rows"].split(",") if x}
    wb = openpyxl.Workbook()
    ws1 = wb.active
    ws1.title = "Contacts"
    ws1.append(cols)
    for c in contacts:
        ws1.append([c[k] for k in cols])
    ws2 = wb.create_sheet("People")
    pc = ["Email", "Contact name", "Affiliation", "Country", "US", "Articles", "Use-case rows", "Outreach status", "Notes"]
    ws2.append(pc)
    for o in sorted(people.values(), key=lambda o: (o["US"] != "yes", -len(o["Articles"]))):
        ws2.append([o["Email"], o["Contact name"], o["Affiliation"], o["Country"], o["US"], ", ".join(sorted(o["Articles"])), ", ".join(sorted(o["Rows"], key=int)), "", ""])
    lg = wb.create_sheet("Read me")
    lg.append(["Personal data: published author contacts. LOCAL ONLY (git-ignored; blocked by the pre-commit check). Do not commit or paste into the repository."])
    lg.append([f"Generated {datetime.date.today().isoformat()} by tools/corpus_contacts.py from PubMed Central front matter and PubMed affiliations. Affiliations are as of publication; verify the current institution before contact. Confidence: high = flagged corresponding author in PubMed Central; medium = an email in the record; low = likely contact without an email."])
    for ws_ in (ws1, ws2):
        for cell in ws_[1]:
            cell.font = openpyxl.styles.Font(bold=True)
        ws_.freeze_panes = "A2"
        ws_.auto_filter.ref = ws_.dimensions
    wb.save(LOCAL / "contacts.xlsx")
    with (LOCAL / "contacts.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for c in contacts:
            w.writerow([c[k] for k in cols])
    arts = {c["ID"] for c in contacts}
    with_email = {c["ID"] for c in contacts if c["Email"]}
    us_email = {c["ID"] for c in contacts if c["Email"] and c["US"] == "yes"}
    us_people = [o for o in people.values() if o["US"] == "yes"]
    print(f"articles {len(recs)}; PubMed Central front matter read for {stats['pmc_ok']} (failed {stats['pmc_fail']}); contact rows {len(contacts)} for {len(arts)} articles")
    print(f"articles with at least one email: {len(with_email)}; with a US contact that has an email: {len(us_email)}")
    print(f"distinct email addresses: {len(people)}; US-affiliated: {len(us_people)}; unknown country: {sum(1 for o in people.values() if not o['US'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
