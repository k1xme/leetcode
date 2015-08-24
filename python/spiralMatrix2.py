# Edges cases, when n%2 == 1.

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n == 0: return []
        if n == 1: return [[1]]
        
        num = 1
        layer = 0
        rst = []
        for i in range(n):
            rst += [[0]*n]

        while layer <= n/2:
            print layer
            #fill up from left to right.
            for i in range(layer,n-layer-1):
                rst[layer][i] = num
                num += 1
            
            for i in range(layer, n-layer-1):
                rst[i][n-layer-1] = num
                num += 1
            
            for i in range(n-layer-1, layer, -1):
                rst[n-layer-1][i] = num
                num += 1
            
            for i in range(n-layer-1, layer, -1):
                rst[i][layer] = num
                num += 1
            
            layer += 1
        if n%2 == 1:
            rst[n/2][n/2] = num

        return rst

s = Solution()
s.generateMatrix(5)
