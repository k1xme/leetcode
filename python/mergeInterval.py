# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
    	return "(%d, %d)" % (self.start, self.end)

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals: return []
        
        intervals.sort()
        rst = [intervals[0]]
        
        for int in intervals:
            pre = rst.pop()
            if int.start <= pre.end:
                pre.end = max(int.end, pre.end)
            
            rst.append(pre)
            
            if int.start > pre.end: rst.append(int)
        
        return rst

i1 = Interval(1,4)
i2 = Interval(2,5)
a = [i1,i2]
s = Solution()
print s.merge(a)
