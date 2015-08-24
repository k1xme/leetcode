class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if not root: return []
        
        dir = 0 # 0 menas from left to right, vice versa for 1.
        
        cur_lev = [root]
        next_lev = []
        cur_rst = []
        result = []
        
        while cur_lev:
            v = cur_lev.pop()
            cur_rst.append(v.val)
            if dir == 0:
                if v.left: next_lev.append(v.left)
                if v.right: next_lev.append(v.right)
            else:
                if v.right: next_lev.append(v.right)
                if v.left: next_lev.append(v.left)
            
            if not cur_lev:
                cur_lev = next_lev
                next_lev = []
                result.append(cur_rst)
                cur_rst = []
                dir = dir ^ 1
        
        return result

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.left.right = TreeNode(5)
s = Solution()
print s.zigzagLevelOrder(r)