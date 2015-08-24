class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if len(nums) < 2 or k == 0: return
        self.reverse(nums, 0, len(nums)-1)
        print nums
        self.reverse(nums, 0, k)
        print nums
        self.reverse(nums, k+1, len(nums)-1)
        print nums
    
    def reverse(self, nums, s, e):
        e = min(len(nums)-1, e)
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

s = Solution()
s.rotate([1,2], 1)