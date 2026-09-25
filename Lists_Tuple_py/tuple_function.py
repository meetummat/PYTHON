# Every function will return a new tuple, they will not change in original tuple.

tuple1 = (2, 43.32, 7797, False, True, "Ronaldo")

print(tuple1.count(2)) # it will count how many times 2 has appeared in the tuple.

print(tuple1.index(False)) # will print the index of first occurance of given value.
# print(tuple1.index(3)) # if the element we have given is not in the tuple then it will raise value error.

# in keyword 
# to check weather the element present in tuple or not.
print(2 in tuple1)
print(4 in tuple1)

# Can find more Operations on tuple like Concatination, Repeat, len(), nin(), max(), slicing, unpacking, etc. and work with them.