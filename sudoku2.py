def sudoku2(grid):
	length = len(grid[0])
	
	# check vertically 
	for j in range (0, length):
		nodupes = {}
		for i, row in enumerate(grid):
			if row[j] in nodupes:
				return False # there is a duplicate in a column
			else:
				nodupes[row[j]] = 1
	
	#check horizontally
	for row in grid:
		nodupes = {}
		for i, num in enumerate(row):
			if num in nodupes:
				return False # there id a duplicate in a row 
			else:
				nodupes[num] = 1     

	return True 


grid = [[".",".",".","1","4",".",".","2","."], 
		[".",".","6",".",".",".",".",".","."], 
		[".",".",".",".",".",".",".",".","."], 
		[".",".","1",".",".",".",".",".","."], 
		[".","6","7",".",".",".",".",".","9"], 
		[".",".",".",".",".",".","8","1","."], 
		[".","3",".",".",".",".",".",".","6"], 
		[".",".",".",".",".","7",".",".","."], 
		[".",".",".","5",".",".",".","7","."]]

sudoku2(grid)