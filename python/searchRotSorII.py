class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            while left+1 < right and nums[left] == nums[left+1]: left += 1
            while left < right-1 and nums[right] == nums[right-1]: right -= 1
            if right > left and nums[right] == nums[left]: right -= 1
            mid = (right-left)/2 + left
            
            if nums[mid] == target: return True
            if nums[mid] > target:
                if nums[mid] >= nums[left] and target >= nums[left]: right = mid - 1
                else: left = mid + 1
            else:
            	
                if nums[mid] <= nums[right] and target <= nums[right]:
                	left = mid + 1
                else: right = mid - 1
        return False



sol = Solution()
print sol.search([0,0,1,1,2,0],2)

        