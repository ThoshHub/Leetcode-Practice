# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG

# brute force method
def almostIncreasingSequence(sequence):
	
	for i in sequence:
		sequence.remove(sequence[0])
		print(sequence)

a = [1, 2, 3, 4, 99, 5, 6]
print(almostIncreasingSequence(a))