def selection_sort(arr,n):
    for current_index in range(n):
        min_index = current_index

        for next_index in range(current_index+1,n):
            if arr[min_index] > arr[next_index]:
                min_index = next_index

        arr[min_index] , arr[current_index] = arr[current_index],arr[min_index]
    return arr


array = [56,98,-100,985,285]
n = len(array)
print(selection_sort(array,n))