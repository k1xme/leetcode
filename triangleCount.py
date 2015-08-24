# Already got the idea... but still have some minor bugs!!!!!SHIT!!!!
# Think carefully about the corner cases!!!
# Problems related to kSUm should have sort the array first!!!!
# And find the conditions between each iteration.

class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        if len(S) < 3: return []
        
        count = 0
        n = len(S)
        S.sort()

        for i in xrange(n-2):
            left = i+1
            right = left + 1
            pre_count = 0
            while left < n:
                while right < n and S[left] + S[i] > S[right]: right += 1
                count += right - left - 1
                left += 1

        return count

s = Solution()
print s.triangleCount([8990,3146,9568,3889,7253,7395,10032,6179,1299,8738,1315,1280,830,6593]
)