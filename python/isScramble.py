# Iterative solution comes first.
# Note: by "partitioning it into a binary tree" doesn't necessarily mean "partitioning it by half".
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2, visited):
        print s1, s2
        if (s1, s2) in visited: return visited[(s1,s2)]
        n = len(s1)
        if n == 1:
            return s1 == s2
        if n == 2: 
            return s1 == s2 or s1[0] == s2[1] and s1[1] == s2[0]
        
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i], visited) and self.isScramble(s1[i:], s2[i:], visited)) or \
               (self.isScramble(s1[:i], s2[-i:], visited) and self.isScramble(s1[i:], s2[:-i], visited)):
               visited[(s1, s2)] = True
               return True

        visited[(s1, s2)] = False
        print visited
        return False




s = Solution()
print s.isScramble("abb", "bab", {})