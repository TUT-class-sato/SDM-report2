#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (100, calc(2.5, 40))

        def test_sample3 (self):
                self.assertEqual (-1, calc(400, 90))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.0, 5))
        
        def test_sample5 (self):
                self.assertEqual (-1, calc(80, 2000))

        def test_sample6 (self):
                self.assertEqual (-1, calc(0.01, 999))

        def test_sample7 (self):
                self.assertEqual (-1, calc('a', 700))

        def test_sample8 (self):
                self.assertEqual (-1, calc(80, 't'))
        
        def test_sample9 (self):
                self.assertEqual (-1, calc('A', 'B'))
        
