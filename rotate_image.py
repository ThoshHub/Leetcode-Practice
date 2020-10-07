def rotateImage(a):
    b = a # create a clone of a
    size = len(a)
    
    for row, columnS in enumerate(a): # row = index, columnS = list object
        new_row = size - row - 1
        # print(columnS)
        for column, num in enumerate(columnS): # column = index, num = VALUE
            # print(num)
            print(str(num) + " inserted into: (" + str(column) + ", " + str(new_row) + ")")
            # b[column][new_row] = num
        # print("\n")
        
    return b

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = rotateImage(a)
for i in b:
	print(i)