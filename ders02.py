## kimya_yuzdesi = 1
# mat_yuzdesi = 3
# fizik_yuzdesi = 2

# fizik = int(input("fizik sivavinin puanini giriniz: "))
# matematik = int(input("matematik sinavinin puanini giriniz: "))

# ortalama = ((mat_yuzdesi * matematik)+(fizik_yuzdesi*fizik))/5
# print(f"bu ogrencinin not ortalamasi: {ortalama}")

# print("you passed the exam") if ortalama > 60 else print("you failed")

#---------------------------------

# tahimin oyunu
# import random 
# gercek_deger = random.randint(1,10)
# kosul = True
# tahmin = int(input("0..100 arasi bir deger giriniz\n"))
# while kosul:
#     if tahmin == gercek_deger:
#         print("TEBRIKLER,DOGRU tahminde bulundunuz\n")
#         break
#     elif tahmin > gercek_deger:
#         print("gercek deger daha KUCUK bir daha deneyiniz\n")
#     else:
#         print("gercek deger daha BUYUK bir daha deneyiniz\n")
#     tahmin = int(input("0 ile 100 arasi tahmini bir tam sayi degeri giriniz --> "))

#----------------loop---------------------------------loop---------------------------------loop-----------------
# iki cesit donguleri(loop) donebiliriz

# 1 - for loop
# 2 - while loop 

# ex:
#---------------------------------

# name = "nova akademi"
# for char in name:
#     print(char)
#---------------------------------

# listeler python en onemli veri yapilarindan biridir ve verileri tutmamizi saglarlar

# ogrenciler = ["burak","yusuf","anil","alperen","adil","mess","enes","taha","arda","emir","ahmet","bahdir"]

# print(ogrenciler[0])                            #-->dizideki ilk elemani verir

# print(ogrenciler[-1])                           #-->dizideki son elemani verir
# print(ogrenciler[len(ogrenciler)-1])            #-->dizideki son elemani verir

# -------------------------------------

# # for ile dongu
# for ogrenci in ogrenciler:
#     # dizideki butun elemanlari yazdirir
#     print(ogrenci)

# -------------------------------------

# while ile dongu
# i = 0                                              #initial value veya ilk deger
# while i < len(ogrenciler):
#     print(ogrenciler[i])
#     i+=1
# -----------------enumerate------------------------------

# names = ["bahadir","samet","erdal","yasemin"]
# brands = ["toyota","fiat","seat","nissan"]

# for indx,_ in enumerate(names):
#     print(f"sayin {names[indx]}'in en cok sevdigi araba: {brands[indx]}")

# -------------------------------------
# fibonacci
# array = [0,1]

# for i in range(10):
#     array.append(array[-1]+array[-2])

# print(array)


# ----------------------------------------

# numbers = [100, 84, 12, 17, 1, 25, 95, 58, 9, 81, 57, 91, 91, 70]
# result = 0
# # print(sum(numbers))

# for number in numbers:
#     result+=number

# print(result)
