"""
Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1

output
[1]

counter
0

[3,4,9,6,1]
p1p2

3 [1,4,6,9] -> binHelp should give 1
4 [9,6,1] -> binHelp should give 1
9 [6,1] -> binHelp should give 2
6 [1] -> binHelp should give 1
1 [0] -> binHelp should give 0

"""

# basic implementation
# def numOfElems(arr):
#     output = []
#     counter = 0

#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             if (arr[i] > arr[j]):
#                 counter+=1
        
#         output.append(counter)
#         counter = 0
#     return output

# O (nlogn) solution
class NumElems:
    def __init__(self, arr):
        self.arr = arr
    

    def numOfElems(self):
        outputArr = []
        for i in range(len(self.arr)):
            outputArr.append(self.binSearch(self.arr[i + 1:], self.arr[i]))
        print(outputArr)

    # helper binary search return num less than that num
    # [1, 6]
    #  l  mh
    # targ = 9
    def binSearch(self, arr, targ):
        # sort arr
        arr.sort()
        low = 0
        high = len(arr) - 1

        while low <= high: 
  
            mid = low + (high - low) / 2; 
            
            # Check if x is present at mid 
            if arr[mid] == targ: 
                return mid 
    
            # If x is greater, ignore left half 
            elif arr[mid] < targ: 
                low = mid + 1
    
            # If x is smaller, ignore right half 
            else: 
                high = mid - 1
      
        # If we reach here, then the element 
        # was not present 
        return low



obj = NumElems([5,2,6,1])

obj.numOfElems()

