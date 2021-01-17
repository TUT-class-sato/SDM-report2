#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        # changes the regular expression from decimal to positive integer
        p = re.compile('\d+$')
        # change the boolean operator from or to and
        if p.match(ai) and p.match(bi):
                # change the convert function from float () to int ()
                a=int(ai) 
                b=int(bi)
                # change the condition of if statement to satisfy specifications
		# and accept the case a >= b
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
