#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        
        # def test_sample1 (self):
        #         self.assertEqual (21, calc(3,7))
        # def test_sample2 (self):
        #         self.assertEqual (-1, calc(0,150))
        # def test_sample3 (self):
        #         self.assertEqual (-1, calc('a','b'))
        # def test_sample4 (self):
        #         self.assertEqual (-1, calc(0.1,999))

        #Equivalence tests
        def test_equivalencesample1 (self):
                self.assertEqual (21, calc(3,7))
        def test_equivalencesample2 (self):
                self.assertEqual(1000, calc(2,500))

        #Other input tests
        def test_othersample1 (self):
                self.assertEqual (-1, calc('a','b'))
        def test_othersample2 (self):
                self.assertEqual (-1, calc(1,'b')) 
        def test_othersample3 (self):
                self.assertEqual (-1, calc('a',1))

        #Decimal Fraction tests
        def test_fractionsample1 (self):
                self.assertEqual(-1, calc(1.5,4.0))
        def test_fractionsample2 (self):
                self.assertEqual (-1, calc(0.1,999))
        
        #Null tests
        def test_nullsample1 (self):
                self.assertEqual(-1, calc(None,1))
        def test_nullsample2 (self):
                self.assertEqual(-1, calc(1,None))
        def test_nullsample3 (self):
                self.assertEqual(-1, calc(None,None))

        #Boundary tests
        def test_boundarysample1 (self):
                self.assertEqual(1, calc(1,1))
        def test_boundary13 (self):
                self.assertEqual(998001,calc(999,999))
        

