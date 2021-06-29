# write an algorithm such that if an element in an MxN matrix is zero,
# its entire row and column are set to 0

# loop through each row, 
# loop each col of that row
# when you come across a zero, add that index to cols
# after you've looped through all the cols of that row, 
# if you came across a zero, set the whole row to zero
# finish looping through the rows

# at the end you should have a list of rows set to zero
# loop through the entire thing again
# set all columns equal to zeros (check if index in cols array)
# then return

def f(mat):
	# list of columns to be set to zero
	cols = []
	return 0
	
mat =  [[1, 1, 1, 1],
	[1, 1, 0, 1],
	[1, 0, 1, 1],
	[1, 1, 1, 1],]

print(f(mat))