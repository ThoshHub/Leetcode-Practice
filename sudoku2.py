def sudoku2(grid):
	length = 9 # len(grid[0])

	# check vertically 
	for j in range (0, length):
		nodupes = {}
		for i, row in enumerate(grid):
			if row[j] == ".":
				l = 1 # Do nothing
			elif row[j] in nodupes:
				return False # there is a duplicate in a column
			else:
				nodupes[row[j]] = 1
	
	#check horizontally
	for row in grid:
		nodupes = {}
		for i, num in enumerate(row):
			if num == ".":
				l = 1 # Do nothing
			elif num in nodupes:
				return False # there id a duplicate in a row 
			else:
				nodupes[num] = 1     
	
	nodupes_1 = {}
	nodupes_2 = {}
	nodupes_3 = {}
	for row in grid[:3]:
		for num in row[:3]:
			if num == ".":
				l = 1 # Do nothing
			elif num in nodupes_1:
				return False # there id a duplicate in a row 
			else:
				nodupes_1[num] = 1

		for num in row[3:6]:
			if num == ".":
				l = 1 # Do nothing
			elif num in nodupes_2:
				return False # there id a duplicate in a row 
			else:
				nodupes_2[num] = 1

		for num in row[6:]:
			if num == ".":
				l = 1 # Do nothing
			elif num in nodupes_3:
				return False # there id a duplicate in a row 
			else:
				nodupes_3[num] = 1

	nodupes_4 = {}
	nodupes_5 = {}
	nodupes_6 = {}
	for row in grid[3:6]:
		for num in row[:3]:
			if num == ".":
				l = 1 # Do nothing
			elif num in nodupes_4:
				return False # there id a duplicate in a row 
			else:
				nodupes_4[num] = 1

		for num in row[3:6]:
			if num == ".":
				l = 1 # Do nothing
			elif num in nodupes_5:
				return False # there id a duplicate in a row 
			else:
				nodupes_5[num] = 1

		for num in row[6:]:
			if num == ".":
				l = 1 # Do nothing
			elif num in nodupes_6:
				return False # there id a duplicate in a row 
			else:
				nodupes_6[num] = 1

	nodupes_7 = {}
	nodupes_8 = {}
	nodupes_9 = {}
	for row in grid[6:]:
		for num in row[:3]:
			if num == ".":
				l = 1 # Do nothing
			elif num in nodupes_7:
				return False # there id a duplicate in a row 
			else:
				nodupes_7[num] = 1

		for num in row[3:6]:
			if num == ".":
				l = 1 # Do nothing
			elif num in nodupes_8:
				return False # there id a duplicate in a row 
			else:
				nodupes_8[num] = 1

		for num in row[6:]:
			if num == ".":
				l = 1 # Do nothing
			elif num in nodupes_9:
				return False # there id a duplicate in a row 
			else:
				nodupes_9[num] = 1
				
	return True


# grid = [[".",".",".","1","4",".",".","2","."], 
# 		[".",".","6",".",".",".",".",".","."], 
# 		[".",".",".",".",".",".",".",".","."], 
# 		[".",".","1",".",".",".",".",".","."], 
# 		[".","6","7",".",".",".",".",".","9"], 
# 		[".",".",".",".",".",".","8","1","."], 
# 		[".","3",".",".",".",".",".",".","6"], 
# 		[".",".",".",".",".","7",".",".","."], 
# 		[".",".",".","5",".",".",".","7","."]]

grid = [[".","4",".",".",".",".",".",".","."], 
		[".",".","4",".",".",".",".",".","."], 
		[".",".",".","1",".",".","7",".","."], 
		[".",".",".",".",".",".",".",".","."], 
		[".",".",".","3",".",".",".","6","."], 
		[".",".",".",".",".","6",".","9","."], 
		[".",".",".",".","1",".",".",".","."], 
		[".",".",".",".",".",".","2",".","."], 
		[".",".",".","8",".",".",".",".","."]]

var = sudoku2(grid)
print(var)