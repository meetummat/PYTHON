# Create dict of hindi words with values as their English translation. Provide user with an option to look it up.

hindi_dict = {
    "idhar" : "here",
    "madad" : "help",
    "kursi" : "chair"
}

word = input("Enter the word you want the meaning of : ")

print(hindi_dict.get(word)) # it will print None if the word is not present
# print(hindi_dict[word]) # it will give error if the word is not present.
