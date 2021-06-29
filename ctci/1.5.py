# there are three types of editw that can be performed 
# on strings: insert, remove,or replace a character. Given two string,
# write a function to check if thy are one edit or zero edits away

# long string is passed in first
def checkinserts(long, short):
	diffCount = 0
	# loop through short
	for index, char in enumerate(short):
		if diffCount == 0:
			if short[index] != long[index]:
				diffCount += 1
		if diffCount == 1:
			if short[index] != long[index + 1]:
				return False
	return True	

def f(str1, str2):
	if len(str1) > len(str2) + 1 or len(str2) > len(str1) + 1:
		return False
	
	diffCount = 0
	
	if len(str1) > len(str2): # str 1 is longer
		return checkinserts(str1, str2)
	elif len(str2) > len(str1): # str2 is longer
		return checkinserts(str2, str1)
	else: # only 1 char must be different
		for index, char in enumerate(str1):
			if str1[index] != str2[index]:
				diffCount += 1
		
	return diffCount == 1 or diffCount == 0

str1 = "abc"
str2 = "dabd"
print(f(str1, str2))