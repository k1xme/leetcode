# Use 2 stacks: operators and operands. Generate a Reverse Polish Notation.
# No need to consider parenthesis, since there is no "*" "/" operators.
# TC: O(n). SC: O(n)

# QUESTIONS: will there be spaces?
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = []
        sign = 1
        num = 0
        rst = 0
        
        for c in s:
            print rst, sign, nums
            if c.isdigit():
                num = num*10 + int(c)
                continue
            rst += sign*num
            num = 0
            
            if c == "-": sign = -1
            elif c == "(":
                nums.append(rst)
                nums.append(sign)
                sign = 1
                rst = 0
            elif c == ")":
                rst *= nums.pop()
                rst += nums.pop()
            elif c == "+": sign = 1
        rst += sign * num
        return rst
            
                
s = Solution()
print s.calculate("1")
# print s.calculate("2-4-(8+2-6+(8+4-(1)+8-10))")