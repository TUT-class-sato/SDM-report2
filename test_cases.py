#!/usr/bin/python3

import unittest
import sys
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_case1 (self):
                self.assertEqual (10000, calc(100,100))

        def test_case2 (self):
                self.assertEqual (1, calc(1,1))

        def test_case3 (self):
                self.assertEqual (999, calc(999,1))

        def test_case4 (self):
                self.assertEqual (999, calc(1,999))

        def test_case5 (self):
                self.assertEqual (998001, calc(999,999))

        def test_case6 (self):
                self.assertEqual (-1, calc(1000,999))

        def test_case7 (self):
                self.assertEqual (-1, calc(999,1000))

        def test_case8 (self):
                self.assertEqual (-1, calc(1000,1000))

        def test_case9 (self):
                self.assertEqual (-1, calc(0,1))

        def test_case10 (self):
                self.assertEqual (-1, calc(1,0))

        def test_case11 (self):
                self.assertEqual (-1, calc(0,0))

        def test_case12 (self):
                self.assertEqual (-1, calc("abc",100))

        def test_case13 (self):
                self.assertEqual (-1, calc(100,"abc"))

        def test_case14 (self):
                self.assertEqual (-1, calc("abc","abc"))

        def test_case15 (self):
                self.assertEqual (-1, calc("",100))

        def test_case16 (self):
                self.assertEqual (-1, calc(100,""))

        def test_case17 (self):
                self.assertEqual (-1, calc("",""))

        def test_case18 (self):
                self.assertEqual (-1, calc(1.23,100))

        def test_case19 (self):
                self.assertEqual (-1, calc(100,1.23))

        def test_case20 (self):
                self.assertEqual (-1, calc(1.23,1.23))

def main():
    unittest.main()


if __name__ == '__main__':
    main()