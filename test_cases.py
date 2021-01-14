#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
    # 有効同値(A,Bに1~999の整数を入力)
    def test_accept(self):
        self.assertEqual(250000, calc(500, 500))

    # 無効同値(A,Bに1〜999の小数を入力)
    def test_float(self):
        self.assertEqual(-1, calc(1.1, 998.9))

    # 無効同値(A,Bに1未満の整数,小数を入力)
    def test_lower_bound1(self):
        self.assertEqual(-1, calc(0, 999))

    def test_lower_bound2(self):
        self.assertEqual(-1, calc(0.9, 999))

    # 無効同値(A,Bに999より大きい整数,小数を入力)
    def test_upper_bound1(self):
        self.assertEqual(-1, calc(1, 1000))

    def test_upper_bound2(self):
        self.assertEqual(-1, calc(1, 999.1))

    # 無効同値(A,Bに文字列,Noneを入力)
    def test_non_number1(self):
        self.assertEqual(-1, calc('a', 999))

    def test_non_number2(self):
        self.assertEqual(-1, calc('a', 'b'))

    def test_non_number3(self):
        self.assertEqual(-1, calc('1', 999))

    def test_non_number4(self):
        self.assertEqual(-1, calc('1', '999'))

    def test_non_number5(self):
        self.assertEqual(-1, calc('1.1', 999))

    def test_non_number6(self):
        self.assertEqual(-1, calc('1.1', '998.9'))

    def test_non_number7(self):
        self.assertEqual(-1, calc(None, 999))

    def test_non_number8(self):
        self.assertEqual(-1, calc(None, None))

