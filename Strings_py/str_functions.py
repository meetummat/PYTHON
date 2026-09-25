# Functions of strings.
# Every method will make new string it will not change in existing string.

name = "Ronaldo"

print(len(name)) # prints the length of the string.

print(name.endswith("ldo")) # will check if the string ends with this, then returns true or false.

print(name.startswith("Ro")) # will check if the string starts with this.

str2 = "this is second string"
print(str2.capitalize()) # only turns the first letter of first word capital.
print(str2.find("second"))

# str2.lower() - will turn every letter to lower case 
# str2.upper() - will turn every letter to upper case 
# str2.title() - will turn first letter of each word to upper case 
# str2.count("c") - will count how many times 'c' has appeared in string.
# str2.find("second") - will find a word and returns the index of first occurance of that word.
# str2.replace("second", "third") - will replace the old word with new word in the entire string.

# find more useful functions and work with them.