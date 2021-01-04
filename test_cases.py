#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # Bは正しい値でAが異常値の場合
        #無効同値

        #数値でない
        def test_sample1 (self):
                self.assertEqual (-1, calc('hello',123))

        #小数点を持つ数値
        def test_sample2 (self):
                self.assertEqual (-1, calc(-1.2345,123))

        #999より大きい整数
        def test_sample3 (self):
                self.assertEqual (-1, calc(1234,123))

        #1未満の整数
        def test_sample4 (self):
                self.assertEqual (-1, calc(0,123))


        #有効同値

        #1から999の間でA>Bとなる整数
        def test_sample5 (self):
                self.assertEqual (645498, calc(987,654))

        #1から999の間でA<Bとなる整数
        def test_sample6 (self):
                self.assertEqual (39483, calc(123,321))

        #1から999の間でA=Bとなる整数
        def test_sample7 (self):
                self.assertEqual (308025, calc(555,555))


        # Aは正しい値でBが異常値の場合

        #無効同値

        #数値でない
        def test_sample8 (self):
                self.assertEqual (-1, calc(123,'hello'))

        #小数点を持つ数値
        def test_sample9 (self):
                self.assertEqual (-1, calc(123,-1.2345))

        #999より大きい整数
        def test_sample10 (self):
                self.assertEqual (-1, calc(123,1234))

        #1未満の整数
        def test_sample11 (self):
                self.assertEqual (-1, calc(123,0))
