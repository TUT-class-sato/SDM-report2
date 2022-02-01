#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        ## Legacy
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))
        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))
        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))
        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        ## Testing out of range, below 1
        def test_invalidPartition1_a (self):
                self.assertEqual (-1, calc('0','123'))
        def test_invalidPartition1_b (self):
                self.assertEqual (-1, calc('123','-500'))
        def test_invalidPartition1_c (self):
                self.assertEqual (-1, calc('0.9999','0.9999'))
        def test_invalidPartition1_d (self):
                self.assertEqual (-1, calc('0.9999999999999','0.9999999999999'))
                #float precision truncates  0.99999999999999999 to 1.0 in my environment

        ## Testing within range
        def test_validPartition_a (self):
                self.assertEqual (21, calc('3','7'))
        def test_validPartition_b (self):
                self.assertEqual (999, calc('1','999'))

        ## Testing out of range, above 999
        def test_invalidPartition2_a (self):
                self.assertEqual (-1, calc('1000','1000'))
        def test_invalidPartition2_b (self):
                self.assertEqual (-1, calc('12345','6789'))
        def test_invalidPartition2_c (self):
                self.assertEqual (-1, calc('1000','0.8'))

        ## Testing rejection of invalid formats
        def test_invalidFormat_a (self):
                self.assertEqual (-1, calc('abc','123'))
        def test_invalidFormat_b (self):
                self.assertEqual (-1, calc('a12','34b'))
        def test_invalidFormat_c (self):
                self.assertEqual (-1, calc('2','pi'))
        def test_invalidFormat_d (self):
                self.assertEqual (-1, calc('三','十'))
        def test_invalidFormat_e (self):
                self.assertEqual (-1, calc('3.','141'))

        ## Testing acceptance of valid formats
        ## Note that RegEx '\d' matches any character in the
        ## Unicode category 'Number, Decimal Digit':
        ## https://www.fileformat.info/info/unicode/category/Nd/list.htm
        def test_specialFormat_a (self):
                self.assertEqual (10*20, calc('10.0','20.0'))
        def test_specialFormat_b (self):
                self.assertEqual (64*46, calc('６４','４６'))
                #full-width digits from Unicode
        def test_specialFormat_c (self):
                self.assertEqual (5*5, calc('๕','᠕'))  # Thai & Mongolian 5
                #unicode digits from Unicode digits block (match \d)
        def test_specialFormat_d (self):
                self.assertEqual (5*5, calc('𝟓.𝟎','𝟝.𝟘'))  # Bold & DoubleStruck
                #unicode digits from Unicode digits block (match \d)
        def test_specialFormat_e (self):
                self.assertEqual (2*314, calc('000000002','314.000000000'))

