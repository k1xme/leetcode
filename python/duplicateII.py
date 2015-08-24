class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) < 2 or k < 2: return False
        # Maintain a window of size k.
        window = {}
        
        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window[nums[i]] = True
            print i
            if len(window) > k+1:
                del window[nums[i-k]]
        
        return False

s = Solution()
print s.containsNearbyDuplicate([1,1], 1)