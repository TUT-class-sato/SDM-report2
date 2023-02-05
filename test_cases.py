#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #境界付近の有効同値のテスト
        def test_sample01 (self):
                self.assertEqual (999, calc(1,999))
        
        def test_sample02 (self):
                self.assertEqual (999, calc(999,1))
        #以下無効同値のテスト
        def test_sample03 (self):
                self.assertEqual (-1, calc(0,1000))

        def test_sample04 (self):
                self.assertEqual (-1, calc(1000,0))
        
        def test_sample05 (self):
                self.assertEqual (-1, calc(0.9,999))
        
        def test_sample06 (self):
                self.assertEqual (-1, calc(1.1,999))
        
        def test_sample07 (self):
                self.assertEqual (-1, calc(1.1,1.1))
        
        def test_sample08 (self):
                self.assertEqual (-1, calc(0.1,0.1))
        
        def test_sample09 (self):
                self.assertEqual (-1, calc('a',999))
        
        def test_sample10 (self):
                self.assertEqual (-1, calc('a',1000))
        
        def test_sample11 (self):
                self.assertEqual (-1, calc('a',0.1))

        def test_sample12 (self):
                self.assertEqual (-1, calc('a',1.1))
        
        def test_sample13 (self):
                self.assertEqual (-1, calc('a','b'))


