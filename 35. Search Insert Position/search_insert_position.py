class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            result = nums.index(target)
            return result
        
        else:
            bisect.insort(nums, target) 
            return nums.index(target)
            