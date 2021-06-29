# striING COMPRESSION

def f(stri):
	# returned
	compressedString = ''
	
	# keeps track of current char
	current = ''
	count = 0
	
	# loop through the string 
	# if the char is different than the held char
	# first append current and count to compressed string
	# set count to 1
	# set new current char
	# else it is the same char
	# increase count
	for char in stri:
		if char == current:
			count += 1
		else:
			# skip first loop
			if count != 0:
				compressedString = compressedString + current + str(count)
			# always set new count and new current char
			count = 1
			current = char
	# set new count and new current char one last time as loop exits
	compressedString = compressedString + current + str(count)
	
	return compressedString

print(f('aabccccaaa'))