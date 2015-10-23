class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        op = '+' # First operator should always be '+'
        rst = cur_res = 0
        i = 0
        
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1

                if op == '+': cur_res += num
                elif op == '-': cur_res -= num
                elif op == '*': cur_res *= num
                elif op == '/':
                    sign = -1 if cur_res < 0 else 1
                    cur_res = sign* (abs(cur_res) / num)

            else:
                if s[i] in '+-':
                    rst += cur_res
                    cur_res = 0
                    
                op = s[i]
                i += 1
        
        return rst + cur_res

s = Solution()
# print s.calculate("1*2-3/4+5*6-7*8+9/10")
print s.calculate("14-3/2")