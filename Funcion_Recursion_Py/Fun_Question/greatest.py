# Write a program using functions to find greatest of three numbers

def greatest(a, b, c):
    if a > b and a > c:
        print(a, "is greatest")
    elif b > c and b > a:
        print(b, "is greatest")
    elif c > a and c > b:
        print(c, "is greatest")

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
greatest(a, b, c)