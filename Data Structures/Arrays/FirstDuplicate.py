def firstDuplicateValue(array):
    if len(array) == 0:
        return -1
    seen = set ()
    for i in range(len(array)):
        if array[i] in seen:
            return array[i]
        seen.add(array[i])
    return -1

# Driver code
array = [2, 1, 5, 2, 3, 3, 4]
result = firstDuplicateValue(array)
print(result)