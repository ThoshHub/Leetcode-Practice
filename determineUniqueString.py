# Problem 1.1 CTCI
# Page 98

# This algorithm will determine if a string has all unique characters

def determine(input):
	listOfChars = {} # Empty Dictionary
	for char in input:
		if char in listOfChars:
			return False
		else:
			listOfChars[char] = char
	return True

# Driver Code
print("-- BEG ---")
# input = "input"
# input = "abcdefg"
input = "abbcdefg"
# input = "abccdefg"
# input = "abcddefg"

isUnique = determine(input)
print("Input String is Unique: {}".format(isUnique))

print("-- END --")