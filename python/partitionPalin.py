class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        rst = []

        self._dfs(s,"", [], rst)
        return rst
    
    def _isPalindrome(self, s):
        if not s: return True
        
        n = len(s)
        l, r = 0, n-1
        
        while l < r:
            if s[l] != s[r]: return False
            
            l += 1
            r -= 1
        
        return True
    
    def _dfs(self, s, path, partition, rst):
        if not s:
            if path:
                partition.append(path)
                rst.append(partition)
            return
        n = len(s)
        
        if self._isPalindrome(path+s[0]):
            if n>1: self._dfs(s[1:], "", partition+[path+s[0]], rst)
            else: rst.append(partition+[path+s[0]])
        
        if n > 1: self._dfs(s[1:], path+s[0], partition, rst)


s = Solution()
print s.partition("aab")