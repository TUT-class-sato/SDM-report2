#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_valid_integer1 (self):
                self.assertEqual (1, calc(1,1))
                
        def test_valid_integer2 (self):
                self.assertEqual (998001, calc(999,999))

        def test_valid_integer3 (self):
                self.assertEqual (200000, calc(400,500))

        def test_invalid_integer1 (self):
                self.assertEqual (-1, calc(1,0))

        def test_invalid_integer2 (self):
                self.assertEqual (-1, calc(999,1000))

        def test_invalid_integer3 (self):
                self.assertEqual (-1, calc(2000,4000))

        def test_invalid_input1 (self):
                self.assertEqual (-1, calc('a',1))

        def test_invalid_input2 (self):
                self.assertEqual (-1, calc('',1))

        def test_invalid_input3 (self):
                self.assertEqual (-1, calc(' ',1))

        def test_invalid_input4 (self):
                self.assertEqual (-1, calc(1.1,1))



