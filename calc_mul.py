#!/usr/bin/python3

import re
                
def calc(A, B):
    if isinstance(A, int) and isinstance(B, int): #isinstanceでAとBの値が整数であることを判定
        if 1 <= A <= 999 and 1 <= B <= 999: #AとBの値が1以上999以下の範囲内であるかを判定
            return A * B
    return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()