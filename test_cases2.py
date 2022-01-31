#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc2 (unittest.TestCase):

        def test_sample01 (self):
                self.assertEqual (999, calc(1,999))

        def test_sample02 (self):
                self.assertEqual (-1, calc(1.1,999))

        def test_sample03 (self):
                self.assertEqual (-1, calc(1,998.9))

        def test_sample04 (self):
                self.assertEqual (-1, calc(1.1,998.9))
        
	def test_sample05 (self):
                self.assertEqual (-1, calc(0,999))

        def test_sample06 (self):
                self.assertEqual (-1, calc(1,1000))
        
        def test_sample07 (self):
                self.assertEqual (-1, calc(0,1000))

        def test_sample08 (self):
                self.assertEqual (999, calc(999,1))

	def test_sample09 (self):
                self.assertEqual (-1, calc('a','b'))

	def test_sample10 (self):
                self.assertEqual (-1, calc(1,'b'))
	
	def test_sample11 (self):
                self.assertEqual (-1, calc('a',999))
