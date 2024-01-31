#!/usr/bin/python3

import re

def is_integer(input_str):
    pattern = r'^-?\d+$'
    return bool(re.match(pattern, input_str))
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        if is_integer(ai) and is_integer(bi):
                a=float(ai)
                b=float(bi)
                if 0<a and a<1000 and 0<b and b<1000:
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
