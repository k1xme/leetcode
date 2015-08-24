# Divide and Conquer?
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if not s or len(s) == 1: return s
        
        n = len(s)
        start = 0
        maxlen = 1
        for i in xrange(n):

            # find odd-length palindrome centered at i.
            low = i - 1
            high = i + 1
            while low >= 0 and high < n:

                if s[low] == s[high]:
                    if high - low + 1 > maxlen:
                        start = low
                        maxlen = high - low + 1 
                        
                    low -= 1
                    high += 1
                else: break
            # find even-length palindromes
            low = i
            high = i+1
            while low >= 0 and high < n:
                if s[low] == s[high]:
                    if high - low + 1 > maxlen:
                        start = low
                        maxlen = high - low + 1 
                        
                    low -= 1
                    high += 1
                else: break
            
        return s[start: start + maxlen]

s = Solution()
a = s.longestPalindrome("ccc")
print a