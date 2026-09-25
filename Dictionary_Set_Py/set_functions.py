# functions related to sets.

# Properties of set:-
# sets are unordered - element's order doesn't matter.
# sets are unindexed - cannot access elements by index.
# There is no way to change the items in sets.
# Sets cannot contain duplicate values.

s = {1, 5, 32, 54, 5, 5, 5, "Meet"}

print(s, type(s)) # we can see with the output it doesnot follow the order in which elements are defined.

s.add(544) # it will add this element in the set.
print(s)

print(len(s)) # it will print the length of the set.

s.remove(1) # it will remove 1 from the set.
print(s)

# find more function about the set and work with them like pop() and clear() etc

# Union and Intersection.


