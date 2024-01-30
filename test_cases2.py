#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (2997, calc(3,999))

        def test_sample2 (self):
                self.assertEqual (2997, calc(999,3))

        def test_sample3 (self):
                self.assertEqual (800, calc(1,800))

        def test_sample4 (self):
                self.assertEqual (800, calc(800,1))

        def test_sample5 (self):
                self.assertEqual (-1, calc(3,1000))

        def test_sample6 (self):
                self.assertEqual (-1, calc(1000,3))

        def test_sample7 (self):
                self.assertEqual (-1, calc(0,10))

        def test_sample8 (self):
                self.assertEqual (-1, calc(10,0))

        def test_sample9 (self):
                self.assertEqual (999, calc('999','1'))

        def test_sample10 (self):
                self.assertEqual (-1, calc(True, True))

