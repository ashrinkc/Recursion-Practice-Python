def quicksort(arr):
    if len(arr) <= 1:
        print(arr)
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("l", left)
    print("r", right)
    return quicksort(left) + middle + quicksort(right)


print(quicksort([2, 5, 6, 1, 2]))
