# gercek dunyada kodlari nasil bir biri ile kiyaslariz ?
# bunun icin parametremiz veya olcumumuz nedir ?
# elimizde eger iki kod var ise
# code1 ve code2 bunlardan hangisi daha iyi ?
# eger zamana gore hesaplamak istersek mesela code1 calisma suresi 1 dak
# ve code2 nin calisma suresi 3 dak ise bu durumda code1 belki daha verimli bir
# code olabilir bu sekilde olcum yaptigimzda buna Time Complexity
# veya zaman karmasikligi diyebiliriz ama bu varsayim ne kadar dogru ?

# ama aslinda Time Complexity aslinda zaman ile bir ilgisi yoktur
# cunku eger biz code2 yi daha guclu bir bilgisayarda calistirirsak
# bu durumda zamansal olarak code2 belkide daha hizli calismis olacaktir
# ama aslinda burada code2 daha iyi sayilmaz , bizim bilgisayarimiz gucludur demektir

# aslinda dikkat etmemiz gereken baska bir parametre daha vardir
# Space complexity -> uzay karmasikligi

# cok hizli calismistir ama cok memory kullanmistir
# veya code2 cok yavas calismis olabilir ama cok daha az memory kullanmistir

# note: genelde bizim icin cok onemli olan zamandir
# ama bazi durumlarda bazi nadir sirketler icin uzay da onemli olabilir
# burada her ikisinde deginecegiz ama derslerimiz kapsaminda en cok zaman
# karmasikligini onemsiyecegiz.

# --------------------------------------------

# my_list = [1,2,3,4,5,6,7,8,9]

# bu ders kapsaminda 3 tane latin karakterini gorecegiz
# - omega          :  Ω  :   Best Case
# - theta          :  θ  :   Avrage Case
# - omicron(big o) :  O  :   Worst Case


# --------------------------------------------


# def print_numbers(n):
#     counter = 0
#     for i in range(n):
#         counter += 1
#         print(counter)

# print_numbers(10)


# --------------------------------------------

# Drop Constants
# carpanlari atabiliriz.

# def print_numbers(n):
#     counter = 0
#     for i in range(n):
#         counter += 1
#         print(counter)

#     for i in range(n):
#         counter += 1
#         print(counter)


# print_numbers(10)
# so in this example we do run the code n + n times: 2n
# O(2n) and then we simplify the notation and drop the constant(sabit)
# so we get O(n)

# --------------------------------------------

# now let's look at O(n^2)


# def print_numbers(n):
#     counter = 0
#     for i in range(n):
#         for j in range(n):
#             counter += 1
#             print(i, j, counter)


# print_numbers(10)

# O(n*n) = O(n^2)

# --------------------------------------------

# now guess what should be this


# def print_numbers(n):
#     counter = 0
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 counter += 1
#                 print(i, j, k, counter)


# print_numbers(10)


# --------------------------------------------

# # Drop Non-Dominants


# def print_numbers(n):
#     counter = 0
#     for i in range(n):
#         for j in range(n):
#             counter += 1
#             print(i, j, counter)

#     for k in range(n):
#         counter += 1
#         print(k, counter)


# print_numbers(10)

# # O(n^2) + O(n) = O(n^2 + n)
# # burada bizim icin O(n) cok da onemli sayilmadiginda dolayi
# # burayida sadelestirebiliriz boylece bizim denklemimiz:

# # O(T):  O(n^2) olacaktir.


# --------------------------------------------

# # now let's look at O(1)


# def add_items(n):
#     return n + n


# print(add_items(10))

# # O(1 )

# # onceki yaptigimiz orneklerde n sayimiz arttikca
# # bizim denklemimiz de buyuyordu ama bu durumda sadece
# # toplamini yaptigimiz n buyuyor ve yaptigimiz islem sayisi
# # aslinda sabit (tek bir kere toplama islemi yapacagiz)


# --------------------------------------------

# # peki ya bu durum nasil ?

# def add_items(n):
#     return n + n + n


# print(add_items(10))

# # O(?)
# # burada asil soru su ki bizim yaptigimiz islem sayisi
# # degisiyor mu acaba ?

# --------------------------------------------

# now let's look at O(log n)
# lets's say we want to find 8

array = [1, 2, 3, 4, 5, 6, 7, 8]
# isleme baslayalim
array = [5, 6, 7, 8]
array = [7, 8]
array = [8]

# if we think of a list like [1,2,3,4,5,6,7,8,9]


# --------------------------------------------

# 1 < logn < n < nlogn < n^2,n^3,... < 2^n < n!
