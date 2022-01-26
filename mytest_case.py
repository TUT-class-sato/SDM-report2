#/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc (unittest.TestCase):

	def test_sample1(self):
		self.assertEqual(20,calc(4,5))

	def test_sample2(self):
		self.assertEqual(-1,calc(10,0.5))

	def test_sample3(self):
		self.assertEqual(-1,calc(20,'a'))

	def test_sample4(self):
		self.assertEqual(-1,calc('b',6))

	def test_sample5(self):
		self.assertEqual(-1,calc(-10,7))

	def test_sample6(self):
		self.assertEqual(-1,calc(0.3,8))

	def test_sample7(self):
		self.assertEqual(30,calc(6,5))


