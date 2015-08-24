# First initialize a HashMap<string, int>(maybe use to store the current matching char index) with `words`.
# This HashMap has to be reset before we start to find the next matching substring.

# What if words is [].

# NOTE: There could be duplicates in `words`.
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if not s: return []
        
        wordLen = len(words[0])
        wordNum = len(words)
        n = len(s)
        wordsCount = {}
        result = []
        left = 0

        for word in words:
            if word not in wordsCount: wordsCount[word] = 0
            wordsCount[word] += 1
        
        while left <= n - wordNum*wordLen:
            foundWords = wordsCount.copy()
            right = left
            while right - left < wordNum*wordLen:
                word = s[right:right+wordLen]
                if word not in foundWords or foundWords[word] == 0: break
                right += wordLen
                foundWords[word] -= 1

            if right - left == wordNum*wordLen:
                result.append(left)
                left += 1
                continue
            left += wordLen
            
        return result

s = Solution()
print s.findSubstring("aaaaaaaa", ["aa","aa","aa"])