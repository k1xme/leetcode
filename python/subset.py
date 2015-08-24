# Need to sort the array first?

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if not nums: return []
        
        nums = sorted(nums)
        
        rst = []
        n = len(nums)
        end = 0
        # compute the last subset bits.
        for i in xrange(n):
            end = (end << 1) + 1
        
        i = 0
        
        while i <= end:
            subset = []
            
            if i > 0:
                mask = 1
                for j in xrange(n):
                    
                    exist = mask & i
                    
                    if exist > 0: subset.append(nums[j])
                    mask = mask << 1
            
            rst.append(subset)
            i += 1
        
        return rst


s = Solution()
print s.subsets([1,2])