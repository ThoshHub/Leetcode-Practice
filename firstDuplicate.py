# https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q/description

def firstDuplicate(a):
	dict = {}
	for index, object in enumerate(a):
		if object in dict:
			return object
		else:
			dict[object] = index
	return -1

A = [2, 1, 3, 5, 3, 2]
B = [2, 2]
C = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
print(firstDuplicate(A))