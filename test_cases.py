99#!/usr/bin/python3

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
                self.assertEqual (-1, calc(1.5,999))



        def test_sample5 (self):
                self.assertEqual (999, calc(1,999))

        def test_sample6 (self):
                self.assertEqual (999, calc(999,1))

        def test_sample7 (self):
                self.assertEqual (15000, calc(30,500))

        def test_sample8 (self):
                self.assertEqual (15000, calc(500,30))

        def test_sample9 (self):
                self.assertEqual (900, calc(30,30))

        def test_sample10 (self):
                self.assertEqual (1, calc(1,1))

        def test_sample11 (self):
                self.assertEqual (998001, calc(999,999))

        def test_sample12 (self):
                self.assertEqual (-1, calc(0,1000))

        def test_sample13 (self):
                self.assertEqual (-1, calc(1000,0))

        def test_sample14 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample15 (self):
                self.assertEqual (-1, calc(1,'a'))

        def test_sample16 (self):
                self.assertEqual (-1, calc('a',1))

        def test_sample17 (self):
                self.assertEqual (-1, calc(3.5,100))

        def test_sample18 (self):
                self.assertEqual (-1, calc(100,3.5))

        def test_sample19 (self):
                self.assertEqual (-1, calc(0,999))

        def test_sample20 (self):
                self.assertEqual (-1, calc(999,0))

        def test_sample21 (self):
                self.assertEqual (-1, calc(-10,300))

        def test_sample22 (self):
                self.assertEqual (-1, calc(300,-10))

        def test_sample23 (self):
                self.assertEqual (-1, calc(0,1))

        def test_sample24 (self):
                self.assertEqual (-1, calc(1,0))

        def test_sample25 (self):
                self.assertEqual (-1, calc(999,1000))

        def test_sample26 (self):
                self.assertEqual (-1, calc(1000,999))
