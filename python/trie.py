class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.flag = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        if not word: return
        v = self.root
        for c in word:
            if c not in v.children: v.children[c] = TrieNode()
            v = v.children[c]
        v.flag = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        if not word: return True
        v = self.root
        for c in word:
            if c not in v.children: return False
        
        return v.flag

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        if not prefix: return True
        v = self.root
        for c in prefix:
            if c not in v.children: return False
        return True

t = Trie()
t.insert("a")
t.search("a")