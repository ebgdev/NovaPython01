# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))  # Output: 120

# Time Complexity: O(n)

# ---------------------

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))  # Output: 8

# Time Complexity: O(2^n)

# ---------------------

# def sum_n(n):
#     if n == 0:
#         return 0
#     return n + sum_n(n - 1)

# print(sum_n(5))  # Output: 15

# Time Complexity: O(n)

# ---------------------

# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return s[-1] + reverse_string(s[:-1])

# print(reverse_string("hello"))  # Output: "olleh"

# Time Complexity: O(n)

# ---------------------

# def power(base, exp):
#     if exp == 0:
#         return 1
#     return base * power(base, exp - 1)

# print(power(2, 3))  # Output: 8

# Time Complexity: O(exp) or O(n)

# ---------------------

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# print(gcd(48, 18))  # Output: 6

# Time Complexity: O(log(min(a, b)))
