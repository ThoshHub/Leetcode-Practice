# Given two binary strings a and b, return their sum as a binary string
# import numpy as np

# def bin_to_dec(a):
#     sum = 0
#     place = 0
#     process = [int(x) for x in str(a)]
#     for i in reversed(process):
#         sum += i*(2**place)
#         place += 1 # increase place
#     return sum

# def dec_to_bin(b):
#     return 0

def pad_array(arr, pad):
    for i in range(0, pad): 
        arr.append(0)
    return arr

def add_binary(a, b):
    result = []
    a_array = [int(x) for x in str(a)]
    b_array = [int(x) for x in str(b)]

    a_array = a_array[::-1] # reverse the array
    b_array = b_array[::-1] # reverse the array

    if(len(a_array) > len(b_array)):
        b_array = pad_array(b_array, len(a_array) - len(b_array))
    elif(len(b_array) > len(a_array)):
        a_array = pad_array(a_array, len(b_array) - len(a_array))

    carryover = 0
    for i in range (0, len(a_array)):
        if(a_array[i] + b_array[i] + carryover == 0):
            result.append(0)
            carryover = 0
        elif(a_array[i] + b_array[i] + carryover == 1):
            result.append(1)
            carryover = 0
        elif(a_array[i] + b_array[i] + carryover == 2):
            result.append(0)
            carryover = 1
        elif(a_array[i] + b_array[i] + carryover == 3):
            result.append(1)
            carryover = 1
    if(carryover == 1):
        result.append(1)

    result = result[::-1]
    strings_arr = [str(a) for a in result]
    string_res = "".join(strings_arr)
    result_int = int(string_res)
    
    # print(result_int)
    return result_int


# 1011 = 11
# 101101 = 45
result = add_binary(111, 11)
print(result)