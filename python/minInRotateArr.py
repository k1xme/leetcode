class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if len(nums) == 1 or nums[-1] > nums[0]: return nums[0]
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (r-l)/2 + l

            if nums[r] < nums[l]:
                if nums[mid] > nums[r]: l = mid+1
                else: r = mid
            else: return nums[l]


s = Solution()
print s.findMin([5,1,2,3,4])