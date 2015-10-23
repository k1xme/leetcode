class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        
        n = len(nums)
        if n == 1: return 0
        
        l, r = 0, n-1
        
        while l <= r:
            mid = (r-l)/2 + l

            if 0 < mid < n-1:
                if nums[mid+1] < nums[mid] > nums[mid-1]:
                    return mid
                if nums[mid] < nums[mid-1]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif mid == 0:
                if nums[mid] > nums[mid+1]: return 0
                l = mid + 1
            else:
                if nums[mid] > nums[mid-1]: return n-1
                r = mid - 1
        
        return -1

sol = Solution()
print sol.findPeakElement([1,2,3,2,1,2])r