# Rotate the array to the right by k steps

def right_rotation(nums, k):
    n = len(nums)
    k = k % n
    return nums[n - k :] + nums[: n - k]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(right_rotation(nums, k))
