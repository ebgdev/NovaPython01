# def deneme(a,b):
#     return a+1,b+13,"selam"



# print(deneme(1,2))

# ------------------count-and-is_in-function--------------------

# def is_in(data,item):
    
#     condition = False
#     for value in data:
#         if value == item:
#             condition = True
#     return condition        
    

# def counter(alist,target):
#     counter = 0
#     if is_in(alist,target) != True:
#         print("Item NOT FOUND: ",end="")
#         return counter
#     else:
#         for value in alist:
#             if value == target:
#                 counter+=1
#         return counter



# print(counter([88,55,33,22,55],55))

# ------------------max-list-and-value---------------------

# def maximum(data):
#     if type(data) != "list":
#         list_data = list(data)
#     else:
#         list_data = data
    
#     max_value = float("-inf")

#     for value in list_data:
#         if value > max_value:
#             max_value = value
#     return max_value


# def minimum(data):
#     min_value = float("inf")
#     if data:
#         for item in data:
#             if item < min_value:
#                 min_value = item
#     else:
#         print("there is an issue with data")
#         min_value = "Veri bulunamadi\n"
#     return min_value


# print(maximum([88,33,22,55]))
# print(minimum([88,33,22,55]))
# print(minimum([]))
# print(minimum([1]))

# --------------even-odd-------------------

# def is_even(x):
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")

# alist = [1,2,3,4,5]

# for i in alist:
#     is_even(i)

# print(is_even(5))
# print(is_even(18))
# -----------prime-v1--------
# def is_prime(num):
#     counter = 0
#     if num < 2:
#         return False
    
#     else:    
#         for i in range(2,num+1):
#             if num%i == 0:
#                 counter +=1
        
#         if counter > 1:
#             return False
#         else:
#             return True

# numbers = [1,2,3,6,7,11,34,65,2345,8934759834,98475,9827345]

# for number in numbers:
#     print(is_prime(number))

# # -----------prime-v2--------

# def is_prime(num):
#     counter = 0
#     if num < 2:
#         return False
    
#     else:    
#         for i in range(2,(num//2)+1):
#             if num%i == 0:
#                 counter +=1
        
#         if counter > 1:
#             return False
#         else:
#             return True

# numbers = [1,2,3,6,7,11,34,65,2345,98475,98273459]

# for number in numbers:
#     print(is_prime(number))

# -----------prime-v3--------
# import math 

# def check_prime(number):
#     if number < 2:
#         return False
#     sqrt_number = math.sqrt(number) 
#     for i in range(2, int(sqrt_number) + 1):
#         if number % i == 0:
#             return False 
#     return True

# print(check_prime(47))

# numbers = [1,2,3,6,7,11,34,65,2345,98475,98273459]
# for number in numbers:
#     print(check_prime(number))

# -------------------------------

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("radar"))  # Output: True
# print(is_palindrome("python"))  # Output: False

# palindromes = [
#     "racecar",
#     "level",
#     "deified",
#     "rotor",
#     "civic",
#     "madam",
#     "refer",
#     "kayak",
#     "repaper",
#     "radar"
# ]


# -----------------------------------------
# def factorial_v1(n):
#     if n < 0:
#         return "Invalid input. Please enter a positive integer."
#     result = 1
#     for i in range(2, n+1):
#         result *= i
#     return result

# print(factorial_v1(5))  # Output: 120

