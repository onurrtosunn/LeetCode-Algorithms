class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        results = [False] * len(candies)

        for i in range(len(candies)): 
            if max_candies <= (candies[i] + extraCandies):
                results[i] = True

        return(results)