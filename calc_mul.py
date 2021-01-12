#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(\.\d+)?')
        if p.match(ai) and p.match(bi):
            if p.match(ai)[0]==ai and p.match(bi)[0]==bi:
                a=int(float(ai))
                b=int(float(bi))
                if 0<a and a<1000 and 0 < b and b<1000:
                        valid=True
                else:
                        valid=False

                if (float(ai)-a)!=0 or (float(bi)-b)!=0:
                        valid=False
                else:
                    if valid != False:
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

