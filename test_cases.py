#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_sample5 (self):
                self.assertEqual (-1, calc(999, 0.1))

        def test_sample6 (self):
                self.assertEqual (-1, calc(150, 0))

        def test_sample7 (self):
                self.assertEqual (6, calc(1, 6))

        def test_sample8 (self):
                self.assertEqual (6, calc(6, 1))

        def test_sample9 (self):
                self.assertEqual (1998, calc(999, 2))

        def test_sample10 (self):
                self.assertEqual (1998, calc(2, 999))

        def test_sample11 (self):
                self.assertEqual (-1, calc(1000, 78))
        
        def test_sample12 (self):
                self.assertEqual (-1, calc(78, 1000))

        def test_sample13 (self):
                self.assertEqual (-1, calc('hoge', 99))
        
        def test_sample14 (self):
                self.assertEqual (-1, calc(99, 'hoge'))

        def test_sample15 (self):
                self.assertEqual (3500, calc(50, 70))

        def test_sample16 (self):
                self.assertEqual (-1, calc(-189, 78))

        def test_sample17 (self):
                self.assertEqual (-1, calc(189, -78))

        def test_sample18 (self):
                self.assertEqual (-1, calc(1000, 0))

        def test_sample19 (self):
                self.assertEqual (-1, calc(0, 1000))

        def test_sample20 (self):
                self.assertEqual (-1, calc(-78.89, 78))

        def test_sample21 (self):
                self.assertEqual (-1, calc(78, -78.89))