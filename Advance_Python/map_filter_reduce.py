# Map, Filter and Reduce Functions in Python

# map() applies a function to every item in an iterable.
# filter() keeps the items for which the function returns True.
# reduce() combines the items of an iterable into a single result
# by applying a function to two items at a time.

from functools import reduce

# Map example
l = [1, 2, 3, 4, 5]

square = lambda x: x * x

sqlist = map(square, l)
# map() applies the square function to every item in l.
# It returns a map object (an iterator), not a list.
print(list(sqlist))
# We convert the map object into a list to see the results.
# Output: [1, 4, 9, 16, 25]


# Filter example
def even(n):
    if n % 2 == 0:
        return True
    return False

onlyEven = filter(even, l)
# filter() takes a function and an iterable.
# It keeps only those items for which the function returns True.
# It also returns an iterator, not a list.
print(list(onlyEven))
# Output: [2, 4]


# Reduce example
# We have to import reduce from the functools module.

def add(a, b):
    return a + b

mul = lambda x, y: x * y

print(reduce(add, l))
# reduce() applies the function to two items at a time
# and combines the results until only one value remains.
# 1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10, 10 + 5 = 15
# Output: 15

print(reduce(mul, l))
# It multiplies the items in the same way:
# 1 * 2 = 2, 2 * 3 = 6, 6 * 4 = 24, 24 * 5 = 120
# Output: 120