"""
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

[34]

Do this in O(N) time.


[34, -50, 42, 14, -5, 86]
[34, -16, 42, 56, 51, 137]

[34, -16, 42, 56, 51, 137] = max sums per index        
[-1, -2, 20, 30, -4, -2]
[-1, -2, 20, 50, 46, 42]

"""


# brute force
# def maxSubArrSum(arr):
#     max = 0
#     for ind in range(len(arr)):
#         # add the first one
#         initialNum = arr[ind]
#         for j in range(ind + 1, len(arr)):
#             # add next numbers see if higher
#             initialNum += arr[j]
#             if (initialNum > max): 
#                 max = initialNum

#     return max

# O (N) solution similar to the find consec sum to target
"""
Either you extend the current sum or START fresh at a different index

"""
def maxSubArrSumPt(arr):
    # create the sum array
    # sumArr = [-float("inf")] * len(arr)
    sumArr = arr[0]
    # sums ending in index ind
    for ind in range(1, len(arr)):
        # update sumArr with appropriate max
        # for the first index the max is the number itself
        # if (ind == 0):
        #     sumArr = arr[0]
        # else:
            # current number in array vs prevmax + current (extension)
            sumArr = max(arr[ind], sumArr + arr[ind])
            # sumArr[ind] = newMax
    
    return sumArr


print(maxSubArrSumPt([-2,-1,-3,-4,-1,-2,-1,-5,-4]))

        
# print(maxSubArrSumPt([34, -50, 42, 14, -5, 86]))

