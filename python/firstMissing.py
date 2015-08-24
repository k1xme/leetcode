class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        if not nums: return 1
        n = len(nums)
        
        # swap positives to correct positions
        for i in range(n):
            while nums[i] > 0 and nums[nums[i]-1] != nums[i] and nums[i] != i+1:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(n):
            if nums[i] != i+1: return i+1

        return n+1

s = Solution()
print s.firstMissingPositive([3,4,-1,1])