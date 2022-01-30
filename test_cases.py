#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(7,3))

        def test_sample2 (self):
                self.assertEqual (-1, calc('1st','2nd'))

        def test_sample3 (self):
                self.assertEqual (-1, calc(0.1,999))

