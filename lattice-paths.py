# lattice paths

def lp(num1, num2):
    
    if(num1 == 0):
        return 1
    
    if(num2 == 0):
        return 1
    
    
    else:
        return (lp(num1-1, num2)) + (lp(num1, num2-1))


print(lp(2,2))
# lp(20,20)
# print(lp(20, 20))