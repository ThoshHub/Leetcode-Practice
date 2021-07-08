# lattice paths
d = {}

def lp(num1, num2):
    if(num1 == 0):
        return 1
    elif(num2 == 0):
        return 1
    else:
        s = str(num1) + ' ' + str(num2)
        if(s not in d):
            d[s] = lp(num1-1, num2) + lp(num1, num2-1)
        return d[s]

print(lp(20,20))