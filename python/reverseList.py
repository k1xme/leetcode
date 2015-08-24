# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# find the node at `m`, then create a dummynode linked to it.
# Keep traversing the list, every time we move forward, insert
# the next node between the dummy and the current head until we
# find the node at `n`.

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n        
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if not head or not head.next: return head
        
        pos = 1
        dummy = ListNode(0)
        dummy.next = head
        
        # find the node before `m`
        pre_m = dummy
        while pos < m:
            pre_m = pre_m.next
            pos += 1
        
        nodeM = pre_m.next
        
        # start to reverse.
        while pos < n and nodeM.next:
            p = nodeM.next
            nodeM.next = p.next
            p.next = pre_m.next
            pre_m.next = p

            pos += 1


        return dummy.next


def printList(head):
    p = head
    while p:
        print p.val
        p = p.next


s = Solution()

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)

printList(s.reverseBetween(h, 1, 3))
