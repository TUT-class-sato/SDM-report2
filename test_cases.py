#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc (unittest.TestCase):

    # 有効同値
    def test_sample1(self):
        self.assertEqual(21, calc(3, 7))  # A<B

    def test_sample2(self):
        self.assertEqual(36, calc(12, 3))  # B<A

    def test_sample3(self):
        self.assertEqual(9, calc(3, 3))  # A=B

    # 無効同値
    def test_sample4(self):
        self.assertEqual(-1, calc(0, 150))  # A<1

    def test_sample5(self):
        self.assertEqual(-1, calc(1, 1000))  # 999<B

    def test_sample6(self):
        self.assertEqual(-1, calc('a', 'b'))  # A,Bがstr(数字じゃない)

    def test_sample7(self):
        self.assertEqual(-1, calc('a',  4))  # 片方がstr

    def test_sample8(self):
        self.assertEqual(-1, calc(12.5, 99.9))  # 両方が浮動小数型

    def test_sample9(self):
        self.assertEqual(-1, calc(0.1, 999))  # 片方が浮動小数型
