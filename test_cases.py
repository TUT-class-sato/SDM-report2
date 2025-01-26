#!/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc(unittest.TestCase):

    # 通常の計算テスト
    def test_valid_cases(self):
        self.assertEqual(21, calc(3, 7))      # 正常な整数の掛け算
        self.assertEqual(1000, calc(20, 50))  # 正常な整数の掛け算

    # 境界値テスト
    def test_boundary_cases(self):
        self.assertEqual(-1, calc(0, 150))    # Aが無効な場合
        self.assertEqual(-1, calc(1000, 150)) # Aが無効な場合
        self.assertEqual(-1, calc(150, 0))    # Bが無効な場合
        self.assertEqual(-1, calc(150, 1000)) # Bが無効な場合

    # 入力が数値以外の場合
    def test_invalid_input(self):
        self.assertEqual(-1, calc('a', 'b'))  # 文字列が入力された場合
        self.assertEqual(-1, calc(0.1, 999))  # 浮動小数点数が入力された場合

    # 入力が数値であるが条件に合わない場合
    def test_out_of_range(self):
        self.assertEqual(-1, calc(-10, 100))   # 負の数が入力された場合
        self.assertEqual(-1, calc(500, 1000))  # 最大値を超えた場合
