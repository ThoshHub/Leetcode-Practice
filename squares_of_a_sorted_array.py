# https://leetcode.com/problems/squares-of-a-sorted-array/

def sortedSquares(A):
	B = []
	for i in A:
		B.append(i ** 2)
	B.sort()
	return B

A = [-4,-1,0,3,10]
sortedSquares(A)
