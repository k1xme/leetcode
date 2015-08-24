# Sort the array first, then use 2 pointers to traverse.
# Have to use a nested loop. These 2 loops has the same
# condition, which is left < right. The difference is
# the inner loop's left pointer >= outer loop's left pointer.
# vice versus for the right pointers.

# EDGE CASES: [0,0,0], [0,0]
# Note: have to remove duplicates at the same time.
# If we do removing duplicates after find out all the triples,
# the run time would be 3x as much.
# class Solution:
#     # @param {integer[]} nums
#     # @return {integer[][]}
#     def threeSum(self, nums):
#         if not nums or len(nums) < 3:
#             return []

#         nums = sorted(nums)
#         result = []
#         pre = nums[0]
        
#         # NOTE: the condition!!
#         for i in range(0, len(nums)-1):
#             # Avoid computing identical num.
#             if i != 0 and pre == nums[i]: continue
#             pre = nums[i]
            
#             m = i + 1
#             prem = nums[m]
            
#             r = len(nums) - 1
#             prer = nums[r]
            
#             while m < r:
#                 sum = nums[i] + nums[m] + nums[r]

#                 if sum  == 0:
#                     result.append([nums[i], nums[m], nums[r]])

#                 if sum > 0:
#                     # Avoid computing identical num.
#                     # NOTE: the condition, avoid index out of range
#                     while  r > 0 and prer == nums[r]: r -= 1
#                     prer = nums[r]
#                 else:
#                     # Avoid computing identical num.
#                     # NOTE: the condition, avoid index out of range
#                     while m < len(nums) - 1 and prem == nums[m]: m += 1
#                     prem = nums[m]

#         return result
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if len(nums) < 3: return []
        
        nums.sort()
        rst = []
        n = len(nums)
        i = 0
        while i < n:
            target = 0 - nums[i]
            pre = nums[i]
            diffMap = {}
            j = i+1

            while j < n:
                prej = nums[j]
                diff = target - nums[j]
                if nums[j] not in diffMap:
                    diffMap[diff] = nums[j]
                    j += 1
                    continue
                rst.append([nums[i], diffMap[nums[j]], nums[j]])
                j += 1
                while j < n and prej == nums[j]: j += 1
            i+= 1    
            while i < n and pre == nums[i]: i += 1
            
        return rst
                
case1 = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
case2 =[0, 0, 0]
s = Solution()
print s.threeSum(case2)