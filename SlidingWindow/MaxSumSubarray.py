# find maximum sum of subarray

def maxsumsubarray(nums):
    if not nums:
        return 0
    max_sum = float("-inf")
    cur_sum = 0
    for num in nums:
        cur_sum += num
        if cur_sum > max_sum:
            max_sum = cur_sum
        if cur_sum < 0:
            cur_sum = 0
    return max_sum

# Return subarray with maximum sum
def subarray_with_maxsum(nums):
    if not nums:
        return []
    max_sum = float("-inf")
    cur_sum = float("-inf")
    start, end = 0, 0
    w_start = 0
    for w_end in range(len(nums)):
        cur_sum += nums[w_end]
        if cur_sum > max_sum:
            max_sum = cur_sum
            start = w_start
            end = w_end
        if cur_sum < 0:
            cur_sum = 0
            w_start = w_end + 1

    return nums[start : end + 1]


nums = [2, -5, 1, 3, 7, -3, 2, 7]
print(subarray_with_maxsum(nums))
