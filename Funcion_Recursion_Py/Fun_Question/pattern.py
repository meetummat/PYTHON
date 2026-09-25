# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def pattern(n):
    if n == 0:
        return # When return is executed, the current function call immediately ends and control returns to the place where that function was called.
    print("*" * n)
    pattern(n-1)

n = int(input("Enter a number : "))
pattern(n)