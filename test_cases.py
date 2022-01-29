#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #def test_sample1 (self):
        #        self.assertEqual (21, calc(3,7))

        #def test_sample2 (self):
        #        self.assertEqual (-1, calc(0,150))

        #def test_sample3 (self):
        #        self.assertEqual (-1, calc('a','b'))

        #def test_sample4 (self):
        #        self.assertEqual (-1, calc(0.1,999))

        # 同値分割法によるテスト
        #１．どちらも正常値である場合（A<B）
        def test_sample1 (self):
                self.assertEqual (999, calc(1,999))

        #２．どちらも正常値である場合（A≧B）
        def test_sample2 (self):
                self.assertEqual (999, calc(999,1))

        #３．どちらかが範囲外である場合
        def test_sample3 (self):
                self.assertEqual (-1, calc(0.1,999))

        #４．どちらも範囲外である場合
        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,1000))

        #５．どちらかが文字である場合
        def test_sample5 (self):
                self.assertEqual (-1, calc('a',999))
        
        #６．どちらも文字である場合
        def test_sample6 (self):
                self.assertEqual (-1, calc('a','b'))

        #７．どちらかが小数である場合
        def test_sample7 (self):
                self.assertEqual (-1, calc(1.1,999))
        
        #８．どちらも小数である場合
        def test_sample8 (self):
                self.assertEqual (-1, calc(1.1,998.9))