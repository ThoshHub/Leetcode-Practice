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
        bef = []
        aft = []
        skip = 0

        for a in s:
            if a < s[pivdex]:
                bef.append(a)
            elif a > s[pivdex]:
                aft.append(a)
            else:
                if skip == 0: # first time coming across it, skip it
                    skip += 1
                else:         # second time, add it
                    bef.append(a)
        
        bef = qsort(bef)
        aft = qsort(aft)
        bef.append(s[pivdex])

        return bef + aft

a = []
b = [1]
c = [2, 1]
d = [3, 5, 2, 43, 12, 4, 5, 7, 88, 432, 23]
e = [5, 4, 3, 2, 1]
f = [3, 2, 1]
g = [5, 4, 3, 2, 1, 5, 5]

print(qsort(d))