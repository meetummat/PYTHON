# functions/methods in list.
# Unlike string every function will change the original list.
# List are mutable.

friends = ["Apple", "Orange", 5, 32.88, False]
print(friends)

friends.append("Meet") # it will add Meet at the end of the string.
print(friends) # original list has changed. Lists are mutable.

# list.sort() - will sort the list elements in ascending order.
# list.reverse() - will reverse the list.

# insert() to insert the element at any particulat index. list.insert(index, elemetn)
friends.insert(3, 567) # this will insert 567 at 3rd index.
print(friends)

# list.pop(index) - will delete the value at the given index and will return the value that it has deleted.
print(friends.pop(3)) # deletes the value which was at index 3 and returns the value that it has deleted.
print(friends)

# list.remove(value) - will remove particular value from the list.
friends.remove("Meet") # will remove "Meet" from list.
print(friends)

# Find more methods of lists and use them.
