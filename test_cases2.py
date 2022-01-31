#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #A, Bの大小
        def test_sample1 (self):
                self.assertEqual (999, calc(1,999))
        def test_sample2 (self):
                self.assertEqual (999, calc(999,1))

        #数値の範囲
        def test_sample3 (self):
                self.assertEqual (-1, calc(0,1))
        def test_sample4 (self):
                self.assertEqual (-1, calc(1,1000))

        #数値の種類
        def test_sample5 (self):
                self.assertEqual (-1, calc(-10, -1))
        def test_sample6 (self):
                self.assertEqual (-1, calc(0.1, 1))

        #文字
        def test_sample7 (self):
                self.assertEqual (-1, calc('a', 1))
        def test_sample8 (self):
                self.assertEqual (-1, calc('123', 999))

        #記号
        def test_sample9 (self):
                self.assertEqual (-1, calc('10%', 999))
        def test_sample10 (self):
                self.assertEqual (-1, calc('1_1', 999))
