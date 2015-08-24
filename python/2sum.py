class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    
    def twoSum(self, nums, target):
        if not nums: return []
        
        index = {}
        n = len(nums)
        left, right = 0, n-1
        
        for i in xrange(n):
            index[nums[i]] = i + 1
        
        for i in xrange(n):
            diff = target - nums[i]
            if diff in index:
                return [i+1, index[diff]] if index[diff] > i + 1 else [index[diff], i+1]
            
        return []

s = Solution()

s.twoSum([3,2,4], 6)