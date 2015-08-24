def heapifyUp(nums, i):
	while i > 0 and nums[i] < nums[(i-1)>>1]:
		nums[(i-1)>>1], nums[i] = nums[i], nums[(i-1)>>1]
		i = (i-1)/2

def heapifyDown(nums, i):
	child = 2*i + 1
	tmp = nums[i]
	while child < len(nums):
		right_child = child + 1
		if right_child < len(nums) and nums[child] > nums[right_child]:
			child = right_child
		if nums[i] <= nums[child]: break
		nums[i] = nums[child]
		i = child
		child = 2 * i + 1

	nums[i] = tmp
