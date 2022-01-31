#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        """
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
        """
        def test_sample1 (self): #a<b 成功
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self): #a>b 成功
                self.assertEqual (21, calc(7,3))

        def test_sample3 (self): #文字
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self): #a<1
                self.assertEqual (-1, calc(0,150))

        def test_sample5 (self): #aが小数
                self.assertEqual (-1, calc(0.1,999))

        def test_sample6 (self): #a>999
                self.assertEqual (-1, calc(1000,100))

        def test_sample7 (self): #b<1
                self.assertEqual (-1, calc(150,0))
        
        def test_sample8 (self): #bが小数
                self.assertEqual (-1, calc(999,0.1))

        def test_sample9 (self): #b>999
                self.assertEqual (-1, calc(100,1000))