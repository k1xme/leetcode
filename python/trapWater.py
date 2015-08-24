class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        if not height: return 0
        
        n = len(height)
        l, r = 0, 1
        stack = []
        rst = 0

        while r < n:
            if height[l] > height[r]:
                stack.append(l)
                l = r
            elif stack:
                base_height = height[l]
                l = stack.pop()
                total = min(height[r]-base_height, height[l]-base_height)*(r-l-1)
                rst += 1
            else:
                l = r
            r += 1

        return rst

s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])


        