# Write a python function to remove a given word from a list ad strip it at the same time.


def remove_word(l, word):
    n = []
    for i in l:
        if not(i == word):
            n.append(i.strip(word)) # strip() removes specified characters from the beginning and end of a string, not necessarily a whole word.
    return n # returning a list.

l = ["Harry", "Rohan", "Sohan", "Rahul", "an"]
print(remove_word(l, "an"))

# also can use this if want to remove "an" from everywhere of the list
# i.replace(word, "")
