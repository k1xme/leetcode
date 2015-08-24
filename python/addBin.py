class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        if not a: return b
        if not b: return a
        
        ai, bi = len(a)-1, len(b)-1
        rst = ""
        carry = 0
        
        while ai >= 0 and bi >= 0:
            sum = int(a[ai]) + int(b[bi]) + carry
            carry = sum >> 1
            sum %= 2
            rst = str(sum) + rst
            bi -= 1
            ai -=1
        
        remaini = ai if ai >= 0 else bi
        remain = a if a > 0 else b
        
        while remaini >=0:
            sum = int(remain[remaini]) + carry
            carry = sum >> 1
            sum %= 2
            rst = str(sum) + rst
            remaini -= 1
        
        return rst if carry == 0 else "1" + rst
            
            

s = Solution()
print s.addBinary("11", "1")