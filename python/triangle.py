class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle: return 0
        
        n = len(triangle)
        preOPT = [triangle[0][0]] # root number.
        
        for i in range(1, n):
            curOPT = [0] * (i + 1)
            for j in range(i+1):
                if j == 0:
                    curOPT[j] = preOPT[j] + triangle[i][j]
                elif j == i:
                    curOPT[j] = preOPT[j-1] + triangle[i][j]
                else:
                    # The min of adjacent cells.
                    curOPT[j] = min(preOPT[j-1], preOPT[j]) + triangle[i][j]
            preOPT = curOPT
            
        return min(preOPT)

s = Solution()
print s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])