#!/usr/bin/env python3
"""Tests for tools/apply_rescore.py, tools/watch_commit.py and the queue reopen rule (no network, no model).

Run from the project root:  python tools/test_autonomy.py
Everything happens in temporary folders; the project's own scores and repository are never touched.
"""
import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import apply_rescore as ar  # noqa: E402
import scoring_queue as sq  # noqa: E402
import watch_commit as wc  # noqa: E402


def run_ar(root, *argv):
    buf = io.StringIO()
    old = sys.argv
    sys.argv = ["apply_rescore.py", "--root", str(root), "--no-regenerate", *argv]
    try:
        with contextlib.redirect_stdout(buf):
            ar.main()
    finally:
        sys.argv = old
    return buf.getvalue()


def make_scores(root, entries):
    d = Path(root) / "usecases" / "scoring"
    d.mkdir(parents=True, exist_ok=True)
    (d / "V1.json").write_text(json.dumps({"unit": "V1", "scores": entries}), encoding="utf-8")


def make_r(root, name, proposals):
    d = Path(root) / "usecases" / "scoring"
    (d / f"{name}.json").write_text(json.dumps({"unit": name, "paper": {"pmid": "1"}, "proposals": proposals}), encoding="utf-8")


def prop(**kw):
    p = {"row": 11, "dimension": "D2", "current": 2, "proposed": 3, "reason": "r", "quote": "q", "confidence": "medium"}
    p.update(kw)
    return p


class ApplyRescore(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        make_scores(self.root, [{"row": 11, "dimension": "D2", "score": 2, "reason": "x"}, {"row": 5, "dimension": "D2", "score": 1}])

    def score(self):
        j = json.loads((self.root / "usecases" / "scoring" / "V1.json").read_text(encoding="utf-8"))
        return j["scores"][0]

    def test_one_point_change_is_applied_with_audit_trail(self):
        make_r(self.root, "R1", [prop()])
        out = run_ar(self.root, "--pending")
        self.assertIn("applied 1", out)
        e = self.score()
        self.assertEqual((e["score"], e["original_score"]), (3, 2))
        self.assertIn("D-48", e["correction"])
        self.assertIn("applied", (self.root / "usecases/scoring/rescore-log.tsv").read_text(encoding="utf-8"))

    def test_rerun_does_not_apply_twice(self):
        make_r(self.root, "R1", [prop()])
        run_ar(self.root, "--pending")
        self.assertIn("nothing to apply", run_ar(self.root, "--pending"))
        self.assertEqual(self.score()["score"], 3)

    def test_everything_else_needs_review_or_is_skipped(self):
        cases = [prop(proposed=4), prop(proposed=None), prop(confidence="low"), prop(quote=""), prop(current=3, proposed=4),
                 prop(dimension="D9"), prop(row=99), prop(proposed=2.5), prop(proposed=-1, current=0)]
        make_r(self.root, "R1", cases)
        out = run_ar(self.root, "--pending")
        self.assertIn("applied 0", out)
        self.assertEqual(self.score()["score"], 2)
        self.assertNotIn("original_score", self.score())
        self.assertEqual(out.count("needs review"), 8)
        self.assertEqual(out.count("no change"), 1)

    def test_two_entries_for_one_cell_need_review(self):
        make_scores(self.root, [{"row": 11, "dimension": "D2", "score": 2}, {"row": 11, "dimension": "D2", "score": 3}])
        make_r(self.root, "R1", [prop()])
        self.assertIn("applied 0", run_ar(self.root, "--pending"))

    def test_dry_run_changes_nothing(self):
        make_r(self.root, "R1", [prop()])
        out = run_ar(self.root, "--pending", "--dry-run")
        self.assertIn("would apply", out)
        self.assertEqual(self.score()["score"], 2)
        self.assertFalse((self.root / "usecases/scoring/rescore-log.tsv").exists())


class QueueReopen(unittest.TestCase):
    def test_new_unit_reopens_done_queue(self):
        root = Path(tempfile.mkdtemp())
        data = sq.load(root)
        data["status"] = "DONE"
        sq.save(root, data)

        class A:
            id, agent, phase, template, dims, rows, needs, inputs, extra, pause_after = (
                "R1", "x", "rescore", "rescore", "D2", "11", "", "", "e", False)
        t = root / "usecases" / "scoring" / "templates"
        t.mkdir(parents=True)
        for f in (HERE.parent / "usecases" / "scoring" / "templates").glob("*.md"):
            (t / f.name).write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            sq.cmd_add(A, root)
        self.assertEqual(sq.load(root)["status"], "RUNNING")


def git(cwd, *a):
    return subprocess.run(["git", *a], cwd=str(cwd), capture_output=True, text=True)


class WatchCommit(unittest.TestCase):
    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "config", "user.email", "t@example.org")
        git(self.repo, "config", "user.name", "t")
        (self.repo / "CHANGELOG.md").write_text("a\n", encoding="utf-8")
        (self.repo / "summary.md").write_text("top\n<!-- SCORECARD:START -->\nold\n<!-- SCORECARD:END -->\n", encoding="utf-8")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "init")
        self.old_root = wc.ROOT
        wc.ROOT = self.repo

    def tearDown(self):
        wc.ROOT = self.old_root

    def run_wc(self, *extra):
        old, buf = sys.argv, io.StringIO()
        sys.argv = ["watch_commit.py", "--message", "t", *extra]
        try:
            with contextlib.redirect_stdout(buf):
                rc = wc.main()
        finally:
            sys.argv = old
        return rc, buf.getvalue()

    def test_commits_only_allowed_files(self):
        (self.repo / "update-watch" / "runs").mkdir(parents=True)
        (self.repo / "update-watch" / "runs" / "2026-10-27-triage.md").write_text("x\n", encoding="utf-8")
        (self.repo / "CHANGELOG.md").write_text("b\n", encoding="utf-8")            # not allowed: must stay uncommitted
        (self.repo / "merged-conclusion.md").write_text("d\n", encoding="utf-8")   # deliverable: never
        rc, out = self.run_wc()
        self.assertEqual(rc, 0)
        files = git(self.repo, "show", "--name-only", "--format=", "HEAD").stdout.split()
        self.assertEqual(files, ["update-watch/runs/2026-10-27-triage.md"])
        st = git(self.repo, "status", "--porcelain").stdout
        self.assertIn("CHANGELOG.md", st)
        self.assertIn("merged-conclusion.md", st)

    def test_summary_only_inside_scorecard_block(self):
        (self.repo / "summary.md").write_text("top\n<!-- SCORECARD:START -->\nnew scorecard rows\n<!-- SCORECARD:END -->\n", encoding="utf-8")
        rc, out = self.run_wc()
        self.assertIn("committing 1 file", out)
        (self.repo / "summary.md").write_text("EDITED text\n<!-- SCORECARD:START -->\nnewer scorecard rows again\n<!-- SCORECARD:END -->\n", encoding="utf-8")
        rc, out = self.run_wc()
        self.assertIn("outside the scorecard block", out)
        self.assertIn("nothing to commit", out)

    def test_wrong_branch_and_nothing_to_do(self):
        rc, out = self.run_wc()
        self.assertEqual((rc, out.strip()), (0, "nothing to commit"))
        git(self.repo, "checkout", "-q", "-b", "other")
        rc, out = self.run_wc()
        self.assertEqual(rc, 2)


if __name__ == "__main__":
    unittest.main(verbosity=1)
