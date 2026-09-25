# Write a program to print the following star pattern.
# ***
# * * for n = 3
# *** 

n = int(input("Enter a number : "))

# this approach builds the entire line at once.
# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"*n)
#     else:
#         print("*" + " "*(n-2) + "*") 
#         # print("*", " "*(n-2), "*") # if we use with "," it will add extra spaces. by default print() puts extra spaces in between.


# this approach builds the line piece by piece.
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"*n, end="")
    else:
        print("*",end="")
        print(" "* (n-2), end="")
        print("*",end="")
    print("") # new line after every iteration in this case.