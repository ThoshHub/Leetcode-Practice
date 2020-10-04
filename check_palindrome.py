def checkPalindrome(A):
	return A == A[::-1]

A = "abcdef"
B = "abccba"
print(checkPalindrome(A))