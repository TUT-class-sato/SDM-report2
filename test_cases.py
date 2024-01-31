#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_case01 (self):
                self.assertEqual (-1, calc(1000,10000))

        def test_case02 (self):
                self.assertEqual (-1, calc(-100,100))

        def test_case03 (self):
                self.assertEqual (-1, calc(100,-100))

        def test_case04 (self):
                self.assertEqual (21, calc(3,7))

        def test_case05 (self):
                self.assertEqual (-1, calc("10a",150))

        def test_case06 (self):
                self.assertEqual (calc(7,3), calc(3,7))

        def test_case07 (self):
                self.assertEqual (-1, calc(0,100))

        def test_case08 (self):
                self.assertEqual (100, calc(1,100))

        def test_case09 (self):
                self.assertEqual (99900, calc(100,999))

        def test_case10 (self):
                self.assertEqual (-1, calc(100,1000))

        def test_case11 (self):
                self.assertEqual (998001, calc(999,999))