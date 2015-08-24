# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# Iteration: using 2 queues for DFS the two children of the root
# at the same time. Note that the order of DFS the subtree is:
# for left subtree, DFS its left child first. For right subtree, DFS
# its right child first.

# New Idea: probably use Pyhon Generator. Create two generator functions:
# leftTreeTraversor and rightTreeTraversor.

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root: return True
        
        left_tree = self.leftChild(root.left)
        right_tree = self.rightChild(root.right)
        
        for l, r in zip(left_tree, right_tree):
            if l != r: return False
        
        if next(left_tree, False) or next(right_tree, False):
            return False
        
        return True
    
    def leftChild(self, left):
        queue = [left]
        
        while queue:
            node = queue.pop(0)
            
            if node:
                yield node.val
                queue.append(node.left)
                queue.append(node.right)
            else: yield
        
    def rightChild(self, right):
        queue = [right]
        
        while queue:
            node = queue.pop(0)
            
            if node:
                yield node.val
                queue.append(node.right)
                queue.append(node.left)
            else: yield
        

root = TreeNode(1)
root.left = TreeNode(2)
#root.right = TreeNode(1)
s = Solution()
print s.isSymmetric(root)