def bubble_sort(lst):
    counter = 0
    for i in range(len(lst)):
        for j in range(0,len(lst)-1-i):
            if lst[j] > lst[j+1]:
                counter += 1
                # ----1.yontem----
                # temp = lst[j]
                # lst[j] = lst[j+1]
                # lst[j+1] = temp
                
                # ----2.yontem----
                lst[j] , lst[j+1] = lst[j+1] , lst[j]
    return lst,counter   

# print(bubble_sort([56,98,-100,985,285]))
print(bubble_sort([9,8,7,6,5])) # worst case O(n^2)
print(bubble_sort([1,2,3,4,5])) # best case O(n)




[-100,56,98,285,985]