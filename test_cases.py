#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_
class TestCalc (unittest.TestCase):

        #有効同値
        def test_enable_int(self):
                self.assertEqual (999, calc(1,999))
        def test_enable_int_equ(self):
                self.assertEqual (250000, calc(500,500))
        def test_enable_float(self):
                self.assertEqual (999, calc(1.0,999.0))
        def test_enable_float_equ(self):
                self.assertEqual (250000, calc(500.0,500.0))
        def test_enable_str_int(self):
                self.assertEqual (999, calc('1','999'))
        def test_enable_str_int_equ(self):
                self.assertEqual (250000, calc('500','500'))
        def test_enable_str_float(self):
                self.assertEqual (999, calc('1.0','999.0'))
        def test_enable_str_float_equ(self):
                self.assertEqual (250000, calc('500.0','500.0'))
        
        #無効同値
        def test_disable_int_out_min(self):
                #int_min
                self.assertEqual(-1, calc(500,0))
        def test_disable_int_out_max(self):
                #int_max
                self.assertEqual(-1, calc(500,1000))
        def test_disable_int_out_out(self):
                #int
                self.assertEqual(-1, calc(1000,1000))            
        def test_disable_float_min(self):
                #float_min
                self.assertEqual(-1, calc(500,1.1))
        def test_disable_float_max(self):
                #float_max
                self.assertEqual(-1, calc(500,998.9))
        def test_disable_float_out_min(self):
                #float_out_min
                self.assertEqual(-1, calc(500,0.9))
        def test_disable_float_out_max(self):
                #float_out_max
                self.assertEqual(-1, calc(500,999.1))
        def test_disable_float_out_out(self):
                #float
                self.assertEqual(-1, calc(999.1,999.1))
        def test_disable_intstr_out_min(self):
                #intstr_min
                self.assertEqual(-1, calc('500','0'))
        def test_disable_intstr_out_max(self):
                #intstr_max
                self.assertEqual(-1, calc('500','1000'))
        def test_disable_intstr_out_out(self):
                #intstr
                self.assertEqual(-1, calc('1000','1000'))            
        def test_disable_floatstr_min(self):
                #floatstr_min
                self.assertEqual(-1, calc('500','1.1'))
        def test_disable_floatstr_max(self):
                #floatstr_max
                self.assertEqual(-1, calc('500','998.9'))
        def test_disable_floatstr_out_min(self):
                #floatstr_out_min
                self.assertEqual(-1, calc('500','0.9'))
        def test_disable_floatstr_out_max(self):
                #floatstr_out_max
                self.assertEqual(-1, calc('500','999.1'))
        def test_disable_floatstr_out_out(self):
                #floatstr
                self.assertEqual(-1, calc('999.1','999.1'))  

        #A=None
        def test_disable_none(self):
                #None
                self.assertEqual(-1, calc(None, None))
        def test_disable_none_str(self):
                #str
                self.assertEqual(-1, calc(None, 'a'))
        def test_disable_none_int(self):
                #範囲内int
                self.assertEqual(-1, calc(None, 500))
        def test_disable_none_int_out_min(self):
                #範囲外int_min
                self.assertEqual(-1, calc(None, 0))
        def test_disable_none_int_out_max(self):
                #範囲外int_max
                self.assertEqual(-1, calc(None, 1000))
        def test_disable_none_float(self):
                #範囲内float
                self.assertEqual(-1, calc(None, 500.0))
        def test_disable_none_float_out_min(self):
                #範囲外float_min
                self.assertEqual(-1, calc(None, 0))
        def test_disable_none_float_out_max(self):
                #範囲外float_max
                self.assertEqual(-1, calc(None, 1000))
        def test_disable_none_intstr(self):
                #範囲内intstr
                self.assertEqual(-1, calc(None, '500'))
        def test_disable_none_intstr_out_min(self):
                #範囲外intstr_min
                self.assertEqual(-1, calc(None, '0'))
        def test_disable_none_intstr_out_max(self):
                #範囲外intstr_max
                self.assertEqual(-1, calc(None, '1000'))
        def test_disable_none_floatstr(self):
                #範囲内floatstr
                self.assertEqual(-1, calc(None, '500.0'))
        def test_disable_none_floatstr_out_min(self):
                #範囲外floatstr_min
                self.assertEqual(-1, calc(None, '0'))
        def test_disable_none_floatstr_out_max(self):
                #範囲外floatstr_max
                self.assertEqual(-1, calc(None, '1000'))
        
        #A='a'
        def test_disable_str(self):
                self.assertEqual(-1, calc('a','a'))
                #A='a'
        def test_disable_str_none(self):
                self.assertEqual(-1, calc('a',None))
        def test_disable_str_int(self):
                #範囲内int
                self.assertEqual(-1, calc('a', 500))
        def test_disable_str_int_out_min(self):
                #範囲外int_min
                self.assertEqual(-1, calc('a', 0))
        def test_disable_str_int_out_max(self):
                #範囲外int_max
                self.assertEqual(-1, calc('a', 1000))
        def test_disable_str_float(self):
                #範囲内float
                self.assertEqual(-1, calc('a', 500.0))
        def test_disable_str_float_out_min(self):
                #範囲外float_min
                self.assertEqual(-1, calc('a', 0))
        def test_disable_str_float_out_max(self):
                #範囲外float_max
                self.assertEqual(-1, calc('a', 1000))
        def test_disable_str_intstr(self):
                #範囲内intstr
                self.assertEqual(-1, calc('a', '500'))
        def test_disable_str_intstr_out_min(self):
                #範囲外intstr_min
                self.assertEqual(-1, calc('a', '0'))
        def test_disable_str_intstr_out_max(self):
                #範囲外intstr_max
                self.assertEqual(-1, calc('a', '1000'))
        def test_disable_str_floatstr(self):
                #範囲内floatstr
                self.assertEqual(-1, calc('a', '500.0'))
        def test_disable_str_floatstr_out_min(self):
                #範囲外floatstr_min
                self.assertEqual(-1, calc('a', '0'))
        def test_disable_str_floatstr_out_max(self):
                #範囲外floatstr_max
                self.assertEqual(-1, calc('a', '1000'))