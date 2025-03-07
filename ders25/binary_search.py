def binary_search(lst:list,target:int) -> int:
    left = 0
    right = len(lst) -1
    mid = 0

    while left <= right:
        mid = (right+left)//2
        if target > lst[mid]:
            left = mid+1
        elif target < lst[mid]:
            right = mid - 1
        else:
            return mid
    return None


# T(n) = O(log n) # Worst Case
# T(n) = Ω(1) # Best Case

array = [2,14,22,28,36,48,62,75,88,94]

print(binary_search(array,48))


