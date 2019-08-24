# // Given a target sum and an array of positive integers, return true if any combination of numbers in the array can add to the target (can even be the number itself!). Each number in the array may only be used once. Return false if the numbers cannot be used to add to the target sum.


# Examples: 

# // subsetSum(2, [1, 10, 5, 3]); // false
# // subsetSum(10, [1, 10, 5, 3]); // true
# // subsetSum(9, [1, 10, 5, 3]); // true
# // subsetSum(19, [1, 10, 5, 3]); // true
# // subsetSum(17, [1, 10, 5, 3]); // false

# Initializing at [0] helps with keeping the number itself in the sum array if it's the target sum

# 0 + 1 => [0, 1]
# 10 + 0 / 10 + 1 => [0, 1, 10, 11]
# 5 + 0, 5 + 1, 5 + 10, 5 + 11 => [0, 1, 10, 11, 5, 6, 15, 16]
# 3 + 0, 3 + 1, 3 + 10, 3 + 11, 3 + 5, 3 + 6, 3 + 15, 3 + 16 

# final array of sums = [0, 1, 10, 11, 5, 6, 15, 16, 3, 4, 13, 14, 8, 9, 18, 19]

def findSum(targSum, arr):
    cacheSum = [0]
    for arrInd in range(len(arr)):
        for cacheInd in range(len(cacheSum)):
            sum = arr[arrInd] + cacheSum[cacheInd]
            if (targSum == sum):
                return True
            # if the sum > targSum then the sum will never be reached
            elif (sum < targSum):
                cacheSum.append(sum)
    return False

print(findSum(19, [1, 10, 5, 3]))


