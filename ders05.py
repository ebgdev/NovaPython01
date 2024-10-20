#-----------------------2-sum------------------------

# my_list = [2 ,7 ,11 ,3 ,8 ,15 ,1]
# target = 9
# results = []
# length = len(my_list)

# for i in range(length-1):
#     for j in range(i+1,length):
#         if my_list[i] + my_list[j] == target:
#            results.append([i,j])
# if results == []:
#     print("No result found")
# else:
#     print(results)

#-----------------------2-sum---with-while---------------------
# i = 0
# while i < length-1:
#     j = i+1
#     while j < length:
#         if my_list[i] + my_list[j] == target:
#             results.append([my_list[i],my_list[j]])
#         j+=1
#     i+=1
# if results == []:
#     print("No result found")
# else:
#     print(results)

#-----------------------3-sum---with-while---------------------

# my_list = [2, 7, 11, 0, 3, 8, 15, 1]
# target = 9
# results = []

# length = len(my_list)

# for i in range(length - 2):
#     for j in range(i + 1, length - 1):
#         for z in range(j + 1, length):
#             if my_list[i] + my_list[j] + my_list[z] == target:
#                 triplet = sorted([my_list[i], my_list[j], my_list[z]])
#                 if triplet not in results:
#                     results.append(triplet)

# print(results)



# ------------------------sum-matrix------------------------------

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = [[0,0,0],[0,0,0],[0,0,0]]

# for i in range(len(matrix1)):
#     for j in range(len(matrix1)):
#         result[i][j] = matrix1[i][j]+matrix2[i][j]

# # printing matrix
# for i in result:
#     print(f"{i}\n")

# # iki matris nasil bir birine carpilir onu siz yapiniz 

# ------------------------------odev------------------------------

# kisi_sayisi = int(input("kac kisinin bilgisi girmek istersiniz ? "))

# bilgi_sirasi = ["isim ","meslek","yas"]
# alist = []

# for i in range(kisi_sayisi):
#     temp = []
#     for j in range(len(bilgi_sirasi)):
#         temp.append([])
#     alist.append(temp)

# i = 0

# while i < kisi_sayisi:
#     j = 0
#     while j < len(bilgi_sirasi):
#         alist[i][j] = input(f"{i+1}'inci kisinin {bilgi_sirasi[j]} bilgisini giriniz: ")
#         j+=1
#     i+=1

# print(alist)


# ------------------------------odev-ogretmen-cozumu----------------------------

# okul

member_count = int(input("kisi sayisini giriniz: "))
info_pri = ["isim","soyisim","yas","sinif"]

student_info = []

for i in range(member_count):
    temp_list= []
    for j in range(len(info_pri)):
        temp_value = input(f"{i+1}. kisi icin {info_pri[j]} giriniz: ")
        temp_list.append(temp_value)
    student_info.append(temp_list)

print(student_info)
