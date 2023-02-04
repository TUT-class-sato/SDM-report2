#!/usr/bin/python3

import unittest
from calc_mul import calc
import math

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))
                self.assertEqual (250000, calc(500,500))
                self.assertEqual (988032, calc(996, 992))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))
                self.assertEqual (-1, calc(150,1000))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))
                self.assertEqual (-1, calc(10, "Hello"))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
                self.assertEqual (-1, calc(math.pi, math.e))

        def test_sample5 (self):
                self.assertEqual (-1, calc(0, 1000))
                self.assertEqual (-1, calc(-500, 1500))
                
        def test_sample6 (self):
                self.assertEqual (-1, calc(None, None))
                self.assertEqual (-1, calc('', [])) 

