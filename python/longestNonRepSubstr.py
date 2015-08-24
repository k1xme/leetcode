class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        
        n = len(s)
        start, end = 0, 0
        maxLen = 1
        showed = {}
        
        while end < n:
            
            if s[end] not in showed or showed[s[end]] < start:
                showed[s[end]] = end
                print end, start
                maxLen = max(end - start + 1, maxLen)
            else:
                start = showed[s[end]] + 1
                showed[s[end]] = end
            end += 1

        return maxLen

s = Solution()
print s.lengthOfLongestSubstring("eee")