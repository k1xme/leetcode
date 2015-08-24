# The basic idea is like K Merge. We can achieve O(k), O(k) space.
# Alternative is to use PriorityQueue, which takes O(klgk), O(k) space.

class Solution:
    """
    @param k: The number k.
    @return: The kth prime number as description.
    """
    def kthPrimeNumber(self, k):
        i3 = i5 = i7 = 0
        count = 1
        uglyNum = 1
        uglyNums = [1]
        uglynum_3, uglynum_5, uglynum_7 = 3, 5, 7
        
        for i in xrange(1,k+1):
            uglyNum = min(uglynum_3, uglynum_5, uglynum_7)
            uglyNums.append(uglyNum)

            if uglyNum == uglynum_3:
                i3 += 1
                uglynum_3 = uglyNums[i3] * 3
            
            if uglyNum == uglynum_5:
                i5 += 1
                uglynum_5 = uglyNums[i5] * 5
            
            if uglyNum == uglynum_7:
                i7 += 1
                uglynum_7 = uglyNums[i7] * 7
        
        return uglyNum

s = Solution()
print s.kthPrimeNumber(321)