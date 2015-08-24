
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        if not root: return []
        
        return self._pathSum(root, sum, [])
        
        
    def _pathSum(self, root, sum, path):
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                path.append(root.val)
                return [path]
            return []
        
        rst = []
        path.append(root.val)
        
        if root.left: rst += self._pathSum(root.left, sum, path)
        if root.right: rst += self._pathSum(root.right, sum, path)
        
        return rst

r = TreeNode(1)
r.right = TreeNode(2)
s = Solution()
print s.pathSum(r, 3)