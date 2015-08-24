class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        if n == 0 or k == 0: return []
        
        rst = []
        nums = [x for x in range(1,n+1)]
        
        self._combine(1, n, k, [], rst)
        return rst
    
    def _combine(self, start, n, k, comb, rst):
        if k == 0:
            rst.append(comb)
        
        for i in range(start,n+1):
            self._combine(i+1, n, k-1, comb+[i], rst)

s = Solution()
print s.combine(4,2)