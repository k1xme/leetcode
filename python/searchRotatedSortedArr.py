
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        
        n = len(nums)
        l, r = 0, n-1
        
        while l <= r:
            mid = (r-l)/2 + l
            
            if nums[mid] == target: return mid
            if nums[mid] > target:
                if nums[mid] <= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid -1
        
        return -1
        
        

s = Solution()
a = [3,1]
# print s.search([8,9,2,3,4],9)
print s.search([1,3], 3)
