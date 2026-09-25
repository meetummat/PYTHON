name = "Meet" # Double quoted string.
name2 = 'Ronaldo' # Single quoted string.
name3 = '''This is a  
            multiline 
            string''' # Triple quoted string.

# name4 = "Name"
# name4[0] = 'G'
# print(name4) # Strings are immutable we can not change the element of string after defining.

# f string 
print(f"Hello {name}") # with the f string we can use variable name to print, but we have mark it as f string.

print(len(name)) # it will print the length of the name.
print(len(name2))

nameshort = name[0:2] # it will slice the string as the index is given 0 is included and 2 is excluded.
# when we count from start we start from 0 and when we count from end we start from -1.
print(name[-4:-2])
print(nameshort)

start_char = name[0] # name[-4] # will store the first character of the string. we can convert negative index to corresponding positive index to make it easy.
print(start_char)

# using indices like this and negative indices is not a good practice.
# total elements in string are 0 to length - 1.
print(name2[:3]) # :3 means [0:3]
print(name2[2:]) # 2: means [2:len] like [2:7]

# Skipping the string in slicing
numbers = "123456789"
print(numbers[1:8:3]) # will start from the 1st index ends at 8th index and jumps over 3 characters everytime like skips 3-1 character everytime.