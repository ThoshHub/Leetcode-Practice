# return a string reversed

def reverseString(A):
	reversed = ""
	for i in A:
		reversed = i + reversed
	return reversed

A = "hello this is a string"
print(reverseString(A))

 # some other solutions:
 # https://www.journaldev.com/23647/python-reverse-string