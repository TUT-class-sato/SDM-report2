#!/usr/bin/python3

import re
                
def calc(A,B):
        if isinstance(A, str) or isinstance(B, str) or isinstance(A, float) or isinstance(B, float):
                valid=False
        else:
                ai=str(A)
                bi=str(B)
                p = re.compile('\d+')
                if p.match(ai) or p.match(bi):
                        a=int(ai)
                        b=int(bi)
                        if a > 0 and a < 1000 and b > 0 and b < 1000:
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
