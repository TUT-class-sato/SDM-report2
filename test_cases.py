#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #正常な入力
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        #A,Bのどちらかの入力値に異常あり
        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('1',8))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_sample5 (self):
                self.assertEqual (-1, calc(3,999.1))
     
        def test_sample6 (self):
                self.assertEqual (-1, calc(3.5,10))       

        #A,Bどちらも入力値に異常あり
        def test_sample7 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample8 (self):
                self.assertEqual (-1, calc(0.1,999.1))

        def test_sample9 (self):
                self.assertEqual (-1, calc(3.5,90.9))
