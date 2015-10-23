class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2: return s
        
        self.maxLen = 1
        self.subStr_l = 0
        def extend(pivot_l, pivot_r):
            while pivot_l >= 0 and pivot_r < len(s) and s[pivot_l] == s[pivot_r]:
                pivot_l -= 1
                pivot_r += 1
            cur_len = pivot_r-pivot_l-1
            if cur_len > self.maxLen:
                self.maxLen = cur_len
                self.subStr_l = pivot_l+1
        
        
        for i in range(len(s)):
            extend(i,i)
            extend(i,i+1)

        return s[self.subStr_l:self.subStr_l+self.maxLen]
            
            
sol = Solution()
print sol.longestPalindrome('bb')