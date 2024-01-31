#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # 正常な入力
        def test_sample_correct (self):
                self.assertEqual (21, calc(3,7))
        # 境界値
        def test_sample_border_1 (self):
                self.assertEqual (1 * 1, calc(1, 1))
        def test_sample_border_2 (self):
                self.assertEqual (1 * 999, calc(1, 999))
        def test_sample_border_3 (self):
                self.assertEqual (999 * 1, calc(999, 1))
        def test_sample_border_4 (self):
                self.assertEqual (999 * 999, calc(999, 999))

        # Aの確認
        # 整数
        # 下側境界値
        def test_sample_A_1 (self):
                self.assertEqual (-1, calc(0,150))
        # 上側境界値
        def test_sample_A_2 (self):
                self.assertEqual (-1, calc(1000, 150))
        # 小数
        # 範囲外
        def test_sample_A_3 (self):
                self.assertEqual (-1, calc(0.99, 150))
        def test_sample_A_4 (self):
                self.assertEqual (-1, calc(999.1, 150))
        # 範囲内
        def test_sample_A_5 (self):
                self.assertEqual (-1, calc(50.1, 150))
        # 不正な文字列
        def test_sample_A_6 (self):
                self.assertEqual (-1, calc('ab124', 150))

        # Bの確認
        # 整数
        # 下側境界値
        def test_sample_B_1 (self):
                self.assertEqual (-1, calc(150,0))
        # 上側境界値
        def test_sample_B_2 (self):
                self.assertEqual (-1, calc(150, 1000))
        # 小数
        # 範囲外
        def test_sample_B_3 (self):
                self.assertEqual (-1, calc(150, 0.99))
        def test_sample_B_4 (self):
                self.assertEqual (-1, calc(150, 999.1))
        # 範囲内
        def test_sample_B_5 (self):
                self.assertEqual (-1, calc(150, 50.01))
        # 不正な文字列
        def test_sample_B_6 (self):
                self.assertEqual (-1, calc(150, 'ab124'))