class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        rst = []
        m = len(matrix)
        n = len(matrix[0])
        rowStart, rowEnd = 0, m
        colStart, colEnd = 0, n
        
        while rowStart < rowEnd and colStart < colEnd:
            for col in range(colStart, colEnd):
                rst.append(matrix[rowStart][col])
            rowStart += 1

            for row in range(rowStart, rowEnd):
                rst.append(matrix[row][colEnd-1])
            colEnd -= 1
            
            if rowStart < rowEnd:
                for col in range(colEnd-1, colStart-1, -1):
                    rst.append(matrix[rowEnd-1][col])
                rowEnd -= 1
            
            for row in range(rowEnd-1, rowStart-1, -1):
                rst.append(matrix[row][colStart])
            colStart += 1
        
        return rst

s = Solution()
print s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print s.spiralOrder([[7],[9],[6]])
print s.spiralOrder([[1]])
print s.spiralOrder([[2,3,4]])