class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
      """
      Solution1
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
      """
      #Solution2
        for i in range(k):
          nums.insert(0, nums[-1]),
          nums.pop(-1)
        print(nums)