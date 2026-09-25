# Lists in python used to store related data together.
# used to store a set of values of any datatype.

friends = ["Apple", "Orange", 5, 32.88, False]

print(friends[0]) # will print the first element of list.

# Lists are mutable we can change the elements of lists after defining  unlike strings.
friends[0] = "Grapes"
print(friends[0]) 

# slicing in lists - same as strings.
print(friends[1:4])

# list of lists
list_of_lists = [["meet", "Ronaldo"], [1,1]]