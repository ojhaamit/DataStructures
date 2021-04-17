def sortedSquaredArray(array):
    squareArray = [0 for _ in array]
    if len(array) == 0:
        return []
    for i in range(len(array)):
        squareArray[i] = array[i] * array[i]
    
    squareArray.sort()
    return squareArray

# Driver Code:
input = [1, 2, 3, 5, 6, 8, 9]
result = sortedSquaredArray(input)
print(result)