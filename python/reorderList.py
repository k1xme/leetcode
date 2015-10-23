# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Split the list. O(n). Then reverse the second half. O(n). Merge.
# class Solution:
#     # @param {ListNode} head
#     # @return {void} Do not return anything, modify head in-place instead.
#     def reorderList(self, head):
#         if not head: return
        
#         dummy = ListNode(0)
#         dummy.next = head
#         slow = quick = dummy

#         while quick and quick.next:
#             slow = slow.next
#             quick = quick.next.next
        
#         dummy.next = None
#         q = slow.next
#         slow.next = None # Remember to set it to None.
        
#         # reverse second_half.
#         while q:
#             tmp = dummy.next
#             dummy.next = q
#             q = q.next
#             dummy.next.next = tmp

#         # merge
#         p = head
#         q = dummy.next

#         while q:
#             tmp = p.next
#             p.next = q
#             q = q.next
#             p.next.next = tmp
#             p = tmp
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return
    
        dummy = ListNode(0)
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        dummy.next = None
        cur = slow.next
        slow.next = None
        
        while cur:
            tmp = dummy.next
            dummy.next = cur
            dummy.next.next = tmp
            cur = cur.next

        cur = head
        slow = dummy.next
        while slow:
            tmp = cur.next
            cur.next = slow
            slow = slow.next
            cur.next.next = tmp
            cur = tmp
        
        
# class Solution:
#     # @param {ListNode} head
#     # @return {void} Do not return anything, modify head in-place instead.
#     def reorderList(self, head):
#         if not head: return
        
#         while head:
#             head.next = self.reverse(head.next)
#             head = head.next
    
#     def reverse(self, head):
#         if not head: return head
#         dummy = ListNode(0)
#         p = dummy
#         while head:
#             tmp = head.next
#             head.next = p.next
#             p.next = head
#             head = tmp
#         return dummy.next

def printList(head):
    p = head
    while p:
        print p.val
        p = p.next


s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
#h.next.next.next.next = ListNode(5)
s.reorderList(h)
printList(h)