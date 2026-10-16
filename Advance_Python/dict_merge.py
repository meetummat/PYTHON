# New updates in Python

# 1. Merging dictionaries using | and |=
# The | operator can be used to merge two dictionaries.
# If the same key is present in both dictionaries,
# the value from the second dictionary is used.

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = dict1 | dict2
print(merged)
# Output: {'a': 1, 'b': 3, 'c': 4}
# Here 'b' was present in both dictionaries,
# so the value from dict2 (3) replaced the value from dict1 (2).


# |= can be used to merge another dictionary into the existing dictionary.
dict1 |= dict2
print(dict1)
# dict1 is now updated to {'a': 1, 'b': 3, 'c': 4}


# 2. Multiple context managers in one with statement
# We can open multiple files in the same with statement.
# Using parentheses makes it cleaner and easier to read.

with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    # We can work with both files here.
    print(f1.read())
    print(f2.read())

# Both files are automatically closed after the with block ends.