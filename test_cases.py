#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # A, B are integer in range (0, 999). A < B
        def test_sample1 (self): 
                self.assertEqual (21, calc(3, 7))
        # A, B are integer in range (0, 999). A > B
        def test_sample2 (self):
                self.assertEqual (100, calc(20, 5))
        # A, B are integer in range (0, 999). A = B
        def test_sample3 (self):
                self.assertEqual (100, calc(10, 10))
        # A, B are not integer in range (0, 999). A < 1
        def test_sample4 (self):
                self.assertEqual (-1, calc(0, 150))
        # A, B are not integer in range (0, 999). B < 1
        def test_sample5 (self):
                self.assertEqual (-1, calc(150, 0))
        # A, B are not integer in range (0, 999). A & B < 1        
        def test_sample6 (self):
                self.assertEqual (-1, calc(0, 0))
        # A is not integer in range (0, 999). A > 999        
        def test_sample7 (self):
                self.assertEqual (-1, calc(1000, 150))
        # B are not integer in range (0, 999). B > 999   
        def test_sample8 (self): # b > 999
                self.assertEqual (-1, calc(150, 1000))
        # A, B are not integer in range (0, 999). A & B > 999
        def test_sample9 (self):
                self.assertEqual (-1, calc(1000, 1000))
        # A, B are not integer in range (0, 999). A > 999, B < 1
        def test_sample10 (self):
                self.assertEqual (-1, calc(1000, 0))
        # A, B are not integer in range (0, 999). A < 1, B > 999
        def test_sample11 (self):
                self.assertEqual (-1, calc(0, 1000))
        # A is String, B is integer in range (0, 999)
        def test_sample12 (self):
                self.assertEqual (-1, calc('aaa', 150))
        # A is integer in range (0, 999), B is String
        def test_sample13 (self): # b is STRING
                self.assertEqual (-1, calc(150, 'bbb'))
        # A, B are string
        def test_sample14 (self):
                self.assertEqual (-1, calc('aaa', 'bbb'))
        # A is decimal, B is integer in range (0, 999). A < B
        def test_sample15 (self):
                self.assertEqual (-1, calc(0.1, 999))
        # A is decimal, B is integer in range (0, 999). A > B
        def test_sample16 (self): 
                self.assertEqual (-1, calc(10.100, 10))
        # A is integer in range (0, 999), B is decimal. A < B
        def test_sample17 (self):
                self.assertEqual (-1, calc(10, 10.100))
        # A is integer in range (0, 999), B is decimal. A > B        
        def test_sample18 (self):
                self.assertEqual (-1, calc(999, 0.1))
        # A, B are decimal. A < B
        def test_sample19 (self):
                self.assertEqual (-1, calc(0.1, 10.100))
        # A, B are decimal. A > B
        def test_sample20 (self):
                self.assertEqual (-1, calc(10.100, 0.1))
        # A, B are decimal. A = B
        def test_sample21 (self):
                self.assertEqual (-1, calc(10.100, 0.1))






        