#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
    # 有効な入力
    def test_valid_input_equal(self):
        self.assertEqual(1, calc(1,1))  # 正の整数でA=B

    def test_valid_input_greater(self):
        self.assertEqual(1, calc(2,1))  # 正の整数でA>B

    def test_valid_input_less(self):
        self.assertEqual(21, calc(3,7))  # 正の整数でA<B

    # 無効な入力
    def test_invalid_input_zero(self):
        self.assertEqual(-1, calc(0,150))  # Aが0
        self.assertEqual(-1, calc(15,0))  # Bが0

    def test_invalid_input_thousand(self):
        self.assertEqual(-1, calc(1000,150))  # Aが1000
        self.assertEqual(-1, calc(565,1000))  # Bが1000

    def test_invalid_input_string(self):
        self.assertEqual(-1, calc('a', 22))  # Aが文字列
        self.assertEqual(-1, calc(456, 'b'))  # Bが文字列

    def test_invalid_input_negative(self):
        self.assertEqual(-1, calc(-500,40))  # Aが負の数
        self.assertEqual(-1, calc(14,-5))  # Bが負の数

    def test_invalid_input_decimal(self):
        self.assertEqual(-1, calc(0.1,999))  # Aが正の小数
        self.assertEqual(-1, calc(45,0.55))  # Bが正の小数