#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample5 (self):
                self.assertEqual (-1, calc(-1,999))
        def test_sample6 (self):
                self.assertEqual (-1, calc(1,999.9))
        def test_sample7 (self):
                self.assertEqual (-1, calc(1.1,999))
        def test_sample8 (self):
                self.assertEqual (999, calc('1','999')) 
        def test_sample9 (self):
                self.assertEqual (1, calc(1,1))
        def test_sample10 (self):
                self.assertEqual (999, calc(999,1))