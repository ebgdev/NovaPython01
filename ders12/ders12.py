# import secondery
# import cekilis.cekilis as ck
# import shopping.shopping_cart as shop
# # # from shopping import shopping_cart
 
# # from secondery import sum_2 , devide_2
# # from secondery import *

# # print(shopping.shopping_cart.buy("tshirt")) 
# # print(sum_2(3,4))
# print(secondery.sum_2(3,4))
# print(ck.cekilis(["bmw","mercedes"],["tom","john"]))
# print(shop.buy(["tshirt","jeans"]))




# -----------------------------

# import random 
# print(random)

# -----------------------------
# from random import choice

# cars = ["skoda","merc","fiat","toyota"]
# print(choice(names))
# -----------------------------

# cars = ["skoda","merc","fiat","toyota"]
# names = ['enes','mess','anil','alperen']

# import cekilis
# print(cekilis.cekilis(names,cars))

# -----------------------------
# import sys

# print("this is argv[0]: ",sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
# -----------------------------


# ================================string=methods===============================


# my_str = "nova AKADEMI programlama egitimi yapilmakta."

# print("upper: ",my_str.upper())                   # butun karakterleri buyuk yapar
# print("lower: ",my_str.lower())                   # butun karakterleri kuckuk yapar
# print("capitalize: ",my_str.capitalize())              # sadece ilk karakteri buyuk yapar
# print("title: ",my_str.title())         # her kelimenin ilk karakteri buyuk yapar
# print("replace: ",my_str.replace("nova","bahcivan"))
# print("find: ",my_str.find("programlama"))
# print("swapcase: ",my_str.swapcase())

# # split() method splits a string into a 
# # list of strings after breaking the given string by the specified separator.

# new_list = my_str.split()
# # new_list = my_str.split(" ")
# print(new_list)

# new_str = "adil, anil, emir, alperen, taha"
# print(new_str.split(","))
# print(new_str.split("a"))


# very_new_str = '-'.join("nova")
# print(very_new_str)

# list1 = ["n","o","v","a"]
# print("".join(list1))

# -----------------------------------

# my_str = "      merhaba dunya!      "
# print("strip:",my_str.strip())
# print("lstrip:",my_str.lstrip())
# print("rstrip:",my_str.rstrip())

# websites = [
#     "www.amazon.com",
#     "www.google.com",
#     "www.github.com",
#     "www.w3.org"
# ]

# plain_url = []

# for link in websites:
#     plain_url.append(link.lstrip("w."))

# print(plain_url)

# plain_url_plus = []
# for link in websites:
#     plain_url_plus.append(link.removeprefix("www."))

# print(plain_url_plus)

# -----------------------------------

# str = "NovaSamsunNova"
 
# # startswith()
# print(str.startswith("Nova"))
# print(str.startswith("Nova", 4, 10))
# print(str.startswith("Nova", 10, 14))
 
# print("\n")
 
# # endswith
# print(str.endswith("Nova"))
# print(str.endswith("Nova", 2, 8))
# print(str.endswith("Samsun", 4, 10))

# -----------------------------------