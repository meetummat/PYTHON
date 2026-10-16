# Enumerate function in Python
# The enumerate() function adds a counter to an iterable
# and returns the index and value together.

l = [3, 5, 6, 77]

# Without enumerate:
# index = 0
# for item in l:
#     print(f"The item at index {index} is {item}")
#     index += 1


# This can be simplified using the enumerate() function.

for index, item in enumerate(l):
    # enumerate() gives us both the index and the value at that index.
    print(f"The item at index {index} is {item}")