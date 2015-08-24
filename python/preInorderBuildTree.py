class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder: return None
        # We keep to pointers, one refers to preorder array, the other refers to inorder.
        root = TreeNode(preorder[0])
        stack = [root]
        j, i = 0, 1
        add_to_right = False
        parent_node = root
        while i < len(preorder):
            if stack and stack[-1].val == inorder[j]:
                add_to_right = True
                parent_node = stack.pop()
                j += 1
                continue
            
            new_node = TreeNode(preorder[i])

            if add_to_right:
                parent_node.right = new_node
                add_to_right = False
            else: stack[-1].left = new_node
            stack.append(new_node)
            i += 1

        return root

s = Solution()
print s.buildTree([1,2,4,5,3,6], [4,2,5,1,6,3]).right.left
