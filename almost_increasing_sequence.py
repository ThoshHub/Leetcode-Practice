# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG

def almostIncreasingSequence(sequence):
	count = 0
	peak = max(sequence)
	sequence.remove(peak)
	print(sequence)
	for index, object in enumerate(sequence[:len(sequence)-1]):
		if sequence[index] >= sequence[index+1]:
			return False
	
	return True

a = [1, 2, 3, 4, 99, 5, 6]
print(almostIncreasingSequence(a))