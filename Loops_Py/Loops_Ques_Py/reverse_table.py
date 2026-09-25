# Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter a number : "))
for i in range(1, 11):
    print(f"{n} * {11 - i} = {n*(11-i)}") # 11 - 1 = 10, so it starts from 5*10, 11 - i is like n+1-i.
