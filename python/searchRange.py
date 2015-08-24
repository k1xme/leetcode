# Find the starting index and ending index of the target number. E.G. find a bunch of targets.

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        l, r = 0, len(nums)-1
        
        def search(left, right):
            if left > right: return [-1, -1]
            if left == right: return [left, right] if nums[left] == target else [-1, -1]
            mid = (right-left)/2 + left
            if nums[mid] == target:
                ret = [mid, mid]
                lr = search(left, mid-1)
                rr = search(mid+1, right)
                if lr[0] != -1: ret[0] = lr[0]
                if rr[1] != -1: ret[1] = rr[1]
                return ret
            elif nums[mid] < target: return search(mid+1, right)
            return search(left, mid-1)
        
        return search(l, r)
    

s = Solution()
print s.searchRange([5,7,8,8], 8)        