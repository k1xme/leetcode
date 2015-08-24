def heapifyUp(nums):
    if not nums: return
    n = len(nums)
    start = n//2
    for i in range(start, -1, -1):
        pos = i
        child = 2*i + 1
        while child < n:
            rightchild = child + 1
            if rightchild < n and nums[rightchild] > nums[child]:
                child = rightchild
            if nums[pos] < nums[child]:
                nums[pos], nums[child] = nums[child], nums[pos]
            pos = child
            child = child * 2 + 1

def popMax(nums):
    x = nums[0]
    nums[0] = nums[-1]
    nums.pop()
    siftDown(nums, 0)
    return x

def siftDown(nums, i):
    n = len(nums)
    pos = i
    child = 2*i + 1
    while child < n:
        rightchild = child + 1
        if rightchild < n and nums[rightchild] > nums[child]:
            child = rightchild
        if nums[pos] < nums[child]:
            nums[pos], nums[child] = nums[child], nums[pos]
        else: break
        pos = child
        child = child * 2 + 1

nums = [-1,2,0]
heapifyUp(nums)
print nums
print popMax(nums)
print nums
print popMax(nums)
print popMax(nums)
