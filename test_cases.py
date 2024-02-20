#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc(unittest.TestCase):

    def test_positive(self):
        """Test multiplication of two positive integers"""
        self.assertEqual(21, calc(3, 7))

    def test_zero1(self):
        """Test multiplication of zero and a positive integer"""
        self.assertEqual(-1, calc(0, 1000))

    def test_zero2(self):
        """Test multiplication of a positive integer and zero"""
        self.assertEqual(-1, calc(1000, 0))

    def test_zero3(self):
        """Test multiplication with zero"""
        self.assertEqual(-1, calc(0, 15))

    def test_zero4(self):
        """Test multiplication with zero"""
        self.assertEqual(-1, calc(15, 0))

    def test_boundary1(self):
        """Test multiplication of two equal positive integers"""
        self.assertEqual(-1, calc(1000, 1000))

    def test_boundary2(self):
        """Test multiplication of 1 and a positive integer"""
        self.assertEqual(999, calc(1, 999))

    def test_boundary3(self):
        """Test multiplication of a positive integer and 1"""
        self.assertEqual(999, calc(999, 1))

    def test_boundary4(self):
        """Test multiplication of two equal positive integers (max)"""
        self.assertEqual(998001, calc(999, 999))

    def test_outside1(self):
        """Test multiplication with negative values"""
        self.assertEqual(-1, calc(-1, 1100))

    def test_outside2(self):
        """Test multiplication with negative values"""
        self.assertEqual(-1, calc(-1, 900))

    def test_outside3(self):
        """Test multiplication with negative values"""
        self.assertEqual(-1, calc(900, -1))

    def test_notnum1(self):
        """Test multiplication with non-numeric inputs"""
        self.assertEqual(-1, calc("a", "b"))

    def test_notnum2(self):
        """Test multiplication with non-numeric input (one numeric)"""
        self.assertEqual(-1, calc("a", 10))

    def test_notnum3(self):
        """Test multiplication with non-numeric input (one numeric)"""
        self.assertEqual(-1, calc(10, "a"))

    def test_decimal1(self):
        """Test multiplication with decimal input"""
        self.assertEqual(-1, calc(0.1, 999))

    def test_decimal2(self):
        """Test multiplication with decimal input"""
        self.assertEqual(-1, calc(999, 1.1))