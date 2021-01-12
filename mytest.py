#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

            def test1 (self):
                self.assertEqual (21, calc(3,7))

            def test2 (self):
                self.assertEqual (-1, calc(0,150))

            def test3 (self):
                self.assertEqual (-1, calc('a','b'))

            def test4 (self):
                self.assertEqual (99.9, calc(0.1,999)) 
