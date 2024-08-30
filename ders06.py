# # ------------------------------odev------------------------------

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
#             elif secim != 1 and secim != 2:
#                 print("basarili bir sekilde cikis yaptiniz")
#                 quit()
#         else:
#             print("basarili bir sekilde sifreniz olusturuldu.")
#             break
# ----------------------------# fonksiyonlar-veya-functions------------------------------

# def function_name(parameter):
#     #statement
#     return expression

# --------------------------------------------

# def say_hi(isim):
#     return f"Merhaba, {isim}!"

# print(say_hi("erfan"))
# ------------------area-of-circle------------

# import math

# def area_of_circle(radius):
#     return math.pi * radius ** 2


# radius = 5
# print(f"when radius is: {radius} area is: {area_of_circle(radius):.2f}")



# ----------------sum-2------------------

# def add(num1: int, num2: int) -> int:
#     num3 = num1 + num2
#     return num3


# num1, num2 = 5, 15
# ans = add(num1, num2)
# print(f"The addition of {num1} and {num2} results {ans}.")


# ---------length-----------

# def length(data):
#     for i,value in enumerate(data):
#         continue
#     return i

# print(length("selam"))

# ---------max-2----------

# def maximum(num1,num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2


# print(maximum(5,8))

# ---------max-3----------

# def maximum(num1,num2,num3):
#     numbers = [num1,num2,num3]
#     max_value = float("-inf")
#     for num in numbers:
#         if num > max_value:
#             max_value = num
#     return max_value
        
# print(maximum(5,8,11))



# -----------list-unpacking-plus-------------

# toyota,*vw,mercedes,bmw = ["lexus","audi","bently","lamborgini","porsche","bugatti","smart","rolls royce"]
# print(toyota)
# # print(vw) ---> this is a list which contain ['audi', 'bently', 'lamborgini', 'porsche', 'bugatti']
# print(mercedes)
# print(bmw)


# def topla(*veri):
#     top_veri = list(veri)
#     top = 0
#     for item in top_veri:
#         top+=item
#     return top

# print(topla(11,11,11))

# ------------------in-function--------------------

# def is_in(data,item):
    
#     condition = False
#     for value in data:
#         if value == item:
#             condition = True
#     return condition        
    


# print(is_in([88,33,22,55],22))