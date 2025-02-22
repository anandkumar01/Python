# Merge sort algorithm

def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = []
    right = []
    for i in range(0, mid):
        left.append(arr[i])
    for i in range(mid, n):
        right.append(arr[i])
    mergeSort(left)
    mergeSort(right)
    merge(arr, left, right)
    return arr


def merge(arr, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [5, 2, 4, 6, 4, 5, 2, 1, 8]
mergeSort(arr)
print(arr)
