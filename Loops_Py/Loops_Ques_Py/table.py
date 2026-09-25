# Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter the number : "))
# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")

# with while loop
i = 1
while(i <= 10):
    print(f"{num} * {i} = {num * i}")
    i += 1
