best_case_counter = 0  # Counter for best-case scenario


def partition_best(array, left, right):
    global best_case_counter
    mid = (left + right) // 2
    array[mid], array[right] = array[right], array[mid]  # Swap mid with rightmost
    pivot = array[right]

    i = left
    j = right - 1

    while i < j:
        while i < right and array[i] < pivot:
            i += 1
            best_case_counter += 1  # Count comparison
        while j > left and array[j] >= pivot:
            j -= 1
            best_case_counter += 1  # Count comparison
        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]
    return i


def quickSort_best(array, left, right):
    if left < right:
        pi = partition_best(array, left, right)
        quickSort_best(array, left, pi - 1)
        quickSort_best(array, pi + 1, right)


# array_best = [22, 11, 88, 66, 55, 77, 33, 44]
array_best = [11, 12, 13, 14, 15, 16, 17, 18]
print("Best Case Unsorted Array:", array_best)

quickSort_best(array_best, 0, len(array_best) - 1)

print("Best Case Sorted Array:", array_best)
print(f"Total comparisons in Best Case: {best_case_counter}")
