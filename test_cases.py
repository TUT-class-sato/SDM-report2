#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #def test_sample1 (self):
        #        self.assertEqual (21, calc(3,7))

        #def test_sample2 (self):
        #        self.assertEqual (-1, calc(0,150))

        #def test_sample3 (self):
        #        self.assertEqual (-1, calc('a','b'))

        #def test_sample4 (self):
        #        self.assertEqual (-1, calc(0.1,999))

        def test_1 (self):
                self.assertEqual (-1, calc(0,1))
        def test_2 (self):
                self.assertEqual (-1, calc(1000,999))
        def test_3 (self):
                self.assertEqual (-1, calc(1,0))
        def test_4 (self):
                self.assertEqual (-1, calc(999,1000))
        def test_5 (self):
                self.assertEqual (-1, calc(0,0))
        def test_6 (self):
                self.assertEqual (-1, calc(1000,1000))
        def test_7 (self):
                self.assertEqual (-1, calc(0.999,1))
        def test_8 (self):
                self.assertEqual (-1, calc(1.001,2))
        def test_9 (self):
                self.assertEqual (-1, calc(999.001,999))
        def test_10 (self):
                self.assertEqual (-1, calc(1,0.999))
        def test_11 (self):
                self.assertEqual (-1, calc(2,1.001))
        def test_12 (self):
                self.assertEqual (-1, calc(999,999.001))
        def test_13 (self):
                self.assertEqual (-1, calc(0.999,0.999))
        def test_14 (self):
                self.assertEqual (-1, calc(999.001,999.001))
        def test_15 (self):
                self.assertEqual (-1, calc(100.001,100.001))
        def test_16 (self):
                self.assertEqual (-1, calc("/",200))
        def test_17 (self):
                self.assertEqual (-1, calc(200,"/"))
        def test_18 (self):
                self.assertEqual (-1, calc("/","/"))
        def test_19 (self):
                self.assertEqual (1*2, calc(1,2))
        def test_20 (self):
                self.assertEqual (500*500, calc(500,500))
        def test_21 (self):
                self.assertEqual (999*998, calc(999,998))



