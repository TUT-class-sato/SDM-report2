#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (-1, calc(0.5,0.7))
        def test_sample2 (self):
                self.assertEqual (-1, calc(999.5,999.7))
        def test_sample3 (self):
                self.assertEqual (1000, calc(100,10))
        def test_sample4 (self):
                self.assertEqual (-1, calc(10.5,20.5))
        def test_sample5 (self):
                self.assertEqual (-1, calc('a',10))

