#!/usr/bin/python
def balance(s):
    rst = ''
    stack = []
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
    print stack
    for i in range(len(s)-1, -1, -1):
        if s[i] == ')' and stack:
            open_bracket = stack.pop(0)
            if open_bracket < i:
                rst = '(' + rst + ')'
    
    print rst
    
balance(')(())(')
balance('(()()(')
balance("())())))()()")

