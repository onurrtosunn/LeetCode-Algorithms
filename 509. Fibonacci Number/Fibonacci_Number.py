class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = [0,1]
        if n < 2:
            return n
        else:
            for i in range(2,n+1):
                answer.append(answer[i-1] + answer[i-2])
            return answer[-1]