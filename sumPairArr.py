"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

So addinf the check to see if sum is < target will decraese the time when you check for the sum again in sum == k logic

We don't care about sums that are > k

"""


def sumPairArr(arr, k):
    sums = [0]
    for i in range(len(arr)):
        for j in range(len(sums)):
            sum = sums[j] + arr[i]
            if (sum == k):
                print(sums)
                return True
            elif(sum < k):
                sums.append(sum)

    print(sums)
    return False

print(sumPairArr([-4, 10, 15, 3, 7, 6], 22))
