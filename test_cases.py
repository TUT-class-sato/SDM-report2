#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        def test_sample01(self):
                self.assertEqual(-1, calc(0, 7))

        def test_sample02(self):
                self.assertEqual(150, calc(1, 150))

        def test_sample03(self):
                self.assertEqual(99900, calc(999, 100))

        def test_sample04(self):
                self.assertEqual(-1, calc(1000, 8))

        def test_sample05(self):
                self.assertEqual(-1, calc(0.1, 1))

        def test_sample06(self):
                self.assertEqual(-1, calc("100", 3))

        def test_sample07(self):
                self.assertEqual(800, calc(100, 8))

        def test_sample08(self):
                self.assertEqual(-1, calc(9, 0))

        def test_sample09(self):
                self.assertEqual(15, calc(15, 1))

        def test_sample10(self):
                self.assertEqual(9990, calc(10, 999))

        def test_sample11(self):
                self.assertEqual(-1, calc(6, 1000))

        def test_sample12(self):
                self.assertEqual(-1, calc(120, 0.1))

        def test_sample13(self):
                self.assertEqual(-1, calc(2, "100"))

        def test_sample14(self):
                self.assertEqual(700, calc(7, 100))
