'''
Find quadralets that satisfy A+B = C+D
'''
def quadralets(nums):
	'''
	@return list[index of the nums]
	'''
	same_sum = {}
	rst = []
	for i in range(len(nums)-1):
		for j in range(i+1, len(nums)):
			current_sum = nums[i] + nums[j]
			index_pair = set((i,j))
			if current_sum not in same_sum:
				same_sum[current_sum] = [set((i,j))]
			else:
				for previous_pair in same_sum[current_sum]:
					if index_pair.isdisjoint(previous_pair):
						previous_pair = list(previous_pair)
						rst.append([previous_pair[0], previous_pair[1], i, j])

				same_sum[current_sum].append(index_pair)

	return rst

print quadralets([3,4,7,1,2,9,8])
# print quadralets([4,4,4,4,4])
