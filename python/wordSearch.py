class Solution1:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if not word: return True
        if not board: return False
        
        roots = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]: roots.append((row, col))
        for r,c in roots:
            if self.search(board, word, 0, r, c): return True
        return False
        
    def search(self, board, word, i, row, col):
        if i == len(word): return True
        if 0 > row or row >= len(board) or 0 > col or col >= len(board[0]): return False
        
        if board[row][col] != word[i] or board[row][col] == "X": 
            print "prob", board, i
            return False
        
        possible_neighbors = [(row-1, col),(row+1, col),(row, col-1),(row, col+1)]
        for r,c in possible_neighbors:
            tmp = board[row][col]
            board[row][col] = "X"
            if self.search(board, word, i+1, r, c): return True
            board[row][col] = tmp
        return False
class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if not board: return False
        chosen = []
        rows = len(board)
        cols = len(board[0])
        
        # initialize chosen.
        for row in range(rows):
            chosen += [[False] * cols]
            
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if self._exist(board, row, col, word, chosen): return True
        
        return False
        
    # @param {integer}startR, the row of the starting cell.
    # @param {integer}startC, the col of the starting cell.
    # @param {(integer, integer)[]}chosen, the cells being chosen so far.
    def _exist(self, board, startR, startC, word, chosen):
        if not word: return True
        rows = len(board)
        cols = len(board[0])
        if startR < 0 or startR >= rows or startC < 0 or startC >= cols or board[startR][startC] != word[0] or chosen[startR][startC]:
            return False

        print "prob", chosen, len(word), startR, startC
        neighbors = [(startR-1, startC),(startR+1, startC),(startR, startC-1),(startR, startC+1)]
        chosen[startR][startC] = True
        for r,c in neighbors:
            if self._exist(board, r, c, word[1:], chosen): return True
        chosen[startR][startC] = False    
        return False
s = Solution()
# print s.exist([["A"]], "A")
print s.exist([["a","a"]], "aaa")