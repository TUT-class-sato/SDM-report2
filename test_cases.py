#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        #valid equivalence
        def test_sample_valid1(self):
                self.assertEqual(250000, calc(500,500))
        
        def test_sample_valid2(self):
                self.assertEqual(10000, calc(100,100))

        def test_sample_valid3(self):
                self.assertEqual(50000, calc(100,500))

        def test_sample_valid4(self):
                self.assertEqual(90000, calc(100,900))
        
        def test_sample_valid5(self):
                self.assertEqual(50000, calc(500,100))
        
        def test_sample_valid6(self):
                self.assertEqual(450000, calc(500,900))
        
        def test_sample_valid7(self):
                self.assertEqual(90000, calc(900,100))
        
        def test_sample_valid8(self):
                self.assertEqual(450000, calc(900,500))
        
        def test_sample_valid9(self):
                self.assertEqual(810000, calc(900,900))

        #invalid equivalence
        def test_sample1 (self):
                self.assertEqual (-1, calc(0,0))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,500))

        def test_sample3 (self):
                self.assertEqual (-1, calc(0,1100))

        def test_sample4 (self):
                self.assertEqual (-1, calc(500,0))
        
        def test_sample5 (self):
                self.assertEqual (-1, calc(1100,0))
        
        def test_sample6 (self):
                self.assertEqual (-1, calc(500,1100))
        
        def test_sample7 (self):
                self.assertEqual (-1, calc(1100,500))

        def test_sample8 (self):
                self.assertEqual (-1, calc(1100,1100))
        
        def test_sample9 (self):
                self.assertEqual (-1, calc('a',500))

        def test_sample10 (self):
                self.assertEqual (-1, calc(500,'b'))

        def test_sample11 (self):
                self.assertEqual (-1, calc(1.1,500))

        def test_sample12 (self):
                self.assertEqual (-1, calc(500,500.1))

        def test_sample13 (self):
                self.assertEqual (-1, calc(500.1,500.1))

        def test_sample14 (self):
                self.assertEqual (-1, calc(0.1,99.9))

        def test_sample15(self):
                self.assertEqual(-1, calc('a','b'))

