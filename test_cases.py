#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        def test_sample1 (self):	# Normal value
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):	# A is out of range
                self.assertEqual (-1, calc(0,10))

        def test_sample3 (self):	# B is out of range
                self.assertEqual (-1, calc(10,1000))

        def test_sample4 (self):	# A is greater than B
                self.assertEqual (21, calc(7,3))

        def test_sample5 (self):	# Input value is a character
                self.assertEqual (-1, calc('a','b'))

        def test_sample6 (self):	# Input value is a letter number
                self.assertEqual (-1, calc('1','2'))

        def test_sample7 (self):	# Input value is a character string
                self.assertEqual (-1, calc("abc","def"))

        def test_sample8 (self):	# Input value is a string number
                self.assertEqual (-1, calc('10','20'))

        def test_sample9 (self):	# Input value is decimal
                self.assertEqual (-1, calc(0.1,999))
