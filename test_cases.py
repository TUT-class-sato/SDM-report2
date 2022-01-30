#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc (unittest.TestCase):

    # どちらも正常な入力

    def test_calc_mul_normal_normal_eq(self):
        self.assertEqual(500*500, calc(500, 500))

    def test_calc_mul_normal_normal_gt(self):
        self.assertEqual(250*750, calc(250, 750))

    def test_calc_mul_normal_normal_lt(self):
        self.assertEqual(250*750, calc(750, 250))

    # 片方、もしくは両方が下限以下
    def test_calc_mul_neg_normal(self):
        self.assertEqual(-1, calc(-100, 500))

    def test_calc_mul_normal_neg(self):
        self.assertEqual(-1, calc(500, -100))

    def test_calc_mul_neg_neg(self):
        self.assertEqual(-1, calc(-100, -100))

    # 片方、もしくは両方が上限以上
    def test_calc_mul_over_normal(self):
        self.assertEqual(-1, calc(5000, 500))

    def test_calc_mul_normal_over(self):
        self.assertEqual(-1, calc(500, 5000))

    def test_calc_mul_over_over(self):
        self.assertEqual(-1, calc(5000, 5000))

    # 片方、もしくは両方が文字列
    def test_calc_mul_str_normal(self):
        self.assertEqual(-1, calc("a", 500))

    def test_calc_mul_normal_str(self):
        self.assertEqual(-1, calc(500, "a"))

    def test_calc_mul_str_str(self):
        self.assertEqual(-1, calc("a", "a"))

    # 片方、もしくは両方が浮動小数点
    def test_calc_mul_float_normal(self):
        self.assertEqual(-1, calc(0.1, 500))

    def test_calc_mul_normal_float(self):
        self.assertEqual(-1, calc(500, 0.1))

    def test_calc_mul_float_float(self):
        self.assertEqual(-1, calc(0.1, 0.1))
