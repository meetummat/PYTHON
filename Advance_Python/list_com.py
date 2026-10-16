# List Comprehension in Python
# List comprehension is an elegant way to create lists
# based on an existing iterable.


myList = [1, 2, 3, 4, 5]

# Without list comprehension:
# squaredList = []
# for item in myList:
#     squaredList.append(item * item)


# This can be simplified using list comprehension.
squaredList = [i * i for i in myList]
# This runs i * i for every item in myList
# and stores the results in a new list.


print(squaredList)