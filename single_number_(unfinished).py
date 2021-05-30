# https://leetcode.com/problems/single-number/
# 136

def solution1(nums): # nums is an array of ints
	# create a hash table
	# loop through array
	# if its not in the hash table, then add it to the hash table with value = 1
	# if its in the hash table, then append value to = 2
	# once the hash table has been built run through the array again 
	# and find the key that has a value of 1
	# This does not satisfy constant space however
	
	
	print("test")

a = [1, 2, 2, 1, 4, 5, 5]
b = [1, 2, 2]
solution1(b)