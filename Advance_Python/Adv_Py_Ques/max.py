# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [111, 2, 54, 88 , 7899 , 899]

def greater(a, b):
    if a > b:
        return a
    return b

print(reduce(greater, l))