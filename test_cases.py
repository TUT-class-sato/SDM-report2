#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample11 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample12 (self):
                self.assertEqual (21, calc(7,3))

        def test_sample21 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample22 (self):
                self.assertEqual (-1, calc(0,'s'))
                
        def test_sample23(self):
                self.assertEqual(-1,calc(3.5,5.0))
        
        def test_sample31 (self):
                self.assertEqual (-1, calc(999,1000))

        def test_sample32 (self):
                self.assertEqual (-1, calc(0.1,1))

        def test_sample33 (self):
                self.assertEqual (-1, calc('03','7'))

        def test_sample34 (self):
                self.assertEqual (21, calc(1+2,3+4))

