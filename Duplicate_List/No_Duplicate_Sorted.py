# Remove all duplicate elements from sorted list 

# With O(1) space complexity
def no_duplicate_sorted1(nums):
    if not nums:
        return []
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
    return nums

# With O(n) space complexity
def no_duplicate_sorted2(nums):
    if not nums:
        return []
    res = [nums[0]]
    for num in nums:
        if num != res[-1]:
            res.append(num)
    return res

nums = [1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9]
print(no_duplicate_sorted2(nums))
