#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (-1, calc(1000,999))

        def test_sample2 (self):
                self.assertEqual (-1, calc(999,1000))

        def test_sample3 (self):
                self.assertEqual (998001, calc(999,999))

        def test_sample4 (self):
                self.assertEqual (350000, calc(700,500))
        
        def test_sample5 (self):
                self.assertEqual (350000, calc(500,700))

        def test_sample6 (self):
                self.assertEqual (250000, calc(500,500))
        
        def test_sample7 (self):
                self.assertEqual (1, calc(1,1))

        def test_sample8 (self):
                self.assertEqual (-1, calc(0,1))
        
        def test_sample9 (self):
                self.assertEqual (-1, calc(1,0))
        
        def test_sample10 (self):
                self.assertEqual (-1, calc(1.5,200))
        
        def test_sample11 (self):
                self.assertEqual (-1, calc(200,1.5))
        
        def test_sample12 (self):
                self.assertEqual (-1, calc(0.1,100))

        def test_sample13 (self):
                self.assertEqual (-1, calc(100,0.1))
        
        def test_sample14 (self):
                self.assertEqual (-1, calc('a',5))
        
        def test_sample15 (self):
                self.assertEqual (-1, calc(5,'a'))
        
        def test_sample16 (self):
                self.assertEqual (-1, calc('a',5.5))
        
        def test_sample17 (self):
                self.assertEqual (-1, calc(5.5,'a'))