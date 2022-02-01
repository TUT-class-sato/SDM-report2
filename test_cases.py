#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

		def test_sample1 (self):	# 入力A,B共に入力範囲内（下限）：有効同値
				self.assertEqual (1, calc(1,1))

		def test_sample2 (self):	# 入力A,B共に入力範囲内（上限）：有効同値
				self.assertEqual (999*999, calc(999,999))

		def test_sample3 (self):	# 入力A,B共に入力範囲内（A下限・B上限）：有効同値
				self.assertEqual (1*999, calc(1,999))

		def test_sample4 (self):	# 入力A,B共に入力範囲内（A上限・B下限）：有効同値
				self.assertEqual (999*1, calc(999,1))
		
		def test_sample5 (self):	# 入力A,B共に文字列：無効同値
				self.assertEqual (-1, calc('a','b'))

		def test_sample6 (self):	# 入力A,B共に入力範囲外（A下限未満・B上限超過）：無効同値
				self.assertEqual (-1, calc(0,1000))

		def test_sample7 (self):	# 入力A,B共に入力範囲外（A上限超過・B下限未満）：無効同値
				self.assertEqual (-1, calc(1000,0))

		def test_sample8 (self):	# 入力Aが文字列，入力Bは入力範囲内（下限）：無効同値
				self.assertEqual (-1, calc('a',1))

		def test_sample9 (self):	# 入力Aが文字列，入力Bは入力範囲内（上限）：無効同値
				self.assertEqual (-1, calc('a',999))

		def test_sample10 (self):	# 入力Aが文字列，入力Bは入力範囲外（下限未満）：無効同値
				self.assertEqual (-1, calc('a',0))

		def test_sample11 (self):	# 入力Aが文字列，入力Bは入力範囲外（上限超過）：無効同値
				self.assertEqual (-1, calc('a',1000))

		def test_sample12 (self):	# 入力Aは入力範囲外（下限未満），入力Bが文字列：無効同値
				self.assertEqual (-1, calc(0,'b'))

		def test_sample13 (self):	# 入力Aは入力範囲外（上限超過），入力Bが文字列：無効同値
				self.assertEqual (-1, calc(1000,'b'))

		def test_sample14 (self):	# 入力Aはfloat，入力Bはint：無効同値
				self.assertEqual (-1, calc(1.5,2))

		def test_sample15 (self):	# 入力Aはint，入力Bはfloat：無効同値
				self.assertEqual (-1, calc(2,1.5))

		def test_sample16 (self):	# 入力A,B共にfloat：無効同値
				self.assertEqual (-1, calc(1.5,2.0))