# https://leetcode.com/problems/squares-of-a-sorted-array/

# Brute Force Method
# def sortedSquares(A): 
# 	B = []
# 	for i in A:
# 		B.append(i ** 2)
# 	B.sort()
# 	return B

def sortedSquares(A):
	B = []
	length = len(A)
	# if length == 1:
	# 	B.append(A[0] ** 2)
	# 	return B

	negatives = 0 # initialize 
	postives = 0 # initialize

	for i in A:
		if i < 0:
			postives += 1 # postives is now index of first non-negative integer
	
	negatives = postives - 1 # negatives is now index of first negative integer

	# counter = 0

	while(negatives >= 0 and postives < length):
		if (A[negatives] ** 2) < (A[postives] ** 2):
			B.append(A[negatives] ** 2)
			negatives -= 1
		else:
			B.append(A[postives] ** 2)
			postives += 1
		# print('counter: {}, len: {}, neg: {}, post: {}'.format(counter, length, negatives, postives))
		# counter += 1

	while postives < length:
		B.append(A[postives] ** 2)
		postives += 1
		# print('counter: {}, len: {}, neg: {}, post: {}'.format(counter, length, negatives, postives))
		# counter += 1

	while negatives >= 0:
		B.append(A[negatives] ** 2)
		negatives -= 1
		# print('counter: {}, len: {}, neg: {}, post: {}'.format(counter, length, negatives, postives))
		# counter += 1
		
	return B

A = [-4,-1,0,3,10]
C = [1]
B = sortedSquares(C)
for i in B:
	print(i)