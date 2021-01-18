#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (21, calc(7,3))

        def test_sample3 (self):
                self.assertEqual (-1, calc(0,10))

        def test_sample4 (self):
                self.assertEqual (-1, calc(10,0))

        def test_sample5 (self):
                self.assertEqual (-1, calc(-1,999))

        def test_sample6 (self):
                self.assertEqual (-1, calc(222,-2))

        def test_sample7 (self):
                self.assertEqual (-1, calc(-0.1,150))

        def test_sample8 (self):
                self.assertEqual (-1, calc(333,-0.3))

        def test_sample9 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_sample10 (self):
                self.assertEqual (-1, calc(3,0.7))

        def test_sample11 (self):
                self.assertEqual (-1, calc(1.1,150))

        def test_sample12 (self):
                self.assertEqual (-1, calc(44.4,44))

        def test_sample13 (self):
                self.assertEqual (-1, calc(11,15.1))

        def test_sample14 (self):
                self.assertEqual (-1, calc(444,4.4))

        def test_sample15 (self):
                self.assertEqual (-1, calc(100,9999))

        def test_sample16 (self):
                self.assertEqual (-1, calc(3333,777))

        def test_sample17 (self):
                self.assertEqual (-1, calc(100,1500.1))

        def test_sample18 (self):
                self.assertEqual (-1, calc(5555.5,555))

        def test_sample19 (self):
                self.assertEqual (-1, calc('a',666))

        def test_sample20 (self):
                self.assertEqual (-1, calc(777,'b'))