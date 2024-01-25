#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_a_zero (self):
                self.assertEqual (-1, calc(0,5))
        def test_b_zero (self):
                self.assertEqual (-1, calc(5,0))
        def test_a_one (self):
                self.assertEqual (5, calc(1,5))
        def test_b_one (self):
                self.assertEqual (5, calc(5,1))
        def test_a_thousand (self):
                self.assertEqual (-1, calc(1000,5))
        def test_b_thousand (self):
                self.assertEqual (-1, calc(5,1000))
        def test_a_under_thousand (self):
                self.assertEqual (4995, calc(999,5))
        def test_b_under_thousand (self):
                self.assertEqual (4995, calc(5,999))

        def test_a_string (self):
                self.assertEqual (-1, calc('a',5))
        def test_b_string (self):
                self.assertEqual (-1, calc(5,'b'))
        def test_a_float (self):
                self.assertEqual (-1, calc(0.1,5))
        def test_b_float (self):
                self.assertEqual (-1, calc(5,0.1))