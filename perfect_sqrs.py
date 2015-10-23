import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        
        for i in range(int(math.sqrt(n)), 0, -1):
            if i*i > n: continue
            squares.append(i*i)
        
        opt = [n]*(n+1)
        
        # Initialize.
        for sqr in squares: opt[sqr] = 1
        
        for i in range(1, n+1):
            if opt[i] == 1: continue
            for sqr in squares:
                if sqr > i: continue
                opt[i] = min(opt[i], 1 + opt[i-sqr])
        
        return opt[-1]
                    
sol = Solution()
print sol.numSquares(12)