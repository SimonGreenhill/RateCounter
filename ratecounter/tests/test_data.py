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
    
    @classmethod
    def setUpClass(cls):
        filename = os.path.join(os.path.dirname(__file__), 'testdata', cls.filename)
        cls.rc = RateCounter(nexusfile=filename)
        cls.scores = cls.rc.get_scores('A', 'B')
    
    def _test(self, key):
        if key not in self.expected:
            # don't care about testing it, ignore
            return True
        if key not in self.scores:
            raise AssertionError("Missing %s from scores in %s" % (key, self.filename))
        if self.scores[key] != self.expected[key]:
            raise AssertionError("Mismatch %s (%d!=%d) from scores in %s" % (
                key, self.scores[key], self.expected[key], self.filename
            ))
    
    def test_nexus_nchar_eq_total(self):
        nchar = self.rc.matrix[list(self.rc.matrix.keys())[0]]
        assert len(nchar) == self.expected['TOTAL']
    
    def test_GAIN_A(self):
        self._test('GAIN A')

    def test_GAIN_B(self):
        self._test('GAIN B')

    def test_LOSS_A(self):
        self._test('LOSS A')

    def test_LOSS_B(self):
        self._test('LOSS B')

    def test_SHARED_LOSS(self):
        self._test('SHARED LOSS')

    def test_SHARED_GAIN(self):
        self._test('SHARED GAIN')

    def test_RETENTION(self):
        self._test('RETENTION')

    def test_ABSENCE(self):
        self._test('ABSENCE')

    def test_UNCOUNTABLE(self):
        self._test('UNCOUNTABLE')

    def test_TOTAL(self):
        self._test('TOTAL')


class TestRandom(DataMixin, unittest.TestCase):
    filename = 'test-Random.nex'
    expected = {
        'GAIN A': 1,
        'GAIN B': 1,
        'LOSS A': 3,
        'LOSS B': 3,
        'SHARED LOSS': 3,
        'SHARED GAIN': 2,
        'RETENTION': 3,
        'ABSENCE': 0,
        'UNCOUNTABLE': 11,
        'TOTAL': 27
    }


class TestRandom2(DataMixin, unittest.TestCase):
    filename = 'test-Random2.nex'
    expected = {
        'GAIN A': 8,
        'GAIN B': 20,
        'LOSS A': 29,
        'LOSS B': 22,
        'SHARED LOSS': 0,
        'SHARED GAIN': 0,
        'RETENTION': 262,
        'ABSENCE': 0,
        'UNCOUNTABLE': 0,
        'TOTAL': 341
    }


class TestAgtaGaddang(DataMixin, unittest.TestCase):
    filename = 'test-Agta_Gaddang.nex'
    expected = {
        'GAIN A': 38,
        'GAIN B': 40,
        'LOSS A': 29,
        'LOSS B': 31,
        'TOTAL': 138,
    }


class TestSeimatWuvulu(DataMixin, unittest.TestCase):
    filename = 'test-Seimat_Wuvulu.nex'
    expected = {
        'GAIN A': 82,
        'GAIN B': 91,
        'LOSS A': 35,
        'LOSS B': 40,
        'TOTAL': 248,
    }


class TestLithuanianLatvian(DataMixin, unittest.TestCase):
    filename = 'test-Lithuanian_Latvian.nex'
    expected = {
        'GAIN A': 58,
        'GAIN B': 58,
        'LOSS A': 38,
        'LOSS B': 33,
        'TOTAL': 338,
    }


class TestDanishSwedish(DataMixin, unittest.TestCase):
    filename = 'test-Danish_Swedish.nex'
    expected = {
        'GAIN A': 2,
        'GAIN B': 13,
        'LOSS A': 22,
        'LOSS B': 14,
        'TOTAL': 309,
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
    

class TestBorongBurum(DataMixin, unittest.TestCase):
    filename = 'test-Borong-Burum.nex'
    expected = {
        'GAIN A': 20,
        'GAIN B': 55,
        'LOSS A': 7,
        'LOSS B': 14,
        'SHARED LOSS': 59,
        'SHARED GAIN': 26,
        'RETENTION': 25,
        'ABSENCE': 186,
        'UNCOUNTABLE': 0,
        'TOTAL': 392
    }


class TestFriulianItalian(DataMixin, unittest.TestCase):
    filename = 'test-Friulian_Italian.nex'
    expected = {
        'GAIN A': 46,
        'GAIN B': 35,
        'LOSS A': 27,
        'LOSS B': 10,
        'SHARED LOSS': 97,
        'SHARED GAIN': 51,
        'RETENTION': 121,
        'ABSENCE': 5876,
        'UNCOUNTABLE': 17,
        'TOTAL': 6280
    }


class TestB52B53(DataMixin, unittest.TestCase):
    filename = 'test-B52_B53.nex'
    expected = {
        'GAIN A': 1,
        'GAIN B': 2,
        'LOSS A': 7,
        'LOSS B': 8,
        'SHARED LOSS': 0,
        'SHARED GAIN': 1,
        'RETENTION': 89,
        'ABSENCE': 0,
        'UNCOUNTABLE': 1,
        'TOTAL': 109
    }



class TestRegression1(DataMixin, unittest.TestCase):
    # This used to raise
    # ValueError: Unknown other pattern ['0', '0', '?', '0']
    # when it should return absence
    filename = 'test_regression_1.nex'
    expected = {
        'GAIN A': 0,
        'GAIN B': 0,
        'LOSS A': 0,
        'LOSS B': 0,
        'SHARED LOSS': 0,
        'SHARED GAIN': 0,
        'RETENTION': 0,
        'ABSENCE': 1,
        'UNCOUNTABLE': 0,
        'TOTAL': 1
    }




