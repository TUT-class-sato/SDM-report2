#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        #test with normal case
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (225, calc(15,15))

        def test_sample3 (self):
                self.assertEqual (129402, calc(237,546))

        def test_sample4 (self):
                self.assertEqual (322625, calc(725,445))

        #test with edge and just outside
        def test_sample5 (self):
                self.assertEqual (999, calc(1,999))

        def test_sample6 (self):
                self.assertEqual (999, calc(999,1))

        def test_sample7 (self):
                self.assertEqual (-1, calc(0,999))

        def test_sample8 (self):
                self.assertEqual (-1, calc(1,1000))

        #test with values other than int type
        def test_sample9 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample10 (self):
                self.assertEqual (-1, calc(0.4,150))

        def test_sample11 (self):
                self.assertEqual (-1, calc(150,7.4))

        def test_sample12 (self):
                self.assertEqual (-1, calc(None,999))

        #overflow and underflow
        def test_sample13 (self):
                self.assertEqual (-1, calc(-2147483648,2))

        def test_sample14 (self):
                self.assertEqual (-1, calc(2147483647,2))

        def test_sample15 (self):
                self.assertEqual (-1, calc(2147483648,1))

        def test_sample16 (self):
                self.assertEqual (-1, calc(-2147483649,1))