class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t or abs(len(s)-len(t)) > 1: return False
        
        # Equal length, so check if 2 strs are just different in 1 char.
        if len(s) == len(t):
            for i in range(len(t)):
                if s[i] != t[i]:
                    return s[i+1:] == t[i+1:]
        
        # Otherwise we check if add or remove a char can make them equal.
        for i in range(min(len(t), len(s))):
            if s[i] == t[i]:
                continue
            if len(s) < len(t):
                return s[i:] == t[i+1:]
            
            return s[i+1] == t[i:]
        
        return True
        
        
            
sol = Solution()
sol.isOneEditDistance("cab", "ab")