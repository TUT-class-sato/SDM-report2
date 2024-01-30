#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

    def test_valid_value(self):
        # 正常な値のテスト
        self.assertEqual(calc(1, 1), 1)
        self.assertEqual(calc(1, 999), 999)
        self.assertEqual(calc(999, 1), 999)
        self.assertEqual(calc(999, 999), 998001)

    def test_invalid_value(self):
        # 入力範囲外の数値
        self.assertEqual(calc(1000, 1), -1)  # Aが999を超える場合
        self.assertEqual(calc(1, 1000), -1)  # Bが999を超える場合
        self.assertEqual(calc(1000, 1000), -1)  # AとBが999を超える場合
        self.assertEqual(calc(0, 1), -1)  # Aが0の場合
        self.assertEqual(calc(1, 0), -1)  # Bが0の場合
        self.assertEqual(calc(0, 0), -1)  # AとBが0の場合
        self.assertEqual(calc(-2, 2), -1)  # Aが負の数の場合
        self.assertEqual(calc(2, -2), -1)  # Bが負の数の場合
        self.assertEqual(calc(-1, -1), -1)  # AとBが負の数の場合
        self.assertEqual(calc(0.5, 1), -1)  # Aが小数の場合
        self.assertEqual(calc(1, 0.5), -1)  # Bが小数の場合
        self.assertEqual(calc(0.5, 1.5), -1)  # AとBが小数の場合

    def test_invalid_others(self):
        # 数値でない入力
        self.assertEqual(calc("abc", 2), -1)  # Aが数値でない場合
        self.assertEqual(calc(1, "xyz"), -1)  # Bが数値でない場合
        self.assertEqual(calc("abc", "xyz"), -1)  # AとBが数値でない場合
        self.assertEqual(calc("1b1", 1), -1)  # Aが数と文字を含む場合
        self.assertEqual(calc(1, "1y1"), -1)  # Bが数と文字を含む場合
        self.assertEqual(calc("1b1", "1y1"), -1)  # AとBが数と文字を含む場合

