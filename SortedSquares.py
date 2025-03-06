# Return the squares of each number sorted in ascending order

def sorted_squares(nums):
    n = len(nums)
    l, r = 0, n - 1
    res = [0] * n
    for i in range(n - 1, -1, -1):
        if abs(nums[l]) < abs(nums[r]):
            val = nums[l]
            l += 1
        else:
            val = nums[r]
            r -= 1
        res[i] = val**2
    return sorted(res)


nums = [-6, 2, 3, 4, 5, 7]
print(sorted_squares(nums))
