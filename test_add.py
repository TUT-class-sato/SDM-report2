#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestAdd (unittest.TestCase):

    def test1(self):
        self.assertEqual(-1, calc(-3, 7))

    def test2(self):
        self.assertEqual(21, calc(7, 3))

    def test3(self):
        self.assertEqual(-1, calc(-1, -5))

    def test4(self):
        self.assertEqual(999, calc(1, 999))

    def test5(self):
        self.assertEqual(-1, calc(2, 1000))

    def test6(self):
        self.assertEqual(-1, calc('p', 2))
