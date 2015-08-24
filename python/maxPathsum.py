# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        self.rst = -1 << 31
        return self._maxPathSum(root)
    
    def _maxPathSum(self, root):
        if not root: return 0
        
        fromLeft = self._maxPathSum(root.left)
        fromRight = self._maxPathSum(root.right)
        self.rst = max(fromLeft+fromRight+root.val, self.rst)

        return max(fromLeft, fromRight) + root.val

s = Solution()
t = TreeNode(0)
print s.maxPathSum(t)
