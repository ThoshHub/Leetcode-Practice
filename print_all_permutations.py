# print all permutations of a string

def insertInbetween(first, intermediate): # returns array
    # a, bc -> abc, bac, bca

    result = []
    for i, obj in enumerate(intermediate):
        result.append(intermediate[:i] + first + intermediate[i:])
    result.append(intermediate + first)
    return result # returns array

def permutations(input): # returns array
    result = []
    if len(input) == 1:
        return input
    else: # greater than 1:
        first_letter = input[0]
        rest_of_input = input[1:]
        
        intermediate = permutations(rest_of_input) # returns array of strings
        for i, obj in enumerate(intermediate):
            a = insertInbetween(first_letter, obj) # returns array
            result = result + a
    result.sort() # optional
    return result

input = "abc"
result = permutations(input)
for i in result:
    print(i)