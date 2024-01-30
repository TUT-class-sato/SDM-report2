#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (999, calc(1,999)) #境界値を入力とした場合のテスト

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150)) #境界値1の隣の値である0を入力とした場合のテスト

        def test_sample3 (self):
                self.assertEqual (-1, calc(1,1000)) #境界値999の隣の値である1000を入力とした場合のテスト

        def test_sample4 (self):
                self.assertEqual (-1, calc('a','b')) #文字が入力された場合のテスト

        def test_sample5 (self):
                self.assertEqual (-1, calc(0.9,150))   #境界値1の隣の値で小数である0.9が入力された場合のテスト
 
        def test_sample6 (self):
                self.assertEqual (-1, calc(1,999.1))  #境界値999の隣の値で小数である999.1が入力された場合のテスト