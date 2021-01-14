#!/usr/bin/python3

def calc(A,B):
    if type(A) == int and type(B) == int:
        if A >= 1 and A <= 999 and B >= 1 and B <= 999:
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
