class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operators = []
        nums = []
        num = 0
        sign = 1
        # Return True if op1's order is lower than op2's
        def is_lower(op1, op2):
            if op1 in "+-": return op2 in "*/"
            return False
        
        def calculate(op, a, b):
            if op == "+": nums.append(a+b)
            elif op == "*": nums.append(a*b)
            else:
                sign = -1 if a*b < 0 else 1
                nums.append(sign*(abs(a)/abs(b)))
            
        for char in s:
            if char == " ": continue
            if char.isdigit():
                num = num*10 + int(char)
                continue
            else:
                nums.append(sign*num)
                num = 0
                sign = 1
            if char == "-":
                sign *= -1
                char = "+"
            else: sign = 1

            if len(nums) < 2 or is_lower(operators[-1], char):
                operators.append(char)
                continue
            
            pre_op = operators.pop()
            b,a = nums.pop(), nums.pop()
            calculate(pre_op, a, b)
            operators.append(char)
        
        nums.append(sign * num)

        while operators:
            b,a = nums.pop(), nums.pop()
            op = operators.pop()
            calculate(op, a, b)
            
        return nums.pop()

s = Solution()
# print s.calculate("1*2-3/4+5*6-7*8+9/10")
print s.calculate("1-1-1")