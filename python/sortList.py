# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# MergeSort
# How to do it iteratively
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head: return head
        if not head.next: return head
        if not head.next.next:
            if head.val < head.next.val: return head
            else:
                new_head = head.next
                head.next = None
                new_head.next = head
                return new_head

        l1, l2 = self.split(head)
        return self.merge(self.sortList(l1), self.sortList(l2))
    
    # @return {ListNode} {ListNode}, the heads of splitted lists.
    def split(self, head):
        # Have to add a dummy. to get the right middle node.
        dummy = ListNode(-1)
        dummy.next = head
        slow, quick = dummy, dummy
        
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next

        l2 = slow.next
        slow.next = None

        return dummy.next, l2

    # @param {ListNode} l1, non-descending order list head.
    # @param {ListNode} l2, non-descending order list head.
    # @return {ListNode}
    def merge(self, l1, l2):
        merged = ListNode(0)
        p = merged

        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1: p.next = l1
        if l2: p.next = l2

        return merged.next


def printList(head):
    p = head
    while p:
        print p.val
        p = p.next

h = ListNode(2)
h.next = ListNode(1)
#h.next.next = ListNode(1)
#h.next.next.next = ListNode(5)
#h.next.next.next.next = ListNode(4)

s = Solution()
a = s.sortList(h)
printList(a)