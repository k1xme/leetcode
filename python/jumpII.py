# The strategy is the same as we do Jump Game I.
# We choose the next jump according to the max cover range, which is max(all(nextIndex+nums[nextIndex])).
# Keep counting in every loop.
# TC: O(n)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if not nums or len(nums)==1: return 0
        
        jumps = 0
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] + i >= n-1: return jumps+1
            if nums[i] == 0: return 0
            maxRange = 0
            nextIndex = i+1
            for p in range(i+1, i + nums[i]+1):
                if p < n-1 and p + nums[p] >= maxRange:
                    maxRange = p+nums[p]
                    nextIndex = p
            i = nextIndex
            jumps += 1
        
        return jumps

s = Solution()

print s.jump([1,2,1,1,1])