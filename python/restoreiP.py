class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        if not s: return []
        if len(s) > 12: return []
        parts = [c for c in s]
        rst = []
        self._restoreIP(parts, 0, rst)
        return rst
        
    def _restoreIP(self, parts, start, rst):
        n = len(parts)

        if n == 4:
            rst.append(".".join(parts))
            return

        if start >= n-1: return
        
        if parts[start] != "0" and int(parts[start] + parts[start+1]) < 256:
            p = parts[:]
            p[start] = parts[start] + parts[start+1]
            del p[start+1]
            self._restoreIP(p, start, rst)
        
        self._restoreIP(parts[:], start+1, rst)

s = Solution()

print s.restoreIpAddresses("010010")