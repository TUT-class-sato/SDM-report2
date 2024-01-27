#!/usr/bin/python3

import unittest
import sys
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

      #test input
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        #test edge cases
        def test_sample2 (self):
                self.assertEqual (1, calc(1,1))
        def test_sample3 (self):
                self.assertEqual (999, calc(1,999))
        def test_sample4 (self):
                self.assertEqual (999, calc(999,1))
        def test_sample5 (self):
                self.assertEqual (998001, calc(999,999))

        #test for outside range cases
        def test_sample6 (self):
                self.assertEqual (-1, calc(0,1))
        def test_sample7 (self):
                self.assertEqual (-1, calc(1,0))
        def test_sample8 (self):
                self.assertEqual (-1, calc(999,1000))
        def test_sample9 (self):
                self.assertEqual (-1, calc(1000,999))
        def test_sample10 (self):
                self.assertEqual (-1, calc(0,1000))
        def test_sample11 (self):
                self.assertEqual (-1, calc(1000,0))

        #test for overflow and underflow
        def test_sample12 (self):
                self.assertEqual (-1, calc(sys.float_info.min - 1,1))
        def test_sample13 (self):
                self.assertEqual (-1, calc(1,sys.float_info.max + 1))
        def test_sample14 (self):
                self.assertEqual (-1, calc(sys.float_info.min - 1,sys.float_info.max + 1))
        
        #test for non-integer input (入力は正数でないもの)
        def test_sample15 (self):
                self.assertEqual (-1, calc('a',1))
        def test_sample16 (self):
                self.assertEqual (-1, calc(1,'b'))
        def test_sample17 (self):
                self.assertEqual (-1, calc('a','z'))
        def test_sample18 (self):
                self.assertEqual (-1, calc(0.3,1))
        def test_sample19 (self):
                self.assertEqual (-1, calc(4,10.0))
        def test_sample20 (self):
                self.assertEqual (-1, calc(11.4,60.8))

        #test for null input
        def test_sample21 (self):
                self.assertEqual (-1, calc(None,1))
        def test_sample22 (self):
                self.assertEqual (-1, calc(1,None))
        def test_sample23 (self):
                self.assertEqual (-1, calc(None,None))

