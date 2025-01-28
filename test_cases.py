#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #テストサンプル
        #def test_sample1 (self):
        #        self.assertEqual (21, calc(3,7))

        #def test_sample2 (self):
        #        self.assertEqual (-1, calc(0,150))

        #def test_sample3 (self):
        #        self.assertEqual (-1, calc('a','b'))

        #def test_sample4 (self):
        #        self.assertEqual (-1, calc(0.1,999))

        #境界値分析
        def test_boundary_value (self):
                #aの最小値まわり
                self.assertEqual (-1, calc(0,500))
                self.assertEqual (500, calc(1,500))
                #bの最小値周り
                self.assertEqual (-1, calc(600,0))
                self.assertEqual (600, calc(600,1))
                #aの最大値周り
                self.assertEqual (499500, calc(999,500))
                self.assertEqual (-1, calc(1000,500))
                #bの最大値周り
                self.assertEqual (24975, calc(25,999))
                self.assertEqual (-1, calc(25,1000))

        #同値分析
        def test_equivalence (self): 
                #無効同値(1 > a・b)
                self.assertEqual (-1, calc(-500,450))  # a < 1
                self.assertEqual (-1, calc(240, -250)) # b < 1
                #有効同値(1 <= a・b <= 999)
                self.assertEqual (80000, calc(200,400)) # 1 <= a・b <= 999, a<b
                self.assertEqual (80000, calc(400,200)) # 1 <= a・b <= 999, a>b
                #無効同値(999 < a・b)
                self.assertEqual (-1, calc(1300, 250)) # 999 < a
                self.assertEqual (-1, calc(240, 2500)) # 999 < b

        #単体テスト例やその他条件から考案したテストケース
        def test_others (self):
                #異常ケース
                self.assertEqual (-1, calc("080",181))  #先頭が0の数列
                #NULLとゼロ
                self.assertEqual (-1, calc("",""))  #入力なしの場合
                self.assertEqual (-1, calc(0,0))  #入力0の場合
                #文字列関係
                self.assertEqual (-1, calc("Hello","World")) # a・b: 文字列
                self.assertEqual (-1, calc("21ab15",3)) # a: 文字列と数値の混合値
                self.assertEqual (-1, calc("２０",24))  # a: 全角数字

                                            
