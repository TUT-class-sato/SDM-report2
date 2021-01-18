#!/usr/bin/python3

import re

def is_int(s):
    try:
        int(s)
    except:
        return False
    return True

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def calc(A,B):
    
        if is_int(A) and is_int(B):
            a = float(A)
            b = float(B)
        else:
            return -1
        
        if 0<a<100 and 0<b<1000:
            if is_integer_num(a) and is_integer_num(b):
                ans=a*b
                return ans
	    else:
		return -1
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