#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        # run strip before checking ( to remove trailing spaces)
        # make sure to allow 0 prefixes, nvm is already allowed
        ai= ai.strip()
        bi = bi.strip()
        p = re.compile(r'^[+-]?\d+$')

        if p.match(ai) and p.match(bi):
                a=float(ai)
                b=float(bi)
                
                # switch values if b is smaller than a
                if b < a: 
                        tmp = a
                        a = b
                        b = tmp

                if 0<a and a<=b and b<1000:
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
