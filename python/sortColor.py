class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        if not nums: return
    
        zeroEnd = 0
        twoStart = len(nums) - 1
        i = 0
        while i <= twoStart:
            print i
            if nums[i] == 0:
                # Swap 0 to the left.
                nums[zeroEnd], nums[i] = nums[i], nums[zeroEnd]
                zeroEnd += 1
            if nums[i] == 2:
                nums[twoStart], nums[i] = nums[i], nums[twoStart]
                twoStart -=1
                continue
            i += 1

s = Solution()
a =[1,1,1]
s.sortColors(a)
print a