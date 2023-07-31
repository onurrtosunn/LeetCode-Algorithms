class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        destination = len(nums) - 1
        for steps_left in range(destination-1, -1 , -1):
            if steps_left + nums[steps_left] >= destination:
                destination = steps_left
            
        return destination == 0