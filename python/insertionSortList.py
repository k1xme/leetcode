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
        
        rst = None
        p = head
        
        while p:
            tmp = p.next
            if not rst or rst.val > p.val:
                p.next = rst
                rst = p
            else:
                insertP = rst
                
                while insertP.next and p.val > insertP.next.val:
                    insertP = insertP.next
                
                p.next = insertP.next
                insertP.next = p
            p = tmp
        
        return rst



def printList(head):
    p = head
    while p:
        print p.val
        p = p.next

s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(4)
#h.next.next.next = ListNode(2)
printList(s.insertionSortList(h))