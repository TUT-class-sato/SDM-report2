#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc (unittest.TestCase):
    def setUp(self):  # fixture
        self.valid_int = [1, 2, 998, 999]
        self.invalid_int = [-1, 0, 1000, 1001]
        self.invalid_str = ['a', 'abc']
        self.invalid_str_with_value = ['2a', '2e5', 'o23r', 'eg2']
        self.invalid_float = [24.7, 30.0]
        self.invalid_type = ['', ' ', None, [1], ['a', 'e']]
        self.valid_str_int = ['1', '2', '998', '999']
        self.invalid_str_int = ['-1', '0', '1000', '1001']
        self.invalids = self.invalid_int
        self.invalids.extend(self.invalid_str)
        self.invalids.extend(self.invalid_str_with_value)
        self.invalids.extend(self.invalid_float)
        self.invalids.extend(self.invalid_type)
        self.invalids.extend(self.invalid_str_int)
        self.valids = self.valid_int
        self.valids.extend(self.valid_str_int)

    def test_both_valid_value(self):
        for a in self.valids:
            for b in self.valids:
                except_value = int(a)*int(b)
                with self.subTest(a=a, b=b):
                    self.assertEqual(except_value, calc(a, b))
                    self.assertEqual(except_value, calc(b, a))

    def test_one_valid_value(self):
        for a in self.valids:
            for b in self.invalids:
                except_value = -1
                with self.subTest(a=a, b=b):
                    self.assertEqual(except_value, calc(a, b))
                    self.assertEqual(except_value, calc(b, a))

    def test_both_invalid(self):

        for a in self.invalids:
            for b in self.invalids:
                except_value = -1
                with self.subTest(a=a, b=b):
                    self.assertEqual(except_value, calc(a, b))
                    self.assertEqual(except_value, calc(b, a))
