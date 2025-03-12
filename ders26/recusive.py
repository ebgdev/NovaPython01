# def factorial(n):
#     # stop point olmali
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(5))

# # factorial(5) = 5 * factorial(4)
# # factorial(4) = 4 * factorial(3)
# # factorial(3) = 3 * factorial(2)
# # factorial(2) = 2 * factorial(1)
# # factorial(1) = 1 * factorial(0)

# # factorial(0) = 1
# # factorial(1) = 1
# # factorial(2) = 2
# # factorial(3) = 6
# # factorial(4) = 4 * 6 = 24
# # factorial(5) = 5 * 24 = 120

# Time Complexity: O(n)

# -------------------------------------


# def fibo(n):
#     # stop point
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)


# print(fibo(6))

# # fibo(6) = fibo(5) + fibo(4)
# # fibo(5) = fibo(4) + fibo(3)
# # fibo(4) = fibo(3) + fibo(2)
# # fibo(3) = fibo(2) + fibo(1)
# # fibo(2) = fibo(1) + fibo(0)
# # fibo(0) = 0
# # fibo(1) = 1
# # fibo(2) = 0 + 1 = 1
# # fibo(3) = 1 + 1 = 2
# # fibo(4) = 2 + 1 = 3
# # fibo(5) = 3 + 2 = 5
# # fibo(6) = 5 + 3 = 8

# what is the time complexity ? (odev)

# -------------------------------------


# def sum_up_n(n):
#     if n == 0:
#         return 0
#     return n + sum_up_n(n - 1)


# print(sum_up_n(5))

# # sum_up_n(5) = 5 + sum_up_n(4)
# # sum_up_n(4) = 4 + sum_up_n(3)
# # sum_up_n(3) = 3 + sum_up_n(2)
# # sum_up_n(2) = 2 + sum_up_n(1)
# # sum_up_n(1) = 1 + sum_up_n(0)
# # sum_up_n(0) = 0
# # sum_up_n(1) = 1 + 0 = 1
# # sum_up_n(2) = 2 + 1 = 3
# # sum_up_n(3) = 3 + 3 = 6
# # sum_up_n(4) = 4 + 6 = 10
# # sum_up_n(5) = 5 + 10 = 15

# Time Complexity: O(n)

# -------------------------------------


# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return s[-1] + reverse_string(s[:-1])


# print(reverse_string("hello"))


# Time Complexity: O(n)

# -------------------------------------

# def power(base, exp):
#     if exp == 0:
#         return 1
#     return base * power(base, exp - 1)

# print(power(2, 3))  # Output: 8

# Time Complexity: O(exp) or O(n)

# -------------------------------------

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# print(gcd(48, 18))  # Output: 6

# Time Complexity: O(log(min(a, b)))
