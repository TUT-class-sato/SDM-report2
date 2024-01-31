#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (7, calc(1,7))

        def test_sample2 (self):
                self.assertEqual (10, calc(10,1))

        def test_sample3 (self):
                self.assertEqual (1998, calc(999,2))

        def test_sample4 (self):
                self.assertEqual (2997, calc(3,999))

        def test_sample5 (self):
                self.assertEqual (-1, calc(10.1,10))
        
        def test_sample6 (self):
                self.assertEqual (-1, calc(10,10.1))

        def test_sample7 (self):
                self.assertEqual (-1, calc(0,10))

        def test_sample8 (self):
                self.assertEqual (-1, calc(10,1000))

        def test_sample9 (self):
                self.assertEqual (-1, calc('abc',10))

        def test_sample10 (self):
                self.assertEqual (-1, calc(10,'xyz'))

