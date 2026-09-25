# Can we change the values inside a list which is contained in set S

s = {3, "Meet", [2,4,5]} 
print(s) # we can't even store the list in a set it will  give error.
# set elements should be immutable and hashable.

# s[2][0] = 6 # we can not change the value of the list present in set. Because we can't use indexing in set.

# print(s)