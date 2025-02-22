# Given 0, 1, 2 and sort with O(1) time complexity

def sort_colors(nums):
    i, j = 0, len(nums) - 1
    k = 0
    while k <= j:
        if nums[k] == 2:
            nums[j], nums[k] = nums[k], nums[j]
            j -= 1
        elif nums[k] == 0:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k += 1
        else:
            k += 1


nums = [2, 0, 1, 1, 2, 0, 0, 2, 1, 2]
sort_colors(nums)
print(nums)
