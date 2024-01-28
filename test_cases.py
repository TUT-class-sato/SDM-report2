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

        def test_valid_positive_integers(self):
                self.assertEqual(21, calc(3, 7))

        def test_invalid_zero_input(self):
                self.assertEqual(-1, calc(0, 150))
                self.assertEqual(-1, calc(150, 0))

        def test_invalid_non_integer_input(self):
                self.assertEqual(-1, calc('a', 'b'))

        def test_invalid_decimal_input(self):
                self.assertEqual(-1, calc(0.1, 999))

        def test_boundary_smallest_integers(self):
                self.assertEqual(1, calc(1, 1))

        def test_boundary_largest_integers(self):
                self.assertEqual(998001, calc(999, 999))

        def test_boundary_one_valid_one_invalid(self):
                self.assertEqual(-1, calc(0, 999))
                self.assertEqual(-1, calc(999, 0))

        def test_boundary_invalid_inputs(self):
                self.assertEqual(-1, calc(0, 1000))
                self.assertEqual(-1, calc(1000, 0))

        def test_special_case_zero_input(self):
                self.assertEqual(-1, calc(0, 999))
                self.assertEqual(-1, calc(999, 0))

        def test_special_case_both_zero(self):
                self.assertEqual(-1, calc(0, 0))
