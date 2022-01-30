#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc (unittest.TestCase):

    def test_sample1(self):
        self.assertEqual(21, calc(3, 7))

    def test_sample2(self):
        self.assertEqual(-1, calc(0, 150))

    def test_sample3(self):
        self.assertEqual(-1, calc('a', 'b'))

    def test_sample4(self):
        self.assertEqual(-1, calc(0.1, 999))

    def test_sample5(self):
        self.assertEqual(-1, calc(-5, 100))

    def test_sample6(self):
        self.assertEqual(-1, calc(20, -10))

    def test_sample7(self):
        self.assertEqual(-1, calc(-50, -20))

    def test_sample8(self):
        self.assertEqual(-1, calc(1000, 300))

    def test_sample9(self):
        self.assertEqual(-1, calc(400, 1000))

    def test_sample10(self):
        self.assertEqual(-1, calc(400, 1000))

    def test_sample11(self):
        self.assertEqual(-1, calc('a', 30))

    def test_sample12(self):
        self.assertEqual(-1, calc(10, 'bc'))

    def test_sample13(self):
        self.assertEqual(-1, calc(10, '25a'))

    def test_sample14(self):
        self.assertEqual(-1, calc('23c', 50))

    def test_sample15(self):
        self.assertEqual(-1, calc('123g', '30l'))

    def test_sample16(self):
        self.assertEqual(21, calc(7, 3))

    def test_sample17(self):
        self.assertEqual(-1, calc('k12g', '3g0'))

    def test_sample18(self):
        self.assertEqual(-1, calc(20, 'kg30'))
