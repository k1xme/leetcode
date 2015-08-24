class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        if n == 0: return []
        rst = []
        self.placeQueen(0, n, [], rst, [False]*n)
        return rst

    def placeQueen(self, row, n, board, rst, colUsed):
        if row == n:
            rst.append(board)
            return
        
        for i in range(n):
            if colUsed[i]: continue
            colUsed[i] = True
            if self.canPlace(row, i, n, board):
                board.append("."*i + "Q" + "."*(n-1-i))
                self.placeQueen(row+1, n, board[:], rst, colUsed)                
                board.pop()

            colUsed[i] = False
        
        
    def canPlace(self, row, col, n, board):
        if row > 0 and col < n -1 and board[row-1][col+1] == "Q": return False
        if row > 0 and col > 0 and board[row-1][col-1] == "Q": return False
        return True

s = Solution()
print s.solveNQueens(4)