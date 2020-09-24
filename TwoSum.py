def printPairs(arr, n, sum, result): 
  
    # count = 0  
  
    # Consider all possible  
    # pairs and check their sums 
    for i in range(0, n ): 
        for j in range(i + 1, n ):
            if (arr[i] + arr[j] == sum): 
                result.append(i)
                result.append(j)
                # print(result)
    return result
  
# Driver Code 
arr = [2, 7, 11, 15] 
result = []
n = len(arr) 
sum = 9
result = printPairs(arr, n, sum, result) 
print(result)