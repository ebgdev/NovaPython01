# İki sayı alan ve a / b döndüren bir Python fonksiyonu safe_divide(a, b) yazın.
# Ancak, eğer b sıfır ise, "Cannot divide by zero!" mesajıyla özel bir ZeroDivisionError
# fırlatın. Kullanıcı sayı dışında bir şey girerse,
# bu durumu da ele alın ve "Invalid input! Please enter numbers." mesajını gösterin.


class CustomZeroDivisionError(Exception):
    pass  # Creating a custom exception


def safe_divide(a, b):
    try:
        if b == 0:
            raise CustomZeroDivisionError("Cannot divide by zero!")
        return a / b
    except CustomZeroDivisionError as e:
        return str(e)
    except TypeError:
        return "Invalid input! Please enter numbers."


# Example Usage

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Result:", safe_divide(num1, num2))
