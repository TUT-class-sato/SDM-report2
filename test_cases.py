#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #無効同値
        def test_disable_null_int (self):
                #Noneと整数
                self.assertEqual (-1, calc(None, 500))
        def test_disable_null_float (self):
                #Noneと整数
                self.assertEqual (-1, calc(None, 500.1))
        
        def test_disable_null_and_int_of_str (self):
                #Noneと文字型の整数
                self.assertEqual (-1, calc(None, '500'))
        
        def test_disable_null_str (self):
                #Noneと文字型
                self.assertEqual (-1, calc(None, 'zzz'))

        def test_disable_str_low (self):
                #str型小文字
                self.assertEqual (-1, calc('a', 500))
        
        def test_disable_str_up (self):
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

        def test_disable_float_min_out (self):
                #1~999を満たさない非整数(小)
                self.assertEqual (-1, calc(0.9, 500))
        
        def test_disable_float_max_out (self):
                #1~999を満たさない非整数(大)
                self.assertEqual (-1, calc(999.1, 500))
        
        def test_disable_int_min_out (self):
                #1~999を満たさない(小)
                self.assertEqual (-1, calc(0, 500))
        
        def test_disable_int_max_out (self):
                #1~999を満たさない(大)
                self.assertEqual (-1, calc(1000, 500))
        
        def test_disable_Negative (self):
                #1~999を満たすの負数
                self.assertEqual (-1, calc(-500, 500))
                
        def test_disable_Negative_out (self):
                #1~999を満たさない負数
                self.assertEqual (-1, calc(-1000, 500))

        #有効同値
        def test_enable_int (self):
                #1~999を満たすA!=B
                self.assertEqual (999, calc(1, 999))
        
        def test_enable_int_equ (self):
                ##1~999を満たすA==B
                self.assertEqual (250000, calc(500, 500))

        def test_enable_float (self):
                #float型の整数
                self.assertEqual (999, calc(1.0, 999.0))
        
        def test_enable_str (self):
                #str型の整数
                self.assertEqual (999, calc('1.0', '999.0'))