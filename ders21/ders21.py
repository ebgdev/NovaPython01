# programlamanin ayrilmaz parcasi: hatalar

# biz yuzlerce kez bu hatalarla karsilasabiliriz syntax error veya turkcesi sözdizimi hatası.
# print('123)


# print("hello"+1) # TypeError

# an error that crashed our program like statments abova called an exceptions
# and python raises these exceptions whenever the interpreter says
# hey i have no idea what you're doing , but something is wrong
# so I'm going to give you the output


# Error Handling
# error handling allows us to let the python script continue running
# even if there are errors

# let's see some of the errors that we've already seen
# https://docs.python.org/3/library/exceptions.html

# ornek1 (syntax error)

# def deneme()
#     pass

# cunku boyle bir syntax python da tanimli degil
# -----------------

# ornek2 (NameError)

# def deneme():
#     1 + name


# deneme()
# cunku name tanimli degil
# -----------------

# ornkek3 (InedexError)
# def deneme():
#     lst = [1,2,3]
#     lst[5]

# cunku boyle bir index listemizde bulunmuyor

# -----------------

# ornek4 (KeyError)


# def deneme():
#     adict = {"a": 1}
#     adict["b"]


# deneme()
# cunku boyle bir key bulunmuyor.


# -----------------
# ornek5 (ZeroDivisionError)
# def deneme():
#     5 / 0


# deneme()
# cunku bolu 0 tanimsizdir

# -----------------
# bunlar surekli olarak gorecegiz dolayisiyla zaten o sira ne oldugunu anlayacaksiniz
# knowing them will help us to read them
# but the main question is how to avoid these ?

# bir cok uygulama dis dunya ile iletisimde


# def division(a: int, b: int) -> float:
#     # bruada birisi beklemediginiz bir sekilde 0 girebilir
#     # ve bu buyuk bir hataya neden olur
#     # ve eger bu buyuk bir sirket ise ona 1000'lerce dollar kaybettirebilir.
#     return a / b


# division(3, 0)

# bunun en buyuk orneklerini SQL Injection konusunu arastirarak gorebiliriz.

# age = int(input("what is your age? "))
# # age : lksjdfksdd --> ValueError
# # ama burada bir str cinsinde str girmediyse hata aliriz
# print(age)

# ------------------genel-yapi------------------
# try Block:
#     # Code that may raise an exception is placed in a try block.
# except Block:
#     # This block catches and handles exceptions raised in the try block.
#     # You can catch specific exceptions or use a generic exception handler.
# else Block (Optional):
#     # Executes if no exceptions were raised in the try block.
# finally Block (Optional):
#     # Executes regardless of whether an exception was raised or not, typically used for cleanup.


# -----------------

# try:
#     age = int(input("what is your age? "))
#     print(age)

# # yukarida herhangi bir sey hataya sebebiyyet verirse asagisi calisir
# except:
#     print("please enter a number")


# dolaysiyla bu sekilde program hic crash yapmadan hatayi bize duzeltme firsati verir
# ama bir sorun var program hatayi yakalamamiza izin versede
# program bir kez calistirdiktan sonra bitiyor.


# -1----------------

# while True:
#     try:
#         age = int(input("what is your age? "))
#         print(age)
#         break
#     except:
#         print("please enter a valid number")


# -2----------------
# burada ctrl-c artik bizi durduramaz
# cunku butun girisleri bir sayi girmedigimiz surece alacaktir

# while True:
#     try:
#         age = int(input("what is your age ? "))
#         print(age)
#     except:
#         print("Enter a VALID number")
#     else:
#         print("thank you!")
#         break


# -3----------------

# while True:
#     try:
#         user_input = input("What is your age? (type 'exit' to quit): ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break
#         age = int(user_input)
#         print(age)
#     except:
#         print("Enter a VALID number")
#     else:
#         print("Thank you!")
#         break


# -4----------------

# while True:
#     try:
#         user_input = input("What is your age? (type 'exit' to quit): ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break
#         age = int(user_input)
#         print(age)
#         # age -> 0 -> ZeroDivisionError
#         # age -> lksdjfsdf -> ValueError
#         # yukaridaki degerlerden hangisini girersek girelim
#         # error handling yapacagiz ama tabiki bu hatalar bir birinden farklidirlar
#         # dolayisiyla
#         10 / age
#     except:
#         print("please enter a number")
#     else:
#         print("thank you! ")
#         break


# -5-ValueError---------------
# # now the problem here is even when I enter a number , Im still gettin "pls enter a number message"
# # so this is a buggy program

# while True:
#     try:
#         user_input = input("What is your age? (type 'exit' to quit): ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break
#         age = int(user_input)
#         print(age)
#         # age -> 0 -> ZeroDivisionError
#         # age -> lksdjfsdf -> ValueError
#         # yukaridaki degerlerden hangisini girersek girelim
#         # error handling yapacagiz ama tabiki bu hatalar bir birinden farklidirlar
#         # dolayisiyla
#         10 / age
#     except:
#         print("please enter a number")
#     else:
#         print("thank you! ")
#         break


# ----------------------instead----------------------

# bu durumda eger ben 0 girersem hata alirim
# because I only except ValueErrors not the ZeroDivisionError
# while True:
#     try:
#         user_input = input("What is your age? (type 'exit' to quit): ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break
#         age = int(user_input)
#         print(age)
#         10 / age
#     except ValueError:
#         print("please enter a number")
#     except ZeroDivisionError:
#         print("please enter value higher than zero! ")
#     else:
#         print("thank you! ")
#         break


# ----------------------only-works-one-time-------------------

# when one of the except blocks run the others won't run

# while True:
#     try:
#         user_input = input("What is your age? (type 'exit' to quit): ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break
#         age = int(user_input)
#         print(age)
#         10 / age
#     except ValueError:
#         print("please enter a number")
#     except ValueError:
#         print("I will never see here")
#     except ZeroDivisionError:
#         print("please enter value higher than zero! ")
#     else:
#         print("thank you! ")
#         break


# ------------------------------------------------------------

# def sum(num1:int,num2:int):
#     try:
#         return num1+num2
#     except TypeError:
#         return "please enter numbers"

# print(sum('1',2))


# -------------------------common-way--------------------------

# def sum(num1:int,num2:int):
#     try:
#         return num1+num2
#     except TypeError as e:
#         return f"please enter numbers. error: {e}"

# print(sum('1',2))


# # -------------------------handle-all-at-once------------------------

# def division(num1:int,num2:int):
#     try:
#         return num1/num2
#     except (TypeError,ValueError,ZeroDivisionError) as e:
#         return f"Oops. error: {e}"

# print(division('1',2))
# print(division(1,0))

# ------------------------finally-----------------------
# find out outputs for 0 and 18 and then erase break in the else block and enter 18
# while True:
#     try:
#         age = int(input("what's your age? "))
#         10/age
#     except ValueError:
#         print("please enter a number")
#         continue
#     except ZeroDivisionError:
#         print("please enter age higher than 0")
#         break
#     else:
#         print("thank you")
#         # break
#     finally:
#         print("ok im finally done.")
#     print("can you here me")
#     break
