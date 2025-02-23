# Missing number in the list where number in the list are in range [0,n]

def missing_number(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i]
        if nums[i] < n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i:
            return i
    return n


nums = [3, 1, 5, 0, 2, 4, 6, 7]
print(missing_number(nums))
