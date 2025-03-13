# split array in half
# call merge sort on each half to sort them recursivley
# merge both sorted halves into sorted array


# -----------------------------


def mergeSort(array):
    # if len is not greater than 1 means the array is sorted.
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array) // 2
        left_array = array[:r]
        right_array = array[r:]

        # -------recursive part-------
        # sort the two halves
        mergeSort(left_array)
        mergeSort(right_array)

        # -------merge part-------
        # i left most element in left array
        # j eft most element in right array
        # k merged array index

        i = j = k = 0

        # until we reach either end of either left array or right_array, pick larger among
        # elements left array and right array and place them in the correct position at A[p..r]
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        # when we run out of elements in either left_array or right_array,
        # pick up the remaining elements and put in A[p..r]
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1


if __name__ == "__main__":
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)
    print("Sorted array is: ")
    print(array)
