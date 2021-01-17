#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # integer in [1, 999]
        def test01_BisGreater (self): # a < b
                self.assertEqual (21, calc(3,7))

        def test02_AisGreater (self): # a > b
                self.assertEqual (21, calc(7,3))

        def test03_BothAreSame (self): # a = b 
                self.assertEqual (25, calc(5,5))

        # integer but NOT in [1, 999]
        def test04_AisBelowTheRange (self): # a < 1
                self.assertEqual (-1, calc(0,150))

        def test05_AisAboveTheRange (self): # a > 999
                self.assertEqual (-1, calc(1000,150))

        def test06_BisBelowTheRange (self): # b < 1
                self.assertEqual (-1, calc(150,0))

        def test07_BisAboveTheRange (self): # b > 999
                self.assertEqual (-1, calc(150,1000))

        def test08_BothAreBelowTheRange (self): # a < 1; b < 1
                self.assertEqual (-1, calc(0,0))

        def test09_BothAreAboveTheRange (self): # a > 999; b > 999
                self.assertEqual (-1, calc(0,0))

        def test10_BothAreOutOfRange1 (self): # a < 1; b > 999
                self.assertEqual (-1, calc(1000,0))

        def test11_BothAreOutOfRange2 (self): # a > 999; b < 1
                self.assertEqual (-1, calc(0,1000))

        # STRING
        def test12_AisString (self): # a is STRING
                self.assertEqual (-1, calc('a',150))

        def test13_BisString (self): # b is STRING
                self.assertEqual (-1, calc(150,'b'))

        def test14_BothAreStrings (self): # a is STRING, b is STRING
                self.assertEqual (-1, calc('a','b'))

        # DECIMAL
        def test15_AisDecimalAndSmaller (self): # a is DECIMAL; a < b
                self.assertEqual (-1, calc(0.1,999))

        def test16_AisDecimalAndGreater (self): # a is DECIMAL; a > b
                self.assertEqual (-1, calc(10.1,9))

        def test17_BisDecimalandSmaller (self): # b is DECIMAL; a > b
                self.assertEqual (-1, calc(999,0.1))

        def test18_BisDecimalandGreater (self): # b is DECIMAL; a < b
                self.assertEqual (-1, calc(9,10.1))

        def test19_BothAreDecimals1 (self): # a is DECIMAL; b is DECIMAL; a < b
                self.assertEqual (-1, calc(0.1,10.1))

        def test20_BothAreDecimals2 (self): # a is DECIMAL; b is DECIMAL; a > b
                self.assertEqual (-1, calc(10.1,0.1))

        def test21_BothAreDecimals3 (self): # a is DECIMAL; b is DECIMAL; a = b
                self.assertEqual (-1, calc(10.1,10.1))

