#!/usr/bin/python3

import re
                
def calc(A,B):
        valid=False
        if (isinstance(A, str) or isinstance(B, str)):
                valid=False
                return -1
        else:
                ai=str(A)
                bi=str(B)
                p = re.compile('\d')
                if p.match(ai) or p.match(bi):
                        a=float(ai)
                        b=float(bi)
                        if ((a.is_integer()==True) and (b.is_integer()==True)):
                                if (1<=a and a<=999) and (1<=b and b<=999):
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
