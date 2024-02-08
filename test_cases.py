#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc (unittest.TestCase):

    def test_expected_value(self):
        self.assertEqual(21, calc(3, 7))

    def test_boundary_value1(self):
        self.assertEqual(-1, calc(0, 1000))

    def test_boundary_value2(self):
        self.assertEqual(-1, calc(1000, 0))

    def test_boundary_value3(self):
        self.assertEqual(-1, calc(1000, 1000))

    def test_boundary_value4(self):
        self.assertEqual(999, calc(1, 999))

    def test_boundary_value5(self):
        self.assertEqual(999, calc(999, 1))

    def test_boundary_value6(self):
        self.assertEqual(998001, calc(999, 999))

    def test_outside_value(self):
        self.assertEqual(-1, calc(-1, 1100))

    def test_outside_value1(self):
        self.assertEqual(-1, calc(-1, 900))

    def test_outside_value2(self):
        self.assertEqual(-1, calc(900, -1))

    def test_notnum_value1(self):
        self.assertEqual(-1, calc('a', 'b'))

    def test_notnum_value2(self):
        self.assertEqual(-1, calc('a', 10))

    def test_notnum_value3(self):
        self.assertEqual(-1, calc(10, 'a'))

    def test_decimal_value1(self):
        self.assertEqual(-1, calc(0.1, 999))

    def test_decimal_value2(self):
        self.assertEqual(-1, calc(999, 1.1))

    def test_zero_value1(self):
        self.assertEqual(-1, calc(0, 15))

    def test_zero_value2(self):
        self.assertEqual(-1, calc(15, 0))
