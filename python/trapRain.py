class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        if len(height) < 2: return 0
        stack = []
        i = 0
        n = len(height)
        rst = 0
        while i < n and height[i] == 0: i+= 1
        
        stack.append(i)
        i += 1
        while i < n:
            base = 0
            if height[i] >= height[stack[-1]]:
                while stack and height[stack[-1]] <= height[i]:
                    left = stack.pop()
                    rst += (i - left - 1)*(height[left] - base)
                    base = height[left]

            # Here is to handle the corner cases like: [4,2,3]
            if stack:
                rst += (i - stack[-1] - 1)*(min(height[stack[-1]], height[i]) - base)
            stack.append(i)
            i += 1
        
        return rst

sol = Solution()
print sol.trap([4,2,3])