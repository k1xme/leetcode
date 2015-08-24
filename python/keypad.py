# what about the number key that doesn't represent any letter.
# do it in recursion is easy.
# can we do it in a iterative fashion?

class Solution:
    keypad = { '2': ['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
               '5': ['j','k','l'], '6': ['m','n', 'o'], '7': ['p','q', 'r','s'],
               '8':['t','u','v'], '9':['w','x','y','z']}

    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if not digits: return []
        return self._letterCombinations(digits, "", [])
        
    def _letterCombinations(self, digits, comb, result):
        if not digits:
            result.append(comb)
            return result
        
        d = digits[0]
        if d in self.keypad:
            letters = self.keypad[d]
        else:
            self._letterCombinations(digits[1:], comb, result)
        
        for letter in letters:
            result = self._letterCombinations(digits[1:], comb+letter, result)
        
        return result

s = Solution()

print s.letterCombinations("23")