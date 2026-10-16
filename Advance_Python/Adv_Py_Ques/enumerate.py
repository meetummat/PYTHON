# Write a program to print third, fifth and seventh element from a list using enumerate function.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for index, value in enumerate(l):
#     if index == 3 or index == 5 or index == 7:
#         print(index, value)

for index, value in enumerate(l):
    if index == 2 or index == 4 or index == 6:
        print(value)