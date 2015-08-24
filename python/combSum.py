class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        rst = []
        candidates.sort()
        self._combinationSum(candidates, target, [], rst)
        return rst
    
    # @param {integer[]} combination, the numbers chosen so far.
    def _combinationSum(self, candidates, target, combination, rst):
        if not candidates: return
        # This combination doesn't sum up to the target. Discard it.
        if target < 0: return
        if target == 0: rst.append(combination)
        
        for i in range(len(candidates)):
            c = candidates[i]
            if c <= target:
                self._combinationSum(candidates[i:], target-c, combination + [c], rst)

s = Solution()
candidates = [2,3,6,7]
print s.combinationSum([8,7,4,3], 11)