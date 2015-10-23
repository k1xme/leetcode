# First initialize a HashMap<string, int>(maybe use to store the current matching char index) with `words`.
# This HashMap has to be reset before we start to find the next matching substring.

# What if words is [].

# NOTE: There could be duplicates in `words`.
# Edge cases: "barfoofoosxxxx", ["bar", "foo"]

# Edge cases: "barfoofoosxxxx", ["bar", "foo"]

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words : return []
        
        wordLen = len(words[0])
        wordNum = len(words)
        
        n = len(s)
        if n < wordLen * wordNum: return []
        
        rst = []
        wordsToFind = {}
        wordsFound = {}
        for word in words:
            if word not in wordsToFind: wordsToFind[word] = 1
            else: wordsToFind[word] += 1
        
        l = 0
        r = l + wordLen

        while l < n - wordLen*wordNum + 1:
            word = s[r-wordLen:r]
            
            if word not in wordsToFind:
                l = r - wordLen + 1
                r += 1
                wordsFound = {}
                continue
            
            if word not in wordsFound: wordsFound[word] = 1
            else: wordsFound[word] += 1
            
            if wordsFound[word] > wordsToFind[word]:
                wordsFound = {}
                l += 1
                r = l + wordLen
                continue
            
            if r - l == wordNum*wordLen:
                rst.append(l)
                wordsFound = {}
                l += 1
                r = l + wordLen
                continue
            r += wordLen
        return rst



s = Solution()
print s.findSubstring("aaaaaaaa" ,["aa","aa","aa"])
print s.findSubstring("ababaab" ,["ab","ba","ba"])
print s.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"])