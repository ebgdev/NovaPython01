# array = ["emir", "adil", "mess"]


# with open("isimler.txt", "w") as file:
#     file.writelines(name + "\n" for name in array)


# ------------------------throw-our-error-----------------------

# while True:
#     try:
#         age = int(input("what is your age ? "))
#         # print(age)
#         if age < 0 or age > 120:
#             raise ValueError('age range is invalid')
#     except ValueError as e:
#         print(f"Enter a VALID number.\nError:{e}")
#         break
#     else:
#         print("thank you!")
#         break


# Q1---------------------------------------------------------

# try:
#     print("Trying to divide...")
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print(f"Error occurred: {e}")
# finally:
#     print("How about me?")


# Q2---------------------------------------------------------

# def check_age(age):
#     if age < 0 or age > 120:
#         raise Exception("Invalid age range!")
#     return 10 / age

# try:
#     age_input = int(input("Enter your age: "))
#     result = check_age(age_input)
#     print(f"Result: {result}")
# except Exception as e:
#     print(f"Error: {e}")

# Q2-Answer--------------------------------------------------------

# def check_age(age):
#     if age < 0 or age > 120:
#         raise ValueError("Age must be between 0 and 120!")
#     return 10 / age

# try:
#     age_input = int(input("Enter your age: "))
#     result = check_age(age_input)
#     print(f"Result: {result}")
# except ValueError as ve:
#     print(f"Invalid input: {ve}")
# except ZeroDivisionError:
#     print("Age cannot be zero, as it causes a division error.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# else:
#     print("Thank you for providing a valid age!")


# -------------------------------------------------------

# a. Arithmetic Errors
#     ZeroDivisionError: Division by zero.
#     Example: 10 / 0

#     OverflowError: Arithmetic operation exceeds the limits for a numeric type.
#     Example: math.exp(1000)
#     FloatingPointError: Issues with floating-point calculations (rarely raised).
# b. Attribute Errors
#     AttributeError: Accessing an undefined attribute of an object.
#     Example: "hello".not_a_method
# c. Lookup Errors
#     IndexError: Accessing an invalid index in a list or other sequence.
#     Example: [1, 2, 3][5]
#     KeyError: Accessing a nonexistent key in a dictionary.
#     Example: {"a": 1}["b"]
# d. Import Errors
#     ImportError: Module or object not found during import.
#     Example: import nonexistent_module
#     ModuleNotFoundError: Subclass of ImportError when a module is not found.
# e. Type Errors
#     TypeError: Invalid operation for the given type.
#     Example: "2" + 2
# f. Name Errors
#     NameError: Using an undefined variable or name.
#     Example: print(undefined_variable)
#     UnboundLocalError: Accessing a local variable before it’s assigned.
# g. Value Errors
#     ValueError: Invalid value passed to a function.
#     Example: int("hello")
# h. IOError and OS Errors
#     FileNotFoundError: File or directory does not exist.
#     Example: open("nonexistent_file.txt")
#     PermissionError: Lack of permission to perform a file operation.
#     IsADirectoryError: File operation on a directory instead of a file.
#     NotADirectoryError: Directory operation on a file instead of a directory.
# i. Assertion Errors
#     AssertionError: Failure of an assert statement.
#     Example: assert 2 + 2 == 5
# j. Runtime Errors
#     RuntimeError: Generic runtime error.
#     Example: raise RuntimeError("Example error")
#     RecursionError: Maximum recursion depth exceeded.
#     Example: def recurse(): recurse()
# k. Memory Errors
#     MemoryError: Operation runs out of memory.
# l. System Errors
#     SystemError: Internal Python error.
#     SystemExit: Raised by sys.exit() to exit the program.
# m. Keyboard Interrupts
#     KeyboardInterrupt: Raised when the user interrupts the program (e.g., Ctrl+C).
# n. EOF Errors
#     EOFError: End of file reached without input.
#     Example: input() with no input in the terminal.

# ----------------------------------
