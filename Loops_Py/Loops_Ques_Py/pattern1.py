# Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

n = int(input("Enter a number : "))

# for i in range(1,n+1):
#     print(" "*(n-i), "*"*((2*i-1)))
#     # print() # to print a line.

for i in range(1,n+1):
    print(" "*(n-i), end="") # end statement prevent print in a next line with print function.
    print("*"*(2*i-1), end="")
    # print("\n") # with this we have to use "\n" to print a line.
    print("")