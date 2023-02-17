#!/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc(unittest.TestCase):
        def test1(self):
                self.assertEqual(1, calc(1,1))

        def test2(self):
                self.assertEqual(998001, calc(999, 999))

        def test3(self):
                self.assertEqual(999, calc(1, 999))

        def test4(self):
                self.assertEqual(999, calc(999, 1))

        def test5(self):
                self.assertEqual(-1, calc(0, 1))

        def test6(self):
                self.assertEqual(-1, calc(1, 0))

        def test7(self):
                self.assertEqual(-1, calc(1000, 1))

        def test8(self):
                self.assertEqual(-1, calc(1, 1000))

        def test9(self):
                self.assertEqual(-1, calc('abc', 1))

        def test10(self):
                self.assertEqual(-1, calc(1, 'def'))

        def test11(self):
                self.assertEqual(-1, calc(0.5, 1))

        def test12(self):
                self.assertEqual(-1, calc(1, 0.5))

        def test13(self):
                self.assertEqual(-1, calc(None, 1))

        def test14(self):
                self.assertEqual(-1, calc(1, None))

