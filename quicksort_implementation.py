from random import randrange

# sorts from SMALLEST to LARGEST
def qsort(s):
    # if array is 0 or 1 long, then return it
    if(len(s) < 2):
        return s
    # if array is 2 long, then check whether first is bigger than the second
    elif(len(s) == 2):
        if(s[0] > s[1]):
            return([s[1], s[0]]) # if it is, return the array reversed
        else:
            return s # return the original
    else: # if array is greater than length 2, then recurse
        pivdex = randrange(len(s)) # pick a random index between 0 and array length
        piv = s[pivdex] # get value of that index

        bef = [] # initialize array of all numbers smaller than piv
        aft = [] # initialize array of all numbers larger than piv

        index = 0
        while index < len(s): # loop through array
            if s[index] == pivdex: # if you hit that index, then skip it
                index += 1
            else: # otherwise, check if the value is bigger or smaller than piv
                if s[index] < piv:
                    bef.append(s[index])
                    index += 1
                else:
                    aft.append(s[index])
                    index += 1

        # take everything before the array and put it into new array "a"
        bef = qsort(bef) # recursively sort subarrays 
        aft = qsort(aft) 

        bef.append(piv) # append the middle element

        return bef + aft # return the combined array

a = []
b = [1]
c = [2, 1]
d = [3, 5, 2, 43, 12, 4, 5, 7, 88, 432, 23]
e = [5, 4, 3, 2, 1]
f = [3, 2, 1]

print(qsort(f))