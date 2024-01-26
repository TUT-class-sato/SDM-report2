#!/usr/bin/python3

import re
                
def calc(A,B):
        #正則表現用のstr変換
        ai = str(A)
        bi = str(B)
        p = re.compile('[0-9０-９]+')

        if p.fullmatch(ai) and p.fullmatch(bi):
                a = int(ai)
                b = int(bi)
                if (0<a and a<1000) and (0<b and b<1000):
                        valid = True
                else:
                        valid = False
        else:
                valid = False
        
        if valid:
                return a*b
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
