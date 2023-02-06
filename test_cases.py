#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample2 (self):
                self.assertEqual (-1, calc('a',7))
        
        def test_sample3 (self):
                self.assertEqual (-1, calc(3,'b'))
                
        def test_sample4 (self):
                self.assertEqual (-1, calc(0,5))
                
        def test_sample5 (self):
                self.assertEqual (5, calc(1,5))
                
        def test_sample6 (self):
                self.assertEqual (-1, calc(999,5))
                
        def test_sample7 (self):
                self.assertEqual (-1, calc(1000,5))
                
        def test_sample8 (self):
                self.assertEqual (-1, calc(5,0))
                
        def test_sample9 (self):
                self.assertEqual (-1, calc(5,1))
                
        def test_sample10 (self):
                self.assertEqual (4995, calc(5,999))
                
        def test_sample11 (self):
                self.assertEqual (-1, calc(5,1000))
                        
        def test_sample12 (self):
                self.assertEqual (-1, calc(5,5))
        
        
        
