#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1_1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample1_2 (self):
                self.assertEqual (21, calc(7,3))

        def test_sample1_3 (self):
                self.assertEqual (-1, calc(0,1000))

        def test_sample1_4 (self):
                self.assertEqual (9, calc(3,3))

        def test_sample2_1 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample2_2 (self):
                self.assertEqual (-1, calc(150,1000))

        def test_sample3_1 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample3_2 (self):
                self.assertEqual (-1, calc(5,'b'))

        def test_sample3_3 (self):
                self.assertEqual (-1, calc('a',5))

        def test_sample4_1 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_sample4_2 (self):
                self.assertEqual (-1, calc(1,999.9))

        def test_sample4_3 (self):
                self.assertEqual (-1, calc(3.1,50.3))

        def test_sample5_1 (self):
                self.assertEqual (-1, calc(-1,1))

        def test_sample5_2 (self):
                self.assertEqual (-1, calc(1,-1))

        def test_sample5_3 (self):
                self.assertEqual (-1, calc(-10,-1))

