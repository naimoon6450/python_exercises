# length of shortest increasing subsequence given an array of integers


def shortestSub(arr):
    # we know that each element starts with len max of 1
    # initialize array of 1s to length of arr
    initCounts = [1] * len(arr)

    # outer loop
    for i in range(len(arr)):
        # inner loop going through prev sums
        for j in range(i):
            # start comparing from second ind
            increasingBool = arr[i] > arr[j]
            # this ensures that the MAX is being updated with greatest length
            # and it's not part of a different sequence
            # You only want to + 1 IFF it's increasing and if 
            # [1, 0, 4, 10, 3] when it gets to 
            # subSeqBool = initCounts[j] + 1 > initCounts[i]
            if (increasingBool):
                initCounts[i] = max(initCounts[i], initCounts[j] + 1)
    
    return max(initCounts)

print(shortestSub([-1, 5, 0, 10, 3, 12]))





# answer is 4,8,10,12 so 4
#shortestSub([4,8,3,5,10,12,7]) 

