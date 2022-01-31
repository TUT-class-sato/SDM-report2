#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #normal  test
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))
        
        # edge cases

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))  # a=0
        
        def test_sample3 (self):
                self.assertEqual (-1, calc(1,1000)) # b > 999
        
        def test_sample4 (self):
                self.assertEqual (-1, calc(-1,2)) # a<0

        # force error

        def test_sample5 (self):
                self.assertEqual (-1, calc(0.1,999)) # Aが少数
 
        def test_sample6 (self):
                self.assertEqual (-1, calc(1,1.5)) #　Bが少数

        def test_sample7 (self):
                self.assertEqual (-1, calc(1.2,1.5)) #　AとBが少数
 
        def test_sample8 (self):
                self.assertEqual (-1, calc('a','b')) #A,Bが数字ではない
        
        def test_sample9 (self):
                self.assertEqual (-1, calc(10**2,2))#数字以外の文字列を含む

        # calc()関数の定義により、"数字"または'数字'が数字として取り扱うことができると考えられる
        def test_sample10 (self):
                self.assertEqual (2, calc("1","2"))

        def test_sample11 (self):
                self.assertEqual (2, calc('1','2'))
        
        def test_sample12 (self):
                self.assertEqual (2, calc(1,'2'))

        #***********
        
        def test_sample13 (self):
                self.assertEqual (-1, calc(3,2)) # a>b

        def test_sample14 (self):
                self.assertEqual (-1, calc(2,2)) # a=b
        
        #とても大き数字を計算
        def test_sample15 (self):
                self.assertEqual (-1, calc(100000000000000000000000000000000000000000000,9223372036854775807000000))
        



        
        


        

