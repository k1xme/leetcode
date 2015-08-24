# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if not head: return None
        
        size = 0
        cur = head
        
        while cur:
            size += 1
            cur = cur.next

        return self._sortedListToBST(head,size)
    
    def _sortedListToBST(self, head, size):
        
        if size == 1:
            return TreeNode(head.val)
        if size == 2:
            root = TreeNode(head.val)
            right = TreeNode(head.next.val)
            root.right = right
            return root
        
        dummy = ListNode(0)
        dummy.next = head
        
        cur = dummy
        pos = 0
        while pos < size/2:
            pos += 1
            cur = cur.next
        
        right_size = size/2 - 1 if size%2 == 0 else size/2
        root = TreeNode(cur.next.val)
        right = cur.next.next
        cur.next = None
        root.left = self._sortedListToBST(dummy.next, size/2)
        root.right = self._sortedListToBST(right, right_size)
        print root.val, root.left.val, root.right.val
        return root

s = Solution()
r = ListNode(3)
r.next = ListNode(5)
r.next.next = ListNode(8)
s.sortedListToBST(r)