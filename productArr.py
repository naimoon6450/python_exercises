"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of 
all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
Before 1 and After 5 there's nothing so include 1
[1, 1, 2, 6, 24]
[120, 60, 20, 5, 1]


If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

# with division
def prodArr(arr):
    totalProd = 1
    for i in range(len(arr)):
        totalProd *= arr[i]

    result = []
    for i in range(len(arr)):
        result.append(totalProd/arr[i])

    return result

# without division
def prodArrNoDiv(arr): 
    # dynamically get the left side
    prod = 1
    # initialize first to 1 as there's nothing before 1
    leftArr = [1]
    for ind in range(len(arr) - 1):
        leftArr.append(arr[ind] * prod)
        prod *= arr[ind]
    
    prod2 = 1
    rightArr = [1] * len(arr)
    # intialize the last elem as 1 since there's nothing after 5
    rightArr[len(arr) - 1] = 1
    for ind in range(len(arr) - 1, 0, -1):
        rightArr[ind - 1] = prod2*arr[ind]
        prod2 *= arr[ind]
    
    # creating actual product
    result = []
    for ind in range(len(arr)):
        result.append(rightArr[ind] * leftArr[ind])
    
    return result


print(prodArrNoDiv([1]))