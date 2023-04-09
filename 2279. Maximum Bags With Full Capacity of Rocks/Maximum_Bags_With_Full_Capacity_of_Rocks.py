class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        n = range(len(capacity))
        count = 0
        for i in n: 
            capacity[i] -= rocks[i]        
        result = sorted(capacity)  
        for x in result:
            if additionalRocks >= x :
                additionalRocks -= x
                count += 1
        return count