# to detect double space in a string.

string = "this  is  to detect  double spaces  "

print(string.count("  ")) # will give how many times double spaces appeared in string
print(string.find("  ")) # will return the index of first space in double space.
# if there is no double space the find() will return -1
print(string.replace("  ", " ")) # will replace double spaces with single space.

# String are immutable after all these functions string will not change with every function new string will be created.
print(string) # string does not change.