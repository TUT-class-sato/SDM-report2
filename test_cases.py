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
        
        # ①
        def test_sample5 (self):
                self.assertEqual ( 6 , calc(2, 3) ) # int型
        def test_sample6 (self):
                self.assertEqual ( 6 , calc('2', '3') ) # str型
        def test_sample7 (self):
                self.assertEqual ( -1 , calc(2.0, 1.5) ) # float型
        def test_sample8 (self):
                self.assertEqual ( -1 , calc([2], [1, 3]) ) # list型
        def test_sample9 (self):
                self.assertEqual ( -1 , calc(None, None) ) # None値
        # ②
        def test_sample10 (self):
                self.assertEqual ( 6 , calc(2, 3) ) # int型-int型
        def test_sample11 (self):
                self.assertEqual ( 6 , calc('2', '3') ) # str型-str型
        def test_sample12 (self):
                self.assertEqual ( 6 , calc(2, '3') ) # int型-str型
        # ② str型-str型 ③
        def test_sample13 (self):
                self.assertEqual ( 6 , calc('2', '3') ) # str型-str型 – 整数
        def test_sample14 (self):
                self.assertEqual ( 600 , calc('2', '3e2') ) # – 指数表記の整数
        def test_sample15 (self):
                self.assertEqual ( -1 , calc('2', '3.0') ) # – 小数
        def test_sample16 (self):
                self.assertEqual ( -1 , calc('2', 'a') ) # – その他
        # ② int型-str型 ③
        def test_sample17 (self):
                self.assertEqual ( 6 , calc(2, '3') ) # int型-str型 – 整数
        def test_sample18 (self):
                self.assertEqual ( 600 , calc(2, '3e2') ) # – 指数表記の整数
        def test_sample19 (self):
                self.assertEqual ( -1 , calc(2, '3.0') ) # – 小数
        def test_sample20 (self):
                self.assertEqual ( -1 , calc(2, 'a') ) # – その他
        # ④
        def test_sample21 (self):
                self.assertEqual ( -1 , calc(0, 999) ) # int型
        def test_sample22 (self):
                self.assertEqual ( 999 , calc(1, 999) )
        def test_sample23 (self):
                self.assertEqual ( -1 , calc(0, 1000) )
        def test_sample24 (self):
                self.assertEqual ( -1 , calc(1, 1000) )
        def test_sample25 (self):
                self.assertEqual ( -1 , calc('0', '999') ) # str型
        def test_sample26 (self):
                self.assertEqual ( 999 , calc('1', '999') )
        def test_sample27 (self):
                self.assertEqual ( -1 , calc('0', '1000') )
        def test_sample28 (self):
                self.assertEqual ( -1 , calc('1', '1000') )
        # ⑤
        def test_sample29 (self):
                self.assertEqual ( 999 , calc(1, 999) )
        def test_sample30 (self):
                self.assertEqual ( 999 , calc(999, 1) )
        def test_sample31 (self):
                self.assertEqual ( 999 , calc('1', '999') )
        def test_sample32 (self):
                self.assertEqual ( 999 , calc('999', '1') )
        # ③-④
        def test_sample33 (self):
                self.assertEqual ( -1 , calc('2', '-3e2') ) # 0以下
        def test_sample34 (self):
                self.assertEqual ( -1 , calc('2', '3e3') ) # 1000以上
