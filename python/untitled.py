# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# The basic idea is: if the number of node before each list reaches the intersected
# node is the same, then we can find the intersected node at the first traversal.
# Else, we have to find a way to make the 2 traversal pointers march at the same pace,
# which means the distance from the head of each list to the intersection must be the same.

# Let d(A) denote the distance from headA to the intersected node. Same for d(B).
# Concate list B to list A and list A to list B. By doing so, we can assure that
# at the second traversal of each list, the distance from head to the intersection is
# d(A) + d(B), thus when pointer A is equal to pointer B, they have arrived at the
# intersection node.

# First compare the last node of these two lists. If they are different,
# then there is no intersection.

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        Alast = headA
        Blast = headB
        while Alast.next:
            Alast = Alast.next
        
        while Blast.next:
            Blast = Blast.next
        
        # No intersection.
        if Alast != Blast:
            return None
        
        p1 = headA
        p2 = headB
        
        while True:
            if p1 == p2:
                return p1
            else:
                p1 = p1.next if p1.next else headB
                p2 = p2.next if p2.next else headA
        
        return None