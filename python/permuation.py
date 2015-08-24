class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if len(nums) < 2: return nums
        
        permutations = [[nums[0]]]
        
        for i in range(1, len(nums)):
            tmp = []
            for p in permutations:
                for j in range(len(p)+1): tmp.append(p[:j]+[nums[i]]+p[j:])
            permutations = tmp
        
        return permutations

s = Solution()
print s.permute([1,2,3])