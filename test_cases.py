#!/usr/bin/python3

import unittest
import unicodedata
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

        def test_sample5 (self):
                self.assertEqual (-1, calc("３３","３"))

        def test_sampleTEST(self):
                y=[1,2,3,4]
                x=[1,2,3,4]
                z=[1,4,9,16]
                for m in y:
                        for k in x:
                                for l in z:
                                        if self.assertEqual(k*m,l):
                                                print ('ok')
"""
        def test_sample_add(self):
                TH=[100,1,999]
                FsH=[0,1000,10000,-100,0.5,10^2]
                FsZ=["１００","-１００","１００００","０","１","９９９","１０００","１０^２","０.５"]
                Fm =["ｔｓｔ","tst"]
                ##K*Mが上手く行えない
                for k in TH:
                        for m in TH:
                                if self.assertEqual(k*m,calc(k,m)):
                                        print("assert error T->F",k,m)
                
                for k in TH:
                        for m in FsH:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)

                for k in TH:
                        for m in FsZ:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)

                for k in TH:
                        for m in Fm:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)

                for k in FsH:
                        for m in FsH:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)

                for k in FsH:
                        for m in FsZ:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)
                
                for k in FsH:
                        for m in Fm:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)
      
                for k in FsZ:
                        for m in FsZ:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)        

                for k in FsZ:
                        for m in Fm:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)

                for k in Fm:
                        for m in Fm:
                                if self.assertEqual(-1,calc(k,m)):
                                        print("assert error F->T",k,m)
"""