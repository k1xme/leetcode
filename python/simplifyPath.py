class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        if not path: return ""
        sep = "/"
        splitted = path.split(sep)

        stack = []
        for comp in splitted:
            if not comp: continue
            if comp == "..": 
                if stack: stack.pop()
            elif comp == ".": continue
            else: stack.append(comp)

        if not stack: return sep

        return sep + sep.join(stack)

s = Solution()
print s.simplifyPath("/./abc")