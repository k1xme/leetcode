#First, take O(n) to find the min and max. Then do a second pass keep shrinking the gap.
# gap = max(nums[pointer] - min, max-nums[pointer])

# No neg numbers.
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        if len(nums) < 2: return 0

        bucketMin = [(1<<31)-1] * (len(nums)-1)
        bucketMax = [-1] * (len(nums)-1)
        minNum, maxNum = nums[0], nums[0]
        
        # Find min and max
        for n in nums:
            minNum = min(n, minNum)
            maxNum = max(n, maxNum)

        gap = (maxNum-minNum-1)/(len(nums)-1)+1
        # Distribute nums into each bucket.
        for n in nums:
            # skip the min and max.
            if n == minNum or n == maxNum: continue
            bucketIndex = (n-minNum)/gap
            bucketMin[bucketIndex] = min(n, bucketMin[bucketIndex])
            bucketMax[bucketIndex] = max(n, bucketMax[bucketIndex])
        
        # Scan the gap between buckets to find max gap.
        maxGap = 0
        prevMax = minNum
        
        for i in range(len(nums)-1):
            if bucketMin[i] == (1<<31)-1: continue
            maxGap = max(bucketMin[i] - prevMax, maxGap)
            prevMax = bucketMax[i]
        
        return max(maxGap, maxNum-prevMax)
        
        
        
s = Solution()
print s.maximumGap([3,6,9,1])