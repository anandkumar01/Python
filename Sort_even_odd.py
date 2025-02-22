# Sort the list based on even and odd numbers
def sort_even_odd(nums):
    c = 0
    for i in range(len(nums)):
        if not nums[i] & 1:
            nums[i], nums[c] = nums[c], nums[i]
            c += 1
    return nums

nums = [3, 5, 2, 8, 5, 4, 6, 7]
print(sort_even_odd(nums))