#!/usr/bin/python3

import unittest
from math import sqrt
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # real integer number
        def test_sample1 (self):
                self.assertEqual (-1, calc(-10,10)) # ok
        def test_sample2 (self):
                self.assertEqual (-1, calc(-1,10)) # ok
        def test_sample3 (self):
                self.assertEqual (-1, calc(0,10)) # ok
        def test_sample4 (self):
                self.assertEqual (10, calc(1,10)) # ok
        def test_sample5 (self):
                self.assertEqual (100, calc(10,10)) # FAIL
        def test_sample6 (self):
                self.assertEqual (1000, calc(100,10)) # FAIL
        def test_sample7 (self):
                self.assertEqual (1000, calc(1e2,10)) # FAIL
        def test_sample8 (self):
                self.assertEqual (9990, calc(999,10)) # FAIL
        def test_sample9 (self):
                self.assertEqual (-1, calc(1000,10)) # ok
        
        # real decimal fraction
        def test_sample10 (self):
                self.assertEqual (-1, calc(0.9,10)) # FAIL
        def test_sample11 (self):
                self.assertEqual (-1, calc(0.999999999999999999999999999,10)) # FAIL
        def test_sample12 (self):
                self.assertEqual (-1, calc(1.000000000000000000000000001,10)) # FAIL
        def test_sample13 (self):
                self.assertEqual (-1, calc(1.1,10)) # FAIL
        def test_sample14 (self):
                self.assertEqual (-1, calc(998.999999999999999999999999,10)) # ok
        def test_sample15 (self):
                self.assertEqual (-1, calc(999.000000000000000000000001,10)) # ok
        def test_sample16 (self):
                self.assertEqual (-1, calc(999.1,10)) # ok
        
        # real irrational number
        def test_sample17 (self):
                self.assertEqual (-1, calc(sqrt(2),10)) # FAIL
        
        # complex number
        def test_sample18 (self):
                self.assertEqual (-1, calc(10j,10)) # ERROR
        def test_sample19 (self):
                self.assertEqual (-1, calc(1+10j,10)) # ERROR
        
        # character
        def test_sample20 (self):
                self.assertEqual (-1, calc('a',10)) # ok
        def test_sample21 (self):
                self.assertEqual (10, calc('1',10)) # ok
        

        # None
        def test_sample22 (self):
                self.assertEqual (-1, calc(None,10)) # ERROR

        


