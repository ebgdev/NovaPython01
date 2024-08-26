# List unpacking 

# x,y,z = ["erfan","anil","ceren","yasemin"]
# print(x)
# print(y)
# print(z)

# --------------------True-and-False---------------------------

# bool(1)                        # True  
# bool(0)                        # False
# bool([])                       # False
# print(bool(-1))                # True

# --------------------True-and-False---------------------------

# print("1",False or True)
# print("2",False or False)
# print("1+",False and True)
# print("2+",False and False)
# print("3",True or True)
# print("4",not True)
# print("5",False + True)
# print("6",False * False)
# print("7",True * False)
# print("8",True * True)
# print("9",False**2)
# print("10",True**2)
# print("11",True*10)
# print("12",False*10)
# print(not True * True)
# print(not True and not True)


# -----------------------------uzun-string----------------------------------

# name = """
# this is erfan and im a computer engeenering student at post bacholor degree
# ai is the most trend maybe these days i would love to become an expret in this topic 
#     """

# name1 = "this is erfan and im a computer engeenering student at post bacholor degree \nai is the most trend maybe these days i would love to become an expret in this topic "

# print(name)
# print(name1)

# ---------------------------Operators Precedence Rule----------------------
# islem oncelikleri

# 1st-Parentheses --> ()

# 2nd-Exponents --> **

# 3rd-Multiplication and Division --> *, /

# 4th-Addition and Subtraction --> +, -


# print(3*(8+4**2/2*3))

#----------------------------------odev-1-2--------------------------------------

#-------------2.dereceden denklem

# import math
# print("Welcome to our Ax^2 + Bx + C equation solution: ")
# print("Enter the A, B, C values by order (press enter after each input): ")

# alist = []
# for i in range(3):
#     alist.append(int(input("Enter value: ")))

# print(f"Our equation now is {alist[0]}x^2 + {alist[1]}x + {alist[2]}")
# a, b, c = alist[0], alist[1], alist[2]
# delta = (b ** 2) - (4 * a * c)

# if delta < 0:
#     print(f"The delta = {delta} has no real roots")
# elif delta == 0:
#     print(f"The delta = {delta} so we have one repeated root: x1 = x2 = {(-b) / (2 * a)}")
# else:
#     x1 = (-b + math.sqrt(delta)) / (2 * a)
#     x2 = (-b - math.sqrt(delta)) / (2 * a)
#     print(f"The delta = {delta} so we have two unequal roots\nx1 = {x1} and x2 = {x2}")

#-------------Reverse Loop

# alist = ["erfan","anil","adil","emir"]
# new_list = []

# index = len(alist)-1
# while index>=0:
#     print(alist[index])
#     new_list.append(alist[index])
#     index-=1

# print(new_list)
#      ------------------------
# length = len(alist)*-1
# index = -1
# while index>=length:
#     print(alist[index])
#     index-=1


# for i in range(len(alist)):
#     print(alist[len(alist)-1-i])

# for i in range(1,len(alist)+1):
#     print(alist[-1*i])

