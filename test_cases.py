#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

         def test_case1 (self):
                self.assertEqual (21, calc(3,7))

        def test_case2 (self):
                self.assertEqual (21, calc(7,3))

        def test_case3 (self):
                self.assertEqual (2, calc(1,2))

        def test_case4 (self):
                self.assertEqual (-1, calc(0,1))
        
        def test_case5 (self):
                self.assertEqual (997002, calc(998,999))
        
        def test_case6 (self):
                self.assertEqual (-1, calc(999,1000))
        
        def test_case7 (self):
                self.assertEqual (250000, calc(500,500))
        
        def test_case8 (self):
                self.assertEqual (-1, calc(1.5,2))
        
        def test_case9 (self):
                self.assertEqual (-1, calc('a','b'))

