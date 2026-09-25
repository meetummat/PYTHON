# find whether a given username contains less than 10 characters or not.

name = input("Enter you name : ")

if len(name) < 10:
    print("Name contains less than 10 character", len(name))
else:
    print("Name contains more than 10 character", len(name))