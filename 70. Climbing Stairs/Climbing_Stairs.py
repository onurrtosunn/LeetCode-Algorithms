class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 0 

        for i in range(n):
            a,b = a+b, a
        return a