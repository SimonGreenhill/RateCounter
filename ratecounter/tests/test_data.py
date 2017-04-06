#!/usr/bin/env python3
#coding=utf-8
"""..."""
__author__ = 'Simon J. Greenhill <simon@simon.net.nz>'
__copyright__ = 'Copyright (c) 2016 Simon J. Greenhill'
__license__ = 'New-style BSD'

import os
import unittest
from ratecounter.main import RateCounter

class DataMixin(object):  # pragma: no cover
    filename = None
    expected = {}
    
    def setUp(self):
        filename = os.path.join(os.path.dirname(__file__), 'testdata', self.filename)
        self.rc = RateCounter(nexusfile=filename)
        self.scores = self.rc.get_scores('A', 'B')
    
    def test_scores(self):
        for key in self.expected:
            if key not in self.scores:
                raise AssertionError("Missing %s from scores in %s" % (key, self.filename))
            if self.scores[key] != self.expected[key]:
                raise AssertionError("Mismatch %s (%d!=%d) from scores in %s" % (
                    key, self.scores[key], self.expected[key], self.filename
                ))
    

class TestAgtaGaddang(DataMixin, unittest.TestCase):
    filename = 'test-Agta_Gaddang.nex'
    expected = {
        'GAIN A': 38,
        'GAIN B': 40,
        'LOSS A': 29,
        'LOSS B': 31,
    }


class TestSeimatWuvulu(DataMixin, unittest.TestCase):
    filename = 'test-Seimat_Wuvulu.nex'
    expected = {
        'GAIN A': 82,
        'GAIN B': 91,
        'LOSS A': 35,
        'LOSS B': 40,
    }


class TestLithuanianLatvian(DataMixin, unittest.TestCase):
    filename = 'test-Lithuanian_Latvian.nex'
    expected = {
        'GAIN A': 58,
        'GAIN B': 58,
        'LOSS A': 38,
        'LOSS B': 33,
    }


class TestDanishSwedish(DataMixin, unittest.TestCase):
    filename = 'test-Danish_Swedish.nex'
    expected = {
        'GAIN A': 2,
        'GAIN B': 13,
        'LOSS A': 22,
        'LOSS B': 14,
    }

class TestHoraCuichol(DataMixin, unittest.TestCase):
    filename = 'test-Cora_Huichol.nex'
    expected = {
        'GAIN A': 4,
        'GAIN B': 5,
        'LOSS A': 0,
        'LOSS B': 1,
        'SHARED LOSS': 6,
        'SHARED GAIN': 2,
        'RETENTION': 2,
        'ABSENCE': 71,
        'UNCOUNTABLE': 12,
        'TOTAL': 103
    }
    