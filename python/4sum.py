class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums) < 4: return []
        rst = []
        nums.sort()

        # Go through 0 to n-4.
        i = 0
        while i < len(nums):
            target3 = target - nums[i]
            k = i + 1

            while k < len(nums):
                diff_map = {}    
                target2 = target3 - nums[k]
                j = k+1
                while j < len(nums):
                    diff = target2 - nums[j]
                    if nums[j] in diff_map: 
                        rst.append([nums[i], nums[k], diff_map[nums[j]], nums[j]])
                    diff_map[diff] = nums[j]
                    prej = nums[j]
                    while j < len(nums) and nums[j] == prej: j+=1
                prek = nums[k]
                while k < len(nums) and nums[k] == prek: k+=1
            prei = nums[i]
            while i < len(nums) and nums[i] == prei: i+=1

        return rst

s = Solution()
print s.fourSum([-3,-2,-1,0,0,1,2,3], 0)