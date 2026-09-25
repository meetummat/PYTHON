# using multiple if

a = int(input("Enter a number : "))
if a > 10:
    print("a is greater than 10") # this is independent if.
# End of if statement 1
# if can be independent but elif and else can not be independent.

if (a > 0 and a < 18):
    print("Child")

elif a <= 0:
    print("Please enter valid a")

elif (a >= 18 and a <= 60):
    print("Adult")

else:
    print("Old")
# End of if statement 2.

print("End of program")