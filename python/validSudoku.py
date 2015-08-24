# use 9 bits to represent the numbers showed up in a sub-box, a row or a column.
# Then scan the board line by line. If a certain number already shows up before, return False.
# Else, continue.

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        if not board: return False
        
        columns = [(1<<9)-1] * 9
        boxes = [(1<<9)-1] * 9
        rows = [(1<<9)-1] * 9
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                n = int(board[i][j])
                mask = ((1 << 9-n) - 1 << n) + (1 << n-1) - 1
                if rows[i] & 1<<(n-1) == 0:
                    return False # n already showed up in this row.
                rows[i] &= mask
                if columns[j] & 1<<(n-1) == 0:
                    return False
                columns[j] &= mask
                if boxes[(i/3)*3 + j/3] & 1<<(n-1) == 0:
                    print "box", (i/3)*3 + j/3, i,j
                    return False
                boxes[i/3 + j/3] &= mask
        return True

s = Solution()
print s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])