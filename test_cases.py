#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        #normal test
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,100)) #a=0

        def test_sample3 (self):
                self.assertEqual (-1, calc(1,1001)) #b>999
        def test_sample4 (self):
                self.assertEqual (-1, calc(-2,2)) #a<0
        #force error

        def test_sample5 (self):
                self.assertEqual (-1, calc(0.1,999)) #aが少数
        def test_sample6 (self):
                self.assertEqual (-1, calc(1,2.2)) #bが少数
        def test_sample7 (self):
                self.assertEqual (-1, calc(1.1,2.2)) #a and b が少数
        def test_sample8 (self):
                self.assertEqual (-1, calc('a','b')) #a and b が文字
        def test_sample9 (self):
                self.assertEqual (-1, calc(2**10,1000)) #数字以外の文字列
        ########################################################################
        def test_sample10 (self):
                self.assertEqual (6, calc('2','3'))
        def test_sample11 (self):
                self.assertEqual (6, calc("2","3")) 
        def test_sample12 (self):
                self.assertEqual (6, calc(2,'3'))
        def test_sample13 (self):
                self.assertEqual (-1, calc(4,3)) #a>b
        def test_sample14 (self):
                self.assertEqual (-1, calc(2,2)) #b=a
        ################################
        def test_sample15 (self):
                self.assertEqual (-1, calc(1000000,100000000)) #b>999