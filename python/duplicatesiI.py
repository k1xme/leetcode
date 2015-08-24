# Bucket filtering
# The nums having the same quotient of n/t will be assigned to the same bucket
# or a closing one.

# Note: have to do the alignment first, since `nums` may contain neg.
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums or k < 1 or t < 0: return False
        
        base = -1 << 31
        buckets = {}
        n = len(nums)
        
        for i in range(n):
            reposNum = nums[i] - base
            bucket = reposNum / (t+1)
            
            if bucket in buckets or bucket-1 in buckets and \
               buckets[bucket-1] + t >= reposNum or \
               bucket+1 in buckets and buckets[bucket+1] - t <= reposNum:
                return True
            buckets[bucket] = reposNum
            
            if len(buckets) > k:
                firstBucket = (nums[i-k] + base)/(t+1)
                del buckets[firstBucket]
            
        return False

s = Solution()
print s.containsNearbyAlmostDuplicate([2,4], 1, 1)