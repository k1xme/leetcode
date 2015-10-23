#!/usr/bin/python
def findKth(nums, start, end, k):
    n = len(nums)
    pivot_index = 0
    for i in range(start, end):
        if nums[i] < nums[end]:
            nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
            pivot_index += 1
    
    nums[pivot_index], nums[end] = nums[end], nums[pivot_index]
    
    if pivot_index == k-1:
        print nums[pivot_index]
        return
    if pivot_index > k-1:
        findKth(nums, start, pivot_index-1, k)
    else:
        findKth(nums, pivot_index+1, end, k)
        
findKth([1,2,3,4,5], 0, 4, 1)
