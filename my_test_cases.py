#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc (unittest.TestCase):

    # 自作テスト
    def test1(self):
        self.assertEqual(-1, calc(0, 1))

    def test2(self):
        self.assertEqual(-1, calc(1, 0))

    def test3(self):
        self.assertEqual(-1, calc(-1, 1))

    def test4(self):
        self.assertEqual(-1, calc(1, -1))

    def test5(self):
        self.assertEqual(-1, calc(1000, 1))

    def test6(self):
        self.assertEqual(-1, calc(1, 1000))

    def test7(self):
        self.assertEqual(-1, calc(0.1, 1))

    def test8(self):
        self.assertEqual(-1, calc(1, 0.1))

    def test9(self):
        self.assertEqual(-1, calc(999.9, 1))

    def test10(self):
        self.assertEqual(-1, calc(1, 999.9))

    def test11(self):
        self.assertEqual(-1, calc("a", 1))

    def test12(self):
        self.assertEqual(-1, calc(1, "b"))

    def test13(self):
        self.assertEqual(-1, calc("+", 1))

    def test14(self):
        self.assertEqual(-1, calc(1, "+"))

    def test15(self):
        self.assertEqual(1, calc(1, 1))

    def test16(self):
        self.assertEqual(998001, calc(999, 999))

    def test17(self):
        self.assertEqual(-1, calc("a", "b"))

    def test18(self):
        self.assertEqual(10, calc(2, 5))

    def test19(self):
        self.assertEqual(10, calc(5, 2))

    def test20(self):
        self.assertEqual(9, calc(3, 3))

    def test21(self):
        self.assertEqual(-1, calc(1.0, 1.0))

    def test22(self):
        self.assertEqual(-1, calc(1.0, 2.0))

    def test23(self):
        self.assertEqual(-1, calc(1.1, 2.2))

    def test24(self):
        self.assertEqual(-1, calc(2.2, 1.1))
