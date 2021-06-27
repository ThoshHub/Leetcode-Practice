# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# loop through the first string add all items to hashmap
# do the same to second string
# return hashmap1 == hashmap2

def dicgen(str):
	d = {}
	for i in str:
		if i in d:
			d[i] = d[i] + 1
		else:
			d[i] = 1 
	return d

def v1(str1, str2):
	d1 = dicgen(str1)
	d2 = dicgen(str2)
	return d1 == d2

str1 = 'abcdeffg'
str2 = 'fedcbafg'
print(v1(str1, str2))