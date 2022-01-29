#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

    def test_sample1_1 (self): #正常ケース
                self.assertEqual (21, calc(3,7)) 
    
    def test_sample1_2 (self): #正常ケース 
                self.assertEqual (21, calc(7,3))

    def test_sample2_1 (self): #1入力目が1未満の整数
                self.assertEqual (-1, calc(0,150)) 

    def test_sample2_2 (self): #2入力目が1未満の整数
                self.assertEqual (-1, calc(150,0)) 

    def test_sample2_3 (self): #2入力が1未満の整数
                self.assertEqual (-1, calc(0,0)) 

    def test_sample3_1 (self): #1入力目が999より大きい値
                self.assertEqual (-1, calc(1000,1)) 

    def test_sample3_2 (self): #2入力目が999より大きい値
                self.assertEqual (-1, calc(1,1000)) 

    def test_sample3_3 (self): #2入力が999より大きい整数
                self.assertEqual (-1, calc(1000,1000)) 

    def test_sample4_1 (self): #1入力目が少数
                self.assertEqual (-1, calc(1.1,900)) 

    def test_sample4_2 (self): #2入力目が少数
                self.assertEqual (-1, calc(900,1.1))
    
    def test_sample4_3 (self): #2入力が少数
                self.assertEqual (-1, calc(99.9,1.1)) 