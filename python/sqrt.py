# Binary seach to find the number.
# TC: O(lgn)
# KEY: when to stop the loop?
class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 1: return 1
        l = 1
        rst = 1
        r = x
        mid = (l+r)/2
        while l < r:
            if mid == x/mid:
                return mid
            elif mid < x/mid:
                l += 1
            else:
                r = mid
                
        return rst

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0
        low = 1
        high = x
        mark = 1
        while low != high - 1:
            mid = (high + low) / 2
            if mid * mid > x:
                high = mid
            elif mid * mid < x:
                mark = mid
                low = mid
            else:
                return mid
        return mark

s = Solution()
print s.mySqrt(3)