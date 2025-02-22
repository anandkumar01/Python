# Allow at most one duplicate elements in sorted list

def allow_one_duplicate(nums):
    if not nums:
        return []
    count = {}
    res = []
    for num in nums:
        if count.get(num, 0) < 2:
            res.append(num)
            count[num] = count.get(num, 0) + 1
    return res


nums = [3, 4, 6, 6, 3, 2, 5, 3, 6, 6, 4, 7, 8]
print(allow_one_duplicate(nums))
