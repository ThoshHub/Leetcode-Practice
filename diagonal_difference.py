# https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def diagonalDifference(arr):
    # Write your code here
	first = 0
	second = 0
	length = len(arr) # size of the array

	for i in range(0, length):
		first += arr[i][i]
		second += arr[i][abs(length-1-i)]
	# print(str(first) + ", " + str(second))
	
	return abs(first - second)

a = [[1, 2, 3],
	[4, 5, 6],
	[9, 8, 9]]

print(diagonalDifference(a))