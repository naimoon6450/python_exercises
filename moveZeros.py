"""
Moving 0s
[0,   1,   0,   3,   12]
sl  fast
[0,   1,   0,   3,   12]
    sl    fast


[1,   0,   3,   0,   12]
     sl   fast      
[1,   3,   0,   0,   12]
          sl        fast

Output: [1,3,12,0,0]


"""


def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # indTrack = 0
        
        # for ind in range(len(nums)):
        #     if (nums[ind] != 0):
        #         # store whatever is in first
        #         temp = nums[indTrack]
        #         nums[indTrack] = nums[ind]
        #         nums[ind] = temp
        #         indTrack += 1
        # print(nums)

        # 2 pointer solution
        slow = 0
        fast = 1
        while (fast <= len(nums) - 1):
            # if fast is not 0 then swap with slow
            if (nums[fast] != 0 and nums[slow] == 0):
                temp = nums[fast]
                nums[fast] = nums[slow]
                nums[slow] = temp
                slow += 1
                fast += 1
            # if slow is not 0 move it to where fast is and increment fast
            elif (nums[slow] != 0):
                slow = fast
                fast += 1
            # if fast bumps into a 0 continue moving
            elif (nums[fast] == 0):
                fast += 1
        
        print(nums)

moveZeroes([0,   0])