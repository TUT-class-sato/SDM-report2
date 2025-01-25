#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        # 既存のテストケース
        # def test_sample1 (self):
        #         self.assertEqual (21, calc(3,7))

        # def test_sample2 (self):
        #         self.assertEqual (-1, calc(0,150))

        # def test_sample3 (self):
        #         self.assertEqual (-1, calc('a','b'))

        # def test_sample4 (self):
        #         self.assertEqual (-1, calc(0.1,999))

        # 同値分割法: 有効同値をテスト
        def test_valid_equivalence(self):
                """有効同値（1〜999 の整数値）"""
                self.assertEqual(calc(1, 1), 1)  # 最小値
                self.assertEqual(calc(10, 20), 200)  # 典型的な有効ケース
                self.assertEqual(calc(999, 999), 998001)  # 範囲内の最大値（A == B）

        # 同値分割法: 無効同値をテスト
        def test_invalid_cases_out_of_range(self):
                """無効同値（有効範囲外の値）"""
                self.assertEqual(calc(0, 10), -1)  # Aが範囲外（0以下）
                self.assertEqual(calc(10, 0), -1)  # Bが範囲外（0以下）
                self.assertEqual(calc(1000, 10), -1)  # Aが範囲外（1000以上）
                self.assertEqual(calc(10, 1000), -1)  # Bが範囲外（1000以上）

        def test_invalid_cases_non_integer(self):
                """無効同値（整数以外の値）"""
                self.assertEqual(calc(1.5, 10), -1)  # Aが小数
                self.assertEqual(calc(10, 1.5), -1)  # Bが小数

                self.assertEqual(calc("abc", 10), -1)  # Aが文字列
                self.assertEqual(calc(10, "abc"), -1)  # Bが文字列

                self.assertEqual(calc(None, 10), -1)  # AがNone
                self.assertEqual(calc(10, None), -1)  # BがNone
                self.assertEqual(calc("", 10), -1)  # Aが空文字列
                self.assertEqual(calc(10, ""), -1)  # Bが空文字列

        # 境界値をテスト
        def test_boundary_values(self):
                """境界値分析: 有効同値と無効同値の境界をテスト"""
                # 有効同値の境界
                self.assertEqual(calc(1, 500), 500)  # A が最小
                self.assertEqual(calc(500, 1), 500)  # B が最小
                self.assertEqual(calc(999, 500), 499500)  # A が最大
                self.assertEqual(calc(500, 999), 499500)  # B が最大

                # 無効同値の境界
                self.assertEqual(calc(0, 500), -1)  # A = 0 は無効
                self.assertEqual(calc(1000, 500), -1)  # A = 1000 は無効
                self.assertEqual(calc(500, 0), -1)  # B = 0 は無効
                self.assertEqual(calc(500, 1000), -1)  # B = 1000 は無効
