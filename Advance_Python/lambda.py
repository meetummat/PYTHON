# Lambda functions in Python
# A lambda function is a small anonymous function written in a single expression.
# It can take multiple arguments but contains only one expression.


# Normal function:
# def square(n):
#     return n * n
#
# print(square(4))


# We can write the same function using a lambda function.
square = lambda x: x * x
print(square(4))  # Output: 16


# A lambda function can also take multiple arguments.
sum = lambda a, b, c: a + b + c
print(sum(1, 2, 3))  # Output: 6