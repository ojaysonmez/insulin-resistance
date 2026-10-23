#!/usr/bin/env python3
"""Tests for tools/scoring_queue.py and tools/scoring_aggregate.py (no network, no model).

Run from the project root:  python tools/test_scoring_tools.py
Uses a temporary folder with copies of the templates; never touches usecases/scoring/ of the project.
"""
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
import scoring_aggregate as agg  # noqa: E402
import scoring_queue as sq  # noqa: E402

PROJECT = HERE.parent


def run_q(root, *argv):
    buf = io.StringIO()
    old = sys.argv
    sys.argv = ["scoring_queue.py", "--root", str(root), *argv]
    try:
        with contextlib.redirect_stdout(buf):
            sq.main()
    finally:
        sys.argv = old
    return buf.getvalue().strip()


def run_cmd_exit(root, *argv):
    """Like run_q, but turns a non-zero return code into SystemExit."""
    old = sys.argv
    sys.argv = ["scoring_queue.py", "--root", str(root), *argv]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            rc = sq.main()
    finally:
        sys.argv = old
    if rc:
        raise SystemExit(rc)


def make_root():
    root = Path(tempfile.mkdtemp())
    t = root / "usecases" / "scoring" / "templates"
    t.mkdir(parents=True)
    for f in (PROJECT / "usecases" / "scoring" / "templates").glob("*.md"):
        shutil.copy(f, t / f.name)
    return root


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.root = make_root()

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def build(self):
        run_q(self.root, "add", "--id", "U1", "--agent", "ir-evidence-searcher", "--dims", "D7,D3", "--rows", "6,5")
        run_q(self.root, "add", "--id", "U2", "--agent", "ir-skeptic", "--rows", "6,5", "--template", "review",
              "--needs", "U1", "--inputs", "U1", "--pause-after")
        run_q(self.root, "add", "--id", "U3", "--agent", "ir-pcp", "--dims", "D1", "--rows", "6", "--needs", "U2")

    def test_order_dependencies_and_pause(self):
        self.build()
        self.assertEqual(json.loads(run_q(self.root, "next"))["id"], "U1")
        run_q(self.root, "done", "U1")
        self.assertEqual(json.loads(run_q(self.root, "next"))["id"], "U2")
        run_q(self.root, "done", "U2")
        self.assertTrue(run_q(self.root, "next").startswith("PAUSED"))
        run_q(self.root, "resume")
        self.assertEqual(json.loads(run_q(self.root, "next"))["id"], "U3")
        run_q(self.root, "done", "U3")
        self.assertTrue(run_q(self.root, "status").startswith("queue DONE"))

    def test_failure_retries_then_blocks(self):
        self.build()
        run_q(self.root, "fail", "U1", "--error", "boom")
        self.assertEqual(json.loads(run_q(self.root, "next"))["id"], "U1")
        run_q(self.root, "fail", "U1", "--error", "boom again")
        self.assertTrue(run_q(self.root, "next").startswith("BLOCKED"))

    def test_prompt_rendering(self):
        self.build()
        p = (self.root / "usecases/scoring/units/U1.md").read_text(encoding="utf-8")
        self.assertIn("Rows to score: 6, 5", p)
        self.assertIn("D7,D3", p)
        self.assertNotIn("{ROWS}", p)
        self.assertNotIn("{UNIT}", p)
        r = (self.root / "usecases/scoring/units/U2.md").read_text(encoding="utf-8")
        self.assertIn("usecases/scoring/U1.md and usecases/scoring/U1.json", r)

    def test_gate(self):
        g = lambda *a: run_q(self.root, "gate", *a)
        self.assertEqual(g("--pct5", "39", "--weekly", "30", "--hour", "3"), "START")
        self.assertTrue(g("--pct5", "41", "--weekly", "30", "--hour", "3").startswith("STOP"))
        self.assertEqual(g("--pct5", "64", "--weekly", "30", "--hour", "3", "--continue"), "CONTINUE")
        self.assertTrue(g("--pct5", "66", "--weekly", "30", "--hour", "3", "--continue").startswith("STOP"))
        self.assertTrue(g("--pct5", "10", "--weekly", "80", "--hour", "3").startswith("STOP: weekly"))
        data = sq.load(self.root)
        data["config"]["quiet_hours"] = [8, 18]
        sq.save(self.root, data)
        self.assertTrue(g("--pct5", "10", "--weekly", "10", "--hour", "10").startswith("STOP: quiet"))
        self.assertEqual(g("--pct5", "10", "--weekly", "10", "--hour", "20"), "START")

    def test_gate_without_usage_figures(self):
        g = lambda *a: run_q(self.root, "gate", *a)
        self.assertTrue(g().startswith("STOP: no usage figures"))
        self.assertTrue(g("--units-this-run", "0").startswith("START"))
        self.assertTrue(g("--units-this-run", "1", "--continue").startswith("CONTINUE"))
        self.assertTrue(g("--units-this-run", "2").startswith("STOP"))

    def test_claim_and_release(self):
        c = lambda *a: run_q(self.root, *a)
        self.assertEqual(c("claim", "--side", "local"), "claimed by local")
        self.assertEqual(c("claim", "--side", "local"), "claimed by local")
        with self.assertRaises(SystemExit):  # the other side is refused with a non-zero exit
            sys.argv = ["x"]
            run_cmd_exit(self.root, "claim", "--side", "cloud")
        self.assertEqual(c("claim", "--side", "cloud", "--force"), "claimed by cloud")
        self.assertEqual(c("release"), "released")
        self.assertEqual(c("claim", "--side", "cloud"), "claimed by cloud")

    def test_log(self):
        run_q(self.root, "log", "--unit", "U1", "--pct5-before", "10", "--pct5-after", "22", "--weekly-before", "30",
              "--weekly-after", "31", "--tokens", "70000", "--tools", "9")
        lines = (self.root / "usecases/scoring/usage-log.tsv").read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 2)
        self.assertTrue(lines[1].split("\t")[1] == "U1" and "70000" in lines[1])


def write_unit(root, unit, scores, extra=None):
    d = root / "usecases" / "scoring"
    d.mkdir(parents=True, exist_ok=True)
    j = {"unit": unit, "role": unit, "scores": [{"row": r, "dimension": dim, "score": v, "reason": "t", "sources": [], "confidence": "high", "origin": "project files"} for r, dim, v in scores]}
    j.update(extra or {})
    (d / f"{unit}.json").write_text(json.dumps(j), encoding="utf-8")


class AggregateTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        # row 6: strong; row 5: weak evidence and a role disagreement on D1; row 7: incomplete
        write_unit(self.root, "U1", [(6, "D7", 4), (6, "D3", 3), (5, "D7", 3), (5, "D3", 2), (7, "D7", 2)],
                   {"path_to_viability": [{"row": 5, "missing_piece": "agreed insulin criteria", "type": "guideline", "effort": "medium"}]})
        write_unit(self.root, "U2", [(6, "D2", 3), (6, "D8", 3), (5, "D2", 1), (5, "D8", 2), (7, "D2", None)])
        write_unit(self.root, "U3", [(6, "D4", 4), (5, "D4", 3)])
        write_unit(self.root, "U4", [(6, "D1", 3), (6, "D5", 3), (6, "D6", 4), (6, "S", 3), (5, "D1", 2), (5, "D5", 2), (5, "D6", 3), (5, "S", 3)],
                   {"settings": [{"row": 6, "setting": "routine care"}, {"row": 5, "setting": "specialist outpatient"}]})
        write_unit(self.root, "U5", [(6, "D1", 3), (6, "D5", 3), (6, "D6", 4), (6, "S", 3), (5, "D1", 4), (5, "D5", 2), (5, "D6", 3), (5, "S", 3)])

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_math_flags_and_ranking(self):
        by, pv, settings, issues, notes = agg.load_scores(self.root)
        out = agg.compute(by)
        r6, r5, r7 = out[6], out[5], out[7]
        self.assertAlmostEqual(r6["UQ"], 0.75)
        self.assertAlmostEqual(r6["R"], 0.875)
        self.assertAlmostEqual(r6["C"], 0.8)
        self.assertAlmostEqual(r6["composite"]["default"], 0.78125)
        self.assertAlmostEqual(r5["dims"]["D1"], 3.0)
        self.assertAlmostEqual(r5["UQ"], 0.5)
        self.assertAlmostEqual(r5["composite"]["default"], 0.59375)
        self.assertTrue(any("roles differ" in f for f in r5["flags"]))
        self.assertTrue(any("weak evidence" in f for f in r5["flags"]))
        self.assertFalse(any("roles differ" in f for f in r6["flags"]))
        self.assertNotIn("composite", r7)
        self.assertTrue(any("not determinable" in n for n in notes))
        self.assertEqual(agg.ranks(out, "default"), {6: 1, 5: 2})

    def test_outputs_written(self):
        by, pv, settings, issues, notes = agg.load_scores(self.root)
        out = agg.compute(by)
        ranked, inc = agg.write(self.root, out, pv, settings, issues, notes)
        self.assertEqual(ranked, [6, 5])
        self.assertEqual(inc, [7])
        md = (self.root / "usecases/scoring/ranking.md").read_text(encoding="utf-8")
        self.assertIn("routine care", md)
        self.assertIn("agreed insulin criteria", md)
        self.assertIn("Incomplete rows", md)
        js = json.loads((self.root / "usecases/scoring/ranking.json").read_text(encoding="utf-8"))
        self.assertIn("6", js["rows"])

    def test_bad_values_are_reported_not_ranked(self):
        write_unit(self.root, "U6", [(6, "D2", 9)])
        by, pv, settings, issues, notes = agg.load_scores(self.root)
        self.assertTrue(any("outside 0-4" in n for n in notes))
        self.assertEqual(sorted(v for _, v in by[(6, "D2")]), [3])


class SupersedeTests(unittest.TestCase):
    def test_later_unit_replaces_earlier_dimension(self):
        root = Path(tempfile.mkdtemp())
        try:
            write_unit(root, "U1", [(6, "D7", 4), (6, "D3", 3)])
            write_unit(root, "V7", [(6, "D7", 3)], {"supersedes": [{"unit": "U1", "dimensions": ["D7"]}]})
            by, pv, settings, issues, notes = agg.load_scores(root)
            self.assertEqual([v for _, v in by[(6, "D7")]], [3])
            self.assertEqual([v for _, v in by[(6, "D3")]], [3])
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
