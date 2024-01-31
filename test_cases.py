#!/usr/bin/python3

import unittest

from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        # representive value: {int_a: [3, 7], int_b: 0, int_c: 1000, float: 1.5, str: ["x", "y"]}
        
        def test_int_a (self):
                self.assertEqual (9, calc(3, 3))
                self.assertEqual (21, calc(3, 7))
                self.assertEqual (21, calc(7, 3))
                
        def test_int_b (self):
                self.assertEqual (-1, calc(0, 0))
                self.assertEqual (-1, calc(0, 3))
                self.assertEqual (-1, calc(3, 0))
                
        def test_int_c (self):
                self.assertEqual (-1, calc(1000, 1000))
                self.assertEqual (-1, calc(1000, 3))
                self.assertEqual (-1, calc(3, 1000)) 

        def test_float (self):
                self.assertEqual (-1, calc(1.5, 1.5))
                self.assertEqual (-1, calc(1.5, 3))
                self.assertEqual (-1, calc(3, 1.5))
        
        def test_str (self):
                self.assertEqual (-1, calc("x", "y"))
                self.assertEqual (-1, calc("x", 3))
                self.assertEqual (-1, calc(3, "x"))
                