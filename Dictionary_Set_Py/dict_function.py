# Dictionaries are mutable every method will change in original dict.

marks = {
    "Meet" : 100,
    "Ronaldo" : 99, 
    "Hunny" : 98,
    0 : "name"
}

print(marks.items()) # returns the list of key value pairs, key value pair will be in tuple.

print(marks.keys()) # will print all the keys

print(marks.get("Meet")) # will print the value of the given key, if that key is not present then it will return None.
print(marks["Meet"]) # will print the value if the key is present and if key is not present will give error.

print(marks.values()) # will print all the values.

# we can update the value of key
marks.update({"Meet" : 97, "kane" : 96}) # will change in the original dictionary. will add the key value pair at the end which is not present and will update the pair which is already present. 
print(marks)

# to print the length of dict.
print(len(marks))

# find some more methods of dict like pop(), popitem(), clear(), copy(),  