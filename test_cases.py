#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc (unittest.TestCase):

    # -----------正業な処理
    def test_sample1(self):
        self.assertEqual(21, calc(3, 7))

    # ------------入力範囲外(下限error)

    def test_sample2_1(self):
        self.assertEqual(-1, calc(0, 150))

    def test_sample2_2(self):
        self.assertEqual(-1, calc(100, 0))

    def test_sample2_3(self):
        self.assertEqual(-1, calc(-230, -100))

    # ------------上界エラー
    def test_sample2_4(self):
        self.assertEqual(-1, calc(1400, 13))

    def test_sample2_5(self):
        self.assertEqual(-1, calc(14, 1300))

    def test_sample2_6(self):
        self.assertEqual(-1, calc(1400, 1300))

    # ------------文字入力
    def test_sample3_1(self):
        self.assertEqual(-1, calc('a', 'b'))

    def test_sample3_2(self):
        self.assertEqual(-1, calc('a', 12))

    def test_sample3_3(self):
        self.assertEqual(-1, calc(12, 'b'))

    def test_sample4(self):
        self.assertEqual(-1, calc(0.1, 999))

    def test_sample4_2(self):
        self.assertEqual(-1, calc(99, 0.1))

    def test_sample4_3(self):
        self.assertEqual(-1, calc(100.0, 0.1))

    def test_sample4_4(self):
        self.assertEqual(-1, calc(0.1, 1000))

    def test_sample4_5(self):
        self.assertEqual(-1, calc(-1000, 0.1))

    def test_sample4_6(self):
        self.assertEqual(-1, calc(0.1, -1000))

    def test_sample4_7(self):
        self.assertEqual(-1, calc(390, 500.3))

    #-------------正常な範囲でA>Bの場合
    def test_sample5(self):
        self.assertEqual(40, calc(10, 4))
