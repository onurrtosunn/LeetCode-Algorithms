class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        open_bracket = {'(':')', '{':'}','[':']'}
        stack = []
        for char in s:
            if char in open_bracket: 
                stack.append(char)
            elif len(stack) == 0 or open_bracket[stack.pop()] != char:  
                return False
        return len(stack) == 0 