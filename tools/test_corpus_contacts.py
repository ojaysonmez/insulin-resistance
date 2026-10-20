#!/usr/bin/env python3
"""Tests for the US and country detectors in tools/corpus_contacts.py (no network). Run from the project root:
  python tools/test_corpus_contacts.py"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_contacts as cc  # noqa: E402

CASES = [
    ("Joslin Diabetes Center and Harvard Medical School, Boston, Massachusetts", "yes", "USA"),
    ("National Institutes of Health, Bethesda, Maryland;", "yes", "USA"),
    ("Yale University, New Haven, CT (K.C.H.); the Departments of Epidemiology, University of Oxford, Oxford, UK", "yes", "USA"),
    ("Baylor College of Medicine, Houston, Texas 77030, USA.", "yes", "USA"),
    ("Mayo Clinic, Rochester, MN, USA. x@example.org", "yes", "USA"),
    ("Stanford University Medical School, Stanford, California", "yes", "USA"),
    ("JDRF, New York, NY", "yes", "USA"),
    ("University of Oxford, Oxford, UK.", "no", "UK"),
    ("Peking Union Medical College Hospital, Beijing, China.", "no", "China"),
    ("University of Toronto, Toronto, ON, Canada", "no", "Canada"),
    ("Hospital Clinic, Barcelona, Spain. a.b@example.org", "no", "Spain"),
    ("University of Melbourne, Melbourne, Victoria, Australia", "no", "Australia"),
    ("Karolinska Institutet, Stockholm, Sweden", "no", "Sweden"),
    ("Jichi Medical University, Tochigi, Japan", "no", "Japan"),
]


class DetectorTests(unittest.TestCase):
    def test_cases(self):
        for aff, us, country in CASES:
            with self.subTest(aff=aff[:50]):
                self.assertEqual(cc.is_us(aff), us)
                self.assertEqual(cc.country_of(aff), country)

    def test_empty(self):
        self.assertEqual(cc.is_us(""), "")
        self.assertEqual(cc.country_of(""), "")


if __name__ == "__main__":
    unittest.main(verbosity=1)
