#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (25, calc(5,5))

        def test_sample2 (self):
                self.assertEqual (2500, calc(50,50))

        def test_sample3 (self):
                self.assertEqual (250000, calc(500,500))

        def test_sample4 (self):
                self.assertEqual (50, calc("５",10))

        def test_sample5 (self):
                self.assertEqual (5, calc(1,5))

        def test_sample6 (self):
                self.assertEqual (499500, calc(999,500))

        def test_sample7 (self):
                self.assertEqual (-1, calc(0,5))

        def test_sample8 (self):
                self.assertEqual (-1, calc(1000,500))

        def test_sample9 (self):
                self.assertEqual (-1, calc(1500,500))

        def test_sample10 (self):
                self.assertEqual (-1, calc(-5,5))

        def test_sample11 (self):
                self.assertEqual (-1, calc(5.5,5))

        def test_sample12 (self):
                self.assertEqual (-1, calc(0.5,5))

        def test_sample13 (self):
                self.assertEqual (-1, calc(5/50,5))

        def test_sample14 (self):
                self.assertEqual (-1, calc("１５００",5))

        def test_sample15 (self):
                self.assertEqual (-1, calc("a",5))


