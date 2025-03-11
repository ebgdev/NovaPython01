# Devide and conquer algorithm
#   - breaks down the problem into multiple subproblems recursiveyly until they
#     become simple to solve
#   - Then the solutions will combine to solve the original problem

# 1- choose the pivot element (random,first,last)
# 2- store the elements less than pivot in the left subarray
#    store the elements greater than pivot in the right subarray
# 3- call quicksort recursively on left subarray
#    call quciksort recursivley on right subarray


# Example:
# array = [22,11,88,66,55,77,33,44]
# now if we pick 44
# then we should track our array using two pointers j and j
# which i is looking for items greater than pivot and j is looking for items less than pivot
# as soon as i found and later j found we'll swap the elemnts
# array = [22,11,33,66,55,77,88,44]
# this will continue until j is placed at the left of i
# at this phase we swap the elements at index i and p: swap(array[i],array[p])

# array = [22,11,33,44,55,77,88,66] now in here the elements that are greater than 44 placed in the right
# the others whcih are less placed at the left of the array


# ----------------------------------------------
# function to find the partition position
# this function returns the index of the pivot element after the first step of the quick sort
def partition(array, left, right):

    # choose the rightmost element as pivot
    pivot = array[right]

    i = left
    j = right - 1
    pivot = array[right]

    while i < j:
        # i moves to the right and j moves to the left until i and j cross
        # while i is not at the end of the array
        # and the element at the index i is less than pivot we'll increase i

        # cunku aslinda burasi true oldugu surece devam ediyor ve bizim aradigimiz
        # ise tam tersi yani array[i] > pivot
        while i < right and array[i] < pivot:
            i += 1
        # if j greater than left
        # and if the element at the index j is greater than pivot
        while j > left and array[j] >= pivot:
            j -= 1

        # now after the loops done we check if i and j cross yet
        # if the didnt cross we need to swap them the elements at index i with index at j
        if i < j:
            array[i], array[j] = array[j], array[i]
    # after i and j cross
    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]
    return i


# function to perform quicksort
def quickSort(array, left, right):
    # check array contains at least 2 elements
    if left < right:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, left, right)

        # recursive call on the left of pivot
        quickSort(array, left, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, right)


array = [22, 11, 88, 66, 55, 77, 33, 44]
print("Unsorted Array")
print(array)

size = len(array)

quickSort(array, 0, size - 1)

print("Sorted Array in Ascending Order:")
print(array)


# ----------------------------------------------

# Time complexity:
#   - O(n^2) Worst case
#   - O(n * logn) Best case


# En iyi durumda her seferinde pivot diziyi tam ortadan böler. Yani diziyi sürekli ikiye bölerek ilerleriz.
# n/2
# n/4
# n/8


# En kötü durumda, pivot her zaman en küçük veya en büyük eleman seçilirse, dizi çok dengesiz bölünür.

# Örneğin, zaten sıralı bir dizimiz varsa ve hep son elemanı pivot olarak seçiyorsak:
# O(1+(n-1)+(n-2)+(n-3)+(n-4)+...) = (n(n+1))/2 = O(n^2)
