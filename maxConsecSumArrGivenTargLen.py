def maxConsecSum(arr, k):
    # max distance ptr1 will go is len(arr) - (k)
    sum = 0
    for ind in range(k - 1):
        sum += arr[ind] + arr[ind + 1]
    

    for ind in range(k, len(arr)):
        # arr[ind - k] will be 0 (k - k), 1 (k + 1 - k), 2 (k + 2 - k) etx. 
        newSum = sum + arr[ind] - arr[ind-k]
        sum = max(newSum, sum)
    
    print(sum)

print(maxConsecSum([1,2,5,2,8,1,5], 2))

# takes an array [1,    2,    5,     2,     8,    1,    5], 4 should give 17 [2,5,2,8]
#                 pt1   pt2

