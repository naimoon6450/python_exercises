"""
Finding unique values of a SORTED array

Can use 2 pointers, one you increment if it's a duplicate and the other one that meets up with the other once a unique value is reached
"""

def unique(arr):
    count = 1
    ptr1 = arr[0]
    ptr2 = arr[0]
    for ind in range(len(arr)):
        if (ptr2 == ptr1):
            # keep moving the 2nd pointer
            ptr2 = arr[ind]
        if (ptr2 != ptr1):
            count += 1
            ptr1 = arr[ind]

    return count

print(unique([1,  1,  1,  2,  3,  4,  4,  5,  5]))
# [1,  1,  1,  2,  3,  4,  4,  5,  5] increment only when one of the pts move but not the other
#            pt1 pt2
