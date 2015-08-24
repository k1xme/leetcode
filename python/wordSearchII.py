from pprint import pprint

# Set up a Trie for the dictionary.
# Then use the Trie to dfs the board.
# Will there be duplicates?
class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children: cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.flag = True

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children: return False
            cur = cur.children[c]
        return True

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        trie = Trie()
        for word in words: trie.insert(word)
        root = trie.root
        rst = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] not in root.children: continue
                tmp = board[i][j]
                board[i][j] = "."
                self.findWord(board, root.children[tmp], i, j, tmp, rst)
                board[i][j] = tmp
        return rst
    
    def findWord(self, board, root, i, j, path, rst):
        if root.flag and path not in rst: rst.append(path)
        positions = []
        if i > 0: positions.append((i-1,j))
        if j > 0: positions.append((i,j-1))
        if i < len(board)-1: positions.append((i+1,j))
        if j < len(board[0])-1: positions.append((i,j+1))

        for i, j in positions:
            if board[i][j] != "." and board[i][j] in root.children:
                tmp = board[i][j]
                board[i][j] = "."
                self.findWord(board, root.children[tmp], i, j, path+tmp, rst)
                board[i][j] = tmp
        

s = Solution()
# print s.findWords([
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ], ["oath","pea","eat","rain"])

print s.findWords([["a","a"]], ["a"])
# print s.findWords(["ab","aa"], ["aba","baa","bab","aaab","aaa","aaaa","aaba"])
# print s.findWords([
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']], ["oath","pea","eat","rain"])
# print s.findWords([["a","b","c"],["a","e","d"],["a","f","g"]], ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"])