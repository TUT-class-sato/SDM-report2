#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # 有効な入力
        def test_sample1 (self):
                self.assertEqual (10, calc(1,10))

        def test_sample2 (self):
                self.assertEqual (10, calc(10,1))

        # 以下，無効な入力

        # 1未満の数値を含むケース
        def test_sample3 (self):
                self.assertEqual (-1, calc(1,-1))
        def test_sample4 (self):
                self.assertEqual (-1, calc(-1,1))

        # 数値以外の入力が与えられるケース
        def test_sample5 (self):
                self.assertEqual (-1, calc(10, 1000))
        def test_sample6 (self):
                self.assertEqual (-1, calc(1000, 10))

        # 数値以外の入力が与えられるケース
        def test_sample7 (self):
                self.assertEqual (-1, calc(1.5, 1))
        def test_sample8 (self):
                self.assertEqual (-1, calc(1, 1.5))

        # 入力に文字が含まれるケース
        def test_sample9 (self):
                self.assertEqual (-1, calc('a','b'))