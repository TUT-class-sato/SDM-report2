#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_int_1_a(self):
                self.assertEqual(-1, calc(-2, 500))
        def test_int_2_a(self):
                self.assertEqual(200000, calc(400, 500))
        def test_int_3_a(self):
                self.assertEqual(-1, calc(1002, 500))
        def test_decimal_a(self):
                self.assertEqual(-1, calc(499.9, 500))
        def test_str_a(self):
                self.assertEqual(-1, calc('abc', 500))

        def test_int_1_b(self):
                self.assertEqual(-1, calc(500, -2))
        def test_int_2_b(self):
                self.assertEqual(250000, calc(500, 500))
        def test_int_3_b(self):
                self.assertEqual(-1, calc(500, 1002))
        def test_decimal_b(self):
                self.assertEqual(-1, calc(500, 499.9))
        def test_str_b(self):
                self.assertEqual(-1, calc(500, 'abc'))
