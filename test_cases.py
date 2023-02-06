#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (20000, calc(100,200)) #有効同値
        def test_sample2 (self):
                self.assertEqual (-1, calc(1.1,5)) #無効同値(小数)
        def test_sample3 (self):
                self.assertEqual (-1, calc('a',1)) #無効同値(a文字列)
        def test_sample4 (self):
                self.assertEqual (-1, calc(1,'b')) #無効同値(b文字列)

        def test_sample5 (self):
                self.assertEqual (-1, calc(0,100)) #境界値分析
        def test_sample6 (self):
                self.assertEqual (100, calc(1,100))
        def test_sample7 (self):
                self.assertEqual (10000, calc(100,100))
        def test_sample8 (self):
                self.assertEqual (99900, calc(100,999))
        def test_sample9 (self):
                self.assertEqual (-1, calc(100,1000))


