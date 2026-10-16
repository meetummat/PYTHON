# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = int(input("Enter a number : "))
# table = [n * i for i in l]
# print(table)

n = int(input("Enter a number : "))
table = [n * i for i in range(1, 11)]
print(table)