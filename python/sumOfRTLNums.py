# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## This kind of tree problems is all about doing backtracking
## You should know how to do it by recursion and by iteration.

# Use recursion with accumulators allNums which stores
# all the root-to-leaf numbers discovered so far and curNum
# holding the prefix of current number.

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        if not root: return 0
        
        allNums = []
        
        # Find all the root-to-leaf numbers.
        self._getNums(root, 0, allNums)

        return sum(allNums)

    def _getNums(self, root, curNum, allNums):
        if not root:
            return
        
        # New digit for the current num.
        curNum = curNum*10 + root.val

        # If this is a leave, then we convert curNum to int
        # and append it to allNums.
        if not (root.left or root.right):
            allNums.append(curNum)
            return
        
        # Keep find new numbers in left and right children.
        self._getNums(root.left, curNum, allNums)
        self._getNums(root.right, curNum, allNums)

s = Solution()
r = TreeNode(0)
r.left = TreeNode(1)
print s.sumNumbers(r)