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

	def test_valid_integer_range_inputA (self):
		self.assertEqual (300, calc(1, 300))
		self.assertEqual (399600, calc(999, 400))
	
	def test_valid_integer_range_inputB (self):
		self.assertEqual (250, calc(250, 1))
		self.assertEqual (665334,calc(666, 999))

	def test_invalid_integer_range_inputA (self):
		self.assertEqual (-1, calc(0, 333))
		self.assertEqual (-1, calc(1000, 500))

	def test_invalid_integer_range_inputB (self):
		self.assertEqual (-1, calc(400, 0))
		self.assertEqual (-1, calc(800, 1000))

	def test_non_integer_inputA (self):
		self.assertEqual (-1, calc("a", 500))
		self.assertEqual (-1, calc(1.5, 500))

	def test_non_integer_inputB (self):
		self.assertEqual (-1, calc(500, "a"))
		self.assertEqual (-1, calc(500, 1.5))
