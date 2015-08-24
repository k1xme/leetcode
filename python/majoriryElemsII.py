# Up to 2 majority elems.
# Use `count1`, `num1` and `count2`, `num2` to store the 2 majority elements for now in subarray(0,i).
# We subtract both count1 and count2 by 1 whenever we meet a number that doesn't equal to both of them.
# The elements that appear more will replace the less ones.

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if not nums:return []
        
        rst = []
        count1 = count2 = num1 = num2 = 0
        
        for n in nums:
            if count1 == 0:
                count1, num1 = 1, n
            elif num1 == n: count1 += 1
            elif count2 == 0:
                count2, num2 = 1, n
            elif num2 == n: count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        if nums.count(num1) > len(nums)/3: rst.append(num1)
        if num2 != num1 and nums.count(num2) > len(nums)/3: rst.append(num2)
        return rst

s = Solution()
print s.majorityElement([8,8,7,7,7])