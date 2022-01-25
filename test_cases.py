#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #無効同値
        def test_disable_null (self):
                self.assertEqual (-1, calc(None, 500))

        def test_disable_char1 (self):
                self.assertEqual (-1, calc('a', 500))
        
        def test_disable_char2 (self):
                self.assertEqual (-1, calc("ZZZ", 500))

        def test_disable_num_of_char (self):
                self.assertEqual (-1, calc('1', 500))
        
        def test_disable_float_min (self):
                self.assertEqual (-1, calc(1.1, 500))
        
        def test_disable_float_max (self):
                self.assertEqual (-1, calc(998.9, 500))
        
        def test_disable_int_min (self):
                self.assertEqual (-1, calc(0, 500))
        
        def test_disable_int_max (self):
                self.assertEqual (-1, calc(1000, 500))
        
        def test_disable_Negative (self):
                self.assertEqual (-1, calc(-500, 500))
                
        def test_disable_Negative2 (self):
                self.assertEqual (-1, calc(-1000, 500))

        #有効同値
        def test_enable1 (self):
                self.assertEqual (999, calc(1, 999))

        def test_enable2 (self):
                self.assertEqual (999, calc(1.0, 999.0))
        
        def test_enable3 (self):
                self.assertEqual (999, calc('1', '999'))
        
        def test_enable4 (self):
                self.assertEqual (999, calc("1.0", "999.0"))