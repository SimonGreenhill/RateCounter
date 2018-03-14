#!/usr/bin/env python3
#coding=utf-8
"""..."""
__author__ = 'Simon J. Greenhill <simon@simon.net.nz>'
__copyright__ = 'Copyright (c) 2016 Simon J. Greenhill'
__license__ = 'New-style BSD'

import unittest

from ratecounter.main import Score

TEST_DATA = [
    (('0', '0', '0'), 'ABSENCE'),
    (('0', '0', '1'), 'SHARED LOSS'),
    (('0', '0', '?'), 'UNCOUNTABLE'),
    (('0', '1', '0'), 'GAIN B'),
    (('0', '1', '1'), 'LOSS A'),
    (('0', '1', '?'), 'UNCOUNTABLE'),
    (('0', '?', '0'), 'UNCOUNTABLE'),
    (('0', '?', '1'), 'UNCOUNTABLE'),
    (('0', '?', '?'), 'UNCOUNTABLE'),
    (('1', '0', '0'), 'GAIN A'),
    (('1', '0', '1'), 'LOSS B'),
    (('1', '0', '?'), 'UNCOUNTABLE'),
    (('1', '1', '0'), 'SHARED GAIN'),
    (('1', '1', '1'), 'RETENTION'),
    (('1', '1', '?'), 'UNCOUNTABLE'),
    (('1', '?', '0'), 'UNCOUNTABLE'),
    (('1', '?', '1'), 'UNCOUNTABLE'),
    (('1', '?', '?'), 'UNCOUNTABLE'),
    (('?', '0', '0'), 'UNCOUNTABLE'),
    (('?', '0', '1'), 'UNCOUNTABLE'),
    (('?', '0', '?'), 'UNCOUNTABLE'),
    (('?', '1', '0'), 'UNCOUNTABLE'),
    (('?', '1', '1'), 'UNCOUNTABLE'),
    (('?', '1', '?'), 'UNCOUNTABLE'),
    (('?', '?', '0'), 'UNCOUNTABLE'),
    (('?', '?', '1'), 'UNCOUNTABLE'),
    (('?', '?', '?'), 'UNCOUNTABLE')
]


class Test_Score(unittest.TestCase):
    def test_check(self):
        with self.assertRaises(ValueError):
            Score('1', 'a', '0')
        with self.assertRaises(ValueError):
            Score('x', '1', '0')
        with self.assertRaises(ValueError):
            Score('0', '1', '_')
    
    def test_repr(self):
        for p, expected in TEST_DATA:
            self.assertIn(expected, repr(Score(*p)))
    
    def test_state(self):
        for p, expected in TEST_DATA:
            self.assertEqual(Score(*p).state, expected)

