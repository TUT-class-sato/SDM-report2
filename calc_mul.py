#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)

        # 一部ではなく完全にマッチするように : (b), (c)
        p = re.compile('^\d+$')

        # or から and へ : (b), (c)
        if p.match(ai) and p.match(bi):
                a=float(ai)
                b=float(bi)

                # A >= B のとき通るように (a)
                if min(a, b) > 0 and max(a, b) < 1000:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
        matchstring = ''
        while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
        main()
