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

        def test_sameValue (self):
                self.assertEqual (998001, calc(999,999))

        def test_AisOvertheRange (self):
                self.assertEqual (-1, calc(1000,1))

        def test_BisOvertheRange (self):
                self.assertEqual (-1, calc(1,1000))

        def test_BothareOvertheRange (self):
                self.assertEqual (-1, calc(1000,1000))

        def test_AisBelowTheRange (self):
        		self.assertEqual (-1, calc(0, 1))

        def test_BisBelowTheRange (self):
        		self.assertEqual (-1, calc(1, 0))

        def test_BothareBelowTheRange (self):
        		self.assertEqual (-1, calc(0, 0))

        def test_AisFraction (self):
        		self.assertEqual (-1, calc(0.1, 1))

        def test_BisFraction (self):
        		self.assertEqual (-1, calc(1, 0.1))

        def test_BothareFraction (self):
        		self.assertEqual (-1, calc(0.1, 0.1))

        def test_AisNotNumber (self):
        		self.assertEqual (-1, calc('a', 1))

        def test_BisNotNumber (self):
        		self.assertEqual (-1, calc(1, 'b'))

        def test_BothareNotNumber (self):
        		self.assertEqual (-1, calc('a', 'b'))

