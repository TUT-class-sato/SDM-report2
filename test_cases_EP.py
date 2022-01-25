#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (1000, calc(10,100))

        def test_sample2 (self):
                self.assertEqual (1000, calc(100,10))

        def test_sample3 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample4 (self):
                self.assertEqual (-1, calc(50,1000))

        def test_sample5 (self):
                self.assertEqual (-1, calc(-1,1000))

        def test_sample6 (self):
                self.assertEqual (1000, calc(10.0,100.0))

        def test_sample7 (self):
                self.assertEqual (-1, calc(0.1,100))

        def test_sample8 (self):
                self.assertEqual (-1, calc(10,999.9))

        def test_sample9 (self):
                self.assertEqual (-1, calc(0.1,999.9))

        def test_sample10 (self):
                self.assertEqual (-1, calc(1.5, 100))

        def test_sample11 (self):
                self.assertEqual (-1, calc(10,500.5))

        def test_sample12 (self):
                self.assertEqual (-1, calc(1.5,500.5))

        def test_sample13 (self):
                self.assertEqual (1000, calc('10','100'))

        def test_sample14 (self):
                self.assertEqual (-1, calc('a',100))

        def test_sample15 (self):
                self.assertEqual (-1, calc(1,'b'))

        def test_sample16 (self):
                self.assertEqual (-1, calc('.',''))

        def test_sample17 (self):
                self.assertEqual (-1, calc('1..','1..'))

        def test_sample18 (self):
                self.assertEqual (-1, calc('a1','b2c'))

        def test_sample19 (self):
                self.assertEqual (-1, calc('1a','2b3'))