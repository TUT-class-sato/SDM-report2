#!/usr/bin/python3

import re

def is_in_range(a,b):
        return 0<a and a<1000 and 0<b and b<1000

def calc(A,B):
        p = re.compile(r'^\d+$')
        if p.match(str(A)) and p.match(str(B)):
                a=int(A)
                b=int(B)
                if is_in_range(a,b):
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
