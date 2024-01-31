#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_equ1 (self):
                self.assertEqual (100, calc(10,10))
        def test_equ2 (self):
                self.assertEqual (-1, calc(-10,-10))
        def test_equ3 (self):
                self.assertEqual (-1, calc(2000,2000))
        def test_equ4 (self):
                self.assertEqual (-1, calc(10.5,10.5))
        def test_equ5 (self):
                self.assertEqual (-1, calc("World","World"))
        def test_equ6 (self):
                self.assertEqual (-1, calc([1,2],[1,2]))
        def test_equ7 (self):
                self.assertEqual (100, calc("10","10"))
        def test_equ8 (self):
                self.assertEqual (-1, calc("10a","10a"))

        def test_bou1 (self):
                self.assertEqual (-1, calc(0,0))
        def test_bou2 (self):
                self.assertEqual (1, calc(1,1))
        def test_bou3 (self):
                self.assertEqual (998001, calc(999,999))
        def test_bou4 (self):
                self.assertEqual (-1, calc(1000,1000))

        def test_two1 (self):
                self.assertEqual (100, calc(5,20))
        def test_two2 (self):
                self.assertEqual (100, calc(10,10))
        def test_two3 (self):
                self.assertEqual (100, calc(20,5))
        def test_two4 (self):
                self.assertEqual (-1, calc(10,-10))
        def test_two5 (self):
                self.assertEqual (-1, calc(-10,10))
        def test_two6 (self):
                self.assertEqual (-1, calc(10,"World"))
        def test_two7 (self):
                self.assertEqual (-1, calc(10,10.5))
