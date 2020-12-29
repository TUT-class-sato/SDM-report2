#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample01 (self):
                self.assertEqual (-1, calc(0.1,0.1))

        def test_sample02 (self):
                self.assertEqual (-1, calc('A',0.1))

        def test_sample03 (self):
                self.assertEqual (-1, calc(0,0.1))

        def test_sample04 (self):
                self.assertEqual (-1, calc(500,0.1))

        def test_sample05 (self):
                self.assertEqual (-1, calc(1000,0.1))

        def test_sample06 (self):
                self.assertEqual (-1, calc(0.1,'B'))

        def test_sample07 (self):
                self.assertEqual (-1, calc('A','B'))

        def test_sample08 (self):
                self.assertEqual (-1, calc(0,'B'))

        def test_sample09 (self):
                self.assertEqual (-1, calc(500,'B'))

        def test_sample10 (self):
                self.assertEqual (-1, calc(1000,'B'))

        def test_sample11 (self):
                self.assertEqual (-1, calc(0.1,0))

        def test_sample12 (self):
                self.assertEqual (-1, calc('A',0))

        def test_sample13 (self):
                self.assertEqual (-1, calc(0,0))

        def test_sample14 (self):
                self.assertEqual (-1, calc(500,0))

        def test_sample15 (self):
                self.assertEqual (-1, calc(1000,0))

        def test_sample16 (self):
                self.assertEqual (-1, calc(0.1,500))

        def test_sample17 (self):
                self.assertEqual (-1, calc('A',500))

        def test_sample18 (self):
                self.assertEqual (-1, calc(0,500))

        def test_sample19 (self):
                self.assertEqual (250000, calc(500,500))

        def test_sample20 (self):
                self.assertEqual (1000, calc(20,50))

        def test_sample21 (self):
                self.assertEqual (1000, calc(50,20))

        def test_sample22 (self):
                self.assertEqual (-1, calc(1000,500))

        def test_sample23 (self):
                self.assertEqual (-1, calc(0.1,1000))

        def test_sample24 (self):
                self.assertEqual (-1, calc('A',1000))

        def test_sample25 (self):
                self.assertEqual (-1, calc(0,1000))

        def test_sample26 (self):
                self.assertEqual (-1, calc(500,1000))

        def test_sample27 (self):
                self.assertEqual (-1, calc(1000,1000))
