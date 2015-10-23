class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quickSelect(start, end):
            pivot = nums[end]
            pivot_index = start
            
            for i in range(start, end):
                if nums[i] > pivot:
                    nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
                    pivot_index += 1
            
            nums[pivot_index], nums[end] = nums[end], nums[pivot_index]
            
            if pivot_index == k - 1: return nums[pivot_index]
            
            if pivot_index < k - 1: return quickSelect(pivot_index+1, end)
            
            return quickSelect(start, pivot_index-1)
            
        return quickSelect(0, len(nums)-1)

            
sol = Solution()
print sol.findKthLargest([2,1], 1)