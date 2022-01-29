#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=A
        bi=B
        #ai=str(A)
        #bi=str(B)
        #p = re.compile('\d+(\.\d+)?')
        if type(ai) is int and type(bi) is int:
                a=float(ai)
                b=float(bi)
                if 0<a and a<b and b<1000:
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
