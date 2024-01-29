#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        # 追加テストケース
        # 1. 有効同値
        # 1.1 範囲に含まれる整数
        # 1.1.1 A>B
        def test_A_lt_B (self):
                self.assertEqual (999, calc(1,999))

        # 1.1.2 B>A
        def test_B_lt_A (self):
                self.assertEqual (999, calc(999,1))

        # 1.1.3 B=A
        def test_B_eq_A (self):
                self.assertEqual (999, calc(999,999))

        # 1.2 範囲に含まれる整数の文字列
        # 1.2.1 0が先頭にある整数
        def test_str_beginzero (self):
                self.assertEqual (999, calc("001","00999"))

        # 1.2.2 0が先頭にない整数
        def test_str_nobeginzero (self):
                self.assertEqual (999, calc("1","999"))

        # 1.2.3 半角の空白に囲まれる整数
        def test_str_spaces (self):
                self.assertEqual (999, calc("  1  ","  999"))

        # 1.2.4 半角の空白に囲まれない整数
        def test_str_nospaces (self):
                self.assertEqual (19960, calc("20","998"))

        # 2. 無効同値
        # 2.1 整数ではない文字列
        # 2.1.1 アルファベット
        # 2.1.2 記号
        # 2.1.3 実数
        # 2.2 範囲に含まれない整数
        # 2.2.1 Aのみ
        # 2.2.2 Bのみ
        # 2.2.3 AとB
        # 2.3 範囲に含まれない整数の文字列
        # 2.3.1 Aのみ
        # 2.3.2 Bのみ
        # 2.3.3 AとB


        def test_string_int(self):
                self.assertEqual (30, calc('5','6'))
        

        # 無効同値

