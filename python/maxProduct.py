class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if len(nums) == 1: return nums[0]
        neg = [1]*len(nums)
        pos = [1]*len(nums)
        if nums[0] > 0: pos[0] = nums[0]
        else: neg[0] = nums[0]
        rst = nums[0]
        for i in range(1, len(nums)):
            pos[i] = max(pos[i-1]*nums[i], nums[i], neg[i-1]*nums[i])
            neg[i] = min(neg[i-1]*nums[i], nums[i], pos[i-1]*nums[i])
            rst = max(pos[i], rst)
        print pos, neg

        return rst

s = Solution()
print s.maxProduct([2,-1,1,1])