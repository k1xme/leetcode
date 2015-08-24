 # Rotate the matrix layer by layer. Every time we just rotate the outer layer.

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        if not matrix: return
        
        n = len(matrix)
        layers = n/2

        for l in xrange(layers):
            print l
            for i in xrange(n-l*2-1):
                tmp = matrix[l][l+i]

                # Swap the elems
                matrix[l][l+i] = matrix[n-l-i-1][l]
                matrix[n-l-i-1][l] = matrix[n-l-1][n-l-i-1]
                matrix[n-l-1][n-l-i-1] = matrix[l+i][n-l-1]
                matrix[l+i][n-l-1] = tmp
            printMatrix(matrix)
        
def printMatrix(matrix):
    print "REGIONS"
    for row in matrix:
        print row

s = Solution()
s.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])