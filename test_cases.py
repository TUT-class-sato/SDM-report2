#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

    def t_sample1 (self):
        self.assertEqual (21, calc(3,7))

    def test_sample2_0 (self):
        self.assertEqual (-1, calc(0,1000))
    def test_sample2_1 (self):
        self.assertEqual (-1, calc(0,150))
    def test_sample2_2 (self): 
        self.assertEqual (-1, calc(150,1000))

    def test_sample3_0 (self):
        self.assertEqual (-1, calc('a','b'))
    def test_sample3_1 (self):                            
        self.assertEqual (-1, calc('a',100))
    def test_sample3_2 (self):
        self.assertEqual (-1, calc(900,'b'))
         
    def test_sample4_0 (self):
        self.assertEqual (-1, calc(0.1,998.9))
    def test_sample4_1 (self):
        self.assertEqual (-1, calc(0.1,999))
    def test_sample4_2 (self):
        self.assertEqual (-1, calc(1,998.9))
