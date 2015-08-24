class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        # scan the whole board to record numbers appeared.
        if not board: return
        self.rows = [[False] * 9 for i in xrange(9)]
        self.cols = [[False] * 9 for i in xrange(9)]
        self.sqrs = [[False] * 9 for i in xrange(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".": continue
                num = int(board[row][col]) - 1
                sqr = (row/3)*3 + col/3
                self.rows[row][num] = self.cols[col][num] = self.sqrs[sqr][num] = True
        self.solve(board, 0)
        
    def solve(self, board, k):
        if k >= 81: return True
        row = k/9
        col = k%9
        sqr = (row/3)*3 + col/3
        next_col = (col+1) % 9
        next_row = row if col <= 8 else row + 1
        if board[row][col] != ".": return self.solve(board, k+1)

        for num in xrange(1, 10):
            if self.rows[row][num-1] or self.cols[col][num-1] or self.sqrs[sqr][num-1]: 
                continue
            self.rows[row][num-1] = True
            self.cols[col][num-1] = True
            self.sqrs[sqr][num-1] = True
            board[row][col] = str(num)

            if self.solve(board, k+1): return True
            self.rows[row][num-1] = False
            self.cols[col][num-1] = False
            self.sqrs[sqr][num-1] = False
            board[row][col] = "."

        return False


s = Solution()
board = [list("..9748..."),list("7........"),list(".2.1.9..."),
        list("..7...24."),list(".64.1.59."),list(".98...3.."),
        list("...8.3.2."),list("........6"),list("...2759..")]
s.solveSudoku(board)

