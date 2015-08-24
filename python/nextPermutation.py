# When the permutation is the largest one, then we just sort it in ascending order.
# Otherwise, we should 

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if not nums: return
        
        n = len(nums)
        
        # Find the "Peak".
        peak = n - 1
        
        while peak > 0:
            if nums[peak] > nums[peak-1]: break
            peak -= 1
        
        if peak == 0:
            nums.sort()
            return
        
        i = n - 1
        while i >= peak:
            if nums[i] > nums[peak-1]:
                nums[peak-1], nums[i] = nums[i], nums[peak-1]
                break
            i -= 1
        print peak
        part = nums[peak:]
        part.sort()
        nums[peak:] = part

a = [1,3,2]
s = Solution()
s.nextPermutation(a)
print a