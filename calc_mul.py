#!/usr/bin/python3

import re
                
def calc(A,B):
	at = type(A)
	bt = type(B)
	#ai=str(A)
	#bi=str(B)
	#p = re.compile('\d+(\.\d+)?')
	#if p.match(ai) or p.match(bi):
	if (at is int) and (bt is int):
		#a=float(ai)
		#b=float(bi)
		if A > B:
			tmp = A
			A = B
			B = tmp
		if 0<A and A<=B and B<1000:
		#if 0<a and a<b and b<1000:
			valid=True
		else:
			valid=False
	else:
		valid=False
                
	if valid:
		#ans=a*b
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
