#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        '''
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
        '''
        def test_sample1 (self):#成功サンプル　a<b
                self.assertEqual (999, calc(1,999))
        
        def test_sample2 (self):#失敗サンプル　a<1
                self.assertEqual (-1, calc(0,100))

        def test_sample3 (self):#失敗サンプル　999<a
                self.assertEqual (-1, calc(1000,100))

        def test_sample4 (self):#失敗サンプル a:小数
                self.assertEqual (-1, calc(0.1,999))
        
        def test_sample5 (self):#失敗サンプル 文字
                self.assertEqual (-1, calc('a','b'))
        
        def test_sample6 (self):#成功サンプル a>b
                self.assertEqual (999, calc(999,1))

        def test_sample7 (self):#失敗サンプル b<1
                self.assertEqual (-1, calc(100,0))
        
        def test_sample8 (self):#失敗サンプル 999<b
                self.assertEqual (-1, calc(100,1000))

        def test_sample9 (self):#失敗サンプル b:小数
                self.assertEqual (-1, calc(999,0.1))
        
        def test_sample10 (self):#失敗サンプル a:負の数
                self.assertEqual (-1, calc(-1,999))

        def test_sample11 (self):#失敗サンプル b:負の数
                self.assertEqual (-1, calc(-1,999))
        

        