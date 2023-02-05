#!/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc (unittest.TestCase):

    def test_sample1 (self):
        self.assertEqual(10, calc(1,10))
    
    def test_sample2 (self):
        self.assertEqual(-1, calc(0,10))

    def test_sample3 (self): 
        self.assertEqual(10, calc(10,0))

    def test_sample4 (self): 
        self.assertEqual(9990, calc(999,10))

    def test_sample5 (self): 
        self.assertEqual(9990, calc(10,999))

    def test_sample6 (self): 
        self.assertEqual(-1, calc(1000,10))

    def test_sample7 (self): 
        self.assertEqual(-1, calc(0.1,10))

    def test_sample8 (self): 
        self.assertEqual(-1, calc(10,'a'))

