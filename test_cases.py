#!/usr/bin/python3

import unittest
from calc_mul import calc
import sys

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

	#範囲内で境界値分析
	def test_sample5_1 (self):
		self.assertEqual (999, calc(1, 999))
	def test_sample5_2 (self):
		self.assertEqual (999, calc(999, 1))
	def test_sample5_3 (self):
		self.assertEqual (1, calc(1, 1))
	def test_sample5_4 (self):
		self.assertEqual (998001, calc(999, 999))

	#範囲外で境界値分析(0も含む)
	def test_sample6_1 (self):
		self.assertEqual (-1, calc(1000, 1000))
	def test_sample6_2 (self):
		self.assertEqual (-1, calc(0, 0))
	def test_sample6_3 (self):
		self.assertEqual (-1, calc(1000, 0))
	def test_sample6_4 (self):
		self.assertEqual (-1, calc(0, 1000))

	#両方もしくは片方の値が負の場合
	def test_sample7_1 (self):
		self.assertEqual (-1, calc(-5, -5))
	def test_sample7_2 (self):
		self.assertEqual (-1, calc(-1, 300))
	def test_sample7_3 (self):
		self.assertEqual (-1, calc(450, -9))

	#両方もしくは片方の値が少数の場合
	def test_sample8_1 (self):
		self.assertEqual (-1, calc(0.1, 0.9))
	def test_sample8_2 (self):
		self.assertEqual (-1, calc(999, 999.1))
	def test_sample8_3 (self):
		self.assertEqual (-1, calc(0.9, 1))

	#両方もしくは片方の値が文字列の場合
	def test_sample9_1 (self):
		self.assertEqual (-1, calc("test", "alpha"))
	def test_sample9_2 (self):
		self.assertEqual (-1, calc("test9.1", "test9"))
	def test_sample9_3 (self):
		self.assertEqual (-1, calc("test9", 80))
	def test_sample9_4 (self):
		self.assertEqual (-1, calc(50, "test9.3"))
	def test_sample9_5 (self):
		self.assertEqual (-1, calc("50", "90"))

	#オーバーフロー、アンダーフローする値
	def test_sample10_1 (self):
		self.assertEqual (-1, calc(sys.float_info.max, 2))
	def test_sample10_2 (self):
		self.assertEqual (-1, calc(sys.float_info.min, sys.float_info.min))
