# Remove all duplicate elements from sorted list 
def no_duplicate_sorted(nums):
    if not nums:
        return []
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
    return nums


nums = [1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9]
print(no_duplicate_sorted(nums))
