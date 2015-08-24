# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Using two pointers, the gap between which is n-1. When
# the quicker pointer which the end of the list, the slower
# one is the node to be removed.
class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head
            
        quickie = slowie = head
        
        # let quickie n-1 ahead of slowie.
        for i in range(1, n):
            quickie = quickie.next
        
        # locate the node to be removed.
        while quickie.next is not None:
            quickie = quickie.next
            slowie = slowie.next

        if n == 1:
            slowie = None
        else:
            slowie.next = slowie.next.next

        return head

s = Solution()

head = ListNode(1)

n = s.removeNthFromEnd(head, 1)
