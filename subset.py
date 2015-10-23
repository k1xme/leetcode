def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    rst = []
    nums.sort()
    def dfs(subset, start):
        rst.append(subset)
        for i in range(start, len(nums)):
            dfs(subset+[nums[i]], i+1)
    
    dfs([], 0)
    return rst

print subsets([1,2,3])