def arrayOfProducts(array):
    prodArray = [1] * len(array)
    prod = 1
    for i in range(len(array) - 2, -1, -1):
        prod *= array[i + 1]
        # print(prod)
        prodArray[i] = prod

    # print(prodArray)
    prod = 1
    for i in range(1, len(array)):
        prod *= array[i - 1]
        prodArray[i] *= prod
    
    # print(prodArray)
    return prodArray

# Driver Code:
array = [5, 1, 4, 2]
result = arrayOfProducts(array)
print(result)