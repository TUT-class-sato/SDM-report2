#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (250000, calc(500,500))

        def test_sample2 (self):
                self.assertEqual (500, calc(1,500))

        def test_sample3 (self):
                self.assertEqual (499500, calc(999,500))

        def test_sample4 (self):
                self.assertEqual (500, calc(500,1))

        def test_sample5 (self):
                self.assertEqual (499500, calc(500,999))

        def test_sample6 (self):
                self.assertEqual (1, calc(1,1))

        def test_sample7 (self):
                self.assertEqual (999, calc(999,1))

        def test_sample8 (self):
                self.assertEqual (999, calc(1,999))

        def test_sample9 (self):
                self.assertEqual (998001, calc(999,999))

        def test_sample10 (self):
                self.assertEqual (-1, calc(-500,500))

        def test_sample11 (self):
                self.assertEqual (-1, calc(2000,500))

        def test_sample12 (self):
                self.assertEqual (-1, calc(500,-500))

        def test_sample13 (self):
                self.assertEqual (-1, calc(500,2000))

        def test_sample14 (self):
                self.assertEqual (-1, calc(0,500))

        def test_sample15 (self):
                self.assertEqual (-1, calc(1000,500))

        def test_sample16 (self):
                self.assertEqual (-1, calc(500,0))

        def test_sample17 (self):
                self.assertEqual (-1, calc(500,1000))

        def test_sample18 (self):
                self.assertEqual (-1, calc(500.5,500))

        def test_sample19 (self):
                self.assertEqual (-1, calc(500,500.5))

        def test_sample20 (self):
                self.assertEqual (-1, calc(500.5,500.5))

        def test_sample21 (self):
                self.assertEqual (1000, calc(('2'),500))

        def test_sample22 (self):
                self.assertEqual (1000, calc('２',500))

        def test_sample23 (self):
                self.assertEqual (1000, calc(500,'2'))

        def test_sample24 (self):
                self.assertEqual (1000, calc(500,'２'))

        def test_sample25 (self):
                self.assertEqual (4, calc('2','2'))

        def test_sample26 (self):
                self.assertEqual (4, calc('2','２'))

        def test_sample27 (self):
                self.assertEqual (4, calc('２','2'))

        def test_sample28 (self):
                self.assertEqual (4, calc('２','２'))

        def test_sample29 (self):
                self.assertEqual (-1, calc('a',500))

        def test_sample30 (self):
                self.assertEqual (-1, calc(500,'a'))

        def test_sample31 (self):
                self.assertEqual (-1, calc('a','b'))

