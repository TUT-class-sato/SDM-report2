#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        # 整数(1~999)
        #１より小さい範囲外の値,１より小さい範囲外の値
        def test_sample1 (self):
                self.assertEqual (-1, calc(-5,0))
        #１より小さい範囲外の値,範囲内の値
        def test_sample2 (self):
                self.assertEqual (-1, calc(0,1))
        #１より小さい範囲外の値,範囲外の値
        def test_sample3 (self):
                self.assertEqual (-1, calc(0,1000))
        #範囲内の値, 範囲内の値
        def test_sample4 (self):
                self.assertEqual (999, calc(1,999))
        #範囲内の値, 範囲外の値
        def test_sample5 (self):
                self.assertEqual (-1, calc(999,1000))
        #範囲外の値,範囲外の値
        def test_sample6 (self):
                self.assertEqual (-1, calc(1000,1000))
        
        # 少数(1~999)
        #１より小さい範囲外の値,１より小さい範囲外の値
        def test_sample7 (self):
                self.assertEqual (-1, calc(-0.5,0.3))
        #１より小さい範囲外の値,範囲内の値
        def test_sample8 (self):
                self.assertEqual (-1, calc(0.1,1.04))
        #１より小さい範囲外の値,範囲外の値
        def test_sample9 (self):
                self.assertEqual (-1, calc(0.115,100.444))
        #範囲内の値, 範囲内の値
        def test_sample10 (self):
                self.assertEqual (-1, calc(1.333,998.3))
        #範囲内の値, 範囲外の値
        def test_sample11 (self):
                self.assertEqual (-1, calc(1.333,1000.333))
        #範囲外の値,範囲外の値
        def test_sample12 (self):
                self.assertEqual (-1, calc(1000.333,10002222))

        # 文字
        #　数字の文字列
        def test_sample13 (self):
                self.assertEqual (-1, calc("1.13","7"))
        #　数字なしの文字列
        def test_sample14 (self):
                self.assertEqual (-1, calc("A","B"))
        # 数字を含む文字列
        def test_sample15 (self):
                self.assertEqual (-1, calc('a1','4.5.6'))


        # 文字と数字(1~999)
        #　文字と少数
        def test_sample16 (self):
                self.assertEqual (-1, calc(1.13,"a"))
        #　文字と数字
        def test_sample17 (self):
                self.assertEqual (-1, calc("A",15))

