#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        #境界値分割法
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
        
        def test_min(self):
                self.assertEqual(1, calc(1,1))
        def test_max(self):
                self.assertEqual(998001, calc(999,999))
        def test_minout(self):
                self.assertEqual(-1, calc(0,0))
        def test_maxout(self):
                self.assertEqual(-1, calc(1000, 1000))
        def test_string(self):
                self.assertEqual(-1, calc("te", "st"))

