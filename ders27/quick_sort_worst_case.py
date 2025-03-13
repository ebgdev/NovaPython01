worst_case_counter = 0  # Counter for worst-case scenario


def partition_worst(array, left, right):
    global worst_case_counter
    pivot = array[right]

    i = left
    j = right - 1

    while i < j:
        while i < right and array[i] < pivot:
            i += 1
            worst_case_counter += 1  # Count comparison
        while j > left and array[j] >= pivot:
            j -= 1
            worst_case_counter += 1  # Count comparison
        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]
    return i


def quickSort_worst(array, left, right):
    if left < right:
        pi = partition_worst(array, left, right)
        quickSort_worst(array, left, pi - 1)
        quickSort_worst(array, pi + 1, right)


array_worst = [1, 2, 3, 4, 5, 6, 7, 8]  # Already sorted input
print("Worst Case Unsorted Array:", array_worst)

quickSort_worst(array_worst, 0, len(array_worst) - 1)

print("Worst Case Sorted Array:", array_worst)
print(f"Total comparisons in Worst Case: {worst_case_counter}")
