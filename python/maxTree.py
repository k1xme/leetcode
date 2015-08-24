class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

# Traverse through A, maintaining a stack storing subtrees formed by the nodes 
# from 0 to i. The root value of all the subtrees in stack increase from the 
# top to the bottom. If A[i] is less than the root value of stack top, we keep
# popping subtrees out the stack and connecting the former one to the right of 
# the later one until the stack top is greater than A[i]. Else we simply push 
# the TreeNode(A[i]) to the stack.

# It's possible that after traversing through A(e.g. [2,5,6,0,3,1]), the stack
# contains more than 1 subtree, so we need an extra pass to process all the
# subtrees remaining in stack to construct our root.

# Every node was pushed and popped out of stack exactly once and we only
# operate on the root of subtrees, so the time complexity is O(2n). In the
# worst cases, stack contains N subtrees. Therefore the space comlexity is O(N).

class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        if not A: return None
        stack = []
        
        for num in A:
            v = TreeNode(num)

            if stack and v.val > stack[-1].val:
                right = stack.pop()
                while stack and v.val > stack[-1].val:
                    subroot = stack.pop()
                    subroot.right = right
                    right = subroot
                v.left = right
            
            stack.append(v)
        r = stack.pop()
        while stack:
            v = stack.pop()
            if r.val < v.val:
                v.right = r
                r = v
            else:
                r.left = v

        return r


s = Solution()
r = s.maxTree([2,5,6,0,3,1])
print r, r.left, r.left.right
r = s.maxTree([6,4,20])
print r, r.left, r.left.right