#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

    # 計算結果の確認
    # 同値
    def test_calc1 (self):
        self.assertEqual (25, calc(5,5))
    
    # A < B
    def test_calc2 (self):
        self.assertEqual (20, calc(4,5))
    
    # A > B
    def test_calc3 (self):
        self.assertEqual (20, calc(5,4))

    # 範囲の確認
    def test_range1 (self):
        self.assertEqual (-1, calc(0,0))

    def test_range2 (self):
        self.assertEqual (-1, calc(0,1))

    def test_range3 (self):
        self.assertEqual (-1, calc(0,999))

    def test_range4 (self):
        self.assertEqual (-1, calc(0,1000))
    
    def test_range5 (self):
        self.assertEqual (-1, calc(1,0))

    def test_range6 (self):
        self.assertEqual (1, calc(1,1))

    def test_range7 (self):
        self.assertEqual (999, calc(1,999))

    def test_range8 (self):
        self.assertEqual (-1, calc(1,1000))

    def test_range9 (self):
        self.assertEqual (-1, calc(999,0))

    def test_range10 (self):
        self.assertEqual (999, calc(999,1))

    def test_range11 (self):
        self.assertEqual (998001, calc(999,999))

    def test_range12 (self):
        self.assertEqual (-1, calc(999,1000))
    
    def test_range13 (self):
        self.assertEqual (-1, calc(1000,0))

    def test_range14 (self):
        self.assertEqual (-1, calc(1000,1))

    def test_range15 (self):
        self.assertEqual (-1, calc(1000,999))

    def test_range16 (self):
        self.assertEqual (-1, calc(1000,1000))
    
    # 文字確認
    def test_str1 (self):
        self.assertEqual (-1, calc(1,'a'))

    def test_str2 (self):
        self.assertEqual (-1, calc('a', 1))
    
    def test_str3 (self):
        self.assertEqual (-1, calc('a','b'))
    
    def test_str4 (self):
        self.assertEqual (-1, calc(1,'1'))

    def test_str5 (self):
        self.assertEqual (-1, calc('1', 1))
    
    def test_str6 (self):
        self.assertEqual (-1, calc('1','1'))

    # 少数確認
    def test_float1 (self):
        self.assertEqual (-1, calc(1,1.1))

    def test_float2 (self):
        self.assertEqual (-1, calc(1.1, 1))
    
    def test_float3 (self):
        self.assertEqual (-1, calc(1.1, 1.1))
        
