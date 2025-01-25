#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_additional01 (self):
            self.assertEqual(480, calc(20, 24))

        def test_additional02 (self):
            self.assertEqual(1, calc(1, 1))

        def test_additional03 (self):
            self.assertEqual(999, calc(999, 1))

        def test_additional04 (self):
            self.assertEqual(999, calc(1, 999))

        def test_additional05 (self):
            self.assertEqual(998001, calc(999, 999))

        def test_additional06 (self):
            self.assertEqual(-1, calc(-2024, 10))

        def test_additional07 (self):
            self.assertEqual(-1, calc(10, -2024))

        def test_additional08 (self):
            self.assertEqual(-1, calc(0, 10))

        def test_additional09 (self):        
            self.assertEqual(-1, calc(10, 0))
                
        def test_additional10 (self):
            self.assertEqual(-1, calc(1000, 10))
                
        def test_additional11 (self):        
            self.assertEqual(-1, calc(10, 1000))

        def test_additional12 (self):
            self.assertEqual(-1, calc(2024, 10))
                
        def test_additional13 (self):        
            self.assertEqual(-1, calc(10, 2024))

        def test_additional14(self):
            self.assertEqual(-1, calc(0.1, 10))

        def test_additional15(self):
            self.assertEqual(-1, calc(10, 0.1))

        def test_additional16(self):
            self.assertEqual(-1, calc(0.1, 0.1))

        def test_additional17(self):
            self.assertEqual(12, calc('2', '6'))

        def test_additional18(self):
            self.assertEqual(-1, calc('２', '６'))

        def test_additional19(self):
            self.assertEqual(-1, calc('a', 10))

        def test_additional20(self):
            self.assertEqual(-1, calc(10, 'a'))

        def test_additional21(self):
            self.assertEqual(-1, calc('a', 'a'))

        def test_additional22(self):
            self.assertEqual(-1, calc('1a', 10))

        def test_additional23(self):
            self.assertEqual(-1, calc(10, '1a'))

        def test_additional24(self):
            self.assertEqual(-1, calc('1a', '1a'))

        def test_additional25(self):
            self.assertEqual(-1, calc('a1', 10))

        def test_additional26(self):
            self.assertEqual(-1, calc(10, 'a1'))

        def test_additional27(self):
            self.assertEqual(-1, calc('a1', 'a1'))

