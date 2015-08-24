class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        # Numbers available to use.
        nums = [x for x in xrange(1, 10)]
        rst = []
        self._combinationSum(k, n, nums, [], rst)
        return rst
    
    def _combinationSum(self, k, n, nums, tmp, rst):
        if k == 0 and n == 0:
            rst.append(tmp)
            return
        elif n == 0 or k == 0: return
        
        for i in range(len(nums)):
            target = n - nums[i]

            if target >=0:
                self._combinationSum(k-1, target, nums[i+1:], tmp + [nums[i]], rst)


s = Solution()

print s.combinationSum3(2, 6)