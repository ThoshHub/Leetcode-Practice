def sum_array(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

def max_subarray(arr):
    if len(arr) == 1:
        return arr[0] # if, it's size 1 just return the element

    sum = 0
    arr_size = len(arr)
    pi = 0 
    pj = 1

    while pi < arr_size - 1 and pj < arr_size - 1:
        sum = sum_array(x for x in arr[pi:pj]) # set sum equal to whatever is between the two pointers

    return 0

a = [1, -14, 34, 23, -15, 12, 34, 45]
b = [1, -1]
c = [-1, 0, 1]
d = [1, 2, 3, -1]

driver = max_subarray(d)
# driver = sum_array(b)
print(driver)
# print([x for x in a[0:2]])