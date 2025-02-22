# Quick sort algorithm

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


arr = [7, 9, 3, 2, 4, 5, 1, 6, 4, 5]
print(quicksort(arr))
