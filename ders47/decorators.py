# def hello():
#     return("hellooooooooooo")

# great = hello
# print(great)

# # <function hello at 0x102aa1440>

# great = hello()
# print(great)

# # hellooooooooooo

# del hello
# print(great)

# # hellooooooooooo

# -----------------------------

# def hello(func):
#     func()
# def greet():
#     print('still here!')

# a = hello(greet)
# print(a)

# # what we done here is we call the function hello 
# # with an argument of great which also is a function
# # and the the function great will call.

# -----------------------------
# # Higher Order Function --> HOC

# # 1- A function that accepts another function

# def greet(func):
#     func()


# # 2- A function that returns another function
# def greet2():
#     def func():
#         return 5
#     return func

# # bunlara ornek olarak map/reduce/filter fonksiyonuda soyleyebiliriz
# -----------------------------
# def my_decorator(func):
#     def wrap_func():
#         print('-------------')
#         func()
#         print('-------------')
#     return wrap_func # notice: we dont call the function here.

# @my_decorator
# def hello():
#     print('helloooooooo')

# # @my_decorator
# # def bye():
# #     print('good byeeeee')


# hello()

# # bye()

# # hello2 = my_decorator(hello)
# # hello2()


# # ----
# def hello():
#     print('helloooooooo')


# my_decorator(hello)()
# -----------------------------

# import time 

# def time_cal(func):
#     def wrapper(astr):
#         t1 = time.time()
#         result = func(astr)
#         t2 = time.time()
#         print(f"Execution time for func,  {t2 - t1} seconds")
#         return result
#     return wrapper

# @time_cal
# def isPalindrome(astr):
#     return astr == astr[::-1]

# print(isPalindrome('kazak'))


# -----------------------------
# Decorator Pattern

# import time 

# def time_cal(func):
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = func(*args, **kwargs)
#         t2 = time.time()
#         print(f"Execution time for func: {func.__name__},  {t2 - t1} seconds")
#         return result
#     return wrapper

# @time_cal
# def isPalindrome(astr):
#     return astr == astr[::-1]

# @time_cal
# def count_to_10():
#     for i in range(10):
#         i
#     return i

# print(isPalindrome('kazak'))
# print()
# print(count_to_10())
# ---------------------------------

# def log_call(func):
#     def wrapper(a, b):
#         print(f"Calling function with a={a}, b={b}")
#         result = func(a, b)
#         print(f"Result: {result}")
#         return result
#     return wrapper

# @log_call
# def add(a, b):
#     return a + b

# @log_call
# def introduce(name, age=30):
#     return f"My name is {name}, and I'm {age} years old."

# print(add(5, 7))
# print(introduce("Alice", age=25))

# ---------------------------------

# def log_call(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Result: {result}")
#         return result
#     return wrapper

# @log_call
# def add(a, b):
#     return a + b

# @log_call
# def introduce(name, age=30):
#     return f"My name is {name}, and I'm {age} years old."

# print(add(5, 7))
# print(introduce("Alice", age=25))


# ---------------------------------

# # Simulated user session
# session = {
#     "logged_in": True,  # Change to True to simulate login
#     "username": "john_doe"
# }

# def require_login(func):
#     def wrapper(*args, **kwargs):
#         if not session.get("logged_in"): # logged_in false oldugu zaman iceri girecektir
#             print("Access denied. Please log in first.")
#             return None
#         print(f"User '{session['username']}' is authenticated.")
#         return func(*args, **kwargs)
#     return wrapper

# @require_login
# def view_dashboard():
#     print("Welcome to your dashboard!")

# @require_login
# def edit_profile(new_name):
#     print(f"Profile updated to name: {new_name}")

# # Test examples
# view_dashboard()
# edit_profile("Jonathan Doe")

# -----------------------------------

