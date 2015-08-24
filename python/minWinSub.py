# Duplicates ?
from collections import defaultdict
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        if not s or not t: return ""
        
        window = {}
        head = tail = 0
        foundNum = 0 # The number of the chars in T found in the current window.
        minWin = (1 << 31) - 1
        rst = ""
        # initialize.
        for c in t:
            if c in window: window[c] -= 1
            else: window[c] = -1
        
        while tail < len(s):
            if s[tail] in window:
                window[s[tail]] += 1
                foundNum += 1 if window[s[tail]] <= 0 else 0
            tail += 1

            # We got a valid substring window, so start to minimize
            # the window by advancing `head` without breaking the validity.
            if foundNum >= len(t):
                while s[head] not in window or window[s[head]] > 0:
                    if s[head] in window:
                        window[s[head]] -= 1
                        foundNum -= 1 if window[s[head]] < 0 else 0
                    head += 1

                if tail - head <= minWin:
                    minWin = tail - head
                    rst = s[head: tail]

        return rst

    def _minWindow(self, s, t):
        if not s or len(t) > len(s): return ""
        
        window = {}
        l = r = found = 0
        minLen = (1 << 31) - 1
        rst = ""
        # initialize
        for c in t:
            if c not in window: window[c] = 0
            window[c] -= 1
        
        while r < len(s):
            if s[r] in window:
                window[s[r]] += 1
                found += 1 if window[s[r]] == 0 else 0
            
            if found == len(window):
                while (s[l] not in window or window[s[l]] > 0):
                    if s[l] in window: window[s[l]] -= 1
                    l += 1
            
                if r-l+1 < minLen:
                    print l,r
                    minLen = r-l+1
                    rst = s[l: r+1]
                
                window[s[l]] -= 1
                l += 1
                found -= 1
                
            r += 1

        return rst
                
                
        
        
        
        
s = Solution()
print s._minWindow("acbbaca", "aba")