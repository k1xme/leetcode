class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        if not s: return []
        rst = []
        if not self.canBreak(s,wordDict): return rst
        self._wordBreak(s, 0, 1, wordDict, "", rst)
        return rst
        
    def _wordBreak(self, s, start, end, wordDict, path, rst):
        if start >= len(s):
            rst.append(path[:-1])
            return

        while end <= len(s):
            if s[start:end] in wordDict:
                self._wordBreak(s, end, end+1, wordDict, path+s[start:end]+" ", rst)
            end += 1

    def canBreak(self, s, wordDict):
        opt = [False] * len(s)
        opt[0] = True if s[0] in wordDict else False

        for i in range(1, len(s)):
            if s[:i+1] in wordDict:
                opt[i] = True
                continue

            for j in range(i, -1, -1):
                if opt[j-1] and s[j:i+1] in wordDict:
                    opt[i] = True
                    break
        return opt[-1]

s = Solution()
print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])