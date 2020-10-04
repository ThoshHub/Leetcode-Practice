def isOneBitCharacter(bits):
	"""
	:type bits: List[int]
	:rtype: bool
	"""
	length = len(bits)
	i = 0
	while i < length:
		if bits[i] == 0 and i == length - 1:
			return True
		if bits[i] == 0:
			i += 1
		if bits[i] == 1:
			i += 2
	return False

A = [1, 0, 0]
B = [1, 1, 1, 0]
C = [1, 0, 1]
print(isOneBitCharacter(C))