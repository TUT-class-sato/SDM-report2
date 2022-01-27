#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalcAdditional (unittest.TestCase):

        def test01 (self):
                self.assertEqual (1, calc(1,1))

        def test02 (self):
                self.assertEqual (999*999, calc(999,999))

        def test03 (self):
                self.assertEqual (-1, calc('a','b'))

        def test04 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test05 (self):
                self.assertEqual (-1, calc('a',1))

        def test06 (self):
                self.assertEqual (-1, calc(999,'b'))

        def test07 (self):
                self.assertEqual (-1, calc(0,1))

        def test08 (self):
                self.assertEqual (-1, calc(1000,5))

        def test09 (self):
                self.assertEqual(999, calc(1,999))

        def test10 (self):
                self.assertEqual(999, calc(999,1))

        def test11 (self):
                self.assertEqual(-1, calc(-1,5))

        def test12 (self):
                self.assertEqual(-1, calc(999,-1))
