#!/usr/bin/python3

import re
                
def calc(A,B):
        if "." in str(A) or "." in str(B):
                return -1
        if str(A).startswith('0') or str(B).startswith('0'):
                return -1

        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(\.\d+)?')
        if p.match(ai) and p.match(bi):
                
                a=float(ai)
                b=float(bi)

                if 1<=a  and b<=999 and (isinstance(a,(int,float))):
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

