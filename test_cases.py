#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
    def test_valid_inputs(self):  #有効な入力
        self.assertEqual(21, calc(3,7))  #正の整数

    def test_invalid_inputs(self):
        self.assertEqual(-1, calc(0,150))  # 入力Aが0
        self.assertEqual(-1, calc(1000,150))  # 入力Aが1000
        self.assertEqual(-1, calc('a','b'))  # 文字列
        self.assertEqual(-1, calc(500,40))  # A<Bでない
        self.assertEqual(-1, calc(0.1,999))  # 正の小数

