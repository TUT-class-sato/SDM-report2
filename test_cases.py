#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc (unittest.TestCase):

    def expected_value(self):
        self.assertEqual(21, calc(3, 7))

    def boundary_value1(self):
        self.assertEqual(-1, calc(0, 1000))

    def boundary_value2(self):
        self.assertEqual(999, calc(1, 999))

    def outside_value(self):
        self.assertEqual(-1, calc(-1, 1100))

    def notnum_value(self):
        self.assertEqual(-1, calc('a', 'b'))

    def decimal_value(self):
        self.assertEqual(-1, calc(0.1, 999))

    def null_value(self):
        self.assertEqual(-1, calc(None, 15))

    def zero_value(self):
        self.assertEqual(-1, calc(0, 15))
