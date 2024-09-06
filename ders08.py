# ----------------------odev---------------------------

# my_str = "tarak"


# def is_palindorme(my_str):
#     length = len(my_str)
#     palindormes = []
#     for i in range(length):
#         for j in range(i+3,length+1):
#             applicant_str = my_str[i:j]
#             if applicant_str == applicant_str[::-1]:
#                 palindormes.append(my_str[i:j])
#     return palindormes

# print(is_palindorme(my_str))

# -----------------------------------------

## Global variable
# y = 10

# def modify_global():
#     global y
#     y = 20
#     print(f"Inside the function, y = {y}")

# modify_global()
# print(f"Outside the function, y = {y}")


# --------------------------------

# y = 20  # y is a global variable

# def example():
#     print(y)  # y can be accessed inside the function

# example()
# print(y)  

# --------------------------------
# z = 100
# def outer_function():
#     z = 10  # z is a local variable in outer_function

#     def inner_function():
#         nonlocal z  # z is treated as nonlocal in inner_function
#         z = 40
#         print(f"Inside inner_function, z = {z}")

#     inner_function()
#     print(f"Inside outer_function, z = {z}")

# outer_function()
# ------------------------------------

# Global variable
# x = 10

# def outer_function():
#     # Local variable in outer_function
#     local_x = 20
    
#     def inner_function():
#         # Modify the local variable of outer_function
#         nonlocal local_x
#         local_x = 30
#         print(f"Inside inner_function, nonlocal x = {local_x}")
        
#         # Modify the global variable
#         global x
#         x = 40
#         print(f"Inside inner_function, global x = {x}")

#     inner_function()
#     print(f"Inside outer_function, after calling inner_function, nonlocal x = {local_x}")

# outer_function()
# print(f"Outside, global x = {x}")


# -----------------------LAMBDA-FONKSIYONU-------------------------

# lambda arguments: expression

# def ve lambda ikiside fonksiyon ama aralarindaki fark:
# def kullanildiginda o fonksiyona isim vermemiz gerekir ama lambda isimsiz bir fonksiyon(anonymous)
# lambda fonksiyonlarinda sonucu return etmeye gerek yoktur

# -------------------------------------------------# -------------------------------------------------
# -1-
# def add_ten(x):
#     return x+10
# -2-
# add_ten = lambda x: x + 10
# -result-
# print(add_ten(5))

# print(type(add_ten)) #--> her iki durum icin de <class 'function'> uretir
# -------------------------------------------------# -------------------------------------------------


# print((lambda x:x+10)(5))                 # sadece 5 sayisini fonkisyona atamak(assign)


# ----------------1-----------------
# liste = [1,2,3,4]                           # bir fonksiyon tanimlayip onu atamak
# iterative = ((lambda x:x+10)(x)for x in liste)

# print(iterative)                             # <generator object <genexpr>
# for item in iterative:
#     print(item)

# ----------------2-----------------
# liste = [1,2,3,4]                           # bir fonksiyon tanimlayip onu atamak

# print([(lambda x:x+10)(x)for x in liste])

# -------------------------------------------------# -------------------------------------------------
 
# multiply = lambda a, b: a * b
# print(multiply(3, 4))

# ----------------------------------------------

numbers = [1, 2, 3, 4, 5]
# -1-
# squared = [(lambda x:x*x)(x)for x in numbers ]
# print(squared)
# -2-
# def my_map(my_func,my_iter):
#     results = []
#     for item in my_iter:
#         new_item = my_func(item)
#         results.append(new_item)
#     return results

# squared = my_map(lambda x:x*x,numbers)
# print(squared)
# -3-
# squared = map(lambda x:x*x,numbers)
# print(list(squared))

# ----------------------------------------------
# my_list = ["erfan","enes"]

# print(list((lambda x:x+" python ogreniyor")(x)for x in my_list))

# ----------------------------------------------

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# evens = filter(lambda x: x % 2 == 0, numbers)
# print(list(evens))  # Output: [2, 4, 6, 8]

# --------------------lists-------------------------

# names = ["erfan","burak","alperen"]

# names.append('anil')                            
# names.append(['adil' , 'mess'])             
# names.extend (['mess' , 'onur'])            
# names.insert ( 2 , 'bob')                   
#                                             
# names.insert ( 5 , 'enes')
# names.remove ('onur')                       
# names.pop()                                 
# names.pop(2)                                
# print (names)                               
# print (names.pop(2))                        
# print(names.index('enes'))                
# print(names.index('enes' ,  2))           
#                                           
# print(names.index('enes' ,2,5))           
#                                           
# print (names.count('enes'))
# names.clear()                             
# print (names)                             


# names.sort()                              

# print (names.sort())                      

# names.reverse()                          
# print(names)