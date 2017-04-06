#!/usr/bin/env python3
#coding=utf-8
"""..."""
__author__ = 'Simon J. Greenhill <simon@simon.net.nz>'
__copyright__ = 'Copyright (c) 2016 Simon J. Greenhill'
__license__ = 'New-style BSD'

import os
import re
import unittest
import contextlib
from io import StringIO
from ratecounter.main import RateCounter
from ratecounter.cli import parse_args, main

class Test_CLI(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(
            parse_args("test.nex", "L1", "L2"),
            ('test.nex', 'L1', 'L2')
        )
    
    def test_parse_error(self):
        with self.assertRaises(SystemExit):
            parse_args("test.nex", "L1")
    
    def test_error_on_no_file(self):
        with self.assertRaises(IOError):
            main(args=["filename", "L1", "L2"])
    
    def test(self):
        filename = os.path.join(os.path.dirname(__file__), 'testdata', 'test.nex')
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            main(args=[filename, 'L1', 'L2'])
        output = temp_stdout.getvalue().strip()
        for result in RateCounter.KEYLIST:
            assert re.findall("%s\s+\d+" % result, output, re.DOTALL)
        