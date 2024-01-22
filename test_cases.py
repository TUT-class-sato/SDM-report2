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

        def test_border (self):
                # 境界値分割
                self.assertEqual (-1, calc(150,0))
                self.assertEqual (-1, calc(1000,150))
                self.assertEqual (-1, calc(150, 1000))
                
        def test_eq (self):
                # 同値分割 (どちらも適切なのは既にtest_sample1で行っている)
                self.assertEqual (-1, calc(-9,3))
                self.assertEqual (-1, calc(3,-9))
                self.assertEqual (-1, calc(1500, 3))
                self.assertEqual (-1, calc(3, 1500))
                self.assertEqual (-1, calc(6.9, 250))
                self.assertEqual (-1, calc(250, 6.9))
        
        def test_eq_str(self):
                # 同値分割、ただし文字列を入力した場合
                # (10進整数の、整数列しか受け付けないとする)
                self.assertEqual (-1, calc('0x12', '3'))
                self.assertEqual (66, calc('3','022'))
                self.assertEqual (-1, calc('3','9e2'))
                self.assertEqual (-1, calc('-3', '3'))
                self.assertEqual (-1, calc('6a', '250'))
                self.assertEqual (-1, calc('250', 'b6'))
