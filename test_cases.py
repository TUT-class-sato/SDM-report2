#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (35, calc(5,7))

        def test_sample2 (self):
                self.assertEqual (35, calc(7,5))

        def test_sample3 (self):
                self.assertEqual (9, calc(3,3))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0,0))

        def test_sample5 (self):
                self.assertEqual (-1, calc(-1,100))

        def test_sample6 (self):
                self.assertEqual (-1, calc(100,-1))

        def test_sample7 (self):
                self.assertEqual (-1, calc(1000,1500))

        def test_sample8 (self):
                self.assertEqual (-1, calc(1000,150))

        def test_sample9 (self):
                self.assertEqual (-1, calc(100,1500))

        def test_sample10 (self):
                self.assertEqual (-1, calc(0.3,0.5))

        def test_sample11 (self):
                self.assertEqual (-1, calc(0.3,5))

        def test_sample12 (self):
                self.assertEqual (-1, calc(3,0.5))

        def test_sample13 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample14 (self):
                self.assertEqual (-1, calc('c',500))

        def test_sample15 (self):
                self.assertEqual (-1, calc(600,'d'))

        def test_sample16 (self):
                self.assertEqual (150, calc('10','15'))