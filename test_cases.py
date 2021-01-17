#!/usr/bin/python3

import unittest
from calc_mul import calc


# Run with testrunner so needs to be in file test_

class TestCalc(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(20, calc(4, 5))

    def test_case2(self):
        self.assertEqual(20, calc(5, 4))

    def test_case3(self):
        self.assertEqual(7, calc(1, 7))

    def test_case4(self):
        self.assertEqual(7, calc(7, 1))

    def test_case5(self):
        self.assertEqual(9990, calc(10, 999))

    def test_case6(self):
        self.assertEqual(9990, calc(999, 10))

    def test_case7(self):
        self.assertEqual(-1, calc(0, 150))

    def test_case8(self):
        self.assertEqual(-1, calc(150, 0))

    def test_case9(self):
        self.assertEqual(-1, calc(10, 2000))

    def test_case10(self):
        self.assertEqual(-1, calc(2000, 10))

    def test_case11(self):
        self.assertEqual(-1, calc(-2, 2000))

    def test_case12(self):
        self.assertEqual(-1, calc(2000, -2))

    def test_case13(self):
        self.assertEqual(-1, calc('a', 2))

    def test_case14(self):
        self.assertEqual(-1, calc(3, 'b'))

    def test_case15(self):
        self.assertEqual(-1, calc('a', 'b'))

    def test_case16(self):
        self.assertEqual(-1, calc(0.1, 10))

    def test_case17(self):
        self.assertEqual(-1, calc(10, 0.1))

    def test_case18(self):
        self.assertEqual(-1, calc(0.2, 0.1))
