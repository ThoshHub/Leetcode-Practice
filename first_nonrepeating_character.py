# https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC/description

def firstNotRepeatingCharacter(s):
	dict = {}
	for i, o in enumerate(s):
		if o in dict.keys():
			dict[o] = dict[o] + 1 # increase by 1
		else: 
			dict[o] = 1
	for i in s:
		if dict[i] == 1:
			return i
	return "_"

A = "abacabad"
B = "z"
C = "bcccccccb"
print(firstNotRepeatingCharacter(C))