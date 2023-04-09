class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_number = 0 

        for i in range(len(nums)):
            #eliminate negative numbers
            if current_number < 0:
                current_number = 0
            current_number += nums[i]
            

            if current_number > max_sum:
                max_sum = current_number

        return max_sum        