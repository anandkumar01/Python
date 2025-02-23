# Rotate the array to the left by k steps

def left_rotation(arr, k):
    k = k % len(arr)
    return arr[k:] + arr[:k]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(left_rotation(nums, k))
