class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if not nums: return False
        
        n = len(nums)
        i = 0
        
        while i < n:
            if i + nums[i] >= n - 1:
                return True
            if nums[i] == 0:
                return False
            # find the max cover.
            step = 1
            nextPos = i + 1
            nextSpan = 0
            while step <= nums[i]:

                if i + step + nums[i+step] > nextSpan:
                    nextPos = i + step
                    nextSpan = i + step + nums[i+step]

                step += 1
            
            i = nextPos
            if i >= n -1: return True
            
        return False

s = Solution()
print s.canJump([2,5,0,0])