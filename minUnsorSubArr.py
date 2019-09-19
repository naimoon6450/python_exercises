"""
Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e] such that sorting this subarray makes the whole array sorted.

1) If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60], your program should be able to find that the subarray lies between the indexes 3 and 8.

2) If the input array is [0, 1, 15, 25, 6, 7, 30, 40, 50], your program should be able to find that the subarray lies between the indexes 2 and 5.

max = 40
right =  
[  0,   1,   15,   25,   6,   7,   30, 18,  40,   27]
                                            max   right                                       

[  0,   1,   2,   4,   6,   7,   30, 18,  40,   27]
                                 r    min

Using stack
index 2 is left bound
[0]


"""

def minUnsortSub(arr):
    leftBound = 0
    rightBound = len(arr) - 1

    maxValue = arr[0] 
    minValue = arr[len(arr) - 1]

    # find right bound
    for ind in range(len(arr)):
        # update the max value seen so far
        maxValue = max(maxValue, arr[ind])
        if (arr[ind] < maxValue):
            rightBound = ind
        
    # find left bound
    for ind  in range(len(arr) - 1, -1, -1):
        minValue = min(minValue, arr[ind])
        if (arr[ind] > minValue):
            leftBound = ind

    return rightBound - leftBound + 1


print(minUnsortSub([0,   1,   15,   25,   6,   7,   30, 18,  40,   27]))


