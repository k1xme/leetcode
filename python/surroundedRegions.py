# Connected Components. BSF to traverse 
# According to the desc, 'O's in the 1st and last rows and cols are not considered.

# Mark the "live" "O" with "+" first, then flips the rest of "O"s.
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if len(board) < 3 or len(board[0]) < 3: return
    
        rows = len(board)
        cols = len(board[0])
        
        for r in xrange(rows):
            if board[r][0] == "O": 
                self.bfs(board, r, 0)
            if board[r][cols-1] == "O": self.bfs(board, r, cols-1)

        for c in xrange(cols):
            if board[0][c] == "O": self.bfs(board, 0, c)
            if board[rows-1][c] == "O": self.bfs(board, rows-1, c)
        
        printMatrix(board)
        
        for r in xrange(rows):
            for c in xrange(cols):
                if board[r][c] == "X": continue
                board[r][c] = "X" if board[r][c] == "O" else "O"
        
    
    def bfs(self, board, row, col):
        # start BFS from board[row][col]
        stack = [(row, col)]
        rows = len(board)
        cols = len(board[0])
        
        while stack:
            r, c = stack.pop()
            board[r][c] = "+"
            
            if r > 0 and board[r-1][c] == "O": 
                stack.append((r-1, c))
                board[r-1][c] = "+"

            if r < rows-1 and board[r+1][c] == "O": 
                stack.append((r+1, c))
                board[r+1][c] = "+"

            if c > 0 and board[r][c-1] == "O": 
                stack.append((r, c-1))
                board[r][c-1] = "+"

            if c < cols-1 and board[r][c+1] == "O": 
                stack.append((r, c+1))
                board[r][c+1] = "+"

def printMatrix(matrix):
    print "REGIONS"
    for row in matrix:
        print row

s = Solution()
s.solve([["X","O","X"],["O","X","O"],["X","O","X"]])



        
        
        
    
        
        