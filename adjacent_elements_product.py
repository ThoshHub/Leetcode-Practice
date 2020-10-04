# https://stackoverflow.com/questions/1011938/python-loop-that-also-accesses-previous-and-next-values

def adjacentElementsProduct(inputArray):
	product = float('-inf') # negative infinity
	l = len(inputArray)
	for index, object in enumerate(inputArray[0:l-1]): # loop through all indexes except last one, keeping track of indexes and object in index
		# print("index: {}, object: {}".format(index, object))
		if inputArray[index] * inputArray[index + 1] > product:
			product = inputArray[index] * inputArray[index + 1]
	return product

A = [3, 6, -2, -5, 7, 3]
C = [5, 1, 2, 3, 1, 4]
D = [-1, -2]
B = adjacentElementsProduct(D)
print(B)