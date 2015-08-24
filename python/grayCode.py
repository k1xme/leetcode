class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        if n == 0: return [0]
        
        codes = ["0", "1"]
        
        for i in range(1, n):
            tmpCodes = []
            for code in codes:
                tmpCodes.append("0"+code)
            for code in codes[::-1]:
                tmpCodes.append("1"+code)
            codes = tmpCodes
            print codes
        codes = map(lambda x: int(x, 2), codes)
        return codes

s = Solution()
print s.grayCode(3)