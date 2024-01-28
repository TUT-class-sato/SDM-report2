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

        def test_sample_add(self):
                T=['１００',100,'１01','１',1,'９９９',999,'９99']
                F=['０',0,'１０００',1000,'１０00','－１００',-100,'-１０0','ｔｓｔ','tst','ｔst','１，０００','1,000','１,00０','０.５',0.5,'０.5']
                for k in T:
                        for m in T:
                                if self.assertEqual(k*m,calc(k,m)):
                                        print("assert error T->F",k,m)
                
                for k in T:
                        for m in F:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)

                for k in F:
                        for m in T:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)

                for k in F:
                        for m in F:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)

      
        

