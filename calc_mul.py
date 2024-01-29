#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        floatp = re.compile('\d+(\.\d+)')
        intp = re.compile('^\d+$')
        if floatp.match(ai) or floatp.match(bi):
                valid = False
        elif intp.match(ai) and intp.match(bi):
                a=int(ai)
                b=int(bi)
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
