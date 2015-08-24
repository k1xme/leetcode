class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def buildTree(self, inorder, postorder):
#         if not inorder or not postorder: return None

#         n = len(inorder)
#         root = TreeNode(postorder.pop())
#         midPos = inorder.index(root.val)
        
#         root.right = self.buildTree(inorder[midPos+1:], postorder)
#         root.left = self.buildTree(inorder[:midPos], postorder)
        
#         return root

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder: return None
        
        root = TreeNode(0)
        stack = [(root, 0, len(inorder))] # for storing root
        while postorder:
            v, start, end = stack.pop()
            v.val = postorder.pop()
            midPos = inorder.index(v.val)
            if start < midPos:
                v.left = TreeNode(0)
                stack.append((v.left, start, midPos))
            # it means we have right child, so we construct it first.
            if midPos + 1 < end:

                v.right = TreeNode(0) # create a placeholder first.
                stack.append((v.right, midPos+1, end))
        
        return root

def printTree(root):
    if not root: return

    stack = [root]
    nextLevel = []
    rst = []
    while stack:
        v = stack.pop(0)
        rst.append(v.val)
        if v.left: nextLevel.append(v.left)
        if v.right: nextLevel.append(v.right)

        if not stack:
            stack = nextLevel
            nextLevel = []

    print rst

s = Solution()
printTree(s.buildTree([1,2], [2,1]))