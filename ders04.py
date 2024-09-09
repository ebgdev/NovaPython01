# int()                                         # integera cevirmek icin
# print(int("234"))                             # 234


# float()                                       # float'a cevirmek icin                                      
# print(float("12.4"))                          # 12.4 uretir

# str()                                         # string'e cevirmek icin 
# print(str(128))                               # "128"
# print(str(128.5))                             # "128.5"

# ---------------------------------------------

# \n --> new line
# \t --> tab
# \a --> alert (ses yapar)

# print("merhaba",end="")
# print("dunya cok kuckuk")

# ---------------------reverse-list---------------------

# my_list = ["erfan","soner","yasemin","mehmet","gulten"]


# length = len(my_list)

# for i in range(length):
# 	print(my_list[-1*(i+1)])

# ------------------------------------------

# alist = [1,2,3,4,5]

# for i in range(len(alist)):
#     print(alist[len(alist)-i-1])


# i = 4

# while i>=0:
#     print(alist[i])
#     i-=1



# array = [1,2,3,4,5,6,7]
# array.reverse() # original array uzerinde islem yapar
#============
# for i in reversed(array):
#     print(i)

# print(array)
# ============
# print(array[::-1])
# -----------------------list-slicing----------------------

# alist[start:end:step]

# alist = [1,2,3,4,5,6,7,8]

# print(alist[0:-2:2])                              # [1, 3, 5]
# print(alist[::-1])                                # [8, 7, 6, 5, 4, 3, 2, 1]
# print(alist[:-1])                                 # [1, 2, 3, 4, 5, 6, 7], alist[-1].eleman kendisi dahil degildir
# print(alist[0:3])                                 # [1, 2, 3] , 3.index burada dahil degildir
# print(alist[::])                                  # [1, 2, 3, 4, 5, 6, 7, 8]
# print(alist)                                      # [1, 2, 3, 4, 5, 6, 7, 8]

# -----------------------nested-lists----------------------
# nested lists or 2d lists -turkcesi-----> ic ice listeler veya 2 boyutlu listeler
# myList = [[1,2,3],[4,5],[6]]
# print(myList[0])                                   # [1, 2, 3]
# print(myList[0][0])                                # 1
# print(myList[-1][0])                               # 6

# print each value in the list with for loop

# for i in myList:
#     for j in i:
#         print(j)

# print each value in the list with while loop

# i = 0
# while i < len(myList):
#     j = 0
#     while j < len(myList[i]):
#         print(myList[i][j])
#         j+=1
#     i+=1
