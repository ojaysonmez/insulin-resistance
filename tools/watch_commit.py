#!/usr/bin/env python3
"""Commit (and optionally push) the files the daily runs are allowed to save. No model, standard library only.

Used by the scheduled update watch and scoring runner (D-48). It stages ONLY files that match the allow list below,
leaves every other change (yours included) alone, never touches the deliverables, and works only on branch main.
summary.md is committed only when its diff is confined to the generated scorecard block.

Usage (project root):
  python tools/watch_commit.py --message "Daily watch 2026-10-27: 12 records, 1 entry" [--push] [--dry-run]
Exit codes: 0 done or nothing to do, 2 wrong branch, 3 git failure, 4 push failed (the commit stays local).
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALLOW = [re.compile(p) for p in (
    r"^update-watch/runs/.+",
    r"^update-watch/(seen-pmids\.txt|registry-baseline\.json|signals\.tsv|URGENT\.md)$",
    r"^usecases/scoring/(queue\.json|usage-log\.tsv|rescore-log\.tsv|ranking\.json|ranking\.md)$",
    r"^usecases/scoring/R\d+\.(md|json)$",
    r"^usecases/scoring/units/R\d+\.md$",
    r"^usecases/scoring/[UV]\d+\.json$",
    r"^corpus/(corpus\.csv|corpus\.xlsx|pdf-wanted\.md)$",
    r"^summary\.md$",
)]
TRAILER = "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
START, END = "<!-- SCORECARD:START -->", "<!-- SCORECARD:END -->"


def git(*args, check=False, raw=False):
    p = subprocess.run(["git", *args], cwd=str(ROOT), capture_output=True, text=True)
    if check and p.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {(p.stdout + p.stderr).strip()[:300]}")
    out = p.stdout + p.stderr
    return p.returncode, (out if raw else out.strip())


def changed_files():
    rc, out = git("status", "--porcelain=v1", "-z", "--untracked-files=all", raw=True)
    files = []
    for ent in out.split("\0"):
        if len(ent) > 3:
            files.append(ent[3:].replace("\\", "/"))
    return files


def outside_block(text):
    i, k = text.find(START), text.find(END)
    return text[:i] + text[k:] if 0 <= i < k else text


def summary_confined():
    rc, old = git("show", "HEAD:summary.md", raw=True)
    if rc:
        return False
    new = (ROOT / "summary.md").read_text(encoding="utf-8")
    return outside_block(old.replace("\r\n", "\n")).strip() == outside_block(new.replace("\r\n", "\n")).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--message", required=True)
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    rc, branch = git("branch", "--show-current")
    if branch != "main":
        print(f"not on main (on '{branch}'); nothing committed")
        return 2
    cand, skipped = [], []
    for f in changed_files():
        if any(p.match(f) for p in ALLOW):
            if f == "summary.md" and not summary_confined():
                skipped.append("summary.md (changed outside the scorecard block)")
                continue
            cand.append(f)
    if skipped:
        print("not committed: " + "; ".join(skipped))
    if not cand:
        print("nothing to commit")
        return 0
    print(f"{'would commit' if a.dry_run else 'committing'} {len(cand)} file(s): " + ", ".join(cand[:8]) + (" ..." if len(cand) > 8 else ""))
    if a.dry_run:
        return 0
    try:
        git("add", "--", *cand, check=True)
        git("commit", "-m", a.message + "\n\n" + TRAILER, "--", *cand, check=True)
    except RuntimeError as e:
        print(f"commit failed: {e}")
        return 3
    print("committed")
    if not a.push:
        return 0
    rc, out = git("push", "origin", "main")
    if rc:
        rc2, out2 = git("pull", "--rebase", "origin", "main")  # refused by git if other local edits are unstaged
        if rc2:
            git("rebase", "--abort")
            print(f"push failed and rebase was not possible; the commit stays local ({out[-120:]})")
            return 4
        rc, out = git("push", "origin", "main")
        if rc:
            print(f"push failed after rebase; the commit stays local ({out[-120:]})")
            return 4
    print("pushed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
