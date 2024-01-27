#!/usr/bin/python3

import unittest
import sys
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        # 同値分割法に基づくテストケース
        def test_eqp (self):
                # 1未満の入力のチェック
                self.assertEqual (-1, calc(0, 20))
                self.assertEqual (-1, calc(550, 0))
                # 999を超過する入力のチェック
                self.assertEqual (-1, calc(1200, 20))
                self.assertEqual (-1, calc(19, 999999))

        # 同値分割法（整数以外の入力）
        def test_eqp_not (self):
                # 整数以外の入力のチェック
                self.assertEqual (-1, calc('111.1', '20'))
                self.assertEqual (-1, calc('19', '99.4'))
                self.assertEqual (-1, calc('19', '3/2'))
                self.assertEqual (-1, calc('1/9', '12'))
        
        # 文字列チェック
        def test_eqp_str (self):
                self.assertEqual (-1, calc('a', 1))
                self.assertEqual (-1, calc('a0', 1))
                self.assertEqual (-1, calc('0a', 1))
        
        # 同値分割法（python由来の条件）
        def test_eqp_py (self):
                self.assertEqual (-1, calc(sys.maxsize+1, 33))
                self.assertEqual (-1, calc('inf', 22))
                self.assertEqual (-1, calc('𝟎', 'ٟ𝟏'))

        # 境界値分析
        def test_b (self):
                self.assertEqual (-1, calc(0, 1))
                self.assertEqual (-1, calc(1, 0))
                self.assertEqual (-1, calc(0, 0))
                self.assertEqual (1, calc(1, 1))
                self.assertEqual (999*999, calc(999, 999))
                self.assertEqual (-1, calc(999, 1000))
                self.assertEqual (-1, calc(1000, 999))
                self.assertEqual (-1, calc(1000, 1000))

