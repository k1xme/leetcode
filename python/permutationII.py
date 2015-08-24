class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        if not nums: return []

        n = len(nums)
        rst = [[]]
        i = n - 1
        
        while i >= 0:
            # insert nums[i] into the previous permutations.
            new_rst = []
            lastPos = len(rst[0])
            for r in rst:
                pos = 0
                while pos < lastPos+1:
                    new_rst.append(r[:pos]+[nums[i]]+r[pos:])
                    if pos < lastPos and nums[i] == r[pos]: break
                    pos += 1

            rst = new_rst
            i-=1

        return rst

    def permuteUnique2(self, num):
        if not num: return []
        ret = [[]]
        for n in num:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):
                    if i < l and seq[i] == n: break

                    new_ret.append(seq[:i] + [n] + seq[i:])
            ret = new_ret
        return ret

s = Solution()
print s.permuteUnique([2,3,2])

