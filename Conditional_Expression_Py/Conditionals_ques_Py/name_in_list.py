# Write a program which finds out whether a given name is present in a list or not.

name_list = ["Meet", "Ronaldo", "Luka", "Mbappe"]
your_name = input("Enter your name : ") # python is case sensitive so if I enter name with the small letter it will say name is not in the list.

if your_name in name_list:
    print("Name present in the list")
else:
    print("Name is not in the list")