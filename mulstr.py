class Solution(object):
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0': return '0'
        n1, n2 = len(num1), len(num2)
        rst = [0]*(n1+n2)
        for i in range(n1-1, -1, -1):
            
            for j in range(n2-1, -1, -1):
                product = rst[i+j+1] + int(num1[i])*int(num2[j])
                rst[i+j+1] = product%10
                rst[i+j] += product/10

        if rst[0] == 0: rst = rst[1:]
        return ''.join(map(lambda num: str(num), rst))

sol = Solution()
print sol.multiply("123", "456")