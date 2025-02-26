# Minimal length of a subarray whose sum is greater than or equal to target.
# positive integers array

def min_len_subarray(nums, target):
    n = len(nums)
    if not nums:
        return 0
    min_len = n + 1
    w_sum = 0
    w_start = 0
    for w_end in range(n):
        w_sum += nums[w_end]
        while w_sum >= target:
            w_sum -= nums[w_start]
            min_len = min(min_len, w_end - w_start + 1)
            w_start += 1
    
    if min_len <= n:
        return min_len
    return 0


nums = [7, 3, 2, 1, 6, 3, 1]
target = 11
print(min_len_subarray(nums, target))
