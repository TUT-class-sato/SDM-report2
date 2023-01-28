#!/usr/bin/python3

import re
                
def calc(A,B):
	at = type(A)
	bt = type(B)
	if (at is int) and (bt is int):
		if A > B:
			tmp = A
			A = B
			B = tmp
		if 0<A and A<=B and B<1000:
			valid=True
		else:
			valid=False
	else:
		valid=False
                
	if valid:
		ans = A * B
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
