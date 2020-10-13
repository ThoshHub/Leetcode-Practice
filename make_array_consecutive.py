# https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

def makeArrayConsecutive2(statues):
	return max(statues) - min(statues) - len(statues) + 1

a = [6, 2, 3, 8]
b = makeArrayConsecutive2(a)
print(b)