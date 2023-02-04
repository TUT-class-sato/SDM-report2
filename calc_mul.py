#!/usr/bin/env python3 
import re 

def calc(A,B):
        ai=str(A)
        bi=str(B)
        #not a digit or int
        if (not re.match("^[0-9 -]+$", ai) or not re.match("^[0-9 -]+$", bi)):
                return -1
        else:
                a=int(ai)
                b=int(bi)
                """
                #not a int
                if a%1.0!=0.0 or b%1.0!=0.0:
                        return -1
                """
                #out of range
                if a<1 or a>=1000 or b<1 or b>=1000:
                        return -1
                else:
                        return a*b


def main ():
        matchstring = ''
        while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
        main()
