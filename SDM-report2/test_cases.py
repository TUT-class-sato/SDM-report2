#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (-1, calc(1.01,998.2))

        def test_sample2 (self):
                self.assertEqual (-1, calc('1','2'))

        def test_sample3 (self):
                self.assertEqual (-1, calc('1',999))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,0.2))

        def test_sample5 (self):
                self.assertEqual (-1, calc(999.1,999.2))
