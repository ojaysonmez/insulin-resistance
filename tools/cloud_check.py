#!/usr/bin/env python3
"""First-run environment check for a new checkout (cloud session, new machine). No model, standard library only.

Prints PASS, WARN or FAIL for each thing the project's tools and scheduled runs depend on, with
the fix for anything that is not PASS. It changes nothing in the repository (it creates and removes
one temporary file in two folders to test that they are writable, and runs git push --dry-run).

Usage (project root):  python tools/cloud_check.py        (or python3 tools/cloud_check.py)
  --brief   what the session-start hook runs: skips the tests and the push dry-run, shows only problems, and stays silent
            when an earlier run on this platform (local or cloud) in this checkout passed less than 7 days ago
            (marker file .claude/env-check.json, git-ignored). A cloud session is a fresh clone, so it runs every time.
Exit code: 0 if there is no FAIL, 1 otherwise.
"""
import concurrent.futures
import datetime
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = []
BRIEF = False
MARKER = ROOT / ".claude" / "env-check.json"


def add(level, name, detail="", fix=""):
    RESULTS.append((level, name, detail, fix))


def run(cmd, timeout=60, cwd=ROOT):
    try:
        p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout + p.stderr).strip()
    except Exception as e:
        return 99, str(e)


def check_python():
    v = sys.version_info
    add("PASS" if v >= (3, 9) else "FAIL", "Python version", f"{platform.python_version()} at {sys.executable}",
        "Use Python 3.9 or newer (the project's scripts use only the standard library).")
    for name in ("python", "python3"):
        found = shutil.which(name)
        lvl = "PASS" if found else ("WARN" if name == "python" else "PASS")
        fix = ""
        if name == "python" and not found:
            fix = ("The hooks and scheduled-task prompts call `python`, which is missing here. Add an alias in the environment setup "
                   "(for example: ln -s \"$(command -v python3)\" /usr/local/bin/python) or change the commands to python3.")
        add(lvl, f"`{name}` on PATH", found or "not found", fix)


def check_packages():
    try:
        import openpyxl  # noqa: F401
        add("PASS", "openpyxl", f"version {openpyxl.__version__}")
    except Exception:
        add("FAIL", "openpyxl", "not installed",
            "Run: pip install openpyxl (or put it in the environment's setup script). Needed by tools/corpus_build.py, corpus_contacts.py and the tests.")


def check_files():
    need = ["CLAUDE.md", "HANDOFF.md", "DECISIONS.md", "usecases/scoring/queue.json", "update-watch/queries.json",
            "usecases-verified.md", "merged-conclusion.md", "tools/scoring_queue.py", "tools/watch_fetch.py"]
    miss = [f for f in need if not (ROOT / f).exists()]
    add("PASS" if not miss else "FAIL", "Project files present", "all found" if not miss else "missing: " + ", ".join(miss),
        "The checkout is incomplete: clone or pull the repository again.")
    agents = sorted(p.name for p in (ROOT / ".claude" / "agents").glob("ir-*.md"))
    add("PASS" if len(agents) >= 12 else "WARN", "Role files (.claude/agents)", f"{len(agents)} ir-* files",
        "Agent roles are missing; the scoring and watch units start roles by these names.")
    wf = list((ROOT / ".claude" / "workflows").glob("*.js"))
    add("PASS" if wf else "WARN", "Workflow files", f"{len(wf)} found", "Only needed for the optional pilot workflow.")


def check_settings():
    s, sl = ROOT / ".claude" / "settings.json", ROOT / ".claude" / "settings.local.json"
    add("PASS" if s.exists() else "FAIL", ".claude/settings.json", "present" if s.exists() else "absent",
        "A cloud session reads only this committed file. It holds the hooks and permission rules (see CLOUD-SETUP.md).")
    if sl.exists() and "hooks" in sl.read_text(encoding="utf-8"):
        add("WARN", ".claude/settings.local.json also defines hooks", "they would run twice on this machine",
            "Keep hooks in settings.json only.")
    remote = os.environ.get("CLAUDE_CODE_REMOTE")
    add("PASS", "Where this runs", "cloud session (CLAUDE_CODE_REMOTE set)" if remote else "local machine (CLAUDE_CODE_REMOTE not set)")
    for f in (s,):
        if f.exists():
            try:
                j = json.loads(f.read_text(encoding="utf-8"))
                hooks = j.get("hooks", {})
                perms = j.get("permissions", {})
                add("PASS", f"{f.name}: hooks and permissions", f"hook events {sorted(hooks)}; permission rules {sum(len(v) for v in perms.values())}")
            except Exception as e:
                add("FAIL", f"{f.name}: valid JSON", str(e), "Fix the JSON.")
    add("WARN", "Session-start hook (cannot be tested from a script)", "check by eye",
        "The first context of a new session should start with the IR project status brief. If it does not, the hooks are not loading.")
    env = os.environ.get("CLAUDE_PROJECT_DIR")
    add("PASS" if env else "WARN", "CLAUDE_PROJECT_DIR in this shell", env or "not set (normal in a plain shell; hooks get it from Claude Code)",
        "")


def check_git():
    rc, out = run(["git", "rev-parse", "--is-inside-work-tree"])
    if rc != 0:
        add("FAIL", "Git work tree", out[:120], "Run from a git checkout.")
        return
    _, br = run(["git", "branch", "--show-current"])
    _, remote = run(["git", "remote", "get-url", "origin"])
    add("PASS", "Git branch and remote", f"{br or '(detached)'} -> {remote[:70]}")
    _, name = run(["git", "config", "user.name"])
    _, mail = run(["git", "config", "user.email"])
    add("PASS" if name and mail else "WARN", "Git author configured", "yes" if name and mail else "missing",
        "Set git config user.name and user.email, or commits from a run will fail.")
    rc, out = run(["git", "ls-remote", "--heads", "origin"], timeout=45)
    add("PASS" if rc == 0 else "FAIL", "Read access to the remote", f"{len(out.splitlines())} branches" if rc == 0 else out[:120],
        "The remote is not reachable from here (network or credentials).")
    if BRIEF:
        return
    rc, out = run(["git", "push", "--dry-run", "origin", "HEAD"], timeout=60)
    add("PASS" if rc == 0 else "WARN", "Write access to the remote (git push --dry-run, nothing is pushed)",
        "accepted" if rc == 0 else out[-160:],
        "Pushing is not possible from here as configured. Runs that must save state need a credential or a branch they may push to.")


def check_write():
    for d in ("update-watch/runs", "usecases/scoring"):
        p = ROOT / d
        try:
            p.mkdir(parents=True, exist_ok=True)
            fd, tmp = tempfile.mkstemp(dir=str(p), prefix=".cloudcheck-")
            os.close(fd)
            os.remove(tmp)
            add("PASS", f"Writable: {d}")
        except Exception as e:
            add("FAIL", f"Writable: {d}", str(e)[:100], "The scheduled runs write their outputs here.")


def check_network():
    hosts = [("PubMed (E-utilities)", "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi?retmode=json"),
             ("Crossref", "https://api.crossref.org/works?rows=0"),
             ("ClinicalTrials.gov", "https://clinicaltrials.gov/api/v2/version"),
             ("PubMed Central pages", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8481000/")]
    def probe(item):
        name, url = item
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (ir-project environment check)"})
            with urllib.request.urlopen(req, timeout=8 if BRIEF else 20) as r:
                r.read(512)
                return ("PASS", f"Network: {name}", f"HTTP {r.status}", "")
        except Exception as e:
            return ("FAIL" if "PubMed" in name else "WARN", f"Network: {name}", str(e)[:90],
                    "Allow this host in the environment's network access settings.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
        for r in ex.map(probe, hosts):
            RESULTS.append(r)


def check_tests():
    for t in ("tools/test_scoring_tools.py", "tools/test_watch_to_queue.py", "tools/test_corpus_contacts.py"):
        rc, out = run([sys.executable, t], timeout=120)
        add("PASS" if rc == 0 else "FAIL", f"Offline tests: {t}", out.splitlines()[-1][:60] if out else "",
            "A test failed; run it by hand to see why (missing openpyxl is the usual cause).")


def check_queue():
    try:
        rc, out = run([sys.executable, "tools/scoring_queue.py", "status"])
        add("PASS" if rc == 0 else "FAIL", "Scoring queue readable", out.splitlines()[0][:110] if out else "")
    except Exception as e:
        add("FAIL", "Scoring queue readable", str(e)[:100])


def platform_tag():
    return "cloud" if os.environ.get("CLAUDE_CODE_REMOTE") else "local"


def marker_fresh():
    try:
        m = json.loads(MARKER.read_text(encoding="utf-8"))
        age = datetime.datetime.now() - datetime.datetime.fromisoformat(m["when"])
        return m.get("platform") == platform_tag() and m.get("fail", 1) == 0 and age < datetime.timedelta(days=7)
    except Exception:
        return False


def main():
    global BRIEF
    BRIEF = "--brief" in sys.argv
    if BRIEF and marker_fresh():
        return 0
    checks = [check_python, check_packages, check_files, check_settings, check_git, check_write, check_network, check_queue]
    if not BRIEF:
        checks.append(check_tests)
    if not BRIEF:
        print(f"Environment check, {datetime.datetime.now().isoformat(timespec='seconds')}; {platform.system()} {platform.release()}; folder {ROOT.name}\n")
    for fn in checks:
        try:
            fn()
        except Exception as e:  # a check must never stop the others
            add("FAIL", fn.__name__, str(e)[:120])
    if BRIEF:  # items that cannot be judged from a script are not counted or shown in the brief
        RESULTS[:] = [r for r in RESULTS if not r[1].startswith(("Session-start hook", "CLAUDE_PROJECT_DIR"))]
    n = {k: sum(1 for r in RESULTS if r[0] == k) for k in ("PASS", "WARN", "FAIL")}
    for lvl, name, detail, fix in RESULTS:
        if BRIEF and lvl == "PASS":
            continue
        if BRIEF and name.startswith(("Session-start hook", "CLAUDE_PROJECT_DIR")):
            continue
        print(f"[{lvl}] {name}" + (f": {detail}" if detail else ""))
        if lvl != "PASS" and fix:
            print(f"       fix: {fix}")
    if BRIEF:
        print(f"Environment check ({platform_tag()}): {n['PASS']} pass, {n['WARN']} warn, {n['FAIL']} fail; full check: python tools/cloud_check.py")
        try:
            MARKER.write_text(json.dumps({"when": datetime.datetime.now().isoformat(timespec="seconds"), "platform": platform_tag(),
                                          "fail": n["FAIL"]}), encoding="utf-8")
        except Exception:
            pass
    else:
        print(f"\n{n['PASS']} pass, {n['WARN']} warn, {n['FAIL']} fail")
    return 1 if n["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
