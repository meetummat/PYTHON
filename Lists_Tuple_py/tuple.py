# Tuple is like list but tuple is also immutable.

a = ()  # empty tuple.
print(type(a)) # type = tuple

b = (1)
print(type(b)) # type = int # if there is only one element in paranthesis then python will consider it as what datatype it is.

# if we want to make a tuple with only one element then
c = (2,) # with "," it will now consider this as tuple with one element.
print(type(c))

tuple1 = (2, 43.32, 7797, False, True, "Ronaldo")
print(tuple1)

tuple1[0] = 3
# print(tuple1) # it will give error that we can not change the elements of tuple after defining, tuple are immutable.
