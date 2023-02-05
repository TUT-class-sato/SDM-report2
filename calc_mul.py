#!/usr/bin/python3

import re
             
def calc(A,B):
        # ai=str(A)
        # bi=str(B)
        checkA = isinstance(A, int)
        checkB = isinstance(B, int)
        # p = re.compile('\d+(\.\d+)?') # convert str to regular expression
        # p = re.compile('[+-]?\d+')
        # if p.match(ai) or p.match(bi): # check that p match ai, bi
        if checkA and checkB:
                # a=float(ai)
                # b=float(bi)
                a = A
                b = B
                # if 0<a and a<b and b<1000:
                if 1<=a and a<=999 and 1<=b and b<=999:
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
