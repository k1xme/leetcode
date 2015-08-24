# Backtracking is relatively easy.
# Another solution will be DP.

# Question: what if p is a empty string?
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        pn = len(p)
        sn = len(s)
        pi, si = 0, 0
        pRetrack, sRetrack = -1, -1

        while si < sn:
            if pi < pn and (p[pi] == "?" or p[pi] == s[si]):
                pi, si = pi+1, si+1
                continue
            if pi < pn and p[pi] == "*":
                pi+=1
                pRetrack = pi
                sRetrack = si+1
                continue
            # No retracking point.
            if pRetrack > -1:
                pi = pRetrack
                si = sRetrack
                sRetrack += 1
                continue
            return False

        while pi < pn and p[pi] == "*": pi+=1
        return pi == pn



s = Solution()
print s.isMatch("aaasdsdsd", "a*d")