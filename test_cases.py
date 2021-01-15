#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

         # 1~999
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))
        # 0以下
        def test_sample2 (self):
                self.assertEqual (-1, calc(-5,150))
        # 1000以上
        def test_sample3 (self):
                self.assertEqual (-1, calc(2000,150))
        # 数字以外
        def test_sample4 (self):
                self.assertEqual (-1, calc('a','b'))
        # 整数以外 によるエラー処理ができていない
        def test_sample5 (self):
                self.assertEqual (-1, calc(0.1,999))

