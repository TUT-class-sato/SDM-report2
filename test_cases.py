#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #無効同値
        def test_disable_null (self):
                #入力無し
                self.assertEqual (-1, calc(None, 500))

        def test_disable_char1 (self):
                #str型小文字
                self.assertEqual (-1, calc('a', 500))
        
        def test_disable_char2 (self):
                #str型大文字
                self.assertEqual (-1, calc('ZZZ', 500))

        def test_disable_symbols (self):
                #str型記号
                self.assertEqual (-1, calc('!', 500))
        
        def test_disable_float_min (self):
                #1~999を満たす非整数(小)
                self.assertEqual (-1, calc(1.1, 500))
        
        def test_disable_float_max (self):
                #1~999を満たす非整数(大)
                self.assertEqual (-1, calc(998.9, 500))
        
        def test_disable_int_min (self):
                #1~999を満たさない(小)
                self.assertEqual (-1, calc(0, 500))
        
        def test_disable_int_max (self):
                #1~999を満たさない(大)
                self.assertEqual (-1, calc(1000, 500))
        
        def test_disable_Negative (self):
                #1~999を満たすの負数
                self.assertEqual (-1, calc(-500, 500))
                
        def test_disable_Negative2 (self):
                #1~999を満たさない負数
                self.assertEqual (-1, calc(-1000, 500))

        #有効同値
        def test_enable1 (self):
                #ノーマル
                self.assertEqual (999, calc(1, 999))

        def test_enable2 (self):
                #float型の整数
                self.assertEqual (999, calc(1.0, 999.0))
        
        def test_enable3 (self):
                #str型の整数
                self.assertEqual (999, calc('1.0', '999.0'))