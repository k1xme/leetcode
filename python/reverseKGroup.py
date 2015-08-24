# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)
class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head: return None
        
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        return self._reverseKGroup(head, k, size)
        
    def _reverseKGroup(self, head, k, size):
        if k > size: return head
        dummy = ListNode(0)
        
        tail = cur = head
        i = k

        while i > 0:
            next_cur = cur.next
            cur.next = None
            tmp = dummy.next
            dummy.next = cur
            dummy.next.next = tmp
            cur = next_cur
            i -= 1
        
        tail.next = self._reverseKGroup(cur, k, size - k)

        return dummy.next


r = ListNode(8)
r.next = ListNode(3)
r.next.next = ListNode(9)
r.next.next.next = ListNode(10)
a = [r, None]

s = Solution()
def printList(head):
    p = head
    while p:
        print p.val
        p = p.next
def swap(head):
    tmp = head.next
    head.next = head.next.next
    tmp.next = head.next.next
    head.next.next = tmp


printList(s.reverseKGroup(r, 3))
