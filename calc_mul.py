#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(\.\d+)?')
        if p.match(ai) and p.match(bi):
                a=float(ai)
                b=float(bi)
                if 0<a  and b<1000 and a<1000 and 0<b:
                   if a%10 == 0.0 or 0.9 < a%10:
                        if b%10 == 0.0 or 0.9 < b%10:
                           valid = True
                        else:
                           valid = False
                   else:
                      valid = False

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
