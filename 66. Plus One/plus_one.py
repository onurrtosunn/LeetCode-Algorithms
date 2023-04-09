class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        str_digits = "".join(map(str,digits))
        digits = int(str_digits) +1
        digits = str(digits)
        return list(map(int,digits))