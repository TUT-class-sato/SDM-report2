#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

    # 正常な値のテスト
    def test1(self):
        self.assertEqual(calc(1, 1), 1)
    def test2(self):
        self.assertEqual(calc(1, 999), 999)
    def test3(self):
        self.assertEqual(calc(999, 1), 999)
    def test4(self):        
        self.assertEqual(calc(999, 999), 998001)

    # 入力範囲外の数値
    def test_5(self):
        self.assertEqual(calc(1000, 1), -1)  # Aが999を超える場合
    def test_6(self):
        self.assertEqual(calc(1, 1000), -1)  # Bが999を超える場合
    def test_7(self):
        self.assertEqual(calc(1000, 1000), -1)  # AとBが999を超える場合
    def test_8(self):
        self.assertEqual(calc(0, 1), -1)  # Aが0の場合
    def test_8(self):
        self.assertEqual(calc(1, 0), -1)  # Bが0の場合
    def test_9(self):
        self.assertEqual(calc(0, 0), -1)  # AとBが0の場合
    def test_10(self):
        self.assertEqual(calc(-2, 2), -1)  # Aが負の数の場合
    def test_11(self):
        self.assertEqual(calc(2, -2), -1)  # Bが負の数の場合
    def test_12(self):
        self.assertEqual(calc(-1, -1), -1)  # AとBが負の数の場合
    def test_13(self):
        self.assertEqual(calc(0.5, 1), -1)  # Aが小数の場合
    def test_14(self):
        self.assertEqual(calc(1, 0.5), -1)  # Bが小数の場合
    def test_15(self):
        self.assertEqual(calc(0.5, 1.5), -1)  # AとBが小数の場合

    # 数値でない入力
    def test_16(self):
        self.assertEqual(calc("abc", 2), -1)  # Aが数値でない場合
    def test_17(self):
        self.assertEqual(calc(1, "xyz"), -1)  # Bが数値でない場合
    def test_18(self):        
        self.assertEqual(calc("abc", "xyz"), -1)  # AとBが数値でない場合
    def test_19(self):        
        self.assertEqual(calc("1b1", 1), -1)  # Aが数と文字を含む場合
    def test_21(self):        
        self.assertEqual(calc(1, "1y1"), -1)  # Bが数と文字を含む場合
    def test_22(self):        
        self.assertEqual(calc("1b1", "1y1"), -1)  # AとBが数と文字を含む場合

