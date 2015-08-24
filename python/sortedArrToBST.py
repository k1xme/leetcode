class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursion. Split the array into 3 parts: left, middle, right. The middle is the root of the tree.
class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if not nums: return None
        
        n = len(nums)
        if n == 1: return TreeNode(nums[0])
        elif n == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root

        mid = n/2
        root = TreeNode(mid)
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

a = [3,5,8]
s = Solution()
print s.sortedArrayToBST(a)