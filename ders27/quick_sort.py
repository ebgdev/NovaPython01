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


array = [11, 12, 13, 14, 15, 16, 17, 18]
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
