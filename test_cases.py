#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

#        def test_sample1 (self):
#                self.assertEqual (21, calc(3,7))

#        def test_sample2 (self):
#                self.assertEqual (-1, calc(0,150))

#        def test_sample3 (self):
#               self.assertEqual (-1, calc('a','b'))

#        def test_sample4 (self):
#                self.assertEqual (-1, calc(0.1,999))

        def test_sample01 (self):
                self.assertEqual (6, calc(2,3))

        def test_sample02 (self):
                self.assertEqual (-1, calc(2,2000))

        def test_sample03 (self):
                self.assertEqual (-1, calc(-5,7))

        def test_sample04 (self):
                self.assertEqual (-1, calc(-5,2000))

        def test_sample05 (self):
                self.assertEqual (-1, calc(77,'a'))

        def test_sample06 (self):
                self.assertEqual (-1, calc(4,4.8))

        def test_sample07 (self):
                self.assertEqual (-1, calc(4,0.8))

        def test_sample08 (self):
                self.assertEqual (-1, calc(2.8,3.8))

        def test_sample09 (self):
                self.assertEqual (6, calc(3,2))

        def test_sample10 (self):
                self.assertEqual (-1, calc(2000,2))

        def test_sample11 (self):
                self.assertEqual (-1, calc(7,-5))

        def test_sample12 (self):
                self.assertEqual (-1, calc(2000,-5))

        def test_sample13 (self):
                self.assertEqual (-1, calc('a',77))

        def test_sample14 (self):
                self.assertEqual (-1, calc(4.8,4))

        def test_sample15 (self):
                self.assertEqual (-1, calc(0.8,4))

        def test_sample16 (self):
                self.assertEqual (-1, calc(3.8,2.8))

        def test_sample17 (self):
                self.assertEqual (25, calc(5,5))

        def test_sample18 (self):
                self.assertEqual (-1, calc('a','c'))

        def test_sample19 (self):
                self.assertEqual (999, calc(1,999))

        def test_sample20 (self):
                self.assertEqual (-1, calc(1,1000))

        def test_sample21 (self):
                self.assertEqual (-1, calc(0,999))

        def test_sample22 (self):
                self.assertEqual (-1, calc(0,1000))

        def test_sample23 (self):
                self.assertEqual (-1, calc(0,1))

        def test_sample24 (self):
                self.assertEqual (-1, calc(999,1000))

        def test_sample25 (self):
                self.assertEqual (999, calc(999,1))

        def test_sample26 (self):
                self.assertEqual (-1, calc(1000,1))

        def test_sample27 (self):
                self.assertEqual (-1, calc(999,0))

        def test_sample28 (self):
                self.assertEqual (-1, calc(1000,0))

        def test_sample29 (self):
                self.assertEqual (-1, calc(1,0))

        def test_sample30 (self):
                self.assertEqual (-1, calc(1000,999))


