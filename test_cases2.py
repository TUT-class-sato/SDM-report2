#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (24, calc(4,6))

        def test_sample2 (self):
                self.assertEqual (-1, calc(-7,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc(432,1238))

        def test_sample4 (self):
                self.assertEqual (-1, calc(-322,1344))

        def test_sample5 (self):
                self.assertEqual (-1, calc('t',6))

        def test_sample6 (self):
                self.assertEqual (-1, calc(78,"test"))

        def test_sample7 (self):
                self.assertEqual (-1, calc("dafda","jfsl"))

        def test_sample8 (self):
                self.assertEqual (-1, calc(-322,"akdd"))

        def test_sample9 (self):
                self.assertEqual (-1, calc("dfafa",2223))

        def test_sample10 (self):
                self.assertEqual (-1, calc(2.2,6.0))
                
        def test_sample11 (self):
                self.assertEqual (-1, calc(2.2,789))

                
        def test_sample12 (self):
                self.assertEqual (-1, calc(3,6.0))


