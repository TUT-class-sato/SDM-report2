#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc (unittest.TestCase):
    def setUp(self):#fixture
        self.valid_int = [1, 2, 998, 999,'998']
        self.invalid_int = [-1, 0, 1000, 1001]
        self.invalid_value = ['a', 'abc','12a','a13', 24.7, 30.0,'']

    def test_both_valid(self):
        for a in self.valid_int:
            for b in self.valid_int:
                with self.subTest(a=a,b=b):
                    self.assertEqual(int(a)*int(b), calc(a, b))
                    self.assertEqual(int(a)*int(b), calc(b, a))

    def test_one_invalid_int(self):
        for a in self.valid_int:
            for b in self.invalid_int:
                with self.subTest(a=a, b=b):
                    self.assertEqual(-1, calc(a, b))
                    self.assertEqual(-1, calc(b, a))

    def test_one_invalid_value(self):
        for a in self.valid_int:
            for b in self.invalid_value:
                with self.subTest(a=a, b=b):
                    self.assertEqual(-1, calc(a, b))
                    self.assertEqual(-1, calc(b, a))

    def test_both_invalid(self):
        target=self.invalid_int
        target.extend(self.invalid_value)
        for a in target:
            for b in target:
                with self.subTest(a=a, b=b):
                    self.assertEqual(-1, calc(a, b))
                    self.assertEqual(-1, calc(b, a))
