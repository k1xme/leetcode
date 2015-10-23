# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        stack = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            v = stack.pop()
            k -= 1
            if k == 0: return v.val
            root = v.right

sol = Solution()
root = TreeNode(1)
print sol.kthSmallest(root,1)