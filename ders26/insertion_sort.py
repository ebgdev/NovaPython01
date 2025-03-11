# Insertion Sort Algorithm in Python


def insertion_sort(arr):
    for current_index in range(1, len(arr)):
        current_value = arr[current_index]  # The element to be placed correctly
        previous_index = current_index - 1

        # Shift elements to the right to create the correct position for current_value
        while previous_index >= 0 and current_value < arr[previous_index]:
            arr[previous_index + 1] = arr[previous_index]
            previous_index -= 1

        # Insert the current_value at the correct position
        arr[previous_index + 1] = current_value


# Example usage
numbers = [9, 5, 1, 4, 3]
insertion_sort(numbers)
print("Sorted Array in Ascending Order:")
print(numbers)
