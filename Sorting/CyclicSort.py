# Cyclic sort algorithm of an array containing elements in range [0, n]

def cyclic_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        correct = arr[i]
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    return arr


arr = [3, 1, 0, 5, 2, 4]
print(cyclic_sort(arr))
