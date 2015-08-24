class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea():
        if not height: return 0

        AREA = lambda l, r: (r-l+1)*min(height[l:r+1])
        n = len(height)
        l, r = 0, 1
        rst = AREA(l, r)

        while r < n and l <= r:
           j8 

    def _largestRectangleArea(self, height):
        if not height: return 0
        
        n = len(height)
        l, r = 0, n-1
        rst = 0
        
        while l <= r:
            rect = (r-l+1)*min(height[l:r+1])
            if rect > rst: rst = rect
            
            if height[l] < height[r]:
                prevL = l
                l += 1
                while height[l] < height[prevL]:
                    l+=1
            else:
                prevR = r
                r -= 1
                while height[r] < height[prevR]:
                    r -= 1
        return rst


s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3])
            