# Join Method for Strings in Python

a = ["Meet", "Ronaldo", "Mbappe"]

final = "-".join(a)
# join() joins all the strings in the list using the string before the dot as a separator.
# Here, "-" is used between each string.

print(final)
# Output: Meet-Ronaldo-Mbappe


# format() Method in Python
# Nowadays, we commonly use f-strings, but we can still find format()
# in older codebases and existing programs.

a = "{} is a good {}".format("Meet", "boy")
# The values passed to format() are placed into the curly braces {} in order.
print(a)
# Output: Meet is a good boy


a = "{0} is a good {1}".format("Meet", "boy")
# We can specify which argument goes into which placeholder using index numbers.
# Indexing starts from 0, so {0} refers to "Meet" and {1} refers to "boy".
print(a)
# Output: Meet is a good boy