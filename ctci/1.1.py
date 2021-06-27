#  Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# loop through each letter and check if it exists in the hash table
# if it exists, return false
# if it doesn't insert into the hash table
# if goes through the whole loop then return true
def v1(inp):
	dic = {}
	for i in inp:
		if i in dic:
			return 'Does not have all unique chars'
		else:
			dic[i] = '1'
	return 'Has all unique chars'

inp = "abc"
inp = "abcd"
print(v1(inp))