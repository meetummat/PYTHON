# Recursions in python.
# Recursion is function that calls itself to execute code.

# if n == 1 or n == 0: this is the base condition of this recursion, base condition is important so that the function doesn’t infinitely keep calling itself and at some point the recursion must resolve.
def fact(n):
    if n < 0:
        return "Factorial is not defined for the negative numbers."
    if n == 1 or n == 0: # when the value of n will be 1 or 0 then it will return 1 because factorial of 1 and 0 is 1.
        return 1
    return n * fact(n-1) # now it will call itself till the value of n is 1.

n = int(input("Enter a number : "))
print(f"The factorial of the number is {fact(n)}")
# Recursion is sometimes the most direct way to code an algorithm.