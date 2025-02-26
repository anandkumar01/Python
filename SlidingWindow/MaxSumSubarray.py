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


nums = [2, -5, 1, 3, 7, -3, 2]
print(maxsumsubarray(nums))
