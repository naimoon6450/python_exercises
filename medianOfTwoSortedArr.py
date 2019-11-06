"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

nums1 = [1, 3]
nums2 = [2]
[2]

The median is 2.0

nums1 = [2, 5]
nums2 = [3, 4]
[2,3,4,5,7]

The median is (2 + 3)/2 = 2.5

Even number lengths will definitely need division between mid 2 numbers
Odd number will be to extract the middle
"""