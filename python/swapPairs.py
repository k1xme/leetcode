# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head: return None
        
        dummy = ListNode(0)
        dummy.next = head
        
        p = dummy
            
        while p.next.next: # it means there is a pair, so we can swap it.
            tmp = p.next.next.next  # store the head of the next pair(if we have).
            first = p.next
            p.next = first.next
            first.next = tmp
            p.next.next = first

            # move on to the next one.
            p = p.next.next
            if not p.next: break 
            
        return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
s = Solution()
print s.swapPairs(head)