# Find the pivot first in O(lgn). Then compare target with the max min of both parts.
# Choose one part to do Binary Search.
# Total: O(lgn)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums: return -1
        n = len(nums)
        # Find pivot.
        low, high = 0, n -1
        pivot = 0
        while low < high:
            pivot = (high + low)/2
            if nums[pivot] < nums[high]: high = pivot
            else: low = pivot + 1

        if target == nums[low]: return low
        if target < nums[low]: return -1

        pivot = low
        low,high = 0, n-1

        while low <= high:
            mid = (high + low)/2

            realmid = (mid + pivot)%n

            if nums[realmid] == target: return realmid
            if nums[realmid] > target:
                high = mid-1
            else:
                low = mid + 1

        return -1

s = Solution()
a = [5,1,3]
print s.search(a,1)
