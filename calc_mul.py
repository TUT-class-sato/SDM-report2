#!/usr/bin/python3

import re

             
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(\.\d+)?')
        if p.match(ai) and p.match(bi):
                parameter1 = ai
                parameter2 = bi
                is_int1 = parameter1.isdecimal()
                is_int2 = parameter2.isdecimal()
                if is_int1 and is_int2:
                    a=int(ai)
                    b=int(bi)
                    if 0<a and 0<b and a<1000 and b<1000:
                        valid=True
                    else:
                        valid=False
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
