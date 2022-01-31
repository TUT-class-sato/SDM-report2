#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample2_1 (self):
                self.assertEqual (-1, calc(0.1,1))

        def test_sample2_2 (self):
                self.assertEqual (2, calc(2,1))

        def test_sample2_3 (self):
                self.assertEqual (1, calc(1,1))

