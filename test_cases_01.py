#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (499500, calc(999,500))

        def test_sample2 (self):
                self.assertEqual (500, calc(1,500))

        def test_sample3 (self):
                self.assertEqual (250000, calc(500,500))

        def test_sample4 (self):
                self.assertEqual (-1, calc(1000,500))

        def test_sample5 (self):
                self.assertEqual (-1, calc(0,500))

        def test_sample6 (self):
                self.assertEqual (-1, calc(-10,500))

        def test_sample7 (self):
                self.assertEqual (-1, calc(1010,500))

        def test_sample8 (self):
                self.assertEqual (-1, calc(0.1,500))

        def test_sample9 (self):
                self.assertEqual (-1, calc('a',500))
                