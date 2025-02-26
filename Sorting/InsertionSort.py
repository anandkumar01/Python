def insertion_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr

arr = [5, 3, 2, 8, 6, 9, 4, 1]
print(insertion_sort(arr))
