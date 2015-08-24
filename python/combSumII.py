# Pitfalls: the numbers in candidates may repeat.

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        if not candidates: return []
        candidates.sort()
        rst = []
        self._combinationSum2(candidates, target, [], rst)

        return rst
        
    def _combinationSum2(self, candidates, target, combination, rst):
        if target == 0:
            rst.append(combination)
            return
        elif target < 0:
            return
        if not candidates: return
        
        n = len(candidates)
        i = 0
        while i < n:
            c = candidates[i]
            if c <= target:
                self._combinationSum2(candidates[i+1:], target-c, combination+[c], rst)
            
            i += 1

s = Solution()
print s.combinationSum2([1,1], 2)