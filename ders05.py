#-----------------------2-sum------------------------

# my_list = [2 ,7 ,11 ,3 ,8 ,15 ,1]
# target = 100
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
#             results.append([i,j])
#         j+=1
#     i+=1
# if results == []:
#     print("No result found")
# else:
#     print(results)

# ------------------------sum-matrix------------------------------

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# result = [[0]*3]*3

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

# ------------------------------odev------------------------------

#sifre sorusu : 
# first_pass , second_pass = "",""

# while True:
#     first_pass = input("Bir sifre belirleyiniz: ")
#     if len(first_pass)<8:
#         print(f"Belirtmis oldugunuz sifre {len(first_pass)} karakterli\nSifreniz en az 8 karakter olmali")
#     else:
#         second_pass = input("girmis oldugunuz sifreyi tekrarlayiniz: ")
#         while second_pass != first_pass:
#             print("!!! Girdiginiz tekrar sifresi yanlis")
#             print("----------------------------------")
#             print("sifre tekrarini bir daha denemek icin 2'i tuslayiniz")
#             print("bastan sifre belirtmek icin 1'i tuslayiniz")
#             print("Tamamen uygulamadan cikmak icin 0'i tuslayiniz")
#             secim = int(input("deger giriniz: "))
#             if secim == 2:
#                 second_pass = input("girmis oldugunuz sifreyi tekrarlayiniz: ")
#             elif secim == 1:
#                 print("bastan sifre belirtmek icin yonlendiriyorsunuz ")
#                 break
#             else:
#                 quit()
#         else:
#             print("basarili bir sekilde sifreniz olusturuldu.")
#             break
