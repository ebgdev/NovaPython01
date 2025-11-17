# number = 12                   # int or integer
# number_in_str = "12"          # here the variable type is str or string

# -------------int()------------- 
# pi = 3.14
# print(int(pi))                 #cikti veya output --> 3

# -------------float()-------------
# num = 4
# print(float(num))              # cikti veya output --> 4.0

# -------------str()-------------

# number = 13
# new_number = str(number)
# print(type(number))              # output :  <class 'int'>
# print(type(new_number))          # output :  <class 'str'>

# -------------concatenate-------------

# print("14"+3)                      # output : Hata verir !!! can only concatenate str (not "int") to str
#                                    # bir str veri tipi ile bir int toplanamaz

# print("nova" + " "+ "akademi")     # output : nova akademi

# -------------operators-------------

# tek esitlik: (=) degiskene veya variable'a deger atamak icin ex: name = "john"
# cift esitlik (==) esitmidir diye kontrol eder ex: 3 == 3.0  output: True
# esit degil ise (!= ) ex : "yasemin" != "kemal"  output: True
# ( >= ) buyuk esit 
# ( <= ) kucuk esit

# 1-( // )--> kesme islemi yapan
# example : 

# print(5/4)                          # output : 1.25
# print(5//4)                         # output : 1

# 2-( ** ) --> ustlu sayilar icin

# print(2**3)                         # 2 uzere 3 = 8
# print(4**2)                         # 4 uzere 2 = 16

# 3-( % ) --> mod islemleri icin

# print(18 % 4)                       # 18 bolu 4 kalani = 8

# -------------if-elif-else-----------

# eger kosul:
#     calisacak kod
# egerde kosul:
#     calisacak kod
# egerde kosul:
#     calisacak kod
# aksi_taktirde:
#     bunu yap

# ----------------------------

# ex: 

# sehir = "samsun"

# if sehir == "samsun":                                                           #<===
#     print("55")                                                                     #
#     sehir = "trabzon"                                                               #
# if sehir == "trabzon":                                                          #<===
#     print("61")                                                                     #
#     sehir = "istanbul"                                                              #
# elif sehir == "istanbul":                                                           #
#     print("34")                                                                     #      if elif else blogu sadece bir kere calisir
#     sehir = "kastamonu"                                                             #      kosullardan herhangi birisi saglanirsa diger
# else:                                                                               #      kosullar dikkate alinmaz.
#     # else de sart YAZILMAZ - else can NOT contain condition                        #
#     print("sehiri tahmin edemedim")                                                 #
#                                                                                 #<===  
# print(sehir)
# ----------------------------
# ex: cift mi tek mi ?

# if sayi %2 == 0:
#     print("sayi cifittir")
# else:
#     print("sayi tektir")

# -------------input-in-python---------

# variable = input("bir girdi girniz : ")           # kullanicidan klavye ile bir girdi alinir
# print(type(variable))                             # girilen degerler str veya string'dir


# sayi = int(input("bir sayi giriniz: "))
# print(type(sayi))                                 # girilen girdinin veri tipi integer'dir


#--------------python-dosyasi-calistirmak------------

# cd --> change directory


# 1- cd file_address
# 2-python file_name.py                             # use python3 if you are in mac\linux

