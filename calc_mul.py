#!/usr/bin/python3

import re
                
def calc(A,B):
        #整数型以外のとき-1を返す
        if(not isinstance(A,int) or not isinstance(B,int)):
                return -1
        
        #入力範囲が正しいか判定
        if(A >= 1 and A <= 999 and B >= 1 and B <= 999):
                pass
        else:
                return -1

        return A * B
        
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
