#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        # calc(A: int, B: int)
        # 入力: A (1 から 999 までの整数が入力可能)  
        #       B (1 から 999 までの整数が入力可能) 
        # 出力: C = A x B
        #       -1 (入力 A，B の値がそれぞれ想定する範囲を超える)
        #          (数字以外の文字列等が入力された)

        # -----------------------------
        # 有効同値
        # -----------------------------
        # 入力A,Bの範囲内の整数か？
        def test_sample1 (self):
                self.assertEqual (460, calc(20,23))

        def test_sample2 (self):
                self.assertEqual (1, calc(1,1))

        def test_sample3 (self):
                self.assertEqual (999, calc(999,1))

        def test_sample4 (self):
                self.assertEqual (999, calc(1,999))

        def test_sample5 (self):
                self.assertEqual (998001, calc(999,999))
                
        # -----------------------------
        # 無効同値
        # -----------------------------
        # 入力A範囲内の整数か？
        def test_sample6 (self):
                self.assertEqual (-1, calc(-2023,11))

        def test_sample7 (self):
                self.assertEqual (-1, calc(0,11))

        def test_sample8 (self):
                self.assertEqual (-1, calc(1000,11))

        def test_sample9 (self):
                self.assertEqual (-1, calc(2023,11))

        # 入力B範囲内の整数か？
        def test_sample10 (self):
                self.assertEqual (-1, calc(11,-2023))

        def test_sample11 (self):
                self.assertEqual (-1, calc(11,0))

        def test_sample12 (self):
                self.assertEqual (-1, calc(11,1000))

        def test_sample13 (self):
                self.assertEqual (-1, calc(11,2023))

        # 入力A,Bが小数か？
        def test_sample14 (self):
                self.assertEqual (-1, calc(0.1,11))

        def test_sample15 (self):
                self.assertEqual (-1, calc(11,0.1))

        def test_sample16 (self):
                self.assertEqual (-1, calc(0.1,0.1))

        # 入力A,Bが数字以外の文字列か？
        def test_sample17 (self):
                self.assertEqual (12, calc('2','6'))

        def test_sample18 (self):
                self.assertEqual (12, calc('２','６'))

        def test_sample19 (self):
                self.assertEqual (-1, calc('a',11))

        def test_sample20 (self):
                self.assertEqual (-1, calc(11,'Z'))

        def test_sample21 (self):
                self.assertEqual (-1, calc('a','z'))