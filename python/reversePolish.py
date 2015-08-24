# scan the tokens from left to right, if the char is a nuber, push it to the stack
# else pop 2 numbers from the stack and do the calculation.

# key, how to handle negative number.

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        if not tokens:
            return 0
        
        stack = []
        
        for token in tokens:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                tmp = a + b
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                tmp = b - a
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                tmp = abs(b) / abs(a)
                if a * b < 0: tmp = -tmp
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                tmp = a * b
            else: tmp = int(token)
            stack.append(tmp)
        
        return stack.pop()

s = Solution()
t = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] 
print s.evalRPN(t)
t = ["10", "6", "-132", "/", "*", "17", "+"]
print s.evalRPN(t)