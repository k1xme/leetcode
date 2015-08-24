# Scan the string from the head to the end, keep a array opt[] storing
# the length of string that can be segmented by the dicts. For each
# pos i, try if s[opt[i-1]:i+1] is in the dict, if so opt[i] = i+1.
# Else, keep try s[opt[opt[i-1]-1]:i+1] until opt[i-1] == 0, if we still
# can increase the length, opt[i] = opt[i-1].
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not wordDict: return False
        if not s: return True
        
        s_len = len(s)
        opt = [0] * s_len
        # initialized the first entry.
        opt[0] = 1 if s[0] in wordDict else 0

        for i in range(1, s_len):
            opt[i] = opt[i-1]
            if s[:i+1] in wordDict: opt[i] = i+1
            else:
                for start in range(opt[i]):
                    if s[opt[start]:i+1] in wordDict:
                        opt[i] = i + 1
                        break
        rst = []
        self.backTrack(s, wordDict, opt, 0, [], rst)
        print rst
        return opt[s_len - 1] == s_len
        
    def backTrack(self, s, wordDict, opt, start, cur, rst):
        if start == len(s):
            rst.append(" ".join(cur))
            return

        for i in range(start, len(s)):
            if s[start: i+1] in wordDict:
                cur.append(s[start:i+1])
                self.backTrack(s, wordDict, opt, i+1, cur, rst)
                cur.pop()
        

s = Solution()
# EDGE CASE: 
#print s.wordBreak("abcd", ["a","abc", "cd", "b"])
#print s.wordBreak("icecream", ["ice","icecream"])
print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
# print s.wordBreak("dogs", ["dog","s","gs"])
                