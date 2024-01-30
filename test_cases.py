#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

    def test_valid_inputs(self):
        # 正常な値のテスト
        self.assertEqual(calc(1, 1), 1)
        self.assertEqual(calc(1, 999), 999)
        self.assertEqual(calc(999, 1), 999)
        self.assertEqual(calc(999, 999), 998001)

    def test_invalid_inputs(self):
        # 無効な入力条件
        self.assertEqual(calc(0, 999), -1)  # Aが0の場合
        self.assertEqual(calc(999, 0), -1)  # Bが0の場合
        self.assertEqual(calc(0, 0), -1)  # AとBが0の場合
        self.assertEqual(calc(0.5, 1), -1)  # Aが小数の場合
        self.assertEqual(calc(1, 0.5), -1)  # Bが小数の場合
        self.assertEqual(calc(0.5, 1.5), -1)  # AとBが小数の場合
        self.assertEqual(calc(-2, 2), -1)  # Aが負の数の場合
        self.assertEqual(calc(2, -2), -1)  # Bが負の数の場合
        self.assertEqual(calc(-1, -1), -1)  # AとBが負の数の場合
        self.assertEqual(calc("abc", 2), -1)  # Aが数値でない場合
        self.assertEqual(calc(1, "xyz"), -1)  # Bが数値でない場合
        self.assertEqual(calc("abc", "xyz"), -1)  # AとBが数値でない場合

    def test_edge_cases(self):
        # エッジケース
        self.assertEqual(calc(float('inf'), 2), -1)  # Aが無限大の場合
        self.assertEqual(calc(2, float('inf')), -1)  # Bが無限大の場合

