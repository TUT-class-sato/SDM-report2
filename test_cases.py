#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        # test_case_1 : 文字を含む場合
        def test_case_1_1 (self):
                self.assertEqual (-1, calc('a', 256))

        def test_case_1_2 (self):
                self.assertEqual (-1, calc(1, 'b'))
        
        # test_case_2 : 負の数を含む場合
        def test_case_2_1 (self):
                self.assertEqual (-1, calc(-100, -10)) # a < b
        
        def test_case_2_2 (self):
                self.assertEqual (-1, calc(-10, -50)) # a > b
        
        def test_case_2_3 (self):
                self.assertEqual (-1, calc(100, -10))
        
        def test_case_2_4 (self):
                self.assertEqual (-1, calc(-100, 10))

        # test_case_3 : 小数を含む場合
        def test_case_3_1 (self):
                self.assertEqual (-1, calc(1.1, 2.2))

        def test_case_3_2 (self):
                self.assertEqual (-1, calc(1, 2.2))

        # test_case_4 : 整数の大小関係が異なる場合
        def test_case_4_1 (self):
                self.assertEqual (15, calc(5, 3)) # a > b

        def test_case_4_2 (self):
                self.assertEqual (2500, calc(50, 50)) # a = b

        def test_case_5 (self):
                self.assertEqual (-1, calc(7, 1000)) # 1000丁度のとき

        def test_case_6 (self):
                self.assertEqual (999, calc(1, 999)) # 入力範囲の最小・最大値