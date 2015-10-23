class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        if not A: return
    
        n = len(A)
        
        for i in reversed(xrange(n//2)):
            child = 2*i + 1
            tmp = A[i]
            while child < n:
                right_child = child + 1
                if right_child < n and A[right_child] < A[child]: child = right_child
                if tmp <= A[child]: break
                A[(child-1)//2] = A[child]
                child = 2*child + 1
            A[(child-1)//2] = tmp


s = Solution()
a = [42,30,27,93,8,34,47,64,82,76,70,79,23,5,67,9]
b = [42,30,27,93,8,34,47,64,82,76,70,79,23,5,67,9]
s.heapify(a)
print a
import heapq
heapq.heapify(b)
print b
