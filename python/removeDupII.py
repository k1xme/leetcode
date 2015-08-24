# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        
        dummy = ListNode(0)
        duplicate = False
        p = dummy

        while head and head.next:
            if head.val == head.next.val:
                v = head.val
                # fastforward to the node with different value.
                while head and head.val == v:
                    head = head.next
            else:
                p.next = head
                head = head.next
                p.next.next = None
                p = p.next
        
        # If head is not None, it means this node has a
        # different value with the previous, and it's the
        # last node of the list, so there is no duplicate of it.
        # Then we should append it to the result list.
        if head: p.next = head

        return dummy.next


def printList(head):
    p = head
    while p:
        print p.val
        p = p.next

s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(2)
h.next.next.next = ListNode(2)
printList(s.deleteDuplicates(h))