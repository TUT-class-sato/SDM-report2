#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # It multiplies given two values
        def test_sample1 (self):
                self.assertEqual (3*7, calc(3,7))
        
        # It multiplies if A is greater than B
        def test_sample2 (self):
                self.assertEqual (7*3, calc(7,3))
        
        # It fails if A is decimal
        def test_sample3 (self):
                self.assertEqual (-1, calc(1.5,2))
        
        # It fails if B is decimal
        def test_sample4 (self):
                self.assertEqual (-1, calc(2,1.5))
        
        # It fails if A is lower than １
        def test_sample5 (self):
                self.assertEqual (-1, calc(0,7))
        
        # It fails if A is greater than 999
        def test_sample6 (self):
                self.assertEqual (-1, calc(1000,7))
        
        # It fails if B is lower than 0
        def test_sample7 (self):
                self.assertEqual (-1, calc(3,0))
        
        # It fails if B is greater than 999
        def test_sample8 (self):
                self.assertEqual (-1, calc(3,1000))
        
        # It fails if A is not an integer
        def test_sample9 (self):
                self.assertEqual (-1, calc("3",7))
        
        # It fails if B is not an integer
        def test_sample10 (self):
                self.assertEqual (-1, calc(3,"7"))

