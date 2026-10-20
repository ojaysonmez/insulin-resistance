#!/usr/bin/env python3
"""Tests for tools/watch_to_queue.py (no network, no model). Run from the project root:
  python tools/test_watch_to_queue.py
Uses a temporary folder; never touches the project's queue or signal log."""
import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import scoring_queue as sq  # noqa: E402
import watch_to_queue as w2q  # noqa: E402
import update_scorecard as usc  # noqa: E402

PROJECT = HERE.parent


def make_root():
    root = Path(tempfile.mkdtemp())
    t = root / "usecases" / "scoring" / "templates"
    t.mkdir(parents=True)
    for f in (PROJECT / "usecases" / "scoring" / "templates").glob("*.md"):
        shutil.copy(f, t / f.name)
    (root / "usecases-verified.md").write_text(
        "| # | Patient type | Test | Decision | Kind | Final status | Sources | Caveats |\n|---|---|---|---|---|---|---|---|\n"
        "| 13 | Stroke or TIA: pioglitazone | HOMA-IR | Start pioglitazone | IR | Limited | s | c |\n"
        "| 6 | Diabetes classification | C-peptide | Replace insulin | Classification | Established | s | c |\n", encoding="utf-8")
    return root


def run(root, signals):
    f = root / "signals.json"
    f.write_text(json.dumps(signals), encoding="utf-8")
    buf, err = io.StringIO(), io.StringIO()
    old = sys.argv
    sys.argv = ["watch_to_queue.py", str(f), "--root", str(root)]
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
            rc = w2q.main()
    finally:
        sys.argv = old
    return rc, buf.getvalue(), err.getvalue()


class SignalTests(unittest.TestCase):
    def setUp(self):
        self.root = make_root()

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_s2_queues_rescore_unit_and_logs(self):
        rc, out, err = run(self.root, {"date": "2026-10-21", "signals": [
            {"type": "S2", "rows": [13], "dimensions": ["D2", "D8"], "pmid": "11111111", "doi": "10.1/x", "read_level": "abstract", "note": "IRIS reanalysis by HOMA-IR stratum"}]})
        self.assertEqual(rc, 0, err)
        self.assertIn("1 rescore unit(s) queued", out)
        d = sq.load(self.root)
        u = [x for x in d["units"] if x["id"] == "R1"][0]
        self.assertEqual(u["rows"], [13])
        self.assertEqual(u["phase"], "rescore")
        prompt = (self.root / u["prompt"]).read_text(encoding="utf-8")
        self.assertIn("PMID 11111111", prompt)
        self.assertIn("D2, D8", prompt)
        self.assertIn("IRIS reanalysis", prompt)
        self.assertNotIn("{ROWS}", prompt)
        log = (self.root / "update-watch" / "signals.tsv").read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(log), 2)
        self.assertIn("rescore queued", log[1])

    def test_duplicate_signal_is_skipped(self):
        sig = {"date": "2026-10-21", "signals": [{"type": "S2", "rows": [13], "dimensions": ["D2"], "pmid": "22222222", "note": "n"}]}
        run(self.root, sig)
        rc, out, err = run(self.root, sig)
        self.assertIn("1 duplicate(s) skipped", out)
        self.assertEqual(len([u for u in sq.load(self.root)["units"] if u["id"].startswith("R")]), 1)

    def test_bad_input_is_rejected_not_queued(self):
        rc, out, err = run(self.root, {"signals": [
            {"type": "S9", "rows": [13], "pmid": "33333333"},
            {"type": "S2", "rows": [999], "pmid": "44444444"},
            {"type": "S2", "rows": [13], "pmid": "not-a-number"}]})
        self.assertEqual(rc, 1)
        self.assertEqual(len(sq.load(self.root)["units"]), 0)
        self.assertEqual(err.count("error:"), 3)

    def test_s5_is_urgent_and_not_queued_s4_logged(self):
        rc, out, err = run(self.root, {"date": "2026-10-21", "signals": [
            {"type": "S5", "rows": [6], "pmid": "55555555", "note": "retraction"},
            {"type": "S4", "rows": [], "pmid": "66666666", "note": "new use"}],
            "new_candidates": [{"pmid": "77777777", "doi": "10.1/z", "title": "A new use", "why": "guideline source"}]})
        self.assertEqual(rc, 0, err)
        self.assertEqual(len(sq.load(self.root)["units"]), 0)
        log = (self.root / "update-watch" / "signals.tsv").read_text(encoding="utf-8")
        self.assertIn("URGENT", log)
        self.assertEqual(log.count("new candidate"), 2)

    def test_rescore_units_are_not_read_as_scores(self):
        sc = self.root / "usecases" / "scoring"
        (sc / "R1.json").write_text(json.dumps({"unit": "R1", "scores": [{"row": 13, "dimension": "D2", "score": 4}], "proposals": []}), encoding="utf-8")
        import scoring_aggregate as agg
        by, pv, settings, issues, notes = agg.load_scores(self.root)
        self.assertEqual(by, {})

    def test_scorecard_shows_latest_signal(self):
        run(self.root, {"date": "2026-10-21", "signals": [{"type": "S2", "rows": [13], "dimensions": ["D2"], "pmid": "88888888", "note": "n"}]})
        self.assertEqual(usc.signals(self.root)[13], "S2 2026-10-21 (rescore queued)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
