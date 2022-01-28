#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

    def test_ab_valid1(self):
        self.assertEqual(21, calc(3, 7))

    def test_ab_valid2(self):
        self.assertEqual(21, calc(7, 3))

    def test_ab_valid3(self):
        self.assertEqual(1, calc(1, 1))

    def test_ab_valid4(self):
        self.assertEqual(999, calc(1, 999))

    def test_ab_valid5(self):
        self.assertEqual(999, calc(999, 1))

    def test_ab_valid6(self):
        self.assertEqual(998001, calc(999, 999))

    def test_ab_valid7(self):
        self.assertEqual(9990, calc(10, 999))

    def test_ab_valid8(self):
        self.assertEqual(9990, calc(999, 10))

    def test_ab_valid9(self):
        self.assertEqual(10, calc(1, 10))

    def test_ab_valid10(self):
        self.assertEqual(10, calc(10, 1))

    def test_a_invalid1(self):
        self.assertEqual(-1, calc(0.1,999))

    def test_a_invalid2(self):
        self.assertEqual(-1, calc(1+2j,999))

    def test_a_invalid3(self):
        self.assertEqual(-1, calc(0, 999))

    def test_a_invalid4(self):
        self.assertEqual(-1, calc(1000, 999))

    def test_a_invalid5(self):
        self.assertEqual(-1, calc('a', 20))

    def test_a_invalid6(self):
        self.assertEqual(-1, calc([], 40))

    def test_b_invalid1(self):
        self.assertEqual(-1, calc(999, 0.1))

    def test_b_invalid2(self):
        self.assertEqual(-1, calc(999, 1+2j))

    def test_b_invalid3(self):
        self.assertEqual(-1, calc(999, 0))

    def test_b_invalid4(self):
        self.assertEqual(-1, calc(999, 1000))

    def test_b_invalid5(self):
        self.assertEqual(-1, calc(40,'b'))

    def test_b_invalid6(self):
        self.assertEqual(-1, calc(40, []))

    def test_ab_invalid1(self):
        self.assertEqual(-1, calc(0,1000))

    def test_ab_invalid2(self):
        self.assertEqual(-1, calc(1000,0))

    def test_ab_invalid3(self):
        self.assertEqual(-1, calc(0.1,0.2))

    def test_ab_invalid4(self):
        self.assertEqual(-1, calc(1-2j,2+2j))

    def test_ab_invalid5(self):
        self.assertEqual(-1, calc('a','b'))

    def test_ab_invalid6(self):
        self.assertEqual(-1, calc(list(), dict()))

