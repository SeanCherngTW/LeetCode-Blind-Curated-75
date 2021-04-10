def quicksort(nums):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    left = [num for num in nums[1:] if num <= pivot]
    right = [num for num in nums[1:] if num > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


nums = [1, 5, 9, 3, 6, 7, 4, 8, 2]
print(quicksort(nums))
