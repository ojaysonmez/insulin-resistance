#!/usr/bin/env python3
"""Pre-commit check for the public IR repository.

Looks at what a commit would ADD (not old content) and blocks the commit if it finds:
  - a PDF, EPUB or Word file, or anything under corpus/fulltext/ (no PDFs or copyrighted full texts in the repository);
  - a Claude session ID of the form local_<hex> (local identifiers, kept out of the public repo);
  - an absolute Windows or Unix user path (CLAUDE.md: use project-relative paths);
  - something that looks like an API key, token or private key.
It only warns (does not block) about email addresses and files over 1 MB.

Usage:
  python tools/precommit_check.py                 check the staged changes (what the git hook runs)
  python tools/precommit_check.py --range A..B    check the changes between two commits (a dry run on history)

Enable the git hook once per clone:  git config core.hooksPath tools/githooks
Standard library only. Skipping the check with --no-verify is against the project rules.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

BLOCKED_SUFFIXES = {".pdf", ".epub", ".docx", ".doc"}
# Files that legitimately mention absolute paths or old names (history, rules, documentation).
PATH_CHECK_EXEMPT = {
    "CHANGELOG.md", "CONVENTIONS.md", "DECISIONS.md", "HANDOFF.md", "CLAUDE.md",
    "tools/README.md", "tools/precommit_check.py",
}
SELF = "tools/precommit_check.py"

SESSION_ID = re.compile(r"local_[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}")
ABS_PATH = re.compile(r"\b[A-Za-z]:[\\/]+(?:Users|dev|Program Files|Windows)\b|/Users/[A-Za-z]|/home/[a-z]")
SECRET = re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}|\bgh[pousr]_[A-Za-z0-9]{20,}|\bAKIA[0-9A-Z]{16}\b|-----BEGIN [A-Z ]*PRIVATE KEY-----")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}")


def git(*args):
    out = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return out.stdout


def main():
    diff_args = ["--cached"]
    if len(sys.argv) >= 3 and sys.argv[1] == "--range":
        diff_args = [sys.argv[2]]
    names = [n for n in git("diff", *diff_args, "--name-only", "--diff-filter=ACM").splitlines() if n]
    blocks, warns = [], []

    for n in names:
        if n.replace("\\", "/").startswith("corpus/fulltext/"):
            blocks.append(f"{n}: corpus full texts and PDFs must stay local (copyrighted)")
        if pathlib.PurePath(n).suffix.lower() in BLOCKED_SUFFIXES:
            blocks.append(f"{n}: document file type not allowed in the repository")
        p = ROOT / n
        try:
            if p.is_file() and p.stat().st_size > 1_000_000 and len(diff_args) == 1 and diff_args[0] == "--cached":
                warns.append(f"{n}: file is over 1 MB")
        except OSError:
            pass

    current = None
    for line in git("diff", *diff_args, "-U0", "--no-color", "--diff-filter=ACM").splitlines():
        if line.startswith("+++ b/"):
            current = line[6:]
            continue
        if not line.startswith("+") or line.startswith("+++") or current is None or current == SELF:
            continue
        text = line[1:]
        if SESSION_ID.search(text):
            blocks.append(f"{current}: contains a local_ session ID")
        if SECRET.search(text):
            blocks.append(f"{current}: looks like a key, token or private key")
        if current not in PATH_CHECK_EXEMPT and not current.startswith("memory/") and ABS_PATH.search(text):
            blocks.append(f"{current}: contains an absolute path (use project-relative paths)")
        if EMAIL.search(text):
            for m in EMAIL.findall(text):
                if "noreply" not in m:
                    warns.append(f"{current}: contains an email address ({m})")

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    for w in sorted(set(warns)):
        print("warning:", w)
    if blocks:
        print("COMMIT BLOCKED by tools/precommit_check.py:")
        for b in sorted(set(blocks)):
            print("  -", b)
        print("Fix the lines above and commit again. Do not skip the check with --no-verify.")
        return 1
    print("pre-commit check passed" + (f" ({len(names)} file(s))" if names else " (nothing staged)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
