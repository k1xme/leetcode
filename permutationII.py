def permutation(nums):
	nums.sort()
	def dfs(start):
		if start == len(nums):
			print nums
			return
		for i in range(start, len(nums)):
			if i > start and nums[i] == nums[start]: continue
			nums[i], nums[start] = nums[start], nums[i]
			dfs(start+1)
			nums[i], nums[start] = nums[start], nums[i]

	dfs(0)

permutation([0,0,1,0,9])