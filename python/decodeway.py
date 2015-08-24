class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s or s[0] == "0": return 0
        
        n = len(s)
        opt = [0]*n
        opt[0] = 1
        
        for i in range(1, n):

            num = int(s[i-1:i+1])

            if "0" < s[i] <= "9" and 9 < num < 27: 
                tmp = opt[i-2] if i > 1 else 1
                opt[i] = opt[i-1] + tmp
            elif s[i] == "0" and ( num < 10 or num > 26): 
                return 0
            elif 9 < num < 27: opt[i] = opt[i-2] if i > 1 else 1
            else: opt[i] = opt[i-1]
        print opt
        return opt[n-1]

s = Solution()
print s.numDecodings("1212")
# 1, 2, 1, 2 or 12, 1, 2 or 1, 21, 2 or 1,2,12