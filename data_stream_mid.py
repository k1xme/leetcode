from heapq import *
class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        # write your code here
        maxHeap = []
        minHeap = []
        m = 0
        rst = []
        for num in nums:
            if len(maxHeap) == len(minHeap):
                if num >= m:
                    heappush(minHeap, num)
                    m = minHeap[0]    
                else:
                    heappush(maxHeap, -num)
                    m = -maxHeap[0]
                rst.append(m)
                continue
            if len(maxHeap) < len(minHeap):
                if num >= m:
                    heappush(maxHeap, -heappop(minHeap))
                    heappush(minHeap, num)
                else:
                    heappush(maxHeap, -num)
            else:
                if num >= m:
                    heappush(minHeap, num)
                else:
                    heappush(minHeap, -heappop(maxHeap))
                    heappush(maxHeap, -num)
            m = -maxHeap[0]
            rst.append(m)
        return rst
