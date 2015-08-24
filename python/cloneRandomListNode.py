class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __repr__(self):
        return str(self.label)

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: return None
        
        cloneNodes = {}
        visited = set([])
        cur = head
        dummy = RandomListNode(0)
        while cur:                
            v = RandomListNode(cur.label)
            cloneNodes[cur.label] = v
            if cur.random:
                cloneNodes[cur.random.label] = RandomListNode(cur.random.label)

            if cur.next:
                cloneNodes[cur.next.label] = RandomListNode(cur.next.label)
                v.next = cloneNodes[cur.next.label]
            dummy.next = v
            cur = cur.next
            dummy = dummy.next

        while cur:
            if cur.random:
                r = cloneNodes[cur.random.label]
                v = cloneNodes[cur.label]
                v.random = r
            
            cur = cur.next
        print cloneNodes
        return cloneNodes[1]

head = RandomListNode(1)
head.next = RandomListNode(2)
head.next.random = head
head.next.next = RandomListNode(3)
head.next.next.random = head

s = Solution()
p = s.copyRandomList(head.next.next)

while p:
    print p, p.random
    p = p.next
