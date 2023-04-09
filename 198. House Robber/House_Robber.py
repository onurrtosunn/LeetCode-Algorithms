class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1 = 0
        rob2 = 0
        #houses
        #[rob1, rob2, n, n+1 ....]
        for i in nums:
            temp = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2