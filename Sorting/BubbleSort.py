def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(1, n - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [3, 5, 2, 7, 1, 4, 6]
print(bubble_sort(arr))
