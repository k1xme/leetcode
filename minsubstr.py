# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         if not s or not t or len(s) < len(t): return ''
        
#         char_count = {}
        
#         for c in t:
#             if c not in char_count: char_count[c] = 0
#             char_count[c] += 1
        
#         foundLetters = 0
#         found_count = {letter: 0 for letter in t}
#         minLen = 1 << 31
#         min_l = 0
#         l = 0
        
#         for r in range(len(s)):
#             letter = s[r]
#             if letter not in char_count: continue
            
#             found_count[letter] += 1
            
#             if found_count[letter] == char_count[letter]:
#                 foundLetters += 1
            
#             while foundLetters == len(char_count):
#                 if r - l + 1 < minLen:
#                     minLen = r-l+1
#                     min_l = l

#                 if s[l] in char_count:
#                     found_count[s[l]] -= 1
#                     if found_count[s[l]] < char_count[s[l]]: foundLetters -= 1
#                 l += 1

#         return s[min_l:min_l+minLen]


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t): return ''
        
        char_count = {}
        
        for c in t:
            if c not in char_count: char_count[c] = 0
            char_count[c] += 1
        
        foundLetters = 0
        found_count = {letter: 0 for letter in t}
        minLen = 1 << 31
        min_l = 0
        l = 0
        
        for r in range(len(s)):
            letter = s[r]
            if letter not in char_count: continue
            
            found_count[letter] += 1
            
            if found_count[letter] == char_count[letter]:
                foundLetters += 1
            
            while foundLetters == len(char_count):
                if r - l + 1 < minLen:
                    minLen = r-l+1
                    min_l = l

                if s[l] in char_count:
                    found_count[s[l]] -= 1
                    if found_count[s[l]] < char_count[s[l]]: foundLetters -= 1
                l += 1

        return s[min_l:min_l+minLen] if minLen < 1 << 31 else ''
                
            
sol = Solution()
print sol.minWindow("bdab","ab")