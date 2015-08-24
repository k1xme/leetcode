# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)
# Implement HeapifyDown, HeapifyUp functions.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Implement HeapifyDown, HeapifyUp functions.
class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if not lists: return None

        rst = ListNode(0) # dummy
        cur = rst
        heap = []

        for v in lists:
            while v:
                self.insert(heap, v)
                v = v.next

        while heap:
            mini = self.getMin(heap)
            cur.next = mini
            cur = cur.next

        return rst.next

    
    def heapifyDown(self, heap, k):
        if not heap: return
        n = len(heap)
        tmp = heap[k]

        childpos = 2*k + 1

        while childpos < n:
            rightpost = childpos + 1
            if rightpost < n and heap[rightpost].val < heap[childpos].val:
                childpos = rightpost
            if tmp.val > heap[childpos].val:
                heap[k] = heap[childpos]
                k = childpos
                childpos = 2*k + 1
            else: break

        heap[k] = tmp


    def heapifyUp(self, heap, k):
        if not heap: return
        tmp = heap[k]
        
        while k > 0:
            parent = (k - 1) /2
            if heap[parent].val > tmp.val:
                heap[k] = heap[parent]
                k = parent
            else: break
        heap[k] = tmp


    def insert(self, heap, item):
        heap.append(item)
        n = len(heap)

        self.heapifyUp(heap, n - 1)

    def getMin(self, heap):
        if not heap: return None
        
        tail = heap.pop()
        
        if heap:
            tmp = heap[0]
            heap[0] = tail
        else:
            tmp = tail

        self.heapifyDown(heap, 0)
        return tmp

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
swap(r)
printList(r)

