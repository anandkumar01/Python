# Find the second largest element in the list

def second_largest(nums):
    largest = float("-inf")
    s_largest = float("-inf")

    for num in nums:
        if num > largest:
            s_largest = largest
            largest = num
        elif num > s_largest and num != s_largest:
            s_largest = num
    return s_largest


nums = [3, 6, 2, 7, 1, 9]
print(second_largest(nums))
