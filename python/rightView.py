# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

# Do BFS using two 2 stacks.
# Pop out the last it

# OR: Do DFS, but change the order, start traverse from
# the right child. Recursive fashion.
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if not root: return []
        
        curLevel = []
        nextLevel = []
        rst = [root.val]
        
        if root.right: curLevel.append(root.right)
        if root.left: curLevel.append(root.left)
        
        while curLevel:
            print curLevel, nextLevel
            v = curLevel.pop()
            
            if v.right: nextLevel.append(v.right)
            if v.left: nextLevel.append(v.left)
            
            # If we have traverse all the nodes in curLevel.
            if not curLevel:
                rst.append(v.val)
                curLevel = nextLevel
                nextLevel = []
        
        return rst

s = Solution()
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.right = TreeNode(5)
r.right.left = TreeNode(6)

s.rightSideView(r)
