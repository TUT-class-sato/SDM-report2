#!/usr/bin/python3
# coding: utf-8

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #同値分割(整数)
        #(1より小さい範囲外整数,1より小さい範囲外整数)
        def test_sample01 (self):
               self.assertEqual (-1, calc(-10,-10))
        #(1より小さい範囲外整数,範囲内整数)
        def test_sample02 (self):
               self.assertEqual (-1, calc(0,150))
        #(範囲内整数A,範囲内整数B) 正しA<B
        def test_sample03 (self):
               self.assertEqual (3*7, calc(3,7))
        #(範囲内整数A,範囲内整数B) 正しA>B
        def test_sample04 (self):
               self.assertEqual (3*7, calc(7,3))
        #(範囲内整数,999より大きい範囲外整数)
        def test_sample05 (self):
                self.assertEqual (-1, calc(1,1000))
        #(999より大きい範囲外整数,999より大きい範囲外整数)
        def test_sample06 (self):
                self.assertEqual (-1, calc(1000,2000))


        #例外判定(小数)
        #(範囲内整数,範囲内小数)
        def test_sample07 (self):
               self.assertEqual (-1, calc(3,7.1))
        #(範囲内小数,範囲内小数)
        def test_sample08 (self):
               self.assertEqual (-1, calc(3.1,7.1))
        

        #例外判定(文字列)
        #(数字無し文字列,数字無し文字列)
        def test_sample09 (self):
                self.assertEqual (-1, calc('a','b'))
        #(数字有り文字列,数字有り文字列)
        def test_sample10 (self):
                self.assertEqual (-1, calc('a1','999b'))
        #(数字のみ文字列,数字のみ文字列)
        def test_sample11 (self):
                self.assertEqual (-1, calc('1','999'))



