#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):


        def test_sample01 (self):
            self.assertEqual(480, calc(20, 24))

        def test_sample02 (self):
            self.assertEqual(1, calc(1, 1))

        def test_sample03 (self):
            self.assertEqual(999, calc(999, 1))

        def test_sample04 (self):
            self.assertEqual(999, calc(1, 999))

        def test_sample05 (self):
            self.assertEqual(998001, calc(999, 999))

        def test_sample06 (self):
            self.assertEqual(-1, calc(-2024, 10))

        def test_sample07 (self):
            self.assertEqual(-1, calc(10, -2024))

        def test_sample08 (self):
            self.assertEqual(-1, calc(0, 10))

        def test_sample09 (self):        
            self.assertEqual(-1, calc(10, 0))
                
        def test_sample10 (self):
            self.assertEqual(-1, calc(1000, 10))
                
        def test_sample11 (self):        
            self.assertEqual(-1, calc(10, 1000))

        def test_sample12 (self):
            self.assertEqual(-1, calc(2024, 10))
                
        def test_sample13 (self):        
            self.assertEqual(-1, calc(10, 2024))

        def test_sample14(self):
            self.assertEqual(-1, calc(0.1, 10))

        def test_sample15(self):
            self.assertEqual(-1, calc(10, 0.1))

        def test_sample16(self):
            self.assertEqual(-1, calc(0.1, 0.1))

        def test_sample17(self):
            self.assertEqual(12, calc('2', '6'))

        def test_sample18(self):
            self.assertEqual(12, calc('２', '６'))

        def test_sample19(self):
            self.assertEqual(-1, calc('a', 10))

        def test_sample20(self):
            self.assertEqual(-1, calc(10, 'a'))

        def test_sample21(self):
            self.assertEqual(-1, calc('a', 'a'))

        def test_sample22(self):
            self.assertEqual(-1, calc('1a', 10))

        def test_sample23(self):
            self.assertEqual(-1, calc(10, '1a'))

        def test_sample24(self):
            self.assertEqual(-1, calc('1a', '1a'))

        def test_sample25(self):
            self.assertEqual(-1, calc('a1', 10))

        def test_sample26(self):
            self.assertEqual(-1, calc(10, 'a1'))

        def test_sample27(self):
            self.assertEqual(-1, calc('a1', 'a1'))



