# Store the sum of power ups in each path and the min initial to reach each cell in the path.
# Have to deal with 2 situations:
# 1. Cell with demons - accumulate abs(cell-value) to min initial health, then subtract it the powerups collected along the sub optimal path.
# 2. Cell with Powerups - accumulate the powerups to the sum of powerups, keep min intial health.

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        for row in xrange(m):
            for col in xrange(n):

                if row == 0 and col == 0: subOPT = (0, 0)
                elif row == 0: subOPT = dungeon[row][col-1]
                elif col == 0: subOPT = dungeon[row-1][col]
                elif sum(dungeon[row-1][col]) > sum(dungeon[row][col-1]):
                    if dungeon[row-1][col][0] > dungeon[row][col-1][0]:
                        subOPT = dungeon[row-1][col]
                    else:
                        subOPT = dungeon[row][col-1]
                else:
                    if dungeon[row-1][col][0] > dungeon[row][col-1][0]:
                        subOPT = dungeon[row][col-1]
                    else:
                        subOPT = dungeon[row-1][col]
                newHealth = subOPT[0] + dungeon[row][col] + subOPT[1]
                if dungeon[row][col] < 0:
                    dungeon[row][col] = (min(newHealth, 0), max(newHealth, 0))
                    continue
                dungeon[row][col] = (subOPT[0], dungeon[row][col] + subOPT[1])
        # print dungeon
        return 1-dungeon[m-1][n-1][0]

# sol = Solution()
# sol.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]])
# sol.calculateMinimumHP([[3,-20,30],[-3,4,0]])