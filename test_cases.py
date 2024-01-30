#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

    def test_valid_inputs(self):
        # 正常な入力条件
        self.assertEqual(calc(1, 2), 2)
        self.assertEqual(calc(0.5, 1.5), 0.75)
        self.assertEqual(calc(0, 999), 0)

    def test_boundary_values(self):
        # 境界値のテスト
        self.assertEqual(calc(0, 1), -1)  # Aが0の場合
        self.assertEqual(calc(1, 999), 999)  # Bが1000に近い場合
        self.assertEqual(calc(999, 1000), -1)  # Bが1000の場合

    def test_invalid_inputs(self):
        # 無効な入力条件
        self.assertEqual(calc("abc", 2), -1)  # Aが数値でない場合
        self.assertEqual(calc(1, "xyz"), -1)  # Bが数値でない場合
        self.assertEqual(calc("abc", "xyz"), -1)  # AとBが数値でない場合

    def test_edge_cases(self):
        # エッジケース
        self.assertEqual(calc(float('inf'), 2), -1)  # Aが無限大の場合
        self.assertEqual(calc(2, float('inf')), -1)  # Bが無限大の場合

