class TrieNode:
    def __init__(self):
        self.sym = ""
        self.children = {}
        self.terminal = False

    def __repr__(self):
        return self.sym

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        if not word: return
        n = len(word)
        cur = self.root
        
        for i in xrange(n):
            if word[i] not in cur.children:
                new_node = TrieNode()
                new_node.sym = word[i]
                cur.children[word[i]] = new_node
                cur = new_node
                continue
            cur = cur.children[word[i]]
        
        cur.terminal = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        if not word: return False
        
        n = len(word)
        cur = self.root
        i = 0
        stack = []
        
        while i < n:
            if word[i] != ".":
                if word[i] not in cur.children:
                    if stack:
                        cur, i = stack.pop()
                        continue
                    return False

                cur = cur.children[word[i]]
                i += 1
            else:
                for child in cur.children.values():
                    stack.append((child, i+1))
                if not stack: return False
                
                cur, i = stack.pop()
            
            if i == n and not cur.terminal and stack:
                cur, i = stack.pop()

        return cur.terminal
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
def traverse(root):
    stack = []
    while root:
        print root, root.terminal
        for n in root.children.values():
            stack.append(n)
        root = stack.pop() if stack else None

s = WordDictionary()

s.addWord("ran")
s.addWord("rune")
s.addWord("runner")
#s.addWord("runs")
#s.addWord("adds")
#s.addWord("adder")
#s.addWord("addee")
print s.search("r.n")
#s.addWord("add")
#traverse(s.root)