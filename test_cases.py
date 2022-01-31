#!/usr/bin/python3

import unittest
from calc_mul2 import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
    #A<1,0<B<1000
    def test_sample0 (self):
        self.assertEqual (-1, calc(-10,10))

    #0<A<1000,B<0
    def test_sample1 (self):
        self.assertEqual (-1, calc(10,-10))

    #<A<1000,0<B<1000
    def test_sample2 (self):
        self.assertEqual (100, calc(10,10))
    
    #A<0,B<0
    def test_sample3 (self):
        self.assertEqual (-1, calc(-10,-10))
    
    #999<A,0<B<1000
    def test_sample4 (self):
        self.assertEqual (-1, calc(1000,10))
      
    #0<A<1000,999<B  
    def test_sample5 (self):
        self.assertEqual (-1, calc(10,1000))

    #999<A,999<B 
    def test_sample6 (self):
        self.assertEqual (-1, calc(1000,1000))
    
    #Aが小数
    def test_sample7 (self):
        self.assertEqual (-1, calc(3.5,10))
    
    #Bが小数
    def test_sample8 (self):
        self.assertEqual (-1, calc(10,3.5))
    
    #AとBが小数
    def test_sample9 (self):
        self.assertEqual (-1, calc(3.5,4.5))
        

