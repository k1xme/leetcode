# Use recursion to solve

class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if n == 1 or n == 2: 

            return n
        
        opt = [0]*(n+1)
        opt[0], opt[1], opt[2] = 0, 1, 2
        
        for i in xrange(3, n+1):
            tmp = 0
            for j in xrange(1, i+1):
                
                if j == 1 or j == i:

                    tmp += opt[i - 1] 
                else:
                    tmp += opt[i - j] * opt[j-1]

            opt[i] = tmp

        return opt[n]

s = Solution()
s.numTrees(4)