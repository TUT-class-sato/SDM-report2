#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        '''
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))
        
        def test_sample4 (self):
                self.assertEqual (99.9, calc(0.1,999))
        '''
        def testcase_int_A(self):
                self.assertEqual(4, calc(4,1))
                
        def testcase_int_B(self):
                self.assertEqual(34500, calc(100,345))

        def testcase_minus_A(self):
                self.assertEqual(-1, calc(-1,-121))

        def testcase_minus_B(self):
                self.assertEqual(-1, calc(1,-900))

        def testcase_over_A(self):
                self.assertEqual(-1, calc(10000,1200))

        def testcase_over_B(self):
                self.assertEqual(-1, calc(13323,1000000))

        def testcase_string_A(self):
                self.assertEqual(-1, calc('A',1))

        def testcase_string_B(self):
                self.assertEqual(-1, calc('X','Y'))

        def testcase_string_C(self):
                self.assertEqual(-1, calc(1,'B'))
        