#!/usr/bin/python3

import re

def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('^[1-9]\d{,2}$')
        if p.match(ai) and p.match(bi):
                a=float(ai)
                b=float(bi)
                valid=True
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

