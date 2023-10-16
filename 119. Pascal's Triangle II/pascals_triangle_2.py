class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        index = 1
        output = [index]
        for i in range(rowIndex):
            index = index * (rowIndex - i) / (i + 1)
            output.append(index)
        return output