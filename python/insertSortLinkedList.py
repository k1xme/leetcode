# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head: return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        while cur.next:
            if cur.next.val < prev.next.val: prev = dummy
            while prev.next.val < cur.next.val: prev = prev.next
            if prev is cur:
                cur = cur.next
                continue
            tmp = prev.next
            prev.next = cur.next
            cur.next = cur.next.next
            prev.next.next = tmp
            
        return dummy.next

a = ListNode(5)
a.next = ListNode(4)
a.next.next = ListNode(1)

s = Solution()
a = s.insertionSortList(a)
while a:
    print a.val
    a = a.next
