class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if not num1 or not num2: return ""
        
        n = len(num1)
        m = len(num2)
        product = [0]*(m+n)
        carry = 0
        rst = ""
        for i in range(n-1, -1, -1):
            carry = 0
            for j in range(m-1, -1, -1):
                product[i+j+1] += int(num1[i]) * int(num2[j]) + carry
                carry = product[i+j+1] / 10
                product[i+j+1] %= 10
            # why the carry should be added outside?
            product[i] += carry 
        
        i = 0
        while i < n+m:
            if product[i] != 0: break
            i+= 1
        else:
            return "0"

        for digit in product[i:]:
            rst += str(digit)
            
        return rst

s = Solution()
print s.multiply("9999", "0")