#!/usr/bin/python3

import unittest
from calc_mul import calc
import math

# Run with testrunner so needs to be in file test_


class TestCalc(unittest.TestCase):
    def test_acceptableNums(self):
        self.assertEqual(21, calc(3, 7))
        self.assertEqual(250000, calc(500, 500))
        self.assertEqual(988032, calc(996, 992))

    def test_lowEdge(self):
        self.assertEqual(-1, calc(0, 150))
        self.assertEqual(150, calc(1, 150))

    def test_highEdge(self):
        self.assertEqual(149850, calc(150, 999))
        self.assertEqual(-1, calc(150, 1000))

    def test_underflow(self):
        self.assertEqual(-1, calc(-100, -200))

    def test_overflow(self):
        self.assertEqual(-1, calc(5000, 10000))

    def test_nonNums(self):
        self.assertEqual(-1, calc("a", "b"))
        self.assertEqual(-1, calc(10, "Hello"))
        self.assertEqual(-1, calc("", []))

    def test_decimalNums(self):
        self.assertEqual(-1, calc(0.1, 999))
        self.assertEqual(-1, calc(math.pi, math.e))

    def test_none(self):
        self.assertEqual(-1, calc(None, None))
