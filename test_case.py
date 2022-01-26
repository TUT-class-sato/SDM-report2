#/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc2 (unittest.TestCase):

	def test1(self):
		self.assertEqual(999,calc(1,999))

	def test2(self):
		self.assertEqual(1,calc(1,1))

	def test3(self):
		self.assertEqual(-1,calc(2,0.9))

	def test4(self):
		self.assertEqual(-1,calc(3,'a'))

	def test5(self):
		self.assertEqual(-1,calc('b',4))

	def test6(self):
		self.assertEqual(-1,calc(-1,7))

	def test7(self):
		self.assertEqual(-1,calc(0.3,8))

	def test8(self):
		self.assertEqual(-1,calc(-0.3,8))

	def test9(self):
		self.assertEqual(-1,calc('a','b'))



