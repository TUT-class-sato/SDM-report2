#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # a,b in [1...999], a < b
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        # a < 1,  b in [1...999]
        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        # a,bは文字列がある
        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        # a in [1...999], b > 999
        def test_sample5 (self):
                self.assertEqual(-1,calc(1,1000))

        # a in [1...999], b < 1
        def test_sample6 (self):
                self.assertEqual(-1,calc(1,0.5))

        # a > 999,  b in [1...999]
        def test_sample7 (self):
                self.assertEqual(-1,calc(1000,1))   

         # a,b in [1...999], a> b
        def test_sample8(self):
                self.assertEqual(15,calc(5,3))

        # a,b in [1...999], a = b
        def test_sample9(self):
                self.assertEqual(16,calc(4,4))

         # a in [1...999], bは文字列がある
        def test_sample10(self):
                self.assertEqual(-1,calc(2,"a"))

        # b in [1...999], aは文字列がある
        def test_sample11(self):
                self.assertEqual(-1,calc("a",1))

        # a, b in [1...999] が、aは整数ではない
        def test_sample12(self):
                self.assertEqual(-1,calc(1.5,2))
                
        # a, b in [1...999] が、bは整数ではない
        def test_sample13(self):
                self.assertEqual(-1,calc(2,2.5))
        
        # a, b in [1...999] が、aは整数ではない
        def test_sample14(self):
                self.assertEqual(-1,calc(1.5,2.5))
                
        


