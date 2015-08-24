class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix: return 0
        #printMatrix(matrix)
        rows = len(matrix)
        cols = len(matrix[0])

        # opt[i][j] is the are of the max square
        # whose lower-right corner is at (i,j).
        # WARN: never initialize the 2D array using the [[0]*m]*n!!!
        # Because every row will point to the same mem addr!!!
        opt = [[0 for m in xrange(cols)] for x in xrange(rows)]
        
        # Intialized the first row and first col
        opt[0][0] = 1 if matrix[0][0] == "1" else 0
        maxArea = opt[0][0]
        
        for col in xrange(1, cols):
            if matrix[0][col] == "1":
                maxArea = opt[0][col] = 1
                
            else: opt[0][col] = 0
        
        for row in xrange(1, rows):
            if matrix[row][0] == "1": 
                maxArea = opt[row][0] = 1
            else: opt[row][0] = 0

        for row in xrange(1, rows):
            
            for col in xrange(1, cols):
                if matrix[row][col] == "1":
                    upper = opt[row-1][col]
                    left = opt[row][col-1]
                    upperLeft = opt[row-1][col-1]
                    #print "row", row -1, "col",col - 1, upperLeft
                    opt[row][col] = min(upper, left, upperLeft) + 1
                    #print upper,left, upperLeft
                    #print "opt", opt[row][col],"row, col:", row, col
                else:
                    opt[row][col] = 0
                    #print "opt", opt[row][col],"row, col:", row, col

                if opt[row][col] > maxArea: maxArea = opt[row][col]
        
        return maxArea**2

def printMatrix(matrix):
    print "the OPT"
    for row in matrix:
        print row
s = Solution()
print s.maximalSquare(["1010","1011","1011","1111"])