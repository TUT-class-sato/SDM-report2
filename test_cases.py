#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc(unittest.TestCase):
    def test_valid_inputs_boundary_values(self):
        self.assertEqual(1, calc(1, 1))  # min A, min B
        self.assertEqual(999, calc(1, 999))  # min A, max B
        self.assertEqual(250000, calc(500, 500))  # nominal
        self.assertEqual(999, calc(999, 1))  # max A, min B
        self.assertEqual(998001, calc(999, 999))  # max A, max B

    def test_invalid_inputs_boundary_values(self):
        self.assertEqual(-1, calc(0, 1))  # A below the lower boundary
        self.assertEqual(-1, calc(1, 0))  # B below the lower boundary
        self.assertEqual(-1, calc(1000, 1))  # A above the upper boundary
        self.assertEqual(-1, calc(1, 1000))  # B above the upper boundary
        self.assertEqual(-1, calc(0, 0))  # A, B below the lower boundary
        self.assertEqual(-1, calc(1000, 1000))  # A, B above the upper boundary

    def test_invalid_inputs_floating_number(self):
        self.assertEqual(-1, calc(5.5, 500))  # A is floating number
        self.assertEqual(-1, calc(500, 5.5))  # B is floating number
        self.assertEqual(-1, calc(5.5, 5.5))  # A, B is floating number

    def test_invalid_inputs_string_values(self):
        self.assertEqual(-1, calc("xyz", 500))  # A is a string
        self.assertEqual(-1, calc(500, "xyz"))  # B is a string
        self.assertEqual(-1, calc("xyz", "xyz"))  # A, B is a string

        self.assertEqual(-1, calc("z28", 500))  # A is a string and number
        self.assertEqual(-1, calc(500, "z28"))  # B is a string and number
        self.assertEqual(-1, calc("z28", "z28"))  # A, B is a string and number
