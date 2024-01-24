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
    
        def test_valid_case1(self):
                self.assertNotEqual(-1, calc(5, 10))

        def test_valid_case2(self):
                self.assertNotEqual(-1, calc(1, 999))

        def test_invalid_case1(self):
                self.assertEqual(-1, calc(-5, 10))
        
        def test_invalid_case2(self):
                self.assertEqual(-1, calc(10, 5))

        def test_invalid_case3(self):
                self.assertEqual(-1, calc(5, 10000))

        def test_invalid_case4(self):
                self.assertEqual(-1, calc(5.3, 10))

