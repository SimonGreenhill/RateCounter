#!/usr/bin/env python3
#coding=utf-8
"""..."""
__author__ = 'Simon J. Greenhill <simon@simon.net.nz>'
__copyright__ = 'Copyright (c) 2016 Simon J. Greenhill'
__license__ = 'New-style BSD'

import re
import unittest
import contextlib
from io import StringIO

from ratecounter.main import RateCounter
from ratecounter.tests.test_score import TEST_DATA

TAXALABELS = ["L1", "L2", "F"]
TEST_DATA_MATRIX = {
    "L1": [], 
    "L2": [],
    'F': []
}

for row, result in TEST_DATA:
    for i, taxon in enumerate(TAXALABELS):
        TEST_DATA_MATRIX[taxon].append(row[i])


class Test_RateCounter(unittest.TestCase):
    def setUp(self):
        self.rc = RateCounter(TEST_DATA_MATRIX)
        self.scores = self.rc.get_scores("L1", "L2")
    
    def test_nchar(self):
        assert self.rc.nchar == 27

    def test_taxa(self):
        self.assertEqual(sorted(self.rc.taxa), sorted(['L1', 'L2', 'F']))
    
    def test_error_on_invalid_matrix(self):
        with self.assertRaises(ValueError):
            _ = RateCounter({
                "A": ['1', '0'],
                "B": ['1', '0'],
                "C": ['1', '0', '1']
            }).nchar
    
    def test_error_on_invalid_taxa(self):
        with self.assertRaises(AssertionError):
            self.rc.get_scores("X", "L1")
        with self.assertRaises(AssertionError):
            self.rc.get_scores("L2", "Z")
    
    def test_scores_ABSENCE(self):
        assert self.scores['ABSENCE'] == 1

    def test_scores_RETENTION(self):
        assert self.scores['RETENTION'] == 1

    def test_scores_SHARED_LOSS(self):
        assert self.scores['SHARED LOSS'] == 1

    def test_scores_SHARED_GAIN(self):
        assert self.scores['SHARED GAIN'] == 1

    def test_scores_GAIN_A(self):
        assert self.scores['GAIN A'] == 1

    def test_scores_GAIN_B(self):
        assert self.scores['GAIN B'] == 1

    def test_scores_LOSS_A(self):
        assert self.scores['LOSS A'] == 1

    def test_scores_LOSS_B(self):
        assert self.scores['LOSS B'] == 1

    def test_scores_UNCOUNTABLE(self):
        assert self.scores['UNCOUNTABLE'] == 19

    def test_display(self):
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            self.rc.display(self.scores)
        output = temp_stdout.getvalue().strip()
        for result in self.rc.KEYLIST:
            assert re.findall(r"%s\s+\d+" % result, output, re.DOTALL)
