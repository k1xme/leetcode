class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        if not buildings: return []

        rst = [[buildings[0][0], buildings[0][2]]]
        prev = buildings[0]

        for b in buildings[1:]:
            if b[0] > prev[1]:
                rst.append([prev[1], 0])
                rst.append([b[0], b[2]])
                prev = b
            elif b[2] > prev[2]:
                rst.append([b[0], b[2]])
                prev = b
            elif prev[1] <= b[1]:
                if b[2] != prev[2]: rst.append([prev[1], b[2]])
                prev = b
            else:
                print "here", b

        return rst

s = Solution()
print s.getSkyline([ [2,9,10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ])
print s.getSkyline([ [2,12,3], [3, 7, 2], [5, 10, 2], [6, 8, 1], [8, 12, 2] ])


