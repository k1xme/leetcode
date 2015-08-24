class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid: return 0
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        paths = []
        
        # initialize the result matrix.
        for i in range(rows): paths += [[0]*cols]
        if obstacleGrid[0][0] == 0: paths[0][0] = 1
        else: paths[0][0] = 0 
        # EDGE CASE: [[1,0]]. It's possible that there is a 1 before 0.
        for i in range(1,rows):
            if obstacleGrid[i][0] == 0:
                paths[i][0] = paths[i-1][0]
            else: paths[i][0] = 0

        for i in range(1,cols):
            if obstacleGrid[0][i] == 0:
                paths[0][i] = paths[0][i-1]
            else: paths[0][i] = 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    continue
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        
        return paths[rows-1][cols-1]
s = Solution()

print s.uniquePathsWithObstacles([[0,0]])