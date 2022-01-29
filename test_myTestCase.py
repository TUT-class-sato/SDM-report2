#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1_IntegerAndInteger(self):
            self.assertEqual(21, calc(3, 7))

        def test_sample2_IntegerAndFloat(self):
            self.assertEqual(-1, calc(3, -1))

        def test_sample3_FloatAndInteger(self):
            self.assertEqual(-1, calc(0.3, 5))

        def test_sample4_FloatAndFloat(self):
            self.assertEqual(-1, calc(0.1, 0.1))

        def test_sample5_IntegerAndString(self):
            self.assertEqual(-1, calc(5, 'a'))

        def test_sample6_StringAndInteger(self):
            self.assertEqual(-1, calc('a', 5))

        def test_sample7_StringAndString(self):
            self.assertEqual(-1, calc('a', 'b'))

        def test_sample8_IntegerAndStringnum(self):
            self.assertEqual(32, calc(4, '8'))
        
        def test_sample9_StringnumAndInteger(self):
            self.assertEqual(32, calc('4', 8))
        
        def test_sample10_StringnumAndStringnum(self):
            self.assertEqual(32, calc('4', '8'))
        
        def test_sample11_AltB(self):
            self.assertEqual(24, calc(4, 6))
        
        def test_sample12_AgtB(self):
            self.assertEqual(24, calc(6, 4))

        def test_sample13_AeqB(self):
            self.assertEqual(25, calc(5, 5))

        def test_sample14_Alt1(self):
            self.assertEqual(-1, calc(-1, 5))
        
        def test_sample15_Blt1(self):
            self.assertEqual(-1, calc(5, -1))

        def test_sample16_Agt999(self):
            self.assertEqual(-1, calc(1000, 5))
        
        def test_sample17_Bgt999(self):
            self.assertEqual(-1, calc(5, 1000))

