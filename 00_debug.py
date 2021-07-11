def insertInbetween(first, intermediate):
    # a, bc -> abc, bac, bca
    result = []
    for i, obj in enumerate(intermediate):
        result.append(intermediate[:i] + first + intermediate[i:])
    result.append(intermediate + first)
    return result

a = insertInbetween('a', 'bcd')
print(a)