class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums: return 0
        if len(nums) == 1: return 1
        
        n = len(nums)
        
        left, right = 0, 1
        rst = 0
        
        while right < n:
            if nums[left] != nums[right]:
                count = right - left if right - left < 3 else 2
                rst += count
                left += count
                nums[left:] = nums[right:]
                right = left + 1
                n = len(nums)
            else:
                right += 1

        rst += right - left if right - left < 3 else 2
        return rst

s = Solution()
print s.removeDuplicates([1,1,1])