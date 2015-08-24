class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums: return ""
        
        def largest_high_pos(x, y):
            x = str(x)
            y = str(y)
            xi, yi = 0, 0
            end = min(len(x), len(y))
            while xi < end:
                if x[xi] > y[yi]: return 1
                if x[xi] < y[yi]: return -1
                xi += 1
                yi += 1
                
            
            if xi < len(x): return -1
            if yi < len(y): return 1
            return 0
        
        nums = sorted(nums, cmp=largest_high_pos, reverse=True)
        return reduce(lambda x, y: x+y, map(lambda x: str(x), nums), "")

s = Solution()
print s.largestNumber([3, 30, 34, 5, 9])