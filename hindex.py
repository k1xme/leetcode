# Binary Search.

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        
        h_index = 0
        l, r = 0, len(citations)-1
        
        while l <= r:
            mid = (r-l)/2 + l
            print mid
            if citations[mid] >= len(citations) - mid:
                h_index = max(h_index, min(citations[mid], len(citations) - mid))
            
            l = mid + 1
        
        return h_index

sol = Solution()
print sol.hIndex([1,1,2,3,4,5,7])