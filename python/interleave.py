# Recursive version: from the end to the head.
# if s3[end] == s2[end] == s1[end]: return isInterleave(s1[:-1], s2, s3[:-1]) or isInterleave(s1, s2[:-1], s3[:-1]).
# elif s3[end] == s2[end]: return isInterleave(s1, s2[:-1], s3[:-1])
# elif s3[end] == s1[end]: return isInterleave(s1[:-1], s2, s3[:-1])
# else: return False
import pprint
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        n, m, k = len(s1), len(s2), len(s3)
        if k != m+n: return False

        # 2D (n+1)*(m+1) array holding solution to sub problems.        
        opt = [[False]*(m+1) for i in range(n+1)]
        
        # Initialize 2d array.
        opt[0][0] = True
        for i in range(1, m+1): opt[0][i] = s2[:i] == s3[:i]
        for i in range(1, n+1): opt[i][0] = s1[:i] == s3[:i]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s3[i+j-1] == s1[i-1] == s2[j-1]:
                    opt[i][j] = opt[i-1][j] or opt[i][j-1]
                elif s3[i+j-1] == s2[j-1]: opt[i][j] = opt[i][j-1]
                elif s3[i+j-1] == s1[i-1]: opt[i][j] = opt[i-1][j]
        
        return opt[n][m]

    def _isInterleave(self, s1, s2, s3):
        n, m, k = len(s1), len(s2), len(s3)
        if k != m+n: return False
        if not s3: return True
        if not s1: return s2 == s3
        if not s2: return s1 == s3
        
        if s3[-1] == s2[-1] == s1[-1]:
            return self.isInterleave(s1[:-1], s2, s3[:-1]) or self.isInterleave(s1, s2[:-1], s3[:-1])
        elif s3[-1] == s2[-1]: return self.isInterleave(s1, s2[:-1], s3[:-1])
        elif s3[-1] == s1[-1]: return self.isInterleave(s1[:-1], s2, s3[:-1])
        
        return False

            
s = Solution()
print s.isInterleave("baababbabbababbaaababbbbbbbbbbbaabaabaaaabaaabbaaabaaaababaabaaabaabbbbaabbaabaabbbbabbbababbaaaabab", "aababaaabbbababababaabbbababaababbababbbbabbbbbababbbabaaaaabaaabbabbaaabbababbaaaababaababbbbabbbbb", "babbabbabbababbaaababbbbaababbaabbbbabbbbbaaabbabaababaabaaabaabbbaaaabbabbaaaaabbabbaabaaaabbbbababbbababbabaabababbababaaaaaabbababaaabbaabbbbaaaaabbbaaabbbabbbbaaabaababbaabababbbbababbaaabbbabbbab")