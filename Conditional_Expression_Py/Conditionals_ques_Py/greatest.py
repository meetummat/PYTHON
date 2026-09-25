# print greatest of four number entered by the user.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = int(input("Enter fourth number : "))

if (a > b and a > c and a > d):
    print("a is greatest", a)
elif(b > a and b > c and b > d):
    print("b is greatest", b)
elif(c > a and c > b and c > d):
    print("c is greatest", c)
else:
    print("d is greatest", d)
