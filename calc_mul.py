#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('^\d+$')
        if p.fullmatch(ai) and p.fullmatch(bi):
                ai.replace("１",'').replace("２",'').replace("３",'').replace("４",'').replace("５",'').replace("６",'').replace("７",'').replace("８",'').replace("９",'').replace("０",'')
                bi.replace("１",'').replace("２",'').replace("３",'').replace("４",'').replace("５",'').replace("６",'').replace("７",'').replace("８",'').replace("９",'').replace("０",'')
                if ai == () or bi == ():
                        valid = False
                else:
                        a=float(ai)##(int(ai)でよくね？)
                        b=float(bi)
                        if 0<a and a<1000 and 0<b and B<1000:
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

