class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix: return []
        
        rowNum = len(matrix)
        colNum = len(matrix[0])
        colStart, colEnd = 0, colNum - 1
        rowStart, rowEnd = 0, rowNum - 1
        rst = []

        # The upper bound of layer is colNum/2 - 1.
        while colStart <= colEnd and rowStart <= rowEnd:
            # Output first row in this layer.
            
            for i in range(colStart, colEnd+1):
                rst.append(matrix[rowStart][i])
            rowStart += 1

            for i in range(rowStart, rowEnd+1): rst.append(matrix[i][colEnd])
            colEnd -= 1
            
            if colEnd < colStart or rowEnd < rowStart: break
            for i in range(colEnd, colStart-1, -1):

                rst.append(matrix[rowEnd][i])
            rowEnd -= 1
            
            for i in range(rowEnd, rowStart-1, -1):
                rst.append(matrix[i][colStart])
            colStart += 1

        return rst
    def _spiralOrder(self, matrix):
        if not matrix: return []
        n = len(matrix)
        m = len(matrix[0])
        layer = (n+1) >> 1
        rst = []
        for i in range(layer):
            for j in range(i, n-i-1): rst.append(matrix[i][j])
            for j in range(i, n-i-1): rst.append(matrix[j][n-i-1])
            for j in range(i, n-i-1): rst.append(matrix[n-i-1][n-j-1])
            for j in range(i, n-i-1): rst.append(matrix[n-j-1][i])
                
        return rst
s = Solution()

print s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print s.spiralOrder([[7],[9],[6]])
print s.spiralOrder([[1]])
print s.spiralOrder([[2,3,4]])