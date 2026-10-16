# Raising custom exception in python.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

# here we are raising error that we can not divide by zero.
if b == 0:
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")

